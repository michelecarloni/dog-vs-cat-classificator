from controller.controller import Controller
from PyQt5.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)
    controller = Controller()
    app.exec()


if __name__ == '__main__':
    main()