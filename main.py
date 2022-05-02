import sys
import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
import random
class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Jogo de adivinhacao da Vivi')
        self.setFixedSize(300, 250)
         # Set the central widget
        self.general_layout = qtw.QVBoxLayout()
        self._centralWidget = qtw.QWidget(self)
        self.setCentralWidget(self._centralWidget)

        self._create_random_number()

        # Create the display and the buttons
        self._createDisplay()
        self._createLineEdit()
        self._createButtons()
        self._centralWidget.setLayout(self.general_layout)

    def _create_random_number(self):
        self.tentativas = 10
        self.numero_secreto = random.randrange(1,101)

    def _create_msg_box(self, title, text, icon=None):
        msg = qtw.QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        if icon is not None:
            msg.setIcon(icon)

        msg.exec_()

    def adivinhar(self):
        if self.tentativas > 0:
            if int(self.numero.text()) == self.numero_secreto:
                self._create_msg_box("PARABÉNS", f"Você acertou, o número secreto é {self.numero_secreto}!!!!")
                QCoreApplication.instance().quit()
            elif int(self.numero.text()) < self.numero_secreto:
                self._create_msg_box("OH NÃO", "O número secreto é maior que o seu chute")
            elif int(self.numero.text()) > self.numero_secreto:
                self._create_msg_box("OH NÃO", "O número secreto é menor que o seu chute")
            self.tentativas -= 1
        
        if self.tentativas == 0:
            self._create_msg_box("PERDEU PLAYBOY", "Acabaram as suas tentativas!!", qtw.QMessageBox.Critical)
            QCoreApplication.instance().quit()

    #comentario novo

    def _create_label(self, text):
        #Criando o label e alinhano no meio e colocando altura maxima
        label_bv = qtw.QLabel()
        label_bv.setText(text)
        label_bv.setAlignment(Qt.AlignCenter)
        label_bv.setFixedHeight(15)

        #Colocando a fonte do label em negrito
        my_font = QFont()
        my_font.setBold(True)
        label_bv.setFont(my_font)
        return label_bv

    def _createDisplay(self):
        label_1 = self._create_label("*********************************")
        label_2 = self._create_label("Bem vindo ao jogo de adivinhação!")
        label_3 = self._create_label("*********************************")

        self.general_layout.addWidget(label_1)
        self.general_layout.addWidget(label_2)
        self.general_layout.addWidget(label_3)

    def _createLineEdit(self):
        line_layout = qtw.QHBoxLayout()

        label_explain = qtw.QLabel("Digite um numero entre 1 a 100:")
        line_layout.addWidget(label_explain)

        self.numero = qtw.QLineEdit()
        line_layout.addWidget(self.numero)

        self.general_layout.addLayout(line_layout)

    def _createButtons(self):
        btn_layout = qtw.QHBoxLayout()
        self.btn = qtw.QPushButton("Adivinhar")
        self.btn.setFixedWidth(100)

        self.btn.clicked.connect(self.adivinhar)
        
        btn_layout.addWidget(self.btn)
        self.general_layout.addLayout(btn_layout)
        

# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    app = qtw.QApplication(sys.argv)
    # Show the calculator's GUI
    view = MainWindow()
    view.show()
    # Execute the window's main loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
