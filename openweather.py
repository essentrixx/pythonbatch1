import sys
import os
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from dotenv import load_dotenv
load_dotenv()

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel("70°F")
        self.emoji_label = QLabel("☀️", self)
        self.description_label = QLabel("Sunny", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label") # setObjectName() gives a widget an ID so you can style or access it easily.
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
                                /* --- GLOBAL STYLES --- */
                                QWidget {
                                    background: qlineargradient(
                                        x1:0, y1:0, x2:0, y2:1,
                                        stop:0 #F0F4F8,   /* Very light gray/blue */
                                        stop:1 #E6EEF4    /* Light blue/gray */
                                    );
                                    font-family: 'Poppins', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
                                    color: #334E68; /* Dark blue-grey text */
                                }

                                /* --- ALL LABELS --- */
                                QLabel {
                                    color: #334E68;
                                }

                                /* --- CITY LABEL (Header/Title) --- */
                                QLabel#city_label {
                                    font-size: 20px;
                                    font-weight: 700;
                                    margin-top: 25px;
                                    margin-bottom: 15px;
                                    color: #102A43; /* Darker heading color */
                                }

                                /* --- INPUT FIELD --- */
                                QLineEdit#city_input {
                                    background: white;
                                    border: 1px solid #C5D9E8;
                                    border-radius: 12px;
                                    padding: 12px 18px;
                                    font-size: 16px;
                                    color: #334E68;
                                    margin-bottom: 20px;
                                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05); /* Soft shadow */
                                }

                                QLineEdit#city_input:focus {
                                    border: 2px solid #5C7CFA; /* Vibrant blue border on focus */
                                    background: #FFFFFF;
                                    outline: none;
                                }

                                /* --- BUTTON --- */
                                QPushButton#get_weather_button {
                                    background: #5C7CFA; /* Primary button color */
                                    border: none;
                                    border-radius: 12px;
                                    padding: 14px 30px;
                                    font-size: 16px;
                                    font-weight: 600;
                                    color: white;
                                    margin-bottom: 25px;
                                    box-shadow: 0 4px 12px rgba(92, 124, 250, 0.3); /* Stronger shadow for lift */
                                }

                                QPushButton#get_weather_button:hover {
                                    background: #4A6BED;
                                }

                                QPushButton#get_weather_button:pressed {
                                    background: #6D8FFF;
                                    box-shadow: none;
                                }

                                /* --- UNIT TOGGLE BUTTON (if present) --- */
                                QPushButton#toggle_button {
                                    background: #FFFFFF;
                                    border: 1px solid #D9E2EC;
                                    border-radius: 12px;
                                    padding: 8px 16px;
                                    font-size: 13px;
                                    font-weight: 500;
                                    color: #526C88;
                                }

                                QPushButton#toggle_button:hover {
                                    background: #F8FAFC;
                                    border: 1px solid #C5D9E8;
                                }

                                /* --- TEMPERATURE DISPLAY --- */
                                QLabel#temperature_label {
                                    font-size: 90px;
                                    font-weight: 300; /* Lighter weight for modern look */
                                    color: #102A43;
                                    margin-top: 15px;
                                    margin-bottom: 0px;
                                    letter-spacing: -3px;
                                }

                                /* --- EMOJI DISPLAY --- */
                                QLabel#emoji_label {
                                    font-size: 140px; /* Increased size for impact */
                                    margin: 0;
                                }

                                /* --- DESCRIPTION --- */
                                QLabel#description_label {
                                    font-size: 22px;
                                    color: #526C88; /* Softer text color */
                                    margin-bottom: 30px;
                                    font-weight: 400;
                                    text-transform: capitalize; /* Ensure nice formatting */
                                }

                                /* --- INFO CARD (if present) --- */
                                QWidget#info_card {
                                    background: white;
                                    border: 1px solid #E6EEF4;
                                    border-radius: 16px;
                                    padding: 20px;
                                    margin-top: 10px;
                                    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.08);
                                }

                                QWidget#info_card QLabel {
                                    font-size: 15px;
                                    color: #334E68;
                                    font-weight: 500;
                                }
                            """)
        self.setFixedSize(400, 600)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = os.getenv("WEATHER_API_KEY")
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request\nPlease check your input")
                case 404:
                    self.display_error("City not found")
                case 500:
                    self.display_error("Internal server error")

        except requests.exceptions.ConnectionError:
            self.display_error("Please check your internet connection")

        except requests.exceptions.Timeout:
            self.display_error("Request timed out")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirect! Check the URL.")

        except requests.exceptions.RequestException as req_err:
            self.display_error(f"Request Error: {req_err}")


    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()


    def display_weather(self, data):
        # self.temperature_label.setStyleSheet("font-size: 75px")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 459.67
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        self.temperature_label.setText(f"{temperature_c:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return '⛈️'  # Thunderstorm
        elif 300 <= weather_id <= 321:
            return '🌦️'  # Drizzle
        elif 500 <= weather_id <= 531:
            return '🌧️'  # Rain
        elif 600 <= weather_id <= 622:
            return '❄️'  # Snow
        elif 700 <= weather_id <= 781:
            return '🌫️'  # Mist / fog
        elif weather_id == 800:
            return '☀️'  # Clear sky
        elif 801 <= weather_id <= 804:
            return '☁️'  # Clouds (incl. 804 overcast)
        else:
            return '️'


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())