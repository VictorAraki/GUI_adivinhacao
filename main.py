import sys
import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QFont
import random
from tela_jogo import MainWindow
class FirstWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Jogo de adivinhação")
        self.setFixedSize(300,250)

        self.main_layout = qtw.QVBoxLayout()
        self._centralWidget = qtw.QWidget(self)
        self.setCentralWidget(self._centralWidget)

        self._create_display()

        self._centralWidget.setLayout(self.main_layout)
    
    def _create_display(self):
        label_bv = qtw.QLabel()
        label_bv.setText("Bem vindo!")
        self.main_layout.addWidget(label_bv)
        
        self.radiobutton = qtw.QRadioButton("Level 1")
        self.main_layout.addWidget(self.radiobutton)

        self.radiobutton2 = qtw.QRadioButton("Level 2")
        self.main_layout.addWidget(self.radiobutton2)

        self.radiobutton3 = qtw.QRadioButton("Level 3")
        self.main_layout.addWidget(self.radiobutton3)

        self.btn = qtw.QPushButton("Começar")
        self.btn.clicked.connect(self.comecar)
        self.main_layout.addWidget(self.btn)

        self.line = qtw.QLineEdit()
        self.line.setReadOnly(True)
        self.main_layout.addWidget(self.line)
    
    def comecar(self):
        if self.radiobutton.isChecked():
            self.line.setText("Você selecionou o level 1!")

        elif self.radiobutton2.isChecked():
            self.line.setText("Você selecionou o level 2!")
        
        elif self.radiobutton3.isChecked():
            self.line.setText("Você selecionou o level 3!")
        
        self._create_random_number()
        self._create_game_window()

    def _create_random_number(self):
        if self.radiobutton.isChecked():
            self.tentativas = 20

        elif self.radiobutton2.isChecked():
            self.tentativas = 10

        elif self.radiobutton3.isChecked():
            self.tentativas = 5

        self.numero_secreto = random.randrange(1,101)
        
    def _create_game_window(self):
        self.main = MainWindow(self.tentativas,self.numero_secreto)
        self.main.show()


def main():
    """Main function."""
    # Create an instance of QApplication
    app = qtw.QApplication(sys.argv)
    # Show the calculator's GUI
    view = FirstWindow()
    view.show()
    # Execute the window's main loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()