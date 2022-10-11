import os, sys
from  PySide2 import QtWidgets

class FileDialog(QtWidgets.QFileDialog):
    def __init__(self, *args):
        QtWidgets.QFileDialog.__init__(self, *args)
        self.setOption(self.DontUseNativeDialog, True)
        self.setFileMode(self.ExistingFiles)
        btns = self.findChildren(QtWidgets.QPushButton)
        self.openBtn = [x for x in btns if 'open' in str(x.text()).lower()][0]
        self.openBtn.clicked.disconnect()
        self.openBtn.clicked.connect(self.openClicked)
        self.tree = self.findChild(QtWidgets.QTreeView)

    def openClicked(self):
        inds = self.tree.selectionModel().selectedIndexes()
        files = []
        for i in inds:
            if i.column() == 0:
                files.append(os.path.join(str(self.directory().absolutePath()), str(i.data())).replace('\\', '/'))
        self.selectedFiles = files
        self.close()

    def filesSelected(self):
        return self.selectedFiles

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = FileDialog()
    w.show()
    w.exec_()
    print(w.filesSelected())