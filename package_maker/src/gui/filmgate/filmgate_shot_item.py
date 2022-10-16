import re
import sys
import os
from PySide2.QtWidgets import QApplication,  QTableWidgetItem, QComboBox, QHeaderView, QMessageBox
from PySide2.QtCore import Qt
from package_maker.src.resource import message_box
from package_maker.src.gui.gui_shot_item import ShotItemWidget
from package_maker.src.gui.filmgate import filmgate_file_importer
from package_maker.src.utils import general_utils


class FilmgateShotItemWidget(ShotItemWidget, object):

    def __init__(self,global_pkg_data, pkg_type='shot', show_data=None, parent_item=None, parent_widget=None):
        super(FilmgateShotItemWidget, self).__init__(
            global_pkg_data, pkg_type, show_data, parent_item, parent_widget
        )
        self.pkg_type = global_pkg_data.get('pkg_dir')


    def get_column_no(self, column_name):
        swi_tableWidget = self.swi_tableWidget
        for column in range(0, swi_tableWidget.columnCount()):
            if column_name == swi_tableWidget.horizontalHeaderItem(column).text():
                return column



    def hide_header_item(self, header_name, state=True):
        header_column_no = self.get_column_no(header_name)
        self.swi_tableWidget.setColumnHidden(header_column_no, state)


    def add_column(self, column_name):
        tableWidget = self.swi_tableWidget
        tableWidget.setColumnHidden(4, True)
        current_column_count = tableWidget.columnCount()
        tableWidget.insertColumn(current_column_count)
        tableWidget.setHorizontalHeaderItem(current_column_count, QTableWidgetItem(column_name))
        horizontalHeader = tableWidget.horizontalHeader()
        shot_column_no = self.get_column_no(column_name=column_name)
        horizontalHeader.setSectionResizeMode(shot_column_no, QHeaderView.ResizeToContents)

    def populate(self):
        self.add_column('shots')
        super(FilmgateShotItemWidget, self).populate()
        self.hide_header_item('pkg item', True)
        self.hide_header_item('custom_name', True)
        pass


    def add_shots_row(self, current_row_count, file_data ):
        shots_column_no = self.get_column_no('shots')
        shots_dropdown_widget = self.shot_dropdown_widget()
        self.swi_tableWidget.setCellWidget(current_row_count, shots_column_no, shots_dropdown_widget)
        shot_name = file_data.get('shot')
        shots_dropdown_widget.setCurrentText(shot_name)



    def add_row_config(self):
        _add_row_config = super(FilmgateShotItemWidget, self).add_row_config()
        _add_row_config['add_custom_name_row'] = False
        return _add_row_config


    def add_row(self, add_row_config, file_data):
        super(FilmgateShotItemWidget, self).add_row(
            add_row_config=self.add_row_config(),
            file_data=file_data
        )
        current_row_count = self.swi_tableWidget.rowCount()
        self.add_shots_row(current_row_count-1, file_data)





    def get_fi_data(self):
        fi_widget = filmgate_file_importer.FilmgateFileImporter(pkg_dir=self.pkg_dir, show_data=None)
        fi_widget.show()
        fi_widget.exec_()
        return fi_widget.import_data

    def shot_dropdown_widget(self):

        row_comboBox = QComboBox(self.swi_tableWidget)
        shot_list = general_utils.get_shots(self.item_data)
        shot_list.insert(0, 'select')
        row_comboBox.addItems(shot_list)
        setattr(row_comboBox, "allItems", lambda: [row_comboBox.itemText(i) for i in range(row_comboBox.count())])
        return row_comboBox


if __name__ == '__main__':

    app = QApplication(sys.argv)
    global_pkg_data = {'date': '20221008', 'vendor': 'dasein', 'show': 'trm', 'pkg_version_prefix': 'v',
                       'pkg_version_num': '0021', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package'}

    w = FilmgateShotItemWidget(global_pkg_data=global_pkg_data)
    w.show()
    app.exec_()