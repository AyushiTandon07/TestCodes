import sys
from PyQt5.QtWidgets import QApplication, QComboBox, QVBoxLayout, QWidget


class CheckableComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setEditable(True)
        self.lineEdit().setPlaceholderText("Search...")
        self._original_items = []

        self.filter_text = ""
        self.is_filtered = False

        self.lineEdit().textChanged.connect(self.set_filter_text)

    def set_filter_text(self, text):
        self.filter_text = text
        self.update_items()

    def update_items(self):
        self.clear()
        if self.filter_text:
            filtered_items = [item for item in self._original_items if self.filter_text.lower() in item.lower()]
            self.addItems(filtered_items)
            self.is_filtered = True
        else:
            self.addItems(self._original_items)
            self.is_filtered = False

    def showPopup(self):
        if not self.is_filtered:
            self.update_items()
        super().showPopup()

    def setItems(self, items):
        self._original_items = items
        self.update_items()


def main():
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout()

    combo_box = CheckableComboBox()
    combo_box.setItems(["Apple", "Banana", "Cherry", "Date", "Grape", "Lemon"])

    layout.addWidget(combo_box)
    window.setLayout(layout)

    window.setWindowTitle("Checkable Combo Box with Line Edit")
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
