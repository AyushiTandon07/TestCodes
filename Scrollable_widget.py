import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout, QTextEdit, QScrollArea, QLineEdit, QCheckBox

class ScrollableWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QLineEdit widget
        self.line_edit = QLineEdit()

        # Create a QTextEdit widget
        # self.text_edit = QTextEdit()
        # self.text_edit.setPlainText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        #                              "Pellentesque nec ante sit amet velit efficitur fringilla. "
        #                              "Sed auctor convallis mauris. Nullam ac odio nec nisl lacinia dignissim. "
        #                              "Nulla eget urna vitae ligula convallis consequat eget id risus. "
        #                              "Fusce non sem sit amet enim posuere lacinia eget eu metus. "
        #                              "Sed in risus id ligula tempor lobortis. "
        #                              "Suspendisse tincidunt nec enim eu placerat. "
        #                              "Nullam tincidunt orci id nulla tempor, ut rhoncus enim laoreet. "
        #                              "Aliquam efficitur lectus eget magna laoreet, id dignissim tortor dapibus. "
        #                              "Ut ac libero nec tortor ultrices dictum vel ac arcu. "
        #                              "Cras at enim nec nisi vulputate lobortis.")

        self.text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '

        # Create a QCheckBox widget
        self.checkbox = QCheckBox()
        self.checkbox.setText(self.text)

        # Create a QHBoxLayout for the QCheckBox and QTextEdit
        checkbox_layout = QHBoxLayout()
        checkbox_layout.addWidget(self.checkbox)
        #checkbox_layout.addWidget(self.text_edit)

        # Create a QVBoxLayout to hold the QLineEdit and the QHBoxLayout containing the QCheckBox and QTextEdit
        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addLayout(checkbox_layout)
        layout.setContentsMargins(0, 0, 0, 0)

        # Set the layout to the QWidget
        self.setLayout(layout)

        #self.checkbox.stateChanged.connect(self.updateCheckbox)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Scrollable Widget Example')

    # Create a scroll area and set the scrollable widget inside it
    scroll_area = QScrollArea()
    scrollable_widget = ScrollableWidget()
    scroll_area.setWidgetResizable(True)
    scroll_area.setWidget(scrollable_widget)

    # Set the scroll area as the main layout of the window
    layout = QVBoxLayout()
    layout.addWidget(scroll_area)
    window.setLayout(layout)

    window.resize(400, 300)
    window.show()
    sys.exit(app.exec_())