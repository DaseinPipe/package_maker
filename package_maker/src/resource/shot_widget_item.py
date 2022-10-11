# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shot_widget_item.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_swi_Frame(object):
    def setupUi(self, swi_Frame):
        if not swi_Frame.objectName():
            swi_Frame.setObjectName(u"swi_Frame")
        swi_Frame.resize(858, 292)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(swi_Frame.sizePolicy().hasHeightForWidth())
        swi_Frame.setSizePolicy(sizePolicy)
        swi_Frame.setBaseSize(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(swi_Frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.swi_delete_toolButton = QToolButton(swi_Frame)
        self.swi_delete_toolButton.setObjectName(u"swi_delete_toolButton")

        self.gridLayout_2.addWidget(self.swi_delete_toolButton, 0, 0, 1, 1)

        self.swi_dropdown_toolButton = QToolButton(swi_Frame)
        self.swi_dropdown_toolButton.setObjectName(u"swi_dropdown_toolButton")

        self.gridLayout_2.addWidget(self.swi_dropdown_toolButton, 0, 1, 1, 1)

        self.swi_lineEdit = QLineEdit(swi_Frame)
        self.swi_lineEdit.setObjectName(u"swi_lineEdit")
        self.swi_lineEdit.setEnabled(False)

        self.gridLayout_2.addWidget(self.swi_lineEdit, 0, 2, 1, 1)

        self.swi_add_pushButton = QPushButton(swi_Frame)
        self.swi_add_pushButton.setObjectName(u"swi_add_pushButton")

        self.gridLayout_2.addWidget(self.swi_add_pushButton, 0, 3, 1, 1)

        self.swi_container_widget = QWidget(swi_Frame)
        self.swi_container_widget.setObjectName(u"swi_container_widget")
        sizePolicy.setHeightForWidth(self.swi_container_widget.sizePolicy().hasHeightForWidth())
        self.swi_container_widget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.swi_container_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.swi_status_lineEdit = QLineEdit(self.swi_container_widget)
        self.swi_status_lineEdit.setObjectName(u"swi_status_lineEdit")

        self.gridLayout.addWidget(self.swi_status_lineEdit, 0, 0, 1, 1)

        self.swi_tableWidget = QTableWidget(self.swi_container_widget)
        if (self.swi_tableWidget.columnCount() < 6):
            self.swi_tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.swi_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.swi_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.swi_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.swi_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.swi_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.swi_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.swi_tableWidget.setObjectName(u"swi_tableWidget")
        self.swi_tableWidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.swi_tableWidget.sizePolicy().hasHeightForWidth())
        self.swi_tableWidget.setSizePolicy(sizePolicy)
        self.swi_tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.swi_tableWidget.setAutoScrollMargin(12)
        self.swi_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.swi_tableWidget.setShowGrid(True)
        self.swi_tableWidget.setRowCount(0)
        self.swi_tableWidget.setColumnCount(6)
        self.swi_tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.swi_tableWidget.horizontalHeader().setDefaultSectionSize(166)
        self.swi_tableWidget.horizontalHeader().setStretchLastSection(False)
        self.swi_tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.swi_tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.swi_tableWidget, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.swi_container_widget, 1, 0, 1, 5)

        self.swi_edit_pushButton = QPushButton(swi_Frame)
        self.swi_edit_pushButton.setObjectName(u"swi_edit_pushButton")
        self.swi_edit_pushButton.setEnabled(False)

        self.gridLayout_2.addWidget(self.swi_edit_pushButton, 0, 4, 1, 1)


        self.retranslateUi(swi_Frame)

        QMetaObject.connectSlotsByName(swi_Frame)
    # setupUi

    def retranslateUi(self, swi_Frame):
        swi_Frame.setWindowTitle(QCoreApplication.translate("swi_Frame", u"Frame", None))
        self.swi_delete_toolButton.setText(QCoreApplication.translate("swi_Frame", u"x", None))
        self.swi_dropdown_toolButton.setText(QCoreApplication.translate("swi_Frame", u">", None))
        self.swi_add_pushButton.setText(QCoreApplication.translate("swi_Frame", u"add", None))
        ___qtablewidgetitem = self.swi_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("swi_Frame", u"source_path", None));
        ___qtablewidgetitem1 = self.swi_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("swi_Frame", u"package_path", None));
        ___qtablewidgetitem2 = self.swi_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("swi_Frame", u"pkg item", None));
        ___qtablewidgetitem3 = self.swi_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("swi_Frame", u"custom_name", None));
        ___qtablewidgetitem4 = self.swi_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("swi_Frame", u"path_data", None));
        self.swi_edit_pushButton.setText(QCoreApplication.translate("swi_Frame", u"edit", None))
    # retranslateUi

