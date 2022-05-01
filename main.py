import sys
import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

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

        # Create the display and the buttons
        self._createDisplay()
        self._createLineEdit()
        self._createButtons()
        self._centralWidget.setLayout(self.general_layout)
        

    def _createDisplay(self):
        label_bv = qtw.QLabel()
        label_bv.setText("Bem vindo ao jogo de adivinhação!")
        label_bv.setAlignment(Qt.AlignCenter)
        label_bv.setFixedHeight(35)

        my_font = QFont()
        my_font.setBold(True)
        label_bv.setFont(my_font)

        self.general_layout.addWidget(label_bv)

    def _createLineEdit(self):
        line_layout = qtw.QHBoxLayout()

        label_explain = qtw.QLabel("Digite o numero:")
        line_layout.addWidget(label_explain)

        self.text = qtw.QLineEdit()
        line_layout.addWidget(self.text)

        self.general_layout.addLayout(line_layout)

    def _createButtons(self):
        btn_layout = qtw.QHBoxLayout()
        self.btn = qtw.QPushButton("Adivinhar")
        self.btn.setFixedWidth(100)
        
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
