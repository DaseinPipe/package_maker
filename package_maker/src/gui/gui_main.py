import sys
from importlib import reload
import re
from datetime import datetime
from PySide2.QtWidgets import QApplication, QDialog, QDialogButtonBox, QListWidgetItem, QStyle
from PySide2.QtGui import QGuiApplication
from PySide2.QtCore import Qt, QFile, QTextStream, QSize

from package_maker.src.config.config_main import *
from package_maker.src.gui import gui_file_importer, gui_shot_item
from package_maker.src.resource import resource_main, shot_widget_item
from package_maker.src.utils import general_utils
from package_maker import package_reload

reload(resource_main)
reload(shot_widget_item)
reload(gui_file_importer)

global GLOBAL_DATA
GLOBAL_DATA = get_global_data()


class PackageMakerDlg(resource_main.Ui_Dialog, QDialog):
    def __init__(self, ):
        super(PackageMakerDlg, self).__init__()
        # Run the .setupUi() method to show the GUI
        self.global_data = GLOBAL_DATA
        self.setupUi(self)
        self.start_size = QSize(self.width(), self.height())
        self.apply_btn = self.main_buttonBox.button(QDialogButtonBox.Apply)
        self.abort_btn = self.main_buttonBox.button(QDialogButtonBox.Abort)
        self.apply_btn.setEnabled(False)
        self.job = UNKNOWN
        self.destination = UNKNOWN
        self.vendor = UNKNOWN
        self.pkg_dir = UNKNOWN
        self.pkg_version_prefix = UNKNOWN
        self.title = UNKNOWN
        self.global_version = UNKNOWN
        self.stackedWidget.setCurrentIndex(0)
        self.populate_page1()
        self.connection()

    def populate_page1(self):
        self.pkg_version_comboBox.setHidden(True)
        self.pkg_version_label.setHidden(True)
        self.job_comboBox.setEnabled(False)
        destination_list = list(self.global_data['destination'].keys())
        destination_list.insert(0, 'Select')
        self.destination_comboBox.addItems(destination_list)

    def connection(self):
        self.job_comboBox.currentTextChanged.connect(self.job_exec)
        self.destination_comboBox.currentTextChanged.connect(self.destination_exec)
        self.apply_btn.clicked.connect(self.apply)
        self.shot_pushButton.clicked.connect(self.add_shot)
        self.listWidget.itemSelectionChanged.connect(self.set_shot_status)
        self.abort_btn.clicked.connect(self.close)
        self.shot_cancel_pushButton.clicked.connect(self.page2_cancel)
        self.shot_view_pushButton.clicked.connect(self.view_summary)
        self.summary_cancel_pushButton.clicked.connect(self.page3_cancel)
        self.pkg_create_pushButton.clicked.connect(self.transfer_files)


    def transfer_files(self):
        for i in range(self.listWidget.count()):
            list_item = self.listWidget.item(i)
            item_data = list_item.data(Qt.UserRole)
            self.update_database(item_data)

    def update_database(self, item_data):
        general_utils.update_shot_version(item_data)

    def page3_cancel(self):
        self.stackedWidget.setCurrentIndex(1)

    def view_summary(self):
        self.populate_page3()
        self.stackedWidget.setCurrentIndex(2)

    def page2_cancel(self):
        self.listWidget.clear()
        self.resize(self.start_size)
        centerPoint = self.screen().availableGeometry().center()
        self.move(centerPoint - self.frameGeometry().center())
        self.stackedWidget.setCurrentIndex(0)

    @property
    def global_pkg_data(self):
        return dict(
            date=datetime.today().strftime('%Y%m%d'),
            vendor=self.vendor,
            show=self.job,
            pkg_version_prefix=self.pkg_version_prefix,
            pkg_version_num=self.global_version,
            pkg_dir=self.pkg_dir,
        )

    def destination_exec(self, state):
        self.job_comboBox.clear()
        if state == 'Select':
            self.job_comboBox.clear()
            self.job_comboBox.setEnabled(False)
            self.apply_btn.setEnabled(False)
            return
        os.environ['destination'] = state
        self.destination = state
        self.pkg_version_prefix = self.global_data['destination'][state]['pkg_version_prefix']
        self.vendor = self.global_data['destination'][state]['vendor']
        job_list = list(self.global_data['destination'][state]['job'].keys())
        job_list.insert(0, 'Select')
        self.job_comboBox.addItems(job_list)
        self.job_comboBox.setEnabled(True)

    def job_exec(self, state):

        if state == 'Select':
            self.apply_btn.setEnabled(False)
            return
        os.environ['job'] = state
        self.job = state
        self.title = self.global_data['destination'][self.destination]['job'][state]['title']
        self.pkg_dir = self.global_data['destination'][self.destination]['job'][state]['dir_path']
        self.global_version = general_utils.get_latest_pkg_version(self.pkg_dir)

        self.apply_btn.setEnabled(True)

    def set_shot_status(self):
        if not self.listWidget.selectedItems():
            self.shot_select_lineEdit.setText('')
            return
        swi_main_widget = self.listWidget.itemWidget(self.listWidget.selectedItems()[0])
        self.shot_select_lineEdit.setText(swi_main_widget.swi_lineEdit.text())

    def apply(self):
        rect = self.screen().availableGeometry()
        self.move(rect.x() + 25, rect.y() + 50)
        self.resize(rect.width() - 50, rect.height() - 150)
        self.stackedWidget.setCurrentIndex(1)
        self.populate_page2()

    def populate_page2(self):
        self.asset_pushButton.setEnabled(False)
        main_pkg_dir_path = main_pkg_dir.format(self.global_pkg_data)
        os.makedirs(main_pkg_dir.format(self.global_pkg_data))
        self.title_label.setText(self.title)
        self.pkg_name_label.setText(GLOBAL_PKG_NAME.format(self.global_pkg_data))

    def populate_page3(self):
        self.summary_title_label.setText(self.title)
        self.summary_pkg_name_label.setText(GLOBAL_PKG_NAME.format(self.global_pkg_data))

    def add_shot(self):
        itemN = QListWidgetItem()
        item_widget = gui_shot_item.ShotItemWidget(
            parent_item=itemN,
            parent_widget=self.listWidget,
            global_pkg_data=self.global_pkg_data
        )
        item_widget.swi_status_lineEdit.textChanged.connect(self.set_selected_info)
        itemN.setSizeHint(item_widget.sizeHint())
        itemN.setData(Qt.UserRole, item_widget.import_data)
        self.listWidget.addItem(itemN)
        self.listWidget.setItemWidget(itemN, item_widget)
        itemN.setSelected(True)

    def set_selected_info(self, info):
        if general_utils.is_name_matched(info, UNKNOWN):
            info = r'<span style="color:#993300;">UNKNOWN</span>'.join(re.split(UNKNOWN, info))
        self.selected_info_textEdit.setHtml(info)


def run():
    app = QApplication(sys.argv)
    with open(stylesheet_path, 'r') as FID:
        qss = FID.read()
        app.setStyleSheet(qss)
    w = PackageMakerDlg()
    w.show()
    app.exec_()


if __name__ == '__main__':
    run()

