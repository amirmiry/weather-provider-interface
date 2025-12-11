## 🌦️ Weather Provider Interface (Python)

This project implements a flexible, extensible weather data system using an abstract base class and multiple provider integrations.
You can easily switch between different weather APIs (OpenWeather and Open-Meteo) to retrieve normalized temperature and humidity data.

---

### 🚀 Features
- Abstract provider interface using Python’s `abc` module

- Two provider implementations:

  - `OpenWeatherProvider` (via OpenWeatherMap API)

  - `OpenMeteoWeatherProvider` (via Open-Meteo API)
 
 - Returns normalized weather data structure for consistency:
```python
{"temp": <temperature_in_Celsius>, "humidity": <humidity_percentage>}
```
- CLI-based provider selection

- Demonstrates clean OOP design, API consumption, and data normalization

---

### 📂 Project Structure
├── weather_providers.py <br>
└── README.md
---

### 🛠️ Technologies Used

- Python 3.x

- requests for HTTP requests

- abc for abstract classes

---
## 🧩 Architecture Overview

1. `WeatherAbstract` (Interface)
- Defines the required method for all providers:
```python
@abstractmethod
def get_current_weather(self, latitude, longitude):
    pass
```
2. OpenWeather Provider
Retrieves data from:
```bash
@abstractmethod
def get_current_weather(self, latitude, longitude):
    pass
```
Normalizes Kelvin temperatures to Celsius and extracts humidity.

3. Open-Meteo Provider
Retrieves data from:
```bash
https://api.open-meteo.com/v1/forecast
```
Returns direct Celsius temperature and humidity fields.

---

### 📌 Usage
1. Install Requirements
```bash
pip install requests
```

2. Update API Key
Inside the script:
```python
OpenWeatherProvider(api_key="YOUR_API_KEY_HERE")
```
Replace with your actual OpenWeather API key.

3. Run the Script
```bash
python3 weather_providers.py
```
4. Select Provider

You will be prompted:

```css
Which one of the provider would you like to use?
1. OpenWeatherProvider
2. OpenMeteoWeatherProvider
Enter your choice:
```
5. Example Output
```bash
{'temp': 18.7, 'humidity': 51}
done
```

### 🔮 Possible Improvements

- Add error-handling for HTTP failures

- Use dependency injection

- Add unit tests

- Add support for more weather providers

- Replace CLI with GUI or REST API interface



### 📜 License

This project is distributed under the MIT License.
Feel free to improve and build upon it!

