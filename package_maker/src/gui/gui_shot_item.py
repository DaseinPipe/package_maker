import random
import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QApplication, QDialog, QToolButton, QTableWidgetItem, QComboBox, QHeaderView

from package_maker.src.config.config_main import *
from package_maker.src.gui import gui_file_importer, gui_edit_cell
from package_maker.src.resource import shot_widget_item
from package_maker.src.utils import general_utils, package_dir_utiles


def cell_editable(item, status=False):
    flags = item.flags()
    if status:
        flags |= Qt.ItemIsEditable
    else:
        flags &= ~Qt.ItemIsEditable
    item.setFlags(flags)


class ShotItemWidget(shot_widget_item.Ui_swi_Frame, QDialog):
    def __init__(self, _global_pkg_data, pkg_type='shot', show_data=None, parent_item=None, parent_widget=None):
        super(ShotItemWidget, self).__init__()
        self.from_add_btn = None
        self.parent_item = parent_item
        self.parent_widget = parent_widget
        self.pkg_type = pkg_type
        self.global_pkg_data = _global_pkg_data
        self.pkg_dir = self.global_pkg_data.get('pkg_dir')
        self.job = _global_pkg_data.get('show', os.environ.get('show'))
        self.show_data = show_data or get_show_data(self.job)
        self.base_data = None
        self.shot = UNKNOWN
        self.discipline = UNKNOWN
        self.plate_version_num = UNKNOWN
        self.shot_version_num = UNKNOWN
        self.plate_version_prefix = UNKNOWN
        self.shot_version_prefix = UNKNOWN
        self.setupUi(self)
        self.populate()
        self.connection()

    def populate(self):
        self.swi_container_widget.setHidden(True)
        # self.swi_status_lineEdit.setHidden(True)
        horizontalHeader = self.swi_tableWidget.horizontalHeader()
        horizontalHeader.resizeSection(0, 30)
        horizontalHeader.setSectionResizeMode(1, QHeaderView.Stretch)
        horizontalHeader.setSectionResizeMode(2, QHeaderView.Stretch)
        horizontalHeader.resizeSection(3, 100)
        horizontalHeader.resizeSection(4, 100)
        self.swi_tableWidget.setColumnHidden(3, True)
        self.swi_tableWidget.setColumnHidden(5, True)
        self.add_exec()

    def connection(self):
        self.swi_dropdown_toolButton.clicked.connect(self.dropdown_exec)
        self.swi_delete_toolButton.clicked.connect(self.delete_exec)
        self.swi_add_pushButton.clicked.connect(lambda: self.add_exec(True))
        self.swi_tableWidget.itemClicked.connect(self.CellChanged)  # required for first selection
        self.swi_tableWidget.currentCellChanged.connect(self.CellChanged)
        self.swi_edit_pushButton.clicked.connect(self.cell_edit)

    def cell_edit(self):
        selected_item = self.swi_tableWidget.selectedItems()[0]
        destination_item = self.swi_tableWidget.item(selected_item.row(), 2)
        pkg_dir_type = self.swi_tableWidget.cellWidget(selected_item.row(), 4).currentText()
        path_data = self.swi_tableWidget.item(selected_item.row(), 5).text()
        if not path_data:
            return
        edit_cell_widget = gui_edit_cell.EditCellWidget(file_data=eval(path_data))
        edit_cell_widget.show()
        edit_cell_widget.exec_()
        revised_path_data = edit_cell_widget.revised_file_data
        if not revised_path_data:
            return
        _, destination_path = package_dir_utiles.get_destination_info(pkg_dir_type, revised_path_data)
        destination_item.setText(destination_path)
        destination_item.setBackgroundColor(QColor('#339966'))
        self.CellChanged(destination_item)

    def CellChanged(self, current):
        selected_item = self.swi_tableWidget.selectedItems()
        if not selected_item:
            self.swi_status_lineEdit.setText('')
            self.swi_edit_pushButton.setEnabled(False)
            return
        if not isinstance(current, int):
            self.swi_status_lineEdit.setText(current.text())

        if selected_item[0].column() == 2:
            destination_path = selected_item[0].text()
            has_error = general_utils.is_name_matched(destination_path, [UNKNOWN])
            if has_error:
                self.swi_edit_pushButton.setEnabled(True)
                return
        self.swi_edit_pushButton.setEnabled(False)

    def dropdown_exec(self):
        if self.swi_dropdown_toolButton.text() == '>':
            self.swi_container_widget.setHidden(False)
            self.swi_dropdown_toolButton.setText('v')
            if self.parent_item:
                self.parent_item.setSizeHint(self.sizeHint())
                self.parent_item.setSelected(True)
        elif self.swi_dropdown_toolButton.text() == 'v':
            self.swi_container_widget.setHidden(True)
            self.swi_dropdown_toolButton.setText('>')
            if self.parent_item:
                self.parent_item.setSizeHint(self.sizeHint())
                self.parent_item.setSelected(True)

    def delete_exec(self):
        self.swi_status_lineEdit.setText('')
        self.swi_edit_pushButton.setEnabled(False)
        if not self.parent_widget and not self.parent_item:
            return
        self.parent_widget.takeItem(self.parent_widget.row(self.parent_item))
        self.parent_item.setSizeHint(self.swi_container_widget.sizeHint())

    def get_fi_data(self):
        fi_widget = gui_file_importer.FileImporterWidget(self.pkg_dir)

        if self.import_data:
            if self.from_add_btn:
                fi_widget.fi_plate_version_comboBox.setCurrentText(self.import_data.get('plate_version_num'))
                fi_widget.fi_shot_comboBox.setCurrentText(self.import_data.get('shot'))
                fi_widget.fi_discipline_comboBox.setCurrentText(self.import_data.get('discipline'))
                fi_widget.fi_plate_version_comboBox.setEnabled(False)
                fi_widget.fi_shot_comboBox.setEnabled(False)
                fi_widget.fi_discipline_comboBox.setEnabled(False)

        fi_widget.show()
        fi_widget.exec_()
        return fi_widget.import_data

    def set_default_source_path_color(self):
        allRows = self.swi_tableWidget.rowCount()
        for row in range(0, allRows):
            source_item = self.swi_tableWidget.item(row, 1)
            source_item.setBackgroundColor('#aaaaaa')

    def set_package_path_dups(self):
        self.set_default_source_path_color()
        allRows = self.swi_tableWidget.rowCount()
        package_path_list = []
        for row in range(0, allRows):
            package_path_list.append(self.swi_tableWidget.item(row, 2).text())
        dups_list = general_utils.list_duplicates(package_path_list)
        if dups_list:
            dup_store_colors = {}
            for row in range(0, allRows):
                package_path_item = self.swi_tableWidget.item(row, 2)
                package_path = package_path_item.text()
                if package_path in dups_list:
                    source_item = self.swi_tableWidget.item(row, 1)
                    if dup_store_colors.get(package_path):
                        rbg_color = dup_store_colors.get(package_path)
                    else:
                        randon_int = random.choice(range(256))
                        rbg_color = QColor(randon_int, 0, 0)
                    source_item.setBackgroundColor(rbg_color)
                    dup_store_colors[package_path] = rbg_color

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
            LOCAL_PKG_NAME = get_nomenclature(self.job, 'LOCAL_PKG_NAME')
            pkg_name = LOCAL_PKG_NAME.format(self.base_data)
            self.swi_lineEdit.setText(pkg_name)
        for file_data in self.base_data.get('files'):
            file_data['pkg_type'] = self.pkg_type
            file_data['job'] = self.job
            file_data.update(self.base_data)
            file_data.pop('files')
            path_data, destination_path = package_dir_utiles.get_destination_info(
                file_data['pkg_dir_type'], file_data.copy()
            )
            file_data['destination_path'] = destination_path
            self.add_row(
                add_row_config=self.add_row_config(),
                file_data=file_data.copy()
            )
        self.set_package_path_dups()
        if self.parent_item and self.swi_dropdown_toolButton.text() == 'v':
            self.parent_item.setSizeHint(self.swi_container_widget.sizeHint())

    def add_source_row(self, file_data, current_row_count):
        source_path = file_data.get('source_path')
        source_item = QTableWidgetItem(source_path)
        cell_editable(source_item, False)
        self.swi_tableWidget.setItem(current_row_count, 1, source_item)

    def add_destination_row(self, file_data, current_row_count):
        destination_path = file_data.get('destination_path')
        destination_item = QTableWidgetItem(destination_path)
        cell_editable(destination_item, False)
        self.swi_tableWidget.setItem(current_row_count, 2, destination_item)

    def add_cancel_row(self, current_row_count):
        self.swi_tableWidget.setCellWidget(current_row_count, 0, self.row_cancel_widget())

    def add_custom_name_row(self, file_data, current_row_count):
        custom_row_dropdown = self.row_dropdown_widget(_type='custom')
        custom_row_dropdown.setEnabled(False)
        self.swi_tableWidget.setCellWidget(current_row_count, 3, custom_row_dropdown)
        custom_row_dropdown.setCurrentText(file_data.get('custom_name', ''))
        if file_data.get('pkg_dir_type', 'select') == 'custom':
            self.swi_tableWidget.setColumnHidden(3, False)
            custom_row_dropdown.setEnabled(True)

    def add_pkg_type_row(self, file_data, current_row_count):
        pkg_type_row_dropdown = self.row_dropdown_widget(_type='pkg_type')
        args = [pkg_type_row_dropdown, current_row_count, file_data]
        pkg_type_row_dropdown.currentIndexChanged.connect(
            lambda _, args=args: self.pkg_type_row_dropdown_exec(args=args))
        self.swi_tableWidget.setCellWidget(current_row_count, 4, pkg_type_row_dropdown)
        pkg_type_row_dropdown.setCurrentText(file_data.get('pkg_dir_type', 'select'))

    def add_path_data_row(self, file_data, current_row_count):
        path_data_item = QTableWidgetItem(str(file_data))
        cell_editable(path_data_item, False)
        self.swi_tableWidget.setItem(current_row_count, 5, path_data_item)

    @property
    def import_data(self):
        if not self.base_data:
            return {}
        base_data = self.base_data
        allRows = self.swi_tableWidget.rowCount()
        filelist = []
        for row in range(0, allRows):
            path_data = eval(self.swi_tableWidget.item(row, 5).text())
            filelist.append(path_data)
        base_data['files'] = filelist
        return base_data

    def update_file_data(self, row):
        path_data_column_no = self.get_column_no('path_data')
        path_data_item = self.swi_tableWidget.item(row, path_data_column_no)
        if not path_data_item:
            return
        path_data = eval(path_data_item.text())
        destination_column_no = self.get_column_no('package_path')
        destination_path = self.swi_tableWidget.item(row, destination_column_no).text()
        path_data['destination_path'] = destination_path
        path_data_item.setText(str(path_data))

    def get_column_no(self, column_name):
        swi_tableWidget = self.swi_tableWidget
        for column in range(0, swi_tableWidget.columnCount()):
            if column_name == swi_tableWidget.horizontalHeaderItem(column).text():
                return column

    @staticmethod
    def add_row_config():
        return {
            'add_cancel_row': True,
            'add_source_row': True,
            'add_destination_row': True,
            'add_custom_name_row': True,
            'add_pkg_type_row': True,
            'add_path_data_row': True
        }

    def add_row(self, add_row_config, file_data):
        current_row_count = self.swi_tableWidget.rowCount()
        self.swi_tableWidget.insertRow(current_row_count)

        if add_row_config.get('add_cancel_row'):
            self.add_cancel_row(current_row_count)

        if add_row_config.get('add_source_row'):
            self.add_source_row(file_data, current_row_count)

        if add_row_config.get('add_path_data_row'):
            self.add_path_data_row(file_data, current_row_count)

        if add_row_config.get('add_destination_row'):
            self.add_destination_row(file_data, current_row_count)

        if add_row_config.get('add_custom_name_row'):
            self.add_custom_name_row(file_data, current_row_count)

        if add_row_config.get('add_pkg_type_row'):
            self.add_pkg_type_row(file_data, current_row_count)

        # has_error = general_utils.is_name_matched(destination_path, [UNKNOWN])
        # if has_error:
        #     source_item.setBackgroundColor(QColor('#993300'))
        #     destination_item.setText('')
        #     pkg_type_row_dropdown.setCurrentText('select')

    @property
    def item_data(self):
        return {
            'pkg_dir': self.pkg_dir,
            'shot': self.shot,
            'discipline': self.discipline,
        }

    def row_dropdown_widget(self, _type):
        """
        :param _type: enum
        :valid types:- valid types 'custom' or 'pkg_type'
        :return: QComboBox Widget
        """
        row_comboBox = QComboBox(self.swi_tableWidget)
        if _type == 'pkg_type':
            content_list = list(self.show_data.get('pkg_dir_types', global_pkg_dir_types).keys())
        elif _type == 'custom':
            content_list = general_utils.get_custom_element_descs(self.item_data) or []
            content_list.append('')
        else:
            return row_comboBox
        row_comboBox.addItems(sorted(content_list))
        return row_comboBox

    def row_cancel_widget(self):

        def row_delete(btn):
            row = self.swi_tableWidget.indexAt(btn.pos()).row()
            self.swi_tableWidget.removeRow(row)
            self.set_package_path_dups()

        cancel_pushButton = QToolButton(self.swi_tableWidget)
        cancel_pushButton.clicked.connect(lambda: row_delete(cancel_pushButton))
        return cancel_pushButton

    def pkg_type_row_dropdown_exec(self, args):

        def destination_cell_process(_dropdown_widget, _row, _file_data):
            destination_cell_item = self.swi_tableWidget.item(_row, 2)
            source_cell_item = self.swi_tableWidget.item(_row, 1)
            _, destination_path = package_dir_utiles.get_destination_info(
                _dropdown_widget.currentText(), _file_data.copy()
            )
            destination_cell_item.setText(destination_path)
            source_cell_item.setBackgroundColor(QColor('#aaaaaa'))
            has_error = general_utils.is_name_matched(destination_path, [UNKNOWN])
            if has_error:
                source_cell_item.setBackgroundColor(QColor('#993300'))
                destination_cell_item.setText('')
                _dropdown_widget.setCurrentText('select')

            if not destination_path:
                source_cell_item.setBackgroundColor(QColor('#993300'))

        def custom_cell_process(_dropdown_widget, _row):
            custom_cell_item = self.swi_tableWidget.item(_row, 4)
            if not custom_cell_item:
                return
            flags = custom_cell_item.flags()
            if _dropdown_widget.currentText() == 'custom':
                flags |= Qt.ItemIsEditable
            else:
                custom_cell_item.setText('')
                flags &= ~Qt.ItemIsEditable
            custom_cell_item.setFlags(flags)

        dropdown_widget, row, file_data = args
        if self.swi_tableWidget.currentRow() != -1:
            row = self.swi_tableWidget.currentRow()
        destination_cell_process(dropdown_widget, row, file_data)
        custom_cell_process(dropdown_widget, row)
        self.update_file_data(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    global_pkg_data = {'date': '20221016', 'vendor': 'dasein', 'show': 'notre_dame', 'pkg_version_prefix': 'v',
                       'pkg_version_num': '0008', 'pkg_dir': '/mnt/mpcparis/NOTRE_DAME/io/To_Client/packages'}
    w = ShotItemWidget(_global_pkg_data=global_pkg_data)
    w.show()
    app.exec_()

    # list_item.setData(Qt.UserRole, item_widget.import_data)
