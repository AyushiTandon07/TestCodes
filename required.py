import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QFrame, QLabel,\
    QSizePolicy, QHBoxLayout, QGraphicsOpacityEffect, QScrollArea, QListWidget, QListWidgetItem, QComboBox, QCheckBox
from PyQt6.QtCore import QPropertyAnimation, Qt, QMetaObject, QSize, QRect, QEasingCurve, pyqtSignal
from PyQt6.QtGui import QPixmap, QPainter, QIcon, QImage, QPainterPath, QStandardItemModel, QStandardItem


class CheckableListWidget(QListWidget):
    raiseComplete = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self._changed = False
        self.clicked.connect(self.HandleItemPressed)
        self.adjustSizeToContents()

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

    def adjustSizeToContents(self):
        self.setMaximumWidth(180)
        # self.setMaximumHeight(105)

    def HandleItemPressed(self, index):
        item = self.itemFromIndex(index)

        if item.text() == 'All':
            if item.checkState() == Qt.CheckState.Unchecked:
                for i in range(self.count()):
                    item = self.item(i)
                    item.setCheckState(Qt.CheckState.Unchecked)
            else:
                for i in range(self.count()):
                    item = self.item(i)
                    item.setCheckState(Qt.CheckState.Checked)
        else:
            if item.checkState() == Qt.CheckState.Unchecked:
                item.setCheckState(Qt.CheckState.Unchecked)
                self.item(0).setCheckState(Qt.CheckState.Unchecked)
            else:
                flag = True
                item.setCheckState(Qt.CheckState.Checked)
                # running look from 1 because we do not need to check if ALL is selected or not if items from 1- count is selected then we # will mark ALL as Checked as well
                for i in range(1, self.count()):
                    item = self.item(i)
                    if item.checkState() == Qt.CheckState.Unchecked:        # if any of the item is found Unchecked we will not update the status of ALL
                        flag = False
                        break
                    else:
                        pass
                if flag:
                    self.item(0).setCheckState(Qt.CheckState.Checked)

        self._changed = True
        self.raiseComplete.emit(0)

    def SetAllItemsChecked(self):
        for i in range(self.count()):
            item = self.item(i)
            item.setCheckState(Qt.CheckState.Checked)

    def ReturnCheckedValues(self):

        CheckedItems = []

        # if self.item(0).checkState() == Qt.CheckState.Checked:
        for i in range(1, self.count()):       # 0th element is ALL
            item = self.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                CheckedItems.append(item.text())

        return CheckedItems