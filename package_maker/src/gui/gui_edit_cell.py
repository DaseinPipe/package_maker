import sys
from PySide2.QtWidgets import QApplication, QDialog, QTableWidgetItem, QHeaderView, QDialogButtonBox
from PySide2.QtCore import Qt

from package_maker.src.resource import edit_cell
from package_maker.src.utils import package_dir_utiles
from package_maker.src.config.config_main import *


class EditCellWidget(edit_cell.Ui_Frame, QDialog):

    def __init__(self, file_data, show_data=None):
        super(EditCellWidget, self).__init__()
        self.setupUi(self)
        self.file_data = file_data
        self.revised_file_data = None
        self.pkg_dir_type = self.file_data['pkg_dir_type']
        self.ok_btn = self.buttonBox.button(QDialogButtonBox.Ok)
        self.cancel_btn = self.buttonBox.button(QDialogButtonBox.Cancel)
        self.show_data = show_data or get_show_data(os.environ.get(('show')))
        horizontalHeader = self.edit_tableWidget.horizontalHeader()
        horizontalHeader.setSectionResizeMode(0, QHeaderView.Stretch)
        horizontalHeader.setSectionResizeMode(1, QHeaderView.Stretch)
        self.populate()
        self.connections()

    def connections(self):
        self.ok_btn.clicked.connect(self.ok)
        self.cancel_btn.clicked.connect(self.close)

    def populate(self):
        self.pkg_dir_type_lineEdit.setText(self.pkg_dir_type)
        path_data, _ = package_dir_utiles.get_destination_info(self.pkg_dir_type, self.file_data)
        for key, value in path_data.items():
            if value != UNKNOWN:
                continue
            current_row_count = self.edit_tableWidget.rowCount()
            key_item = QTableWidgetItem(key)
            self.edit_tableWidget.insertRow(current_row_count)
            self.edit_tableWidget.setItem(current_row_count, 0, key_item)
            self.edit_tableWidget.setItem(current_row_count, 1, QTableWidgetItem(value))
            flags = key_item.flags()
            flags &= ~Qt.ItemIsEditable
            key_item.setFlags(flags)
        self.setFixedSize(self.gridLayout.sizeHint())

    def ok(self):
        self.revised_file_data = self.file_data.copy()
        allRows = self.edit_tableWidget.rowCount()
        for row in range(0, allRows):
            key = self.edit_tableWidget.item(row, 0).text()
            value = self.edit_tableWidget.item(row, 1).text()
            self.revised_file_data[key] = value
        self.close()








if __name__ == '__main__':
    app = QApplication(sys.argv)
    base_data = {'pkg_dir': 'temp_dir',
                 'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705D/exr_seq/test.0-99@.exr', 'ext': 'exr',
                 'pkg_dir_type': 'for_approval', 'custom_name': '', 'shot': '080_bb_0375', 'discipline': 'roto',
                 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master',
                 'shot_version_prefix': 'v', 'date': '20221002', 'vendor': 'dasein', 'show': 'asterix',
                 'pkg_version_prefix': 'v', 'pkg_version_num': '0005', 'pkg_type': 'shot'}

    w = EditCellWidget(file_data=base_data)
    w.show()
    app.exec_()