
import sys
from package_maker.src.gui import gui_shot_item
from package_maker.src.gui.filmgate import filmgate_shot_item
from PySide2.QtWidgets import QApplication


def get_shot_widget(job, parent_item, parent_widget, global_pkg_data ):
    if job.lower() == 'trm':
        return filmgate_shot_item.FilmgateShotItemWidget(
            parent_item=parent_item,
            parent_widget=parent_widget,
            _global_pkg_data=global_pkg_data
        )
    return gui_shot_item.ShotItemWidget(
        parent_item=parent_item,
        parent_widget=parent_widget,
        _global_pkg_data=global_pkg_data
    )
if __name__ == '__main__':
    app = QApplication(sys.argv)
    global_pkg_data = {'date': '20221008', 'vendor': 'dasein', 'show': 'trm', 'pkg_version_prefix': 'v',
                       'pkg_version_num': '0021', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package'}

    t = get_shot_widget('trm', None, None, global_pkg_data)


    t.show()
    app.exec_()

