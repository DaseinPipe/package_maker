# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resource_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Package_Maker(object):
    def setupUi(self, Package_Maker):
        if not Package_Maker.objectName():
            Package_Maker.setObjectName(u"Package_Maker")
        Package_Maker.resize(373, 299)
        self.gridLayout_6 = QGridLayout(Package_Maker)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.stackedWidget = QStackedWidget(Package_Maker)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setInputMethodHints(Qt.ImhNone)
        self.stackedWidget.setFrameShape(QFrame.Box)
        self.global_page = QWidget()
        self.global_page.setObjectName(u"global_page")
        self.gridLayout_5 = QGridLayout(self.global_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.global_page)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.WinPanel)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setLineWidth(0)
        self.label.setTextFormat(Qt.RichText)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.main_buttonBox = QDialogButtonBox(self.global_page)
        self.main_buttonBox.setObjectName(u"main_buttonBox")
        self.main_buttonBox.setOrientation(Qt.Horizontal)
        self.main_buttonBox.setStandardButtons(QDialogButtonBox.Abort|QDialogButtonBox.Apply)

        self.gridLayout_2.addWidget(self.main_buttonBox, 2, 0, 1, 1)

        self.frame = QFrame(self.global_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(9)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.destination_comboBox = QComboBox(self.frame)
        self.destination_comboBox.addItem("")
        self.destination_comboBox.setObjectName(u"destination_comboBox")

        self.gridLayout.addWidget(self.destination_comboBox, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.job_comboBox = QComboBox(self.frame)
        self.job_comboBox.addItem("")
        self.job_comboBox.setObjectName(u"job_comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.job_comboBox.sizePolicy().hasHeightForWidth())
        self.job_comboBox.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.job_comboBox, 1, 1, 1, 1)

        self.pkg_type_label = QLabel(self.frame)
        self.pkg_type_label.setObjectName(u"pkg_type_label")
        self.pkg_type_label.setFont(font1)

        self.gridLayout.addWidget(self.pkg_type_label, 2, 0, 1, 1)

        self.pkg_type_comboBox = QComboBox(self.frame)
        self.pkg_type_comboBox.addItem("")
        self.pkg_type_comboBox.addItem("")
        self.pkg_type_comboBox.addItem("")
        self.pkg_type_comboBox.addItem("")
        self.pkg_type_comboBox.setObjectName(u"pkg_type_comboBox")

        self.gridLayout.addWidget(self.pkg_type_comboBox, 2, 1, 1, 1)

        self.vendor_name_label = QLabel(self.frame)
        self.vendor_name_label.setObjectName(u"vendor_name_label")
        self.vendor_name_label.setFont(font1)

        self.gridLayout.addWidget(self.vendor_name_label, 3, 0, 1, 1)

        self.vendor_name_comboBox = QComboBox(self.frame)
        self.vendor_name_comboBox.addItem("")
        self.vendor_name_comboBox.setObjectName(u"vendor_name_comboBox")

        self.gridLayout.addWidget(self.vendor_name_comboBox, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.global_page)
        self.shot_page = QWidget()
        self.shot_page.setObjectName(u"shot_page")
        self.gridLayout_3 = QGridLayout(self.shot_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.line_4 = QFrame(self.shot_page)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_4, 5, 0, 1, 1)

        self.line_5 = QFrame(self.shot_page)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 2, 0, 1, 1)

        self.listWidget = QListWidget(self.shot_page)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy2)
        self.listWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget.setMovement(QListView.Free)
        self.listWidget.setResizeMode(QListView.Adjust)

        self.gridLayout_3.addWidget(self.listWidget, 6, 0, 1, 1)

        self.selected_info_textEdit = QTextEdit(self.shot_page)
        self.selected_info_textEdit.setObjectName(u"selected_info_textEdit")
        self.selected_info_textEdit.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.selected_info_textEdit.sizePolicy().hasHeightForWidth())
        self.selected_info_textEdit.setSizePolicy(sizePolicy3)
        self.selected_info_textEdit.setMinimumSize(QSize(0, 22))
        self.selected_info_textEdit.setMaximumSize(QSize(16777215, 22))
        self.selected_info_textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.selected_info_textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.selected_info_textEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.gridLayout_3.addWidget(self.selected_info_textEdit, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.title_label_header = QLabel(self.shot_page)
        self.title_label_header.setObjectName(u"title_label_header")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.title_label_header.sizePolicy().hasHeightForWidth())
        self.title_label_header.setSizePolicy(sizePolicy4)
        self.title_label_header.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(10)
        self.title_label_header.setFont(font2)

        self.horizontalLayout_3.addWidget(self.title_label_header)

        self.title_label = QLabel(self.shot_page)
        self.title_label.setObjectName(u"title_label")
        font3 = QFont()
        font3.setFamily(u"Times New Roman")
        font3.setPointSize(17)
        font3.setBold(True)
        font3.setWeight(75)
        self.title_label.setFont(font3)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.title_label)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.shot_select_lineEdit = QLineEdit(self.shot_page)
        self.shot_select_lineEdit.setObjectName(u"shot_select_lineEdit")
        self.shot_select_lineEdit.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.shot_select_lineEdit.sizePolicy().hasHeightForWidth())
        self.shot_select_lineEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.shot_select_lineEdit)

        self.asset_pushButton = QPushButton(self.shot_page)
        self.asset_pushButton.setObjectName(u"asset_pushButton")

        self.horizontalLayout.addWidget(self.asset_pushButton)

        self.shot_pushButton = QPushButton(self.shot_page)
        self.shot_pushButton.setObjectName(u"shot_pushButton")

        self.horizontalLayout.addWidget(self.shot_pushButton)

        self.horizontalSpacer_5 = QSpacerItem(66, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.shot_cancel_pushButton = QPushButton(self.shot_page)
        self.shot_cancel_pushButton.setObjectName(u"shot_cancel_pushButton")

        self.horizontalLayout_2.addWidget(self.shot_cancel_pushButton)

        self.shot_view_pushButton = QPushButton(self.shot_page)
        self.shot_view_pushButton.setObjectName(u"shot_view_pushButton")

        self.horizontalLayout_2.addWidget(self.shot_view_pushButton)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pkg_name_label_header = QLabel(self.shot_page)
        self.pkg_name_label_header.setObjectName(u"pkg_name_label_header")
        sizePolicy4.setHeightForWidth(self.pkg_name_label_header.sizePolicy().hasHeightForWidth())
        self.pkg_name_label_header.setSizePolicy(sizePolicy4)
        self.pkg_name_label_header.setFont(font2)

        self.horizontalLayout_4.addWidget(self.pkg_name_label_header)

        self.pkg_name_label = QLabel(self.shot_page)
        self.pkg_name_label.setObjectName(u"pkg_name_label")
        font4 = QFont()
        font4.setFamily(u"Times New Roman")
        font4.setPointSize(15)
        font4.setBold(True)
        font4.setWeight(75)
        self.pkg_name_label.setFont(font4)

        self.horizontalLayout_4.addWidget(self.pkg_name_label)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.shot_page)
        self.summary_page = QWidget()
        self.summary_page.setObjectName(u"summary_page")
        self.gridLayout_4 = QGridLayout(self.summary_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.summary_title_label_header = QLabel(self.summary_page)
        self.summary_title_label_header.setObjectName(u"summary_title_label_header")
        sizePolicy4.setHeightForWidth(self.summary_title_label_header.sizePolicy().hasHeightForWidth())
        self.summary_title_label_header.setSizePolicy(sizePolicy4)
        self.summary_title_label_header.setMinimumSize(QSize(0, 0))
        self.summary_title_label_header.setFont(font2)

        self.horizontalLayout_5.addWidget(self.summary_title_label_header)

        self.summary_title_label = QLabel(self.summary_page)
        self.summary_title_label.setObjectName(u"summary_title_label")
        self.summary_title_label.setFont(font3)
        self.summary_title_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.summary_title_label)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.summary_pkg_name_label_header = QLabel(self.summary_page)
        self.summary_pkg_name_label_header.setObjectName(u"summary_pkg_name_label_header")
        sizePolicy4.setHeightForWidth(self.summary_pkg_name_label_header.sizePolicy().hasHeightForWidth())
        self.summary_pkg_name_label_header.setSizePolicy(sizePolicy4)
        self.summary_pkg_name_label_header.setFont(font2)

        self.horizontalLayout_6.addWidget(self.summary_pkg_name_label_header)

        self.summary_pkg_name_label = QLabel(self.summary_page)
        self.summary_pkg_name_label.setObjectName(u"summary_pkg_name_label")
        self.summary_pkg_name_label.setFont(font4)

        self.horizontalLayout_6.addWidget(self.summary_pkg_name_label)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.line = QFrame(self.summary_page)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 2, 0, 1, 1)

        self.summary_tableWidget = QTableWidget(self.summary_page)
        self.summary_tableWidget.setObjectName(u"summary_tableWidget")

        self.gridLayout_4.addWidget(self.summary_tableWidget, 3, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.summary_cancel_pushButton = QPushButton(self.summary_page)
        self.summary_cancel_pushButton.setObjectName(u"summary_cancel_pushButton")

        self.horizontalLayout_7.addWidget(self.summary_cancel_pushButton)

        self.pkg_create_pushButton = QPushButton(self.summary_page)
        self.pkg_create_pushButton.setObjectName(u"pkg_create_pushButton")

        self.horizontalLayout_7.addWidget(self.pkg_create_pushButton)


        self.gridLayout_4.addLayout(self.horizontalLayout_7, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.summary_page)
        self.exit_page = QWidget()
        self.exit_page.setObjectName(u"exit_page")
        self.gridLayout_7 = QGridLayout(self.exit_page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pkg_name_label_header_2 = QLabel(self.exit_page)
        self.pkg_name_label_header_2.setObjectName(u"pkg_name_label_header_2")
        sizePolicy4.setHeightForWidth(self.pkg_name_label_header_2.sizePolicy().hasHeightForWidth())
        self.pkg_name_label_header_2.setSizePolicy(sizePolicy4)
        self.pkg_name_label_header_2.setFont(font2)

        self.horizontalLayout_8.addWidget(self.pkg_name_label_header_2)

        self.pkg_name_exit_label = QLabel(self.exit_page)
        self.pkg_name_exit_label.setObjectName(u"pkg_name_exit_label")
        self.pkg_name_exit_label.setFont(font4)

        self.horizontalLayout_8.addWidget(self.pkg_name_exit_label)


        self.gridLayout_7.addLayout(self.horizontalLayout_8, 0, 0, 1, 3)

        self.done_pushButton = QPushButton(self.exit_page)
        self.done_pushButton.setObjectName(u"done_pushButton")

        self.gridLayout_7.addWidget(self.done_pushButton, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(132, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.open_pkg_pushButton = QPushButton(self.exit_page)
        self.open_pkg_pushButton.setObjectName(u"open_pkg_pushButton")

        self.gridLayout_7.addWidget(self.open_pkg_pushButton, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.exit_page)

        self.gridLayout_6.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(Package_Maker)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Package_Maker)
    # setupUi

    def retranslateUi(self, Package_Maker):
        Package_Maker.setWindowTitle(QCoreApplication.translate("Package_Maker", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Package_Maker", u"PACKAGE MAKER", None))
        self.label_2.setText(QCoreApplication.translate("Package_Maker", u"Destination:- ", None))
        self.destination_comboBox.setItemText(0, QCoreApplication.translate("Package_Maker", u"Select", None))

        self.label_3.setText(QCoreApplication.translate("Package_Maker", u" Job :- ", None))
        self.job_comboBox.setItemText(0, QCoreApplication.translate("Package_Maker", u"Select", None))

        self.pkg_type_label.setText(QCoreApplication.translate("Package_Maker", u"Package Type:", None))
        self.pkg_type_comboBox.setItemText(0, QCoreApplication.translate("Package_Maker", u"Select", None))
        self.pkg_type_comboBox.setItemText(1, QCoreApplication.translate("Package_Maker", u"client", None))
        self.pkg_type_comboBox.setItemText(2, QCoreApplication.translate("Package_Maker", u"vendor", None))
        self.pkg_type_comboBox.setItemText(3, QCoreApplication.translate("Package_Maker", u"local", None))

        self.vendor_name_label.setText(QCoreApplication.translate("Package_Maker", u"vendor name", None))
        self.vendor_name_comboBox.setItemText(0, QCoreApplication.translate("Package_Maker", u"Select", None))

        self.selected_info_textEdit.setHtml(QCoreApplication.translate("Package_Maker", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.title_label_header.setText(QCoreApplication.translate("Package_Maker", u"Title:- ", None))
        self.title_label.setText("")
        self.asset_pushButton.setText(QCoreApplication.translate("Package_Maker", u"+ ASSET", None))
        self.shot_pushButton.setText(QCoreApplication.translate("Package_Maker", u"+ SHOT", None))
        self.shot_cancel_pushButton.setText(QCoreApplication.translate("Package_Maker", u"Cancel", None))
        self.shot_view_pushButton.setText(QCoreApplication.translate("Package_Maker", u"View Summary", None))
        self.pkg_name_label_header.setText(QCoreApplication.translate("Package_Maker", u"PKG Name :-", None))
        self.pkg_name_label.setText("")
        self.summary_title_label_header.setText(QCoreApplication.translate("Package_Maker", u"Title:- ", None))
        self.summary_title_label.setText("")
        self.summary_pkg_name_label_header.setText(QCoreApplication.translate("Package_Maker", u"PKG Name :-", None))
        self.summary_pkg_name_label.setText("")
        self.summary_cancel_pushButton.setText(QCoreApplication.translate("Package_Maker", u"Cancel", None))
        self.pkg_create_pushButton.setText(QCoreApplication.translate("Package_Maker", u"Create Package", None))
        self.pkg_name_label_header_2.setText(QCoreApplication.translate("Package_Maker", u"PKG Name :-", None))
        self.pkg_name_exit_label.setText("")
        self.done_pushButton.setText(QCoreApplication.translate("Package_Maker", u"Done", None))
        self.open_pkg_pushButton.setText(QCoreApplication.translate("Package_Maker", u"Open Package", None))
    # retranslateUi

