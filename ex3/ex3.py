from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton,QLineEdit
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("exercicio 2")
        self.button = QPushButton("botao",self)
        self.button.setGeometry(10,100,300,150)
        
        self.label1=QLabel("Numero 1 ",self)
        self.label1.setGeometry(10,10,80,30)
        self.input1=QLineEdit(self)
        self.input1.saveGeometry(30,50,80,30)
        
        self.input2=QLineEdit(self)
        self.input2.setGeometry(100,50,80,30)
        
        
        self.button=QPushButton("CALCULAR",self)
        self.button.setGeometry(100,10,100,70)
        
        
        
    def calcular_soma(self):
        num1=int(self.input1.text())
        num2=int(self.input2.text())
        
        
        