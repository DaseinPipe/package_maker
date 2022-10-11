import sys
import os
from PySide2.QtWidgets import QApplication, QDialog, QToolButton, QLineEdit, QTableWidgetItem, QComboBox, QHeaderView, QMessageBox
from PySide2.QtCore import Qt
from PySide2.QtGui import QColor
from package_maker.src.resource import custom_file_dailog, file_importer, message_box
from package_maker.src.utils import exr_utils, general_utils
from package_maker.src.config.config_main import *


class FileImporterWidget(file_importer.Ui_File_Importer, QDialog):

    def __init__(self,pkg_dir, show_data=None):
        super(FileImporterWidget, self).__init__()
        self.show_data = show_data or get_show_data(os.environ.get(('show')))
        self.setupUi(self)
        self.pkg_dir = pkg_dir
        # self.setModal(True)
        self.populate()
        self.connection()
        self.set_shot_version()
        self.import_data = None
        horizontalHeader = self.fi_tableWidget.horizontalHeader()
        horizontalHeader.resizeSection(0, 30)
        horizontalHeader.setSectionResizeMode(1, QHeaderView.Stretch)
        horizontalHeader.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        horizontalHeader.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        horizontalHeader.resizeSection(4, 100)
        self.fi_tableWidget.setColumnHidden(3, True)

    def populate(self):
        self.fi_shot_version_label.setHidden(True)
        self.fi_shot_version_comboBox.setHidden(True)
        shot_line_edit = QLineEdit(self)
        shot_line_edit.setFrame(False)
        shot_line_edit.resize(self.fi_shot_comboBox.sizeHint())
        self.fi_shot_comboBox.setLineEdit(shot_line_edit)
        self.fi_shot_comboBox.clear()
        self.fi_discipline_comboBox.clear()
        self.fi_plate_version_comboBox.clear()
        self.fi_shot_version_comboBox.clear()
        discipline_list = self.show_data.get('discipline', global_discipline)

        shot_list = general_utils.get_shots(self.item_data)
        self.fi_discipline_comboBox.addItems(discipline_list)
        self.fi_shot_comboBox.addItems(shot_list)
        plate_padding = int(self.show_data.get("plate_version_padding", "2"))
        shot_padding = int(self.show_data.get("shot_version_padding", "3"))
        self.fi_shot_version_comboBox.addItems(
            [str(each).zfill(shot_padding) for each in range(1, 50)]
        )
        self.fi_plate_version_comboBox.addItems(
            [str(each).zfill(plate_padding) for each in range(1, 10)]
        )

    def connection(self):
        self.fi_shot_comboBox.currentTextChanged.connect(self.set_shot_version)
        self.fi_discipline_comboBox.currentTextChanged.connect(self.refresh_all)
        self.fi_import_pushButton.clicked.connect(self.fi_import)
        self.fi_apply_pushButton.clicked.connect(self.fi_apply)
        self.fi_cancel_pushButton.clicked.connect(self.close)

    def refresh_row(self, row, auto_assume=True):
        discipline = self.fi_discipline_comboBox.currentText()
        dirpath_item = self.fi_tableWidget.item(row, 1)
        filename_item = self.fi_tableWidget.item(row, 2)
        custom_dropdown_widget = self.fi_tableWidget.cellWidget(row, 3)
        pkg_type_dropdown_widget = self.fi_tableWidget.cellWidget(row, 4)
        filepath = os.path.join(dirpath_item.text(), filename_item.text()).replace('\\', '/')
        _, ext = os.path.splitext(filename_item.text())
        if auto_assume:
            if general_utils.get_custom_element_descs(self.item_data) and ext == '.exr':
                pkg_dir_type = 'custom'
                self.fi_tableWidget.setColumnHidden(3, False)
                custom_dropdown_widget.setEnabled(True)
            else:
                custom_dropdown_widget.setCurrentText('')
                pkg_dir_type = general_utils.assumed_pkg_type(discipline, filepath)
            pkg_type_dropdown_widget.setCurrentText(pkg_dir_type)
        else:
            pkg_dir_type = pkg_type_dropdown_widget.currentText()
        if pkg_dir_type == 'select':
            filename_item.setBackgroundColor(QColor('#993300'))
        else:
            filename_item.setBackgroundColor(QColor('#FFFFFF'))


    def refresh_all(self):
        self.set_shot_version()
        allRows = self.fi_tableWidget.rowCount()
        has_custom_pkg_type = False
        for row in range(0, allRows):
            self.refresh_row(row)
            if self.fi_tableWidget.cellWidget(row, 4).currentText() == 'custom':
                has_custom_pkg_type = True

        if has_custom_pkg_type:
            self.fi_tableWidget.setColumnHidden(3, False)
        else:
            self.fi_tableWidget.setColumnHidden(3, True)
    @property
    def item_data(self):
        return {
            'pkg_dir': self.pkg_dir,
            'shot': self.fi_shot_comboBox.currentText(),
            'discipline': self.fi_discipline_comboBox.currentText(),
        }

    def set_shot_version(self):
        _shot_version_num = general_utils.get_latest_shot_version(self.item_data)
        shot_padding = int(self.show_data.get("shot_version_padding", "3"))
        self.shot_version_num = str(_shot_version_num).zfill(shot_padding)

    def validate_pkg_type(self):
        allRows = self.fi_tableWidget.rowCount()
        for row in range(0, allRows):
            dropdown_widget = self.fi_tableWidget.cellWidget(row, 4)
            if dropdown_widget.currentText() == 'select':
                return False
        return True

    def row_cancel_widget(self):

        def fi_row_delete(btn):
            row = self.fi_tableWidget.indexAt(btn.pos()).row()
            self.fi_tableWidget.removeRow(row)

        fi_table_cancel_pushButton = QToolButton(self.fi_tableWidget)
        fi_table_cancel_pushButton.clicked.connect(lambda: fi_row_delete(fi_table_cancel_pushButton))
        return fi_table_cancel_pushButton

    def row_dropdown_widget(self, type):
        '''
        :param type: enum
        :valid types:- valid types 'custom' or 'pkg_type'
        :return: QComboBox Widget
        '''
        row_comboBox = QComboBox(self.fi_tableWidget)
        if type == 'pkg_type':
            content_list = list(self.show_data.get('pkg_dir_types', global_pkg_dir_types).keys())
        elif type == 'custom':
            content_list = general_utils.get_custom_element_descs(self.item_data) or []
            content_list.append('')
        else:
            return row_comboBox
        row_comboBox.addItems(content_list)
        return row_comboBox

    def remove_select_rows(self):
        allRows = self.fi_tableWidget.rowCount()
        for row in range(0, allRows):
            dropdown_widget = self.fi_tableWidget.cellWidget(row, 4)
            if dropdown_widget.currentText() == 'select':
                self.fi_tableWidget.removeRow(row)
                return self.remove_select_rows()
        return



    def fi_apply(self):
        if not self.validate_pkg_type():
            msg_widget = message_box.pop_up(
                messType='quest',
                messTitle='Source File have issue cells.',
                messText='Do you want to remove all red cell and proceed?',
                buttons=QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                defaultButton=QMessageBox.No
            )
            if msg_widget != QMessageBox.Yes:
                return
            self.remove_select_rows()

        allRows = self.fi_tableWidget.rowCount()
        filelist = []
        for row in range(0, allRows):
            dirpath = self.fi_tableWidget.item(row, 1).text()
            filename = self.fi_tableWidget.item(row, 2).text()
            pkg_dir_type = self.fi_tableWidget.cellWidget(row, 4).currentText()
            filepath = os.path.join(dirpath, filename).replace('\\', '/')
            filelist.append(
                {
                    'source_path': filepath,
                    'pkg_dir_type': pkg_dir_type,
                    'custom_name': self.fi_tableWidget.cellWidget(row, 3).currentText(),
                    'ext': os.path.splitext(filepath)[-1].replace('.', '')
                }
            )
        plate_prefix = self.show_data.get("plate_version_prefix", "master")
        shot_prefix = self.show_data.get("shot_version_prefix", "v")
        self.import_data = {
            'shot': self.fi_shot_comboBox.currentText(),
            'discipline': self.fi_discipline_comboBox.currentText(),
            'plate_version_num': self.fi_plate_version_comboBox.currentText(),
            'shot_version_num': self.shot_version_num,
            'plate_version_prefix': plate_prefix,
            'shot_version_prefix': shot_prefix,
            'files': filelist
        }
        self.close()

    def fi_import(self):
        custom_fileDailog = custom_file_dailog.FileDialog()
        custom_fileDailog.show()
        custom_fileDailog.exec_()
        files = custom_fileDailog.filesSelected()
        if not files:
            return
        extended_files = []
        for file in files:
            if os.path.isdir(file):
                extended_files.extend(exr_utils.extend_files(file))
            else:
                extended_files.append(file.replace('\\', '/'))
        for file in extended_files:
            dirpath, filename = os.path.split(file)
            current_row_count = self.fi_tableWidget.rowCount()
            pkg_dir_dropdown_widget = self.row_dropdown_widget(type='pkg_type')
            args = [pkg_dir_dropdown_widget, current_row_count]
            pkg_dir_dropdown_widget.currentIndexChanged.connect(lambda _, args=args: self.pkg_dir_dropdown_exec(args=args))
            custom_dropdown_widget = self.row_dropdown_widget(type='custom')
            custom_dropdown_widget.setEnabled(False)
            filename_item = QTableWidgetItem(filename)
            self.fi_tableWidget.insertRow(current_row_count)
            self.fi_tableWidget.setCellWidget(current_row_count, 0, self.row_cancel_widget())
            self.fi_tableWidget.setItem(current_row_count, 1, QTableWidgetItem(dirpath))
            self.fi_tableWidget.setItem(current_row_count, 2, filename_item)
            self.fi_tableWidget.setCellWidget(current_row_count, 3, custom_dropdown_widget)
            self.fi_tableWidget.setCellWidget(current_row_count, 4, pkg_dir_dropdown_widget)
            discipline = self.fi_discipline_comboBox.currentText()
            _, ext = os.path.splitext(filename)
            if general_utils.get_custom_element_descs(self.item_data) and ext == '.exr':
                pkg_dir_type = 'custom'
                self.fi_tableWidget.setColumnHidden(3, False)
                custom_dropdown_widget.setEnabled(True)
            else:
                pkg_dir_type = general_utils.assumed_pkg_type(discipline, file)
            custom_dropdown_widget.setCurrentText('')
            pkg_dir_dropdown_widget.setCurrentText(pkg_dir_type)
            if pkg_dir_type == 'select':
                filename_item.setBackgroundColor(QColor('#993300'))

    def pkg_dir_dropdown_exec(self, args):


        def custom_cell_process(dropdown_widget, row):
            custon_cell_item = self.fi_tableWidget.item(row, 4)
            if not custon_cell_item:
                return
            flags = custon_cell_item.flags()
            if dropdown_widget.currentText() == 'custom':
                flags |= Qt.ItemIsEditable
            else:
                custon_cell_item.setText('')
                flags &= ~Qt.ItemIsEditable
            custon_cell_item.setFlags(flags)

        dropdown_widget, row = args
        self.refresh_row(row, auto_assume=False)
        custom_cell_process(dropdown_widget, row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pkg_dir = r'C:/mnt/mpcparis/A5/io/To_Client/packages'
    w = FileImporterWidget(pkg_dir=pkg_dir)
    w.show()
    app.exec_()
