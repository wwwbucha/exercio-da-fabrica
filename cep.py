import brazilcep 
import sys
from PySide6.QtWidgets import QMainWindow , QApplication
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BUSCAR CEP: ")
ENDERECO = brazilcep.get_address_from_cep('79106361')
print(ENDERECO)


app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
sys.exit(app.exec_())