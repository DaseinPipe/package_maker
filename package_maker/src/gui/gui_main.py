import re
import sys
from importlib import reload

from PySide2.QtCore import Qt, QSize
from PySide2.QtWidgets import QApplication, QDialog, QDialogButtonBox, QListWidgetItem

from package_maker.src.config.config_main import *
from package_maker.src.gui import gui_file_importer, shot_widget_selector
from package_maker.src.resource import resource_main, shot_widget_item
from package_maker.src.utils import general_utils

reload(resource_main)
reload(shot_widget_item)
reload(gui_file_importer)

GLOBAL_DATA: dict = get_global_data()


def update_database(item_data):
    general_utils.update_shot_version(item_data)


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
        self.pkg_dir = UNKNOWN
        self.title = UNKNOWN
        self._global_pkg_data =None
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
        self.pkg_create_pushButton.clicked.connect(self.create_pkg)

    def create_pkg(self):
        for i in range(self.listWidget.count()):
            list_item = self.listWidget.item(i)
            item_data = list_item.data(Qt.UserRole)
            item_widget = item_data['item_widget']
            import_data = item_widget.import_data
            general_utils.process_executor(
                project=self.job,
                processor='create_package',
                process=import_data['discipline'],
                data=import_data,
            )

    def page3_cancel(self):
        self.stackedWidget.setCurrentIndex(1)

    def view_summary(self):
        self.populate_page3()
        self.stackedWidget.setCurrentIndex(2)

    def page2_cancel(self):
        self.listWidget.clear()
        self.resize(self.start_size)
        center_point = self.screen().availableGeometry().center()
        self.move(center_point - self.frameGeometry().center())
        self.stackedWidget.setCurrentIndex(0)

    @property
    def global_pkg_data(self):
        return self._global_pkg_data

    def destination_exec(self, state):
        self.job_comboBox.clear()
        if state == 'Select':
            self.job_comboBox.clear()
            self.job_comboBox.setEnabled(False)
            self.apply_btn.setEnabled(False)
            return
        os.environ['destination'] = state
        self.destination = state
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
        self.apply_btn.setEnabled(True)

    def set_shot_status(self):
        if not self.listWidget.selectedItems():
            self.shot_select_lineEdit.setText('')
            return
        swi_main_widget = self.listWidget.itemWidget(self.listWidget.selectedItems()[0])
        self.shot_select_lineEdit.setText(swi_main_widget.swi_lineEdit.text())

    def apply(self):
        self.global_pkg_data = 'initiate'
        rect = self.screen().availableGeometry()
        self.move(rect.x() + 25, rect.y() + 50)
        self.resize(rect.width() - 50, rect.height() - 150)
        self.stackedWidget.setCurrentIndex(1)
        self.populate_page2()

    @property
    def global_pkg_name(self):
        template = get_path(self.job.lower(), 'GLOBAL_PKG_NAME')
        return template.format(self.global_pkg_data)

    def make_pkg_dirs(self):
        main_pkg_dir = get_path(self.job.lower(), 'main_pkg_dir')
        main_pkg_dir_path = main_pkg_dir.format(self.global_pkg_data)
        os.makedirs(main_pkg_dir_path)

    def populate_page2(self):
        self.asset_pushButton.setEnabled(False)
        self.make_pkg_dirs()
        self.title_label.setText(self.title)
        self.pkg_name_label.setText(self.global_pkg_name)

    def populate_page3(self):
        self.summary_title_label.setText(self.title)
        self.summary_pkg_name_label.setText(self.global_pkg_name)

    def add_shot(self):
        list_item = QListWidgetItem()
        print(self.global_pkg_data)
        item_widget = shot_widget_selector.get_shot_widget(
            job=self.job,
            parent_item=list_item,
            parent_widget=self.listWidget,
            global_pkg_data=self.global_pkg_data
        )
        item_widget.swi_status_lineEdit.textChanged.connect(self.set_selected_info)
        list_item.setSizeHint(item_widget.sizeHint())
        list_item.setData(Qt.UserRole, {'item_widget': item_widget})
        self.listWidget.addItem(list_item)
        self.listWidget.setItemWidget(list_item, item_widget)
        list_item.setSelected(True)

    def set_selected_info(self, info):
        if general_utils.is_name_matched(info, UNKNOWN):
            info = r'<span style="color:#993300;">UNKNOWN</span>'.join(re.split(UNKNOWN, info))
        self.selected_info_textEdit.setHtml(info)

    @global_pkg_data.setter
    def global_pkg_data(self, value):
        if value != 'initiate':
            raise RuntimeError('value should be "initiate" but plz make sur global_pkg_data is initiate once only')
        self._global_pkg_data = general_utils.get_global_pkg_data(
            self.job.lower(),
            self.destination,
            self.pkg_dir
        )

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
