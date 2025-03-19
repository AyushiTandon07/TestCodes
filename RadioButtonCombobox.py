import sys

from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QRadioButton

class ComboBoxWithRadio(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Create a radio button for "Select Date"
        self.select_date_radio = QRadioButton("Select Date")
        self.select_date_radio.setChecked(True)  # Initially selected
        layout.addWidget(self.select_date_radio)

        # Create the combobox

        # self.comboBox = QComboBox()
        self.comboBox = CheckableCombobox()
        # self.comboBox.addItem("Option 1")
        # self.comboBox.addItem("Option 2")
        # self.comboBox.addItem("Option 3")
        layout.addWidget(self.comboBox)

        self.setLayout(layout)
        self.setWindowTitle("ComboBox with Radio Button")

class CheckableCombobox(QComboBox):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.view().pressed.connect(self.handle_item_pressed)
        self.setModel(QStandardItemModel(self))

        # when any item get pressed
        def handle_item_pressed(self, index):

            # getting which item is pressed
            item = self.model().itemFromIndex(index)

            # make it check if unchecked and vice-versa
            if item.checkState() == Qt.Checked:
                item.setCheckState(Qt.Unchecked)
            else:
                item.setCheckState(Qt.Checked)

            # calling method
            self.check_items()

        # method called by check_items
        def item_checked(self, index):

            # getting item at index
            item = self.model().item(index, 0)

            # return true if checked else false
            return item.checkState() == Qt.Checked




        self.addItem("Option 1")
        self.addItem("Option 2")
        self.addItem("Option 3")
        self.se



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ComboBoxWithRadio()
    window.show()
    sys.exit(app.exec_())
