import re
import sys
import os
from PySide2.QtWidgets import QApplication, QTableWidgetItem, QComboBox, QHeaderView, QMessageBox
from PySide2.QtGui import QColor
from package_maker.src.resource import message_box
from package_maker.src.gui.gui_file_importer import FileImporterWidget
from package_maker.src.utils import general_utils


class FilmgateFileImporter(FileImporterWidget, object):

    def __init__(self, pkg_dir, show_data=None):
        super(FilmgateFileImporter, self).__init__(pkg_dir, show_data)
        self.valid_ext_list = ['.exr']
        self.filmgate_populate()

    @property
    def hide_widget_list(self):
        return [
            self.fi_shot_comboBox,
            self.fi_shot_label,
            self.fi_plate_version_label,
            self.fi_plate_version_comboBox
        ]

    def add_column(self, column_name):
        tableWidget = self.fi_tableWidget
        tableWidget.setColumnHidden(4, True)
        current_column_count = tableWidget.columnCount()
        tableWidget.insertColumn(current_column_count)
        tableWidget.setHorizontalHeaderItem(current_column_count, QTableWidgetItem(column_name))
        horizontalHeader = self.fi_tableWidget.horizontalHeader()
        shot_column_no = self.get_column_no(column_name=column_name)
        horizontalHeader.setSectionResizeMode(shot_column_no, QHeaderView.ResizeToContents)

    def filmgate_populate(self):
        self.fi_discipline_comboBox.setCurrentText('comp')
        self.fi_discipline_comboBox.setEnabled(False)

        for each_widget in self.hide_widget_list:
            each_widget.setHidden(True)
        self.add_column('shots')

    def get_column_no(self, column_name):
        fi_tableWidget = self.fi_tableWidget
        for column in range(0, fi_tableWidget.columnCount()):
            if column_name == fi_tableWidget.horizontalHeaderItem(column).text():
                return column

    def validate_source_file(self, row_no):
        source_file_column_no = self.get_column_no(column_name='source_file')
        source_file_item = self.fi_tableWidget.item(row_no, source_file_column_no)
        source_filepath = source_file_item.text()
        _, ext = os.path.splitext(source_filepath)
        if not ext in self.valid_ext_list:
            source_file_item.setBackgroundColor(QColor('#993300'))
            return False
        return True

    def fi_import(self, **kwargs):
        super().fi_import(do_dropdown_process=False)
        fi_tableWidget = self.fi_tableWidget
        fi_tableWidget.setColumnHidden(3, True)
        self.set_shot_version()
        allRows = self.fi_tableWidget.rowCount()
        for row in range(0, allRows):
            shots_dropdown_widget = self.shot_dropdown_widget()
            shot_column_no = self.get_column_no(column_name='shots')
            fi_tableWidget.setCellWidget(row, shot_column_no, shots_dropdown_widget)
            shots_dropdown_widget.currentTextChanged.connect(self.shot_changed_event)
            if self.validate_source_file(row):
                self.set_assumed_shot(row)

    def set_assumed_shot(self, row_no):
        shot_column_no = self.get_column_no(column_name='shots')
        shot_item = self.fi_tableWidget.cellWidget(row_no, shot_column_no)
        shots = shot_item.allItems()
        source_file_column_no = self.get_column_no(column_name='source_file')
        source_file_item = self.fi_tableWidget.item(row_no, source_file_column_no)
        source_filepath = source_file_item.text()
        shot_name = general_utils.find_patten(source_filepath, shots, get_matched_pattern=True)
        if not shot_name:
            source_file_item.setBackgroundColor(QColor('#993300'))
            shot_name = 'select'
        shot_item.setCurrentText(shot_name)

    def shot_changed_event(self, state):
        if state == 'select':
            return
        row_no = self.fi_tableWidget.currentRow()
        source_file_column_no = self.get_column_no(column_name='source_file')
        source_file_item = self.fi_tableWidget.item(row_no, source_file_column_no)
        source_file_item.setBackgroundColor(QColor('#aaaaaa'))

    def validate_shots(self):
        allRows = self.fi_tableWidget.rowCount()
        shot_column_no = self.get_column_no('shots')
        for row in range(0, allRows):
            dropdown_widget = self.fi_tableWidget.cellWidget(row, shot_column_no)
            if dropdown_widget.currentText() == 'select':
                return False
        return True

    def pkg_dir_dropdown_exec(self, args):
        return None

    def remove_select_rows(self):
        allRows = self.fi_tableWidget.rowCount()
        shot_column_no = self.get_column_no('shots')
        for row in range(0, allRows):
            dropdown_widget = self.fi_tableWidget.cellWidget(row, shot_column_no)
            if dropdown_widget.currentText() == 'select':
                self.fi_tableWidget.removeRow(row)
                return self.remove_select_rows()
        return

    def fi_apply(self):

        if not self.validate_shots():
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
        shot_prefix = self.show_data.get("shot_version_prefix", "v")
        filelist = []
        for row in range(0, allRows):
            source_dir_column_no = self.get_column_no('source_dir')
            source_file_column_no = self.get_column_no(column_name='source_file')
            shot_column_no = self.get_column_no(column_name='shots')

            dirpath = self.fi_tableWidget.item(row, source_dir_column_no).text()
            filename = self.fi_tableWidget.item(row, source_file_column_no).text()
            shot = self.fi_tableWidget.cellWidget(row, shot_column_no).currentText()

            filepath = os.path.join(dirpath, filename).replace('\\', '/')
            item_data = self.item_data.copy()
            item_data['shot'] = shot
            self.set_shot_version(item_data=item_data)
            filelist.append(
                {
                    'source_path': filepath,
                    'ext': os.path.splitext(filepath)[-1].replace('.', ''),
                    'shot_version_num': self.shot_version_num,
                    'shot_version_prefix': shot_prefix,
                    'shot': shot,
                    'pkg_dir_type': 'for_approval',
                    'filename': filename,
                    'pkg_version': 'A',
                }
            )
        self.import_data = {
            'discipline': self.fi_discipline_comboBox.currentText(),
            'files': filelist
        }
        self.close()

    def shot_dropdown_widget(self):

        row_comboBox = QComboBox(self.fi_tableWidget)
        # print(self.item_data)
        shot_list = general_utils.get_shots(self.item_data)
        # print(shot_list)
        shot_list.insert(0, 'select')
        row_comboBox.addItems(shot_list)
        setattr(row_comboBox, "allItems", lambda: [row_comboBox.itemText(i) for i in range(row_comboBox.count())])
        return row_comboBox


if __name__ == '__main__':
    app = QApplication(sys.argv)
    os.environ['show'] = 'boderland'
    pkg_dir = r'/mnt/pb6/Filmgate/Boderland/io/To_Client/Package'
    w = FilmgateFileImporter(pkg_dir=pkg_dir)
    w.show()
    app.exec_()
