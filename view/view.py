import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class View(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.button = QPushButton('press', self)
        self.categoryLabel = QLabel('category', self)
        self.probabilityLabel = QLabel('probability', self)
        self.picLabel = QLabel(self)
        self.picPixmap = QPixmap('placeholder/placeholder.png')
        
        self.setGeometry(800, 400, 900, 1000)
        self.initUI()
        
    
    def initUI(self):
        
        self.picLabel.setGeometry(0, 0, 500, 500)
        self.picLabel.setGeometry((self.width() - self.picLabel.width()) // 2, 100, 500, 500)
        self.picLabel.setPixmap(self.picPixmap)
        self.picLabel.setScaledContents(True)
        
        self.button.setGeometry(0, 0, 200, 100)
        self.button.setGeometry((self.width() - self.button.width()) // 2, 800, 200, 100)
        self.button.setStyleSheet("font-size: 20px;")
        self.button.clicked.connect(self.load_image)
        
        self.categoryLabel.setGeometry(100, 650, 200, 100)
        self.categoryLabel.setAlignment(Qt.AlignHCenter)
        self.categoryLabel.setStyleSheet("font-size: 30px;")
        
        self.probabilityLabel.setGeometry(600, 650, 200, 100)
        self.probabilityLabel.setAlignment(Qt.AlignHCenter)
        self.probabilityLabel.setStyleSheet("font-size: 30px;")
    
    
    def load_image(self):
        
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp *webp)")

        if file_name:
            
            self.picPixmap = QPixmap(file_name)
            self.picLabel.setPixmap(self.picPixmap)
            self.picLabel.setScaledContents(True)
            self.controller.getData(file_name)
        
    def setData(self, category, probability):
        self.categoryLabel.setText(category)
        self.probabilityLabel.setText(str(probability[0]))
            
        
        