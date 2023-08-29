import sys 
import os
import requests
from dotenv import load_dotenv 
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox, QLabel

load_dotenv()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.key = os.getenv('KEY')

        self.setWindowTitle("Weather")
        self.setGeometry(200, 200, 400, 400)

        layout = QVBoxLayout()

        self.data_input = QComboBox()
        self.data_input.setEditable(True)
        self.data_input.addItems(["Moscow", "Ottawa", "Paris"])

        # self.data_input = QLineEdit()
        
        self.data_input.currentIndexChanged.connect(self.click)
        
        # self.addItems(["One", "Two", "Three"])
        layout.addWidget(self.data_input)

        submit_button = QPushButton("Enter")
        submit_button.clicked.connect(self.click)
        layout.addWidget(submit_button)

        self.data_temperature = QLabel(":")
        layout.addWidget(self.data_temperature)


        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def click(self):
        city = self.get_city()
        temperature = self.get_temperature(city, self.key)
        self.refresh_widget_temperature(temperature)

    def get_city(self):
        return self.data_input.currentText()

    def get_temperature(self, city, key):
        url = 'http://api.weatherstack.com/current?query=' + city + '&access_key=' + key + '&units=m'
        print(url)
        res = requests.get(url)
        json = res.json()
        return json["current"]["temperature"]

    def refresh_widget_temperature(self, temperature):
        self.data_temperature.setText(f"temperature: {temperature}")

# class MainWindow(QMainWindow):

#     def __init__(self):
#         super(MainWindow, self).__init__()

#         self.setWindowTitle("My App")

#         widget = QComboBox()
#         widget.addItems(["One", "Two", "Three"])

#         # Отправляет текущий индекс (позицию) выбранного элемента.
#         widget.currentIndexChanged.connect( self.index_changed )

#         # # Есть альтернативный сигнал отправки текста.
#         widget.text_changed.connect( self.text_changed )

#         self.setCentralWidget(widget)

    # def input_data(self):
    #     city = self.data_input.text()




app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())