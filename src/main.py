import sys
from calc_widget import CalcUI
from PySide6 import QtWidgets
from PySide6.QtCore import Qt

# open styles.qss and read in file
def load_stylesheet(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    # load style sheet
    stylesheet = load_stylesheet('src\static\styles.qss')

    # define app as a QApp
    app = QtWidgets.QApplication([])
    
    # get widget frome calc_widget.py
    widget = CalcUI()

    # resize the window
    widget.resize(400, 600)
    # set the window title
    widget.setWindowTitle('Calculator')
    #set the stylesheet
    widget.setStyleSheet(stylesheet)
    # render the app
    widget.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
