import re
import sys
import os
from PySide2.QtWidgets import QApplication,  QTableWidgetItem, QComboBox, QHeaderView, QMessageBox
from PySide2.QtCore import Qt
from package_maker.src.resource import message_box
from package_maker.src.gui.gui_shot_item import ShotItemWidget
from package_maker.src.gui.filmgate import filmgate_file_importer
from package_maker.src.config.config_main import *


class FilmgateShotItemWidget(ShotItemWidget):

    def __init__(self,global_pkg_data, pkg_type='shot', show_data=None, parent_item=None, parent_widget=None):
        super(FilmgateShotItemWidget, self).__init__(
            global_pkg_data, pkg_type, show_data, parent_item, parent_widget
        )
        self.pkg_type = global_pkg_data.get('pkg_dir')



    def get_fi_data(self):
        fi_widget = filmgate_file_importer.FilmgateFileImporter(pkg_dir=self.pkg_dir)
        fi_widget.show()
        fi_widget.exec_()
        return fi_widget.import_data


if __name__ == '__main__':

    app = QApplication(sys.argv)
    global_pkg_data = {'date': '20221008', 'vendor': 'dasein', 'show': 'trm', 'pkg_version_prefix': 'v',
                       'pkg_version_num': '0021', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package'}

    w = FilmgateShotItemWidget(global_pkg_data=global_pkg_data)
    w.show()
    app.exec_()