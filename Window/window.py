from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("exercicio 2")
        self.button = QPushButton("botao",self)
        self.button.setGeometry(190,10,100,70)
        self.result_label = QLabel(self)
        self.result_label.setGeometry(10,90,200,30)
        
        self.button.clicked.connect(self.imprimir)
        
    def imprimir(self):
        numero = 4
        if numero % 2 == 0:
            self.result_label.setText(f"Este numero é {numero} par")
        else:
            self.result_label.setText(f"Este numero é {numero} impar")
        
        
app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()