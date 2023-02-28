from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPixmap, QPainter, QColor, QBrush, QPen
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtCore import QRect   


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400)
        self.setStyleSheet('background-color: white;')
        self.initUI()

    def initUI(self):
        # Создание фона
        pixmap = QPixmap('background.jpg')
        bg_label = QLabel(self)
        bg_label.setPixmap(pixmap)
        bg_label.setGeometry(0, 0, self.width(), self.height())

        # Создание поля ввода
        self.input_line = QLineEdit(self)
        self.input_line.setGeometry(20, 20, 260, 60)
        self.input_line.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.input_line.setStyleSheet('font-size: 28px; color: black; background-color: white; border-radius: 30px; padding: 10px;')

        # Создание кнопок
        buttons = ['7', '8', '9', 'C',
                   '4', '5', '6', '+',
                   '1', '2', '3', '-',
                   '0', '.', '=', '*']

        vbox = QVBoxLayout()
        vbox.setContentsMargins(20, 100, 20, 20)
        for row in range(4):
            hbox = QVBoxLayout()
            for col in range(4):
                button = QPushButton(buttons[row * 4 + col])
                button.setStyleSheet('background-color: white; border-radius: 30px; padding: 10px; font-size: 24px;')
                button.clicked.connect(self.buttonClicked)
                hbox.addWidget(button)
            vbox.addLayout(hbox)

        self.setLayout(vbox)

    def buttonClicked(self):
        button = self.sender()
        text = button.text()

        if text == 'C':
            self.input_line.setText('')
        elif text == '=':
            try:
                result = str(eval(self.input_line.text()))
                self.input_line.setText(result)
            except:
                self.input_line.setText('Error')
        else:
            self.input_line.setText(self.input_line.text() + text)


if __name__ == '__main__':
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec()
