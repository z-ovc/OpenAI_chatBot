from PyQt6.QtWidgets import QMainWindow, QTextEdit, QPushButton, QApplication
import sys

class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimunSize(500,700)
        #add Chat area 
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10,10,480,320)
        self.chat_area.setReadOnly(True)


        #add the input frame
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10,340,480,50)

        #add button
        self.button = QPushButton("Send",self)
        self.button.setGeometry(500,340,100,50)
        self.show()

class ChatBot():
    pass


app = QApplication(sys.argv)
main_window = ChatBotWindow()
sys.exit(app.exec())
