from PySide2.QtWidgets import QApplication, QMessageBox, QWidget
import sys


QT_MESSAGE_TYPE = {
    "info": QMessageBox.Information,
    "warn": QMessageBox.Warning,
    "crit": QMessageBox.Critical,
    "quest": QMessageBox.Question
    }

def pop_up(messType, messTitle, messText, buttons= QMessageBox.Yes | QMessageBox.No, defaultButton=QMessageBox.No):
    if messType in QT_MESSAGE_TYPE:
        type = QT_MESSAGE_TYPE[messType]
    else:
        type = QMessageBox.Question
    mess = QMessageBox(type, messTitle, messText, defaultButton)
    mess.setStandardButtons(buttons)
    mess.setDefaultButton(defaultButton)
    mess.show()
    return mess.exec_()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ret = pop_up(
        messType='quest',
        messTitle='popup_test',
        messText='testing_popup',
        defaultButton=QMessageBox.No
    )
    # print(ret == QMessageBox.Yes)

    