import sys
import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Jogo de adivinhacao da Vivi')
        self.setFixedSize(500, 300)
         # Set the central widget
        self._centralWidget = qtw.QWidget(self)
        self.setCentralWidget(self._centralWidget)

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
