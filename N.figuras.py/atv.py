from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QLineEdit
import sys
from PySide6.QtCore import QSize,Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" ex08")
        self.setGeometry(400,100,300,150)
        self.label1 =QLabel("numero: ",self)
        self.label1.setGeometry(100,10,40,30)
        self.input1 =QLineEdit(self)
        self.input1.setGeometry(100,10,60,20)
app = QApplication(sys.argv)
janela=MainWindow()
janela.show()
app.exec()
