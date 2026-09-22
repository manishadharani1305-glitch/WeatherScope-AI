# 🌦️ WeatherScope-AI

**WeatherScope-AI** is an interactive weather application developed using **Python and Streamlit**. It allows users to search for a city and view its current weather information through a simple and user-friendly interface.

The application uses the **OpenWeather API** to retrieve real-time weather data.

---

## 📸 Application Preview

<img width="1143" height="807" alt="Screenshot 2026-09-22 230553" src="https://github.com/user-attachments/assets/fe50970c-b770-431e-8af0-fb0cbc8a1080" />


---

## ✨ Features

* 🌍 Search weather information for any city
* 🌡️ Display current temperature
* 💧 Display humidity
* 💨 Display wind speed
* ☁️ Show current weather conditions
* 📝 Display weather description
* 🔄 Fetch weather data dynamically using an API
* 🖥️ Interactive Streamlit interface
* 🔐 Secure API key handling using environment variables

---

## 🎯 Project Objective

The objective of WeatherScope-AI is to create a simple web-based application that provides users with current weather information for different locations.

The project demonstrates how Python, APIs, environment variables, and Streamlit can be combined to develop an interactive real-world application.

---

## 🛠️ Technologies Used

| Technology         | Purpose                             |
| ------------------ | ----------------------------------- |
| 🐍 Python          | Application development             |
| 🎈 Streamlit       | Web application interface           |
| 🌐 OpenWeather API | Weather data                        |
| 📡 Requests        | API requests                        |
| 🔐 Python-dotenv   | Environment variable management     |
| 💻 Git & GitHub    | Version control and project hosting |

---

## 📁 Project Structure

```text
WeatherScope-AI/
│
├── app.py
├── requirements.txt
├── .gitignore
├── weather-app.png
└── README.md
```

### File Description

**`app.py`**
Contains the main Python code for the WeatherScope-AI application.

**`requirements.txt`**
Contains the Python libraries required to run the project.

**`.gitignore`**
Prevents sensitive and unnecessary files such as `.env` from being uploaded to GitHub.

**`weather-app.png`**
Screenshot of the WeatherScope-AI application.

**`README.md`**
Project documentation and setup instructions.

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/manishadharani1305-glitch/WeatherScope-AI.git
```

### 2. Navigate to the Project Folder

```bash
cd WeatherScope-AI
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## 🔑 API Configuration

WeatherScope-AI uses the **OpenWeather API** to retrieve weather information.

Create a file named:

```text
.env
```

inside the project folder.

Add your API key in this format:

```text
WEATHER_API_KEY=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
```

## ▶️ Running the Application

After completing the setup, run:

```bash
streamlit run app.py
```

The application will start locally and can be opened in a web browser.

---

## 🔄 Application Workflow

```text
User
  ↓
Enter City Name
  ↓
WeatherScope-AI
  ↓
Send Request to Weather API
  ↓
Receive Weather Data
  ↓
Process Weather Information
  ↓
Display Weather Details
```

---

## 🌦️ Weather Information

WeatherScope-AI can display information such as:

* 🌍 City name
* 🌡️ Current temperature
* ☁️ Weather condition
* 📝 Weather description
* 💧 Humidity
* 💨 Wind speed

The displayed information is retrieved dynamically from the weather API.

---

## 💡 Key Concepts Demonstrated

This project demonstrates practical usage of:

* 🐍 Python programming
* 🌐 REST API integration
* 📦 JSON data handling
* 🎈 Streamlit application development
* 🔐 Environment variables
* 🔑 API authentication
* ⚠️ Error handling
* 💻 Git and GitHub

---

## 🚀 Future Enhancements

The application can be extended with additional features such as:

* 📅 5-day weather forecast
* 🌅 Sunrise and sunset information
* 🌧️ Rain probability
* 🌡️ Temperature unit conversion
* 📍 Automatic location detection
* 🗺️ Weather map integration
* 📊 Weather data visualization
* 🌙 Dark and light theme options
* 📱 Improved mobile responsiveness

---

## 📌 Project Highlights

| Category             | Details                 |
| -------------------- | ----------------------- |
| Project Name         | WeatherScope-AI         |
| Application Type     | Weather Web Application |
| Programming Language | Python                  |
| Framework            | Streamlit               |
| Weather API          | OpenWeather API         |
| Version Control      | Git                     |
| Repository           | GitHub                  |

---

## 👩‍💻 Author

### Manisha

Developed as a Python and Streamlit weather application project.

**GitHub:**
https://github.com/manishadharani1305-glitch

---

## 📜 License

This project is created for educational and project development purposes.
