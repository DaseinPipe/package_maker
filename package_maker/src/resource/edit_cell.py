# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_cell.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(333, 169)
        self.gridLayout_2 = QGridLayout(Frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pkg_dir_type_lineEdit = QLineEdit(Frame)
        self.pkg_dir_type_lineEdit.setObjectName(u"pkg_dir_type_lineEdit")
        self.pkg_dir_type_lineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.pkg_dir_type_lineEdit, 0, 1, 1, 1)

        self.edit_tableWidget = QTableWidget(Frame)
        if (self.edit_tableWidget.columnCount() < 2):
            self.edit_tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.edit_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.edit_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.edit_tableWidget.setObjectName(u"edit_tableWidget")
        self.edit_tableWidget.setColumnCount(2)

        self.gridLayout.addWidget(self.edit_tableWidget, 1, 0, 1, 2)

        self.buttonBox = QDialogButtonBox(Frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Frame", u"Package Dir Types:-", None))
        ___qtablewidgetitem = self.edit_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Frame", u"keys", None));
        ___qtablewidgetitem1 = self.edit_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Frame", u"values", None));
    # retranslateUi

