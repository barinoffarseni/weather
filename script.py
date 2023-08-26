
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
import sys 
import os
from dotenv import load_dotenv 
import requests

load_dotenv()

key = os.getenv('KEY')


class DataInputApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather")
        self.setGeometry(200, 200, 400, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.data_input = QLineEdit()
        layout.addWidget(self.data_input)

        self.submit_button = QPushButton("Enter")
        self.submit_button.clicked.connect(self.input_data)
        layout.addWidget(self.submit_button)

        self.data_label = QLabel(":")
        layout.addWidget(self.data_label)

        self.data_temperature = QLabel(":")
        layout.addWidget(self.data_temperature)

        self.data_observation_time = QLabel(":")
        layout.addWidget(self.data_observation_time)

        self.data_query = QLabel(":")
        layout.addWidget(self.data_query)

    def input_data(self,):
        city = self.data_input.text()

        url = 'http://api.weatherstack.com/current?query=' + city + '&access_key=' + key + '&units=m'
        res = requests.get(url)

        print(res.text)
        json = res.json()
        observation_time = json["current"]["observation_time"]
        temperature = json["current"]["temperature"]
        query = json["request"]["query"]

        self.data_label.setText(f"url: {url}")
        self.data_temperature.setText(f"temperature: {temperature}")
        self.data_observation_time.setText(f"observation_time: {observation_time}")
        self.data_query.setText(f"query: {query}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataInputApp()
    window.show()
    sys.exit(app.exec())