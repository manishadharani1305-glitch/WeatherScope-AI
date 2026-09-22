import os
import requests
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.weather-card {
    padding: 25px;
    border-radius: 20px;
    background: linear-gradient(135deg, #e0f2fe, #f0f9ff);
    margin-top: 20px;
    margin-bottom: 20px;
}

.weather-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}

.weather-subtitle {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-bottom: 30px;
}

.metric-card {
    padding: 20px;
    border-radius: 15px;
    background-color: #f8fafc;
    text-align: center;
    border: 1px solid #e2e8f0;
}

.ai-card {
    padding: 25px;
    border-radius: 20px;
    background: linear-gradient(135deg, #f5f3ff, #eef2ff);
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

st.set_page_config(
    page_title="WeatherScope AI",
    page_icon="🌤️",
    layout="centered"
)

st.markdown(
    '<div class="weather-title">🌤️ WeatherScope AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="weather-subtitle">Smart Weather Information & AI Assistant</div>',
    unsafe_allow_html=True
)

if not HF_TOKEN:
    st.error("Hugging Face token is missing. Please add HF_TOKEN to your .env file.")
    st.stop()

client = InferenceClient(
    provider="hf-inference",
    api_key=HF_TOKEN
)


def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "results" not in data:
        return None

    location = data["results"][0]

    return {
        "name": location["name"],
        "country": location.get("country", ""),
        "latitude": location["latitude"],
        "longitude": location["longitude"]
    }


def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
        "timezone": "auto"
    }

    response = requests.get(url, params=params)

    return response.json()


def weather_description(code):
    descriptions = {
        0: "Clear sky ☀️",
        1: "Mainly clear 🌤️",
        2: "Partly cloudy ⛅",
        3: "Overcast ☁️",
        45: "Fog 🌫️",
        48: "Depositing rime fog 🌫️",
        51: "Light drizzle 🌦️",
        53: "Moderate drizzle 🌦️",
        55: "Dense drizzle 🌧️",
        61: "Slight rain 🌦️",
        63: "Moderate rain 🌧️",
        65: "Heavy rain 🌧️",
        71: "Slight snow ❄️",
        73: "Moderate snow ❄️",
        75: "Heavy snow ❄️",
        80: "Slight rain showers 🌦️",
        81: "Moderate rain showers 🌧️",
        82: "Violent rain showers ⛈️",
        95: "Thunderstorm ⛈️",
        96: "Thunderstorm with hail ⛈️",
        99: "Thunderstorm with heavy hail ⛈️"
    }

    return descriptions.get(code, "Unknown weather")


city = st.text_input(
    "📍 Enter a city",
    placeholder="Example: Chennai"
)

if st.button("🔍 Check Weather"):

    if not city:
        st.warning("Please enter a city name.")

    else:
        with st.spinner("Fetching weather information..."):

            location = get_coordinates(city)

            if location is None:
                st.error("City not found. Please check the city name.")

            else:
                weather = get_weather(
                    location["latitude"],
                    location["longitude"]
                )

                current = weather["current"]

                st.success(
                    f"Weather information for {location['name']}, "
                    f"{location['country']}"
                )

               description = weather_description(
    current["weather_code"]
)

st.markdown(
    '<div class="weather-card">',
    unsafe_allow_html=True
)

st.subheader(
    f"📍 {location['name']}, {location['country']}"
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div class="metric-card">
            <h3>🌡️ Temperature</h3>
            <h2>{current['temperature_2m']} °C</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="metric-card">
            <h3>💧 Humidity</h3>
            <h2>{current['relative_humidity_2m']} %</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="metric-card">
            <h3>💨 Wind</h3>
            <h2>{current['wind_speed_10m']} km/h</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <div class="metric-card">
            <h3>🌦️ Condition</h3>
            <h2>{description}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

                st.divider()

                st.subheader("🤖 AI Weather Assistant")

                question = st.text_input(
                    "Ask something about this weather",
                    placeholder="Example: Is this weather suitable for going outside?"
                )

                if st.button("🤖 Ask AI"):

                    if not question:
                        st.warning("Please enter a question.")

                    else:

                        prompt = f"""
You are a helpful weather assistant.

Current weather:
City: {location['name']}
Country: {location['country']}
Temperature: {current['temperature_2m']} °C
Humidity: {current['relative_humidity_2m']} %
Wind Speed: {current['wind_speed_10m']} km/h
Condition: {description}

User question:
{question}

Answer clearly and briefly using the weather information above.
"""

                        with st.spinner("AI is thinking..."):

                            try:
                                response = client.chat_completion(
                                    model="HuggingFaceH4/zephyr-7b-beta",
                                    messages=[
                                        {
                                            "role": "user",
                                            "content": prompt
                                        }
                                    ],
                                    max_tokens=200
                                )

                                answer = response.choices[0].message.content

                                st.info(answer)

                            except Exception as e:
                                st.error(
                                    "AI response failed. Please check your Hugging Face token or model availability."
                                )
                                st.caption(str(e))