from PyQt5 import QtWidgets
from ui_handler import MainWindow_controller

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())