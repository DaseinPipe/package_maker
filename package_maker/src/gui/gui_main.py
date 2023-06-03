import re
import sys

from PySide2.QtCore import Qt, QSize
from PySide2.QtWidgets import QApplication, QDialog, QDialogButtonBox, QListWidgetItem
import subprocess
from package_maker.src.config.config_client import *
from package_maker.src.config.config_vendor import *
from package_maker.src.config.config_internal import *
from package_maker.src.config.global_pkg_data_selector import get_global_pkg_data
from package_maker.src.config import shot_widget_selector
from package_maker.src.resource import resource_main
from package_maker.src.utils import general_utils

CLIENT_GLOBAL_DATA: dict = get_global_data()
LOCAL_GLOBAL_DATA: dict = internal_config_data()


def update_database(item_data):
    general_utils.update_shot_version(item_data)


class PackageMakerDlg(resource_main.Ui_Package_Maker, QDialog):
    def __init__(self, ):
        super(PackageMakerDlg, self).__init__()
        # Run the .setupUi() method to show the GUI
        self.client_global_data = CLIENT_GLOBAL_DATA
        self.local_global_data = LOCAL_GLOBAL_DATA
        self.setupUi(self)
        self.start_size = QSize(self.width(), self.height())
        self.apply_btn = self.main_buttonBox.button(QDialogButtonBox.Apply)
        self.abort_btn = self.main_buttonBox.button(QDialogButtonBox.Abort)
        self.apply_btn.setEnabled(False)
        self.job = UNKNOWN
        self.destination = UNKNOWN
        self.pkg_dir = UNKNOWN
        self.pkg_type = UNKNOWN
        self.vendor_name = UNKNOWN
        self.title = UNKNOWN
        self._global_pkg_data = None
        self.stackedWidget.setCurrentIndex(0)
        self.populate_page1()
        self.connection()

    def populate_page1(self):
        self.vendor_name_comboBox.setHidden(True)
        self.vendor_name_label.setHidden(True)
        self.job_comboBox.setEnabled(False)
        self.pkg_type_comboBox.setEnabled(False)
        destination_list = list(self.client_global_data['destination'].keys())
        self.destination_comboBox.addItems(destination_list)

    def connection(self):
        self.job_comboBox.currentTextChanged.connect(self.job_exec)
        self.destination_comboBox.currentTextChanged.connect(self.destination_exec)
        self.pkg_type_comboBox.currentTextChanged.connect(self.pkg_type_exec)
        self.vendor_name_comboBox.currentTextChanged.connect(self.vendor_name_exec)
        self.apply_btn.clicked.connect(self.apply)
        self.shot_pushButton.clicked.connect(self.add_shot)
        self.listWidget.itemSelectionChanged.connect(self.set_shot_status)
        self.abort_btn.clicked.connect(self.close)
        self.shot_cancel_pushButton.clicked.connect(self.page2_cancel)
        self.shot_view_pushButton.clicked.connect(self.view_summary)
        self.summary_cancel_pushButton.clicked.connect(self.page3_cancel)
        self.pkg_create_pushButton.clicked.connect(self.create_pkg)
        self.done_pushButton.clicked.connect(self.close)
        self.open_pkg_pushButton.clicked.connect(self.open_pkg_dir)

    def open_pkg_dir(self):
        if self.pkg_type == 'local':
            main_pkg_dir = self.pkg_dir
        else:
            main_pkg_dir_template = general_utils.get_path(self.job.lower(), 'main_pkg_dir')
            main_pkg_dir = main_pkg_dir_template.format(self.global_pkg_data)
        subprocess.Popen(['xdg-open', main_pkg_dir])

    def create_pkg(self):
        process = None
        if self.pkg_type == 'vendor':
            process = 'vendor'
        elif self.pkg_type == 'local':
            process = 'local'
        for i in range(self.listWidget.count()):
            list_item = self.listWidget.item(i)
            item_data = list_item.data(Qt.UserRole)
            item_widget = item_data['item_widget']
            import_data = item_widget.import_data
            if not process:
                process = import_data['discipline']
            general_utils.process_executor(
                project=self.job,
                processor='create_package',
                process=process,
                data=import_data,
            )
        self.populate_page4()
        self.stackedWidget.setCurrentIndex(3)

    def page3_cancel(self):
        self.stackedWidget.setCurrentIndex(1)

    def view_summary(self):
        if self.pkg_type == 'local':
            return
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
        job_list = list(self.client_global_data['destination'][state]['job'].keys())
        job_list.insert(0, 'Select')
        self.job_comboBox.addItems(job_list)
        self.job_comboBox.setEnabled(True)

    def job_exec(self, state):
        if not state:
            return
        if state == 'Select':
            self.pkg_type_comboBox.setEnabled(False)
            self.apply_btn.setEnabled(False)
            return
        os.environ['job'] = state
        os.environ['show'] = state
        self.job = state
        self.pkg_type_comboBox.setEnabled(True)

    def pkg_type_exec(self, state):
        if not state:
            return
        if state == 'Select':
            self.apply_btn.setEnabled(False)
            return
        os.environ['pkg_type'] = state
        self.pkg_type = state
        # print(self.destination)
        if state == 'vendor':
            self.vendor_name_comboBox.setHidden(False)
            self.vendor_name_label.setHidden(False)
            self.vendor_name_comboBox.clear()
            self.vendor_name_comboBox.addItems(VENDOR_LIST)
        elif state == 'client':
            self.title = self.client_global_data['destination'][self.destination]['job'][self.job]['title']
            self.pkg_dir = self.client_global_data['destination'][self.destination]['job'][self.job]['dir_path']
            self.apply_btn.setEnabled(True)
        else:
            self.pkg_dir = self.local_global_data['job'][self.job]['dir_path']
            self.apply_btn.setEnabled(True)

    def vendor_name_exec(self, state):
        if not state:
            return
        if state == 'Select':
            self.apply_btn.setEnabled(False)
            return

        os.environ['vendor_name'] = state
        vendor_data = vendor_config_data(vendor=state)
        self.title = vendor_data['destination'][self.destination]['job'][self.job]['title']
        self.pkg_dir = vendor_data['destination'][self.destination]['job'][self.job]['dir_path']
        self.vendor_name = state
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
        # print(self.global_pkg_data)
        # print(template.format(self.global_pkg_data))
        return template.format(self.global_pkg_data)

    def make_pkg_dirs(self):
        main_pkg_dir = get_path(self.job.lower(), 'main_pkg_dir')
        main_pkg_dir_path = main_pkg_dir.format(self.global_pkg_data)
        if not os.path.exists(main_pkg_dir_path):
            os.makedirs(main_pkg_dir_path)

    def populate_page2(self):
        self.asset_pushButton.setEnabled(False)
        self.hide_widget()
        if self.pkg_type == 'local':
            self.shot_view_pushButton.setText('Create Package')
            self.shot_view_pushButton.clicked.connect(self.create_pkg)
            return
        self.make_pkg_dirs()
        self.title_label.setText(self.title)
        self.pkg_name_label.setText(self.global_pkg_name)

    def hide_widget(self):
        hide_list = None
        if self.pkg_type == 'local':
            hide_list = [self.title_label_header, self.title_label, self.pkg_name_label_header, self.pkg_name_label]

        if hide_list:
            for each_widget in hide_list:
                each_widget.setHidden(True)

    def populate_page3(self):
        self.summary_title_label.setText(self.title)
        self.summary_pkg_name_label.setText(self.global_pkg_name)

    def populate_page4(self):
        if self.pkg_type == 'local':
            self.pkg_name_exit_label.setText('Creating Local Package')
        else:
            self.pkg_name_exit_label.setText(self.global_pkg_name)  # remove if else
        self.setMaximumHeight(84)
        self.setMaximumWidth(400)
        self.resize(400, 84)

    def add_shot(self):
        list_item = QListWidgetItem()
        item_widget = shot_widget_selector.get_shot_widget(
            job=self.job,
            parent_item=list_item,
            parent_widget=self.listWidget,
            global_pkg_data=self.global_pkg_data,
            pkg_for=self.pkg_type
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
        text_size = self.selected_info_textEdit.fontMetrics().boundingRect(info).width()
        widget_size = self.selected_info_textEdit.size().width()
        maximum_size = self.selected_info_textEdit.maximumSize()
        minimum_size = self.selected_info_textEdit.minimumSize()
        if text_size > (widget_size - 20):
            maximum_size.setHeight(44)
            minimum_size.setHeight(44)
            self.selected_info_textEdit.setMaximumSize(maximum_size)
            self.selected_info_textEdit.setMinimumSize(minimum_size)
        else:
            maximum_size.setHeight(22)
            minimum_size.setHeight(22)
            self.selected_info_textEdit.setMaximumSize(maximum_size)
            self.selected_info_textEdit.setMinimumSize(minimum_size)

        self.selected_info_textEdit.setHtml(info)

    @global_pkg_data.setter
    def global_pkg_data(self, value):
        if value != 'initiate':
            raise RuntimeError('value should be "initiate" but plz make sure global_pkg_data is initiate once only')
        self._global_pkg_data = get_global_pkg_data(
            self.job.lower(),
            self.destination,
            self.pkg_dir,
            self.pkg_type,
            self.vendor_name
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
