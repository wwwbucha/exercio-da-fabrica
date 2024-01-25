from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFrame
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,600)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Poketex")
        
        self.button_pikachu = QPushButton('bozo.jpg')
        self.button_caramelo = QPushButton('lula.jpg')
        
        self.image_frame = QFrame(self)
        self.image_frame.setFrameShape(QFrame.Box)
        self.image_frame.setFixedSize(800,600)
        self.image_frame.setLayout(QVBoxLayout())
        
        self.image_label = QLabel(self.image_frame)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_frame.layout().addWidget(self.image_label)
        
        layout = QVBoxLayout()
        layout.addWidget(self.button_pikachu)
        layout.addWidget(self.button_caramelo)
        layout.addWidget(self.image_frame)
        
        self.button_pikachu.clicked.connect(self.display_pikachu)
        self.button_caramelo.clicked.connect(self.display_caramelo)
        
        self.setLayout(layout)
    
    def display_pikachu(self):
        pixmap = QPixmap('bozo.jpg')
        self.image(pixmap)
    
    def display_caramelo(self):
        pixmap = QPixmap('lula.jpg')
        self.image(pixmap)
        
    def image(self, pixmap):
        scale_pixmap = pixmap.scaled(600,400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(scale_pixmap)
        
       
        
    

app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()