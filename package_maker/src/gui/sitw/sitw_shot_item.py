import sys
from package_maker.src.config.config_client import *
from PySide2.QtWidgets import QApplication, QTableWidgetItem, QComboBox, QHeaderView
from package_maker.src.gui.gui_shot_item import ShotItemWidget
from package_maker.src.gui.sitw import sitw_file_importer
from package_maker.src.utils import general_utils, package_dir_utiles, sitw_utils


class SitwShotItemWidget(ShotItemWidget, object):

    def __init__(self, _global_pkg_data, pkg_type='shot', show_data=None, parent_item=None, parent_widget=None):
        super(SitwShotItemWidget, self).__init__(
            _global_pkg_data, pkg_type, show_data, parent_item, parent_widget
        )
        self.global_pkg_data = _global_pkg_data
        self.pkg_type = _global_pkg_data.get('pkg_dir')

    def populate(self):
        self.add_column('shots')
        super(SitwShotItemWidget, self).populate()
        self.hide_header_item('pkg item', True)
        self.hide_header_item('custom_name', True)

    def add_exec(self, from_btn=False):
        self.from_add_btn = from_btn
        self.base_data = self.get_fi_data()
        if not self.base_data:
            return
        self.base_data.update(self.global_pkg_data)
        self.shot = self.base_data.get('shot', UNKNOWN)
        self.discipline = self.base_data.get('discipline', UNKNOWN)

        if not from_btn:
            self.base_data['pkg_type'] = self.pkg_type

            self.swi_lineEdit.setText(self.pkg_name)
        for file_data in self.base_data.get('files'):
            file_data['pkg_type'] = self.pkg_type
            file_data['job'] = self.job

            file_data.update(self.base_data)
            file_data.pop('files')
            path_data, destination_path = package_dir_utiles.get_destination_info(
                file_data['pkg_dir_type'], file_data.copy()
            )
            file_data['destination_path'] = destination_path
            print(destination_path)
            self.add_row(
                add_row_config=self.add_row_config(),
                file_data=file_data.copy()
            )
        self.set_package_path_dups()
        if self.parent_item and self.swi_dropdown_toolButton.text() == 'v':
            self.parent_item.setSizeHint(self.swi_container_widget.sizeHint())

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

    def add_shots_row(self, current_row_count, file_data):
        shots_column_no = self.get_column_no('shots')
        shots_dropdown_widget = self.shot_dropdown_widget()
        self.swi_tableWidget.setCellWidget(current_row_count, shots_column_no, shots_dropdown_widget)
        shot_name = file_data.get('shot')
        shots_dropdown_widget.setCurrentText(shot_name)

    def add_row_config(self):
        _add_row_config = super(SitwShotItemWidget, self).add_row_config()
        _add_row_config['add_custom_name_row'] = False
        return _add_row_config

    def add_row(self, add_row_config, file_data):
        super(SitwShotItemWidget, self).add_row(
            add_row_config=self.add_row_config(),
            file_data=file_data
        )
        current_row_count = self.swi_tableWidget.rowCount()
        self.add_shots_row(current_row_count - 1, file_data)

    def get_fi_data(self):
        fi_widget = sitw_file_importer.SitwFileImporter(
            pkg_dir=self.pkg_dir, pkg_for='client', show_data=None)
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
    global_pkg_data = {'date': '2023_05_02', 'vendor': 'dasein', 'root_dir': '/mnt/sitw', 'show': 'sitw',
                       'pkg_version_prefix': 'send_', 'pkg_version_num': '01', 'pkg_dir': '/mnt/sitw/io/to_client',
                       'pkg_for': 'client', 'vendor_name': 'UNKNOWN'}
    os.environ['show'] = 'sitw'
    w = SitwShotItemWidget(_global_pkg_data=global_pkg_data)
    w.show()
    app.exec_()

t = dict(discipline='roto', files=[
    {'source_path': '/mnt/sitw/io/from_client/202302220/230217_SITW_VFX_LIST_2_Uel_Dasein_VFX_mos.mov', 'ext': 'mov',
     'shot_version_num': '001', 'shot_version_prefix': 'v', 'shot': '001air_0030', 'pkg_dir_type': 'for_approval',
     'filename': '230217_SITW_VFX_LIST_2_Uel_Dasein_VFX_mos.mov', 'pkg_version': 'A'},
    {'source_path': '/mnt/sitw/io/from_client/202302220/230217_SITW_VFX_LIST_2_Uel_Dasein_VFX_mos_CLEAN.mov',
     'ext': 'mov', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'shot': '007hot_0010',
     'pkg_dir_type': 'for_approval', 'filename': '230217_SITW_VFX_LIST_2_Uel_Dasein_VFX_mos_CLEAN.mov',
     'pkg_version': 'A'},
    {
        'source_path': '/mnt/mpcparis/LABETE/io/from_client/PKG-20230404-mpc-labete-v0005/20230404-mpc-labete-v0005/shot-003_010-prep-master01-mpc-v001/element/003_010-src-master01-v002-aces-exr',
        'ext': '', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'shot': '001air_0030',
        'pkg_dir_type': 'for_approval', 'filename': '003_010-src-master01-v002-aces-exr',
        'pkg_version': 'A'}])
