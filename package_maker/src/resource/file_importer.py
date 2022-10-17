# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_importer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_File_Importer(object):
    def setupUi(self, File_Importer):
        if not File_Importer.objectName():
            File_Importer.setObjectName(u"File_Importer")
        File_Importer.resize(1127, 772)
        self.gridLayout_2 = QGridLayout(File_Importer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_7 = QFrame(File_Importer)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_7, 5, 0, 1, 3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.fi_plate_version_label = QLabel(File_Importer)
        self.fi_plate_version_label.setObjectName(u"fi_plate_version_label")
        font = QFont()
        font.setFamily(u"Times New Roman")
        self.fi_plate_version_label.setFont(font)
        self.fi_plate_version_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.fi_plate_version_label, 0, 2, 1, 1)

        self.fi_discipline_label = QLabel(File_Importer)
        self.fi_discipline_label.setObjectName(u"fi_discipline_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fi_discipline_label.sizePolicy().hasHeightForWidth())
        self.fi_discipline_label.setSizePolicy(sizePolicy)
        self.fi_discipline_label.setFont(font)
        self.fi_discipline_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.fi_discipline_label, 1, 0, 1, 1)

        self.fi_shot_comboBox = QComboBox(File_Importer)
        self.fi_shot_comboBox.setObjectName(u"fi_shot_comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fi_shot_comboBox.sizePolicy().hasHeightForWidth())
        self.fi_shot_comboBox.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.fi_shot_comboBox, 0, 1, 1, 1)

        self.fi_shot_version_label = QLabel(File_Importer)
        self.fi_shot_version_label.setObjectName(u"fi_shot_version_label")
        sizePolicy.setHeightForWidth(self.fi_shot_version_label.sizePolicy().hasHeightForWidth())
        self.fi_shot_version_label.setSizePolicy(sizePolicy)
        self.fi_shot_version_label.setFont(font)
        self.fi_shot_version_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.fi_shot_version_label, 1, 2, 1, 1)

        self.fi_shot_version_comboBox = QComboBox(File_Importer)
        self.fi_shot_version_comboBox.setObjectName(u"fi_shot_version_comboBox")
        sizePolicy1.setHeightForWidth(self.fi_shot_version_comboBox.sizePolicy().hasHeightForWidth())
        self.fi_shot_version_comboBox.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.fi_shot_version_comboBox, 1, 3, 1, 1)

        self.fi_shot_label = QLabel(File_Importer)
        self.fi_shot_label.setObjectName(u"fi_shot_label")
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(8)
        self.fi_shot_label.setFont(font1)
        self.fi_shot_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.fi_shot_label, 0, 0, 1, 1)

        self.fi_plate_version_comboBox = QComboBox(File_Importer)
        self.fi_plate_version_comboBox.setObjectName(u"fi_plate_version_comboBox")

        self.gridLayout.addWidget(self.fi_plate_version_comboBox, 0, 3, 1, 1)

        self.fi_discipline_comboBox = QComboBox(File_Importer)
        self.fi_discipline_comboBox.setObjectName(u"fi_discipline_comboBox")
        sizePolicy1.setHeightForWidth(self.fi_discipline_comboBox.sizePolicy().hasHeightForWidth())
        self.fi_discipline_comboBox.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.fi_discipline_comboBox, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 3)

        self.fi_import_pushButton = QPushButton(File_Importer)
        self.fi_import_pushButton.setObjectName(u"fi_import_pushButton")

        self.gridLayout_2.addWidget(self.fi_import_pushButton, 7, 1, 1, 1)

        self.fi_apply_pushButton = QPushButton(File_Importer)
        self.fi_apply_pushButton.setObjectName(u"fi_apply_pushButton")

        self.gridLayout_2.addWidget(self.fi_apply_pushButton, 7, 2, 1, 1)

        self.line_5 = QFrame(File_Importer)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_5, 2, 0, 1, 3)

        self.fi_global_pkg_label = QLabel(File_Importer)
        self.fi_global_pkg_label.setObjectName(u"fi_global_pkg_label")

        self.gridLayout_2.addWidget(self.fi_global_pkg_label, 0, 1, 1, 1)

        self.status_lineEdit = QLineEdit(File_Importer)
        self.status_lineEdit.setObjectName(u"status_lineEdit")
        self.status_lineEdit.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.status_lineEdit.sizePolicy().hasHeightForWidth())
        self.status_lineEdit.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.status_lineEdit, 8, 0, 1, 3)

        self.fi_cancel_pushButton = QPushButton(File_Importer)
        self.fi_cancel_pushButton.setObjectName(u"fi_cancel_pushButton")

        self.gridLayout_2.addWidget(self.fi_cancel_pushButton, 7, 0, 1, 1)

        self.fi_item_pkg_label = QLabel(File_Importer)
        self.fi_item_pkg_label.setObjectName(u"fi_item_pkg_label")

        self.gridLayout_2.addWidget(self.fi_item_pkg_label, 1, 1, 1, 1)

        self.line_6 = QFrame(File_Importer)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_6, 4, 0, 1, 3)

        self.label_4 = QLabel(File_Importer)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(File_Importer)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.fi_tableWidget = QTableWidget(File_Importer)
        if (self.fi_tableWidget.columnCount() < 5):
            self.fi_tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.fi_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.fi_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.fi_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.fi_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.fi_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.fi_tableWidget.setObjectName(u"fi_tableWidget")
        self.fi_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.fi_tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.fi_tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.fi_tableWidget.setRowCount(0)
        self.fi_tableWidget.setColumnCount(5)
        self.fi_tableWidget.horizontalHeader().setMinimumSectionSize(25)

        self.gridLayout_2.addWidget(self.fi_tableWidget, 6, 0, 1, 3)


        self.retranslateUi(File_Importer)

        QMetaObject.connectSlotsByName(File_Importer)
    # setupUi

    def retranslateUi(self, File_Importer):
        File_Importer.setWindowTitle(QCoreApplication.translate("File_Importer", u"Frame", None))
        self.fi_plate_version_label.setText(QCoreApplication.translate("File_Importer", u"Plate Version:-", None))
        self.fi_discipline_label.setText(QCoreApplication.translate("File_Importer", u"Discipline:- ", None))
        self.fi_shot_version_label.setText(QCoreApplication.translate("File_Importer", u"Shot Version:-", None))
        self.fi_shot_label.setText(QCoreApplication.translate("File_Importer", u"shot:- ", None))
        self.fi_import_pushButton.setText(QCoreApplication.translate("File_Importer", u"Import", None))
        self.fi_apply_pushButton.setText(QCoreApplication.translate("File_Importer", u"Apply", None))
        self.fi_global_pkg_label.setText("")
        self.fi_cancel_pushButton.setText(QCoreApplication.translate("File_Importer", u"Cancel", None))
        self.fi_item_pkg_label.setText("")
        self.label_4.setText(QCoreApplication.translate("File_Importer", u"Global PKG Name :-", None))
        self.label_5.setText(QCoreApplication.translate("File_Importer", u"Item PKG Name :-", None))
        ___qtablewidgetitem = self.fi_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("File_Importer", u"source_dir", None));
        ___qtablewidgetitem1 = self.fi_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("File_Importer", u"source_file", None));
        ___qtablewidgetitem2 = self.fi_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("File_Importer", u"custom_name", None));
        ___qtablewidgetitem3 = self.fi_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("File_Importer", u"pkg item", None));
    # retranslateUi

