import sys
import os  
from PyQt6.QtGui import QPixmap
import requests
from dotenv import load_dotenv 
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox, QLabel
from threading import Timer

load_dotenv()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.key = os.getenv('KEY')

        self.setWindowTitle("Weather")
        self.setGeometry(200, 200, 400, 400)


        self.data_input = QComboBox()
        self.data_input.setEditable(True)
        self.data_input.addItems(["Moscow", "Ottawa", "Paris"])

        layout = QVBoxLayout()
        layout.addWidget(self.data_input)
        self.home = QLabel()
        layout.addWidget(self.home)

        submit_button = QPushButton("Enter")
        submit_button.clicked.connect(self.click)
        layout.addWidget(submit_button)

        self.data_temperature = QLabel(":")
        layout.addWidget(self.data_temperature)


        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def temperature_timer(self):
        temperature = self.get_temperature(self.city, self.key)
        self.refresh_widget_temperature(temperature)
        Timer(10, self.temperature_timer).start()

    def click(self):
        self.city = self.get_city()
        temperature = self.get_temperature(self.city, self.key)
        self.refresh_widget_temperature(temperature)

        # self.temperature_timer()

    def get_city(self):
        return self.data_input.currentText()

    def get_temperature(self, city, key):
        url = 'http://api.weatherstack.com/current?query=' + city + '&access_key=' + key + '&units=m'
        res = requests.get(url)
        json = res.json()
        return json["current"]["temperature"]

    def refresh_widget_temperature(self, temperature):
        if temperature < 15:
            self.home.setPixmap(QPixmap('снежинка.png.'))
        elif temperature > 15:
            self.home.setPixmap(QPixmap('солнышко.png.'))
        self.data_temperature.setText(f"temperature: {temperature}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
