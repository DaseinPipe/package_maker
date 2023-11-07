import pathlib
import sys

from PySide2.QtWidgets import QApplication, QTableWidgetItem, QComboBox, QHeaderView
from package_maker.src.gui.gui_client_shot_item import ShotItemWidget
from package_maker.src.config.config_client import get_path
from package_maker.src.gui import gui_file_importer


class InternalShotItemWidget(ShotItemWidget, object):

    def __init__(self, _global_pkg_data, pkg_type='shot', show_data=None, parent_item=None, parent_widget=None):
        super(InternalShotItemWidget, self).__init__(
            _global_pkg_data, pkg_type, show_data, parent_item, parent_widget
        )


    def populate(self):
        super(InternalShotItemWidget, self).populate()
        self.hide_header_item('pkg item', True)
        self.hide_header_item('custom_name', True)

    def hide_header_item(self, header_name, state=True):
        header_column_no = self.get_column_no(header_name)
        self.swi_tableWidget.setColumnHidden(header_column_no, state)

    def add_column(self, column_name):
        tableWidget = self.swi_tableWidget
        tableWidget.setColumnHidden(4, True)
        current_column_count = tableWidget.columnCount()
        tableWidget.insertColumn(current_column_count)
        tableWidget.setHorizontalHeaderItem(current_column_count, QTableWidgetItem(column_name))

    def add_row_config(self):
        _add_row_config = super(InternalShotItemWidget, self).add_row_config()
        _add_row_config['add_custom_name_row'] = False
        return _add_row_config

    def add_row(self, add_row_config, file_data):
        super(InternalShotItemWidget, self).add_row(
            add_row_config=self.add_row_config(),
            file_data=file_data
        )

    def add_exec(self, from_btn=False):
        self.from_add_btn = from_btn
        self.base_data = self.get_fi_data()

        if not self.base_data:
            return
        self.base_data.update(self.global_pkg_data)
        # print(self.base_data)
        self.discipline = self.base_data['discipline']
        local_pkg_dir_template = get_path(self.job, 'local_pkg_dir')
        local_pkg_dir = local_pkg_dir_template.format(self.base_data)
        for file_data in self.base_data.get('files'):
            source_path = pathlib.Path(file_data['source_path'])
            source_name = source_path.name
            destination_path = pathlib.PurePath(local_pkg_dir, source_name)
            file_data['destination_path'] = str(destination_path)
            self.add_row(
                add_row_config=self.add_row_config(),
                file_data=file_data.copy()
            )
        self.set_package_path_dups()
        if self.parent_item and self.swi_dropdown_toolButton.text() == 'v':
            self.parent_item.setSizeHint(self.swi_container_widget.sizeHint())

    def get_fi_data(self):
        fi_widget = gui_file_importer.FileImporterWidget(current_pkg_dir=self.pkg_dir, pkg_for='local',
                                                         show_data=None)
        fi_widget.show()
        fi_widget.exec_()
        return fi_widget.import_data

    def add_pkg_type_row(self, file_data, current_row_count):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    global_pkg_data = {'date': '20221214', 'vendor': 'dasein', 'show': 'labete', 'pkg_version_prefix': 'v',
                       'pkg_version_num': '0004',
                       'pkg_dir': '/mnt/mpcparis/LABETE/io/to_shakti/packages', 'pkg_for': 'vendor',
                       'vendor_name': 'Shakti'}

    w = InternalShotItemWidget(_global_pkg_data=global_pkg_data)
    w.show()
    app.exec_()
