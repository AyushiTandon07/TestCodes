# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QLabel
from PyQt5.QtGui import QTextFormat, QFont, QPainter
from PyQt5.QtCore import Qt, QRect, QSize
import sys


class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.editor = editor
        self.setFixedWidth(50)

    def sizeHint(self):
        return QSize(50, 0)

    def paintEvent(self, event):
        self.editor.lineNumberAreaPaintEvent(event)


class CodeEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout(self)

        self.lineNumberArea = LineNumberArea(self)

        self.editor = QPlainTextEdit()
        self.editor.setStyleSheet("font-size: 12px;")
        self.editor.setTabStopWidth(20)
        self.editor.textChanged.connect(self.updateLineNumberArea)

        layout.addWidget(self.lineNumberArea)
        layout.addWidget(self.editor)
        self.setLayout(layout)

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('PyQt5 Text Editor')
        self.show()

        self.updateLineNumberArea()

    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.lineNumberArea)
        painter.fillRect(event.rect(), Qt.lightGray)

        block_number = self.editor.document().blockCount()
        block = self.editor.document().findBlockByNumber(block_number - 1)
        top = int(self.editor.blockBoundingGeometry(block).translated(self.editor.contentOffset()).top())
        bottom = top + int(self.editor.blockBoundingRect(block).height())

        # Iterate over visible blocks in reverse order and draw line numbers
        while block.isValid() and bottom >= event.rect().top():
            if block.isVisible() and top <= event.rect().bottom():
                number = str(block_number)
                painter.setPen(Qt.black)
                painter.drawText(0, top, self.lineNumberArea.width(), self.editor.fontMetrics().height(),
                                 Qt.AlignRight, number)

            block = block.previous()
            bottom = top
            top = bottom - int(self.editor.blockBoundingRect(block).height())
            block_number -= 1

    def updateLineNumberArea(self, *args):
        self.lineNumberArea.update(0, 0, self.lineNumberArea.width(), self.editor.height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CodeEditor()
    sys.exit(app.exec_())
