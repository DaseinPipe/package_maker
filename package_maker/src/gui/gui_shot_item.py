import sys
import random
from PySide2.QtWidgets import QApplication, QDialog, QToolButton, QTableWidgetItem, QComboBox, QHeaderView
from PySide2.QtCore import Qt
from PySide2.QtGui import QColor
from package_maker.src.resource import shot_widget_item
from package_maker.src.gui import gui_file_importer, gui_edit_cell
from package_maker.src.utils import general_utils, package_dir_utiles
from package_maker.src.config.config_main import *


class ShotItemWidget(shot_widget_item.Ui_swi_Frame, QDialog):
    def __init__(self, global_pkg_data, pkg_type='shot', show_data=None, parent_item=None, parent_widget=None):
        super(ShotItemWidget, self).__init__()
        self.parent_item = parent_item
        self.parent_widget = parent_widget
        self.pkg_type = pkg_type
        self.global_pkg_data = global_pkg_data
        self.pkg_dir = self.global_pkg_data.get('pkg_dir')
        self.show_data = show_data or get_show_data(os.environ.get(('show')))
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
        # self.swi_container_widget.setHidden(True)
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
        self.swi_tableWidget.itemClicked.connect(self.CellChanged) # required for first selection
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

    @staticmethod
    def get_fi_data(parent_item, pkg_type, from_add_btn=False):
        fi_widget = gui_file_importer.FileImporterWidget(pkg_dir=pkg_type)
        if from_add_btn:
            fi_widget.fi_shot_comboBox.setEnabled(False)
            fi_widget.fi_discipline_comboBox.setEnabled(False)
        if parent_item:
            item_data = parent_item.data(Qt.UserRole)
        else:
            item_data = {}
        if item_data:
            if item_data.get('plate_version_num'):
                fi_widget.fi_plate_version_comboBox.setCurrentText(item_data.get('plate_version_num'))
                fi_widget.fi_plate_version_comboBox.setEnabled(False)
        fi_widget.show()
        fi_widget.exec_()
        return fi_widget.import_data

    def set_package_path_dups(self):
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
        self.import_data = self.get_fi_data(self.parent_item, self.pkg_dir, from_btn)
        if not self.import_data:
            return
        self.import_data.update(self.global_pkg_data)
        self.shot = self.import_data.get('shot', UNKNOWN)
        self.discipline = self.import_data.get('discipline', UNKNOWN)

        if not from_btn:
            self.import_data['pkg_type'] = self.pkg_type
            shot_pkg_name = SHOT_PKG_NAME.format(self.import_data)
            self.swi_lineEdit.setText(shot_pkg_name)
        for file_data in self.import_data.get('files'):
            file_data['pkg_type'] = self.pkg_type
            file_data.update(self.import_data)
            file_data.pop('files')
            path_data, destination_path = package_dir_utiles.get_destination_info(
                file_data['pkg_dir_type'], file_data.copy()
            )
            file_data['destination_path'] = destination_path
            self.add_row(file_data.copy())
        self.set_package_path_dups()
        if self.parent_item and self.swi_dropdown_toolButton.text() == 'v':
            self.parent_item.setSizeHint(self.swi_container_widget.sizeHint())


    def add_row(self, file_data):
        source_path = file_data.get('source_path')
        destination_path = file_data.get('destination_path')
        current_row_count = self.swi_tableWidget.rowCount()
        pkg_type_row_dropdown = self.row_dropdown_widget(type='pkg_type')
        args = [pkg_type_row_dropdown, current_row_count, file_data]
        pkg_type_row_dropdown.currentIndexChanged.connect(lambda _, args=args: self.pkg_type_row_dropdown_exec(args=args))

        custom_row_dropdown = self.row_dropdown_widget(type='custom')
        custom_row_dropdown.setEnabled(False)

        destination_item = QTableWidgetItem(destination_path)
        self.cell_editable(destination_item, False)
        source_item = QTableWidgetItem(source_path)
        self.cell_editable(source_item, False)
        path_data_item = QTableWidgetItem(str(file_data))
        self.cell_editable(path_data_item, False)

        self.swi_tableWidget.insertRow(current_row_count)
        self.swi_tableWidget.setCellWidget(current_row_count, 0, self.row_cancel_widget())
        self.swi_tableWidget.setItem(current_row_count, 1, source_item)
        self.swi_tableWidget.setItem(current_row_count, 2, destination_item)
        self.swi_tableWidget.setCellWidget(current_row_count, 3, custom_row_dropdown)
        self.swi_tableWidget.setCellWidget(current_row_count, 4, pkg_type_row_dropdown)
        self.swi_tableWidget.setItem(current_row_count, 5, path_data_item)

        pkg_type_row_dropdown.setCurrentText(file_data.get('pkg_dir_type', 'select'))
        custom_row_dropdown.setCurrentText(file_data.get('custom_name', ''))

        if file_data.get('pkg_dir_type', 'select') == 'custom':
            self.swi_tableWidget.setColumnHidden(3, False)
            custom_row_dropdown.setEnabled(True)

        has_error = general_utils.is_name_matched(destination_path, [UNKNOWN])
        if has_error:
            source_item.setBackgroundColor(QColor('#993300'))
            destination_item.setText('')
            pkg_type_row_dropdown.setCurrentText('select')


    def cell_editable(self, item, status=False):
        flags = item.flags()
        if status:
            flags |= Qt.ItemIsEditable
        else:
            flags &= ~Qt.ItemIsEditable
        item.setFlags(flags)

    @property
    def item_data(self):
        return {
            'pkg_dir': self.pkg_dir,
            'shot': self.shot,
            'discipline': self.discipline,
        }

    def row_dropdown_widget(self, type):
        '''
        :param type: enum
        :valid types:- valid types 'custom' or 'pkg_type'
        :return: QComboBox Widget
        '''
        row_comboBox = QComboBox(self.swi_tableWidget)
        if type == 'pkg_type':
            content_list = list(self.show_data.get('pkg_dir_types', global_pkg_dir_types).keys())
        elif type == 'custom':
            content_list = general_utils.get_custom_element_descs(self.item_data) or []
            content_list.append('')
        else:
            return row_comboBox
        row_comboBox.addItems(content_list)
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

        def destination_cell_process(dropdown_widget, row, file_data):
            destination_cell_item = self.swi_tableWidget.item(row, 2)
            source_cell_item = self.swi_tableWidget.item(row, 1)
            _, destination_path = package_dir_utiles.get_destination_info(
                dropdown_widget.currentText(), file_data.copy()
            )
            destination_cell_item.setText(destination_path)
            has_error = general_utils.is_name_matched(destination_path, [UNKNOWN])

            if has_error:
                source_cell_item.setBackgroundColor(QColor('#993300'))
                destination_cell_item.setText('')
                dropdown_widget.setCurrentText('select')


        def custom_cell_process(dropdown_widget, row, file_data):
            custom_cell_item = self.swi_tableWidget.item(row, 4)
            if not custom_cell_item:
                return
            flags = custom_cell_item.flags()
            if dropdown_widget.currentText() == 'custom':
                flags |= Qt.ItemIsEditable
            else:
                custom_cell_item.setText('')
                flags &= ~Qt.ItemIsEditable
            custom_cell_item.setFlags(flags)

        dropdown_widget, row, file_data = args
        destination_cell_process(dropdown_widget, row, file_data)
        custom_cell_process(dropdown_widget, row, file_data)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    global_pkg_data = {'date': '20221008', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0021', 'pkg_dir': 'C:/mnt/mpcparis/A5/io/To_Client/packages'}
    w = ShotItemWidget(global_pkg_data=global_pkg_data)
    w.show()
    app.exec_()