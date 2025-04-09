import sys, os, re, openpyxl
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFrame, QLabel, QSizePolicy, \
    QHBoxLayout, QGraphicsOpacityEffect, QScrollArea, QLineEdit, QTextEdit, QSpacerItem, QGridLayout, QRadioButton, \
    QListWidget, QListWidgetItem, QAbstractScrollArea, QComboBox, QCheckBox, QFileDialog
from PyQt6.QtCore import QPropertyAnimation, Qt, QMetaObject, QSize, QRect, QEasingCurve, QThread, pyqtSignal
from PyQt6.QtGui import QPixmap, QPainter, QIcon, QImage,\
    QPainterPath
import required as rq

# DSA Report Repo size: 1 TB


# global variables
ClickedRadioButton = [[3, "Both"]]


class AnimatedDropdown(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Animated Dropdown Menu")
        self.setStyleSheet("background-color: rgb(212, 239, 223);")
        self.resize(800, 600)
        icon = QIcon()
        icon.addPixmap(QPixmap("C:\\Users\\ayushit\\Documents\\Python\\Icons\\Icon.png"), QIcon.Mode.Normal)
        icon.addPixmap(QPixmap("C:\\Users\\ayushit\\Documents\\Python\\Icons\\Icon.png"),
                       QIcon.Mode.Disabled)  # Not clickable Icon
        self.setWindowIcon(icon)

        # image = QImage("C:\\Users\\ayushit\\Documents\\Python\\Icons\\Icon_1.png")
        # image = QImage("C:\\Users\\ayushit\\Documents\\Python\\Icons\\AllInOneApp.jpg")
        # resized_image = image.scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        # self.image_label.size()
        # Apply rounded corners after scaling
        # rounded_image = self.apply_rounded_corners(resized_image, radius=30)

        # Get available screen size (excluding taskbar)
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        initial_width = min(1200, screen_width)
        initial_height = min(800, screen_height - 100)
        self.resize(initial_width, initial_height)

        # Central widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.central_widget.setGeometry(self.rect())

        # Layout for main UI
        self.CentralWidgetLayout = QVBoxLayout(self.central_widget)
        self.CentralWidgetLayout.setContentsMargins(4, 4, 4, 4)
        self.CentralWidgetLayout.setSpacing(3)

        # Heading Widget with Label
        self.MainHeadingWidget = QWidget(self.central_widget)
        self.MainHeadingWidget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.CentralWidgetLayout.addWidget(self.MainHeadingWidget)

        self.heading_layout = QHBoxLayout(self.MainHeadingWidget)
        self.heading_layout.setContentsMargins(5, 5, 5, 5)
        self.heading_layout.setSpacing(2)

        self.MainHeadingLabel = QLabel(self)
        self.MainHeadingLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.MainHeadingLabel.setSizePolicy(QLabel.sizePolicy(self.MainHeadingLabel))

        self.MainHeadingLabel_1 = QLabel(self.MainHeadingWidget)
        self.MainHeadingLabel_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.MainHeadingLabel_1.setSizePolicy(QLabel.sizePolicy(self.MainHeadingLabel_1))

        self.MainHeadingLabel_2 = QLabel(self.MainHeadingWidget)
        self.MainHeadingLabel_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.heading_layout.addWidget(self.MainHeadingLabel)
        self.heading_layout.addWidget(self.MainHeadingLabel_1)
        self.heading_layout.addWidget(self.MainHeadingLabel_2)

        self.heading_layout.setStretch(0, 1)
        self.heading_layout.setStretch(1, 9)
        self.heading_layout.setStretch(2, 1)

        # Button to trigger dropdown
        self.toggle_button = QPushButton("Show Menu")
        self.toggle_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.CentralWidgetLayout.addWidget(self.toggle_button)

        # ✅ Dropdown Menu
        self.dropdown_menu = QFrame(self.central_widget)  # ✅ Added parent
        self.dropdown_layout = QVBoxLayout(self.dropdown_menu)

        self.button1 = QPushButton("Option 1")
        self.button2 = QPushButton("Option 2")
        self.button3 = QPushButton("Option 3")

        self.dropdown_layout.addWidget(self.button1)
        self.dropdown_layout.addWidget(self.button2)
        self.dropdown_layout.addWidget(self.button3)

        # ✅ Initially Hidden
        self.dropdown_menu.setFixedHeight(0)
        self.CentralWidgetLayout.addWidget(self.dropdown_menu)

        # Adding Scroll Area
        self.scroll_area = QScrollArea(self.central_widget)
        self.scroll_area.setWidgetResizable(True)  # Allows resizing dynamically
        self.CentralWidgetLayout.addWidget(self.scroll_area)

        self.ScrollAreaWidget = QWidget(self)
        self.ScrollAreaWidget.setContentsMargins(3, 3, 3, 3)
        self.scroll_area.setWidget(self.ScrollAreaWidget)

        # ScrollArea Widget Layout to hold Items
        self.ScrollAreaWidgetLayout = QVBoxLayout(self.ScrollAreaWidget)
        self.ScrollAreaWidgetLayout.setSpacing(7)

        #  Widget to hold clickable buttons
        # self.widget_1 = QWidget(self.central_widget)
        self.widget_1 = QWidget(self.ScrollAreaWidget)
        self.widget_1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.widget_1.setMinimumHeight(120)
        self.ScrollAreaWidgetLayout.addWidget(self.widget_1)

        self.widget_1_Layout = QHBoxLayout(self.widget_1)
        self.widget_1_Layout.setContentsMargins(2, 2, 2, 2)
        self.widget_1_Layout.setSpacing(2)

        # Button 1 to mark reports DONE
        self.MarkReportsDoneButton = QPushButton(self.widget_1)
        self.MarkReportsDoneButton.setObjectName("MarkReportsDoneButton")
        self.MarkReportsDoneButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.MarkReportsDoneButton.setIcon(
            QIcon('C:/Users/ayushit/Documents/Python/BI layer UI/Lavendarfeather/check-square.svg'))
        self.MarkReportsDoneButton.setIconSize(QSize(78, 78))
        self.widget_1_Layout.addWidget(self.MarkReportsDoneButton)

        # Button 2 to search reports in GitHub and Report Repository
        self.SearchButton = QPushButton(self.widget_1)
        self.SearchButton.setObjectName("SearchButton")
        self.SearchButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.SearchButton.setIcon(QIcon('C:/Users/ayushit/Documents/Python/BI layer UI/Lavendarfeather/search.svg'))
        self.SearchButton.setIconSize(QSize(78, 78))
        self.widget_1_Layout.addWidget(self.SearchButton)

        # Button 3 to get list of reports having Airflow DAG
        self.AirflowReportsButton = QPushButton(self.widget_1)
        self.AirflowReportsButton.setObjectName("AirflowReportsButton")
        self.AirflowReportsButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.AirflowReportsButton.setIcon(
            QIcon('C:/Users/ayushit/Documents/Python/BI layer UI/Lavendarfeather/list.svg'))
        self.AirflowReportsButton.setIconSize(QSize(78, 78))
        self.widget_1_Layout.addWidget(self.AirflowReportsButton)

        # Button 4 to get history or queries running on generic ID
        self.QueryHistoryButton = QPushButton(self.widget_1)
        self.QueryHistoryButton.setObjectName("QueryHistoryButton")
        self.QueryHistoryButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.QueryHistoryButton.setIcon(
            QIcon('C:/Users/ayushit/Documents/Python/BI layer UI/Lavendarfeather/clock.svg'))
        self.QueryHistoryButton.setIconSize(QSize(78, 78))
        self.widget_1_Layout.addWidget(self.QueryHistoryButton)

        #  Big Parent Widget to hold small child widgets after clicking buttons
        self.widget_2 = QWidget(self.ScrollAreaWidget)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.widget_2.setMaximumHeight(0)
        self.widget_2.setContentsMargins(2, 2, 2, 2)
        self.ScrollAreaWidgetLayout.addWidget(self.widget_2)

        self.widget_2_Layout = QHBoxLayout(self.widget_2)
        self.widget_2_Layout.setContentsMargins(2, 2, 2, 2)
        self.widget_2_Layout.setSpacing(2)

        # Child Widget 1 for mark reports done button
        self.ChildWidget1 = QWidget(self.widget_2)
        self.ChildWidget1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.ChildWidget1.setVisible(False)
        self.ChildWidget1.setObjectName("ChildWidget1")
        self.widget_2_Layout.addWidget(self.ChildWidget1)

        # Layout of Child Widget 1 for mark reports done button
        self.ChildWidget1Layout = QHBoxLayout(self.ChildWidget1)
        self.ChildWidget1Layout.setContentsMargins(0, 0, 0, 0)
        self.ChildWidget1Layout.setSpacing(2)

        # Child Widget 1 Label for mark reports done button
        self.ChildWidget1Label = QLabel(self.ChildWidget1)
        self.ChildWidget1Label.setObjectName("ChildWidget1Label")
        self.ChildWidget1Layout.addWidget(self.ChildWidget1Label)

        # Child Widget 2 for Search reports button
        self.ChildWidget2 = QWidget(self.widget_2)
        self.ChildWidget2.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.ChildWidget2.setVisible(False)
        self.ChildWidget2.setObjectName("ChildWidget2")
        self.widget_2_Layout.addWidget(self.ChildWidget2)

        # Layout of Child Widget 2 for Search reports button
        self.ChildWidget2Layout = QHBoxLayout(self.ChildWidget2)
        self.ChildWidget2Layout.setContentsMargins(2, 4, 2, 2)
        self.ChildWidget2Layout.setSpacing(1)

        # Inner widget so that the form will be displayed only in center
        self.ChildWidget2FormWidget = QWidget(self.ChildWidget2)
        self.ChildWidget2FormWidget.setObjectName("ChildWidget2FormWidget")
        self.ChildWidget2FormWidget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.ChildWidget2FormWidget.setMaximumWidth(800)
        # self.ChildWidget2FormWidget.setFixedHeight(830)
        self.ChildWidget2Layout.addWidget(self.ChildWidget2FormWidget)

        # Vertical Layout for form items
        self.ChildWidget2FormWidgetLayout = QVBoxLayout(self.ChildWidget2FormWidget)
        self.ChildWidget2FormWidgetLayout.setContentsMargins(8, 5, 6, 4)  # left , top , right , bottom
        self.ChildWidget2FormWidgetLayout.setSpacing(10)
        self.ChildWidget2FormWidget.setLayout(self.ChildWidget2FormWidgetLayout)

        self.ChildWidget2WidgetForSearch = QWidget(self.ChildWidget2FormWidget)

        #  A horizontal Layout to store search label & line edit
        self.ChildWidget2LayoutForSearch = QHBoxLayout(self.ChildWidget2WidgetForSearch)
        self.ChildWidget2LayoutForSearch.setContentsMargins(0, 0, 4, 0)  # left , top , right , bottom
        self.ChildWidget2LayoutForSearch.setSpacing(0)

        # Child Widget 2 Label for Search reports button
        self.StingSearchLabel = QLabel(self.ChildWidget2WidgetForSearch)
        self.StingSearchLabel.setObjectName("StingSearchLabel")
        self.StingSearchLabel.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.ChildWidget2LayoutForSearch.addWidget(self.StingSearchLabel)

        self.ChildWidget2WidgetForSearch.setLayout(self.ChildWidget2LayoutForSearch)

        # Line edit to search the string
        self.StringSearchInput = QLineEdit(self.ChildWidget2WidgetForSearch)
        self.StringSearchInput.setObjectName("StringSearchInput")
        self.StringSearchInput.setPlaceholderText("Enter string you want to search...")
        self.StringSearchInput.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.ChildWidget2LayoutForSearch.addWidget(self.StringSearchInput)

        self.ChildWidget2LayoutForSearch.setStretch(0, 2)
        self.ChildWidget2LayoutForSearch.setStretch(1, 8)

        # Widget for windows path , save result file and combobox
        self.WindowsPathWidget = QWidget(self.ChildWidget2FormWidget)
        self.WindowsPathWidget.setContentsMargins(0, 0, 4, 0)  # left , top , right , bottom
        self.WindowsPathWidget.setObjectName("WindowsPathWidget")
        self.WindowsPathWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.WindowsPathWidget.setMaximumHeight(0)  # instead of setVisible(False) keep setMaximumHeight(0) because after the animation the widget contents are disappearing

        # vertical layout to contain multiple items
        self.WindowsPathWidgetLayout = QVBoxLayout(self.WindowsPathWidget)
        self.WindowsPathWidgetLayout.setContentsMargins(0, 0, 4, 0)  # left , top , right , bottom
        self.WindowsPathWidgetLayout.setSpacing(0)
        self.WindowsPathWidget.setLayout(self.WindowsPathWidgetLayout)

        #  A horizontal Layout for windows path
        self.WindowsPathSearchLayout = QHBoxLayout(self.WindowsPathWidget)
        self.WindowsPathSearchLayout.setContentsMargins(0, 0, 4, 4)  # left , top , right , bottom
        self.WindowsPathSearchLayout.setSpacing(4)

        # windows label for windows path
        self.WindowsPathSearchLabel = QLabel(self.WindowsPathWidget)
        self.WindowsPathSearchLabel.setObjectName("WindowsPathSearchLabel")
        self.WindowsPathSearchLabel.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.WindowsPathSearchLayout.addWidget(self.WindowsPathSearchLabel)

        # Line edit for windows path
        self.WindowsPathSearchInput = QLineEdit(self.WindowsPathWidget)
        self.WindowsPathSearchInput.setObjectName("WindowsPathSearchInput")
        self.WindowsPathSearchInput.setPlaceholderText("Enter the absolute path...")
        self.WindowsPathSearchInput.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.WindowsPathSearchInput.setEnabled(False)
        self.WindowsPathSearchLayout.addWidget(self.WindowsPathSearchInput)

        # Search button for windows path
        self.WindowsFilePathButton = QPushButton(self.WindowsPathWidget)
        self.WindowsFilePathButton.setObjectName("WindowsFilePathButton")
        self.WindowsFilePathButton.setIcon(
            QIcon('C:/Users/ayushit/Documents/Python/BI layer UI/Lavendarfeather/file.svg'))
        self.WindowsFilePathButton.setIconSize(QSize(20, 20))
        self.WindowsPathSearchLayout.addWidget(self.WindowsFilePathButton)

        # Adding items in Windows Path Search Layout
        self.WindowsPathSearchLayout.setStretch(0, 2)
        self.WindowsPathSearchLayout.setStretch(1, 7)
        self.WindowsPathSearchLayout.setStretch(2, 1)

        #  A horizontal Layout for windows result file
        self.WindowsResultFileLayout = QHBoxLayout(self.WindowsPathWidget)
        self.WindowsResultFileLayout.setContentsMargins(0, 0, 4, 4)  # left , top , right , bottom
        self.WindowsResultFileLayout.setSpacing(4)

        # Windows label to store the result file
        self.WindowsResultFileLabel = QLabel(self.WindowsPathWidget)
        self.WindowsResultFileLabel.setObjectName("WindowsResultFileLabel")
        self.WindowsResultFileLabel.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.WindowsResultFileLayout.addWidget(self.WindowsResultFileLabel)

        # Line edit for windows result file
        self.WindowsResulFileInput = QLineEdit(self.WindowsPathWidget)
        self.WindowsResulFileInput.setObjectName("WindowsResulFileInput")
        self.WindowsResulFileInput.setPlaceholderText("Enter the absolute path...")
        self.WindowsResulFileInput.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.WindowsResulFileInput.setEnabled(False)
        self.WindowsResultFileLayout.addWidget(self.WindowsResulFileInput)

        # Directory choose button for windows result file
        self.WindowsResultFilePathButton = QPushButton(self.WindowsPathWidget)
        self.WindowsResultFilePathButton.setObjectName("WindowsResultFilePathButton")
        self.WindowsResultFilePathButton.setIcon(
            QIcon('C:/Users/ayushit/Documents/Python/BI layer UI/Lavendarfeather/file.svg'))
        self.WindowsResultFilePathButton.setIconSize(QSize(20, 20))
        self.WindowsResultFileLayout.addWidget(self.WindowsResultFilePathButton)

        # Adding items in Windows Result File Layout
        self.WindowsResultFileLayout.setStretch(0, 2)
        self.WindowsResultFileLayout.setStretch(1, 7)
        self.WindowsResultFileLayout.setStretch(2, 1)

        # Widget to hold Combobox and its label
        self.WindowsComboboxWidget = QWidget(self.WindowsPathWidget)
        self.WindowsComboboxWidget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.WindowsComboboxWidget.setContentsMargins(0, 0, 4, 0)  # left , top , right , bottom

        # Vertical layout to hold File type extension combobox and label
        self.WindowsComboboxLayout = QHBoxLayout(self.WindowsComboboxWidget)
        self.WindowsComboboxLayout.setSpacing(0)
        self.WindowsComboboxLayout.setContentsMargins(0, 0, 4, 0)

        self.WindowsComboboxWidget.setLayout(self.WindowsComboboxLayout)

        # Label to hold combobox label
        self.WindowsExtensionComboboxLabel = QLabel(self.WindowsComboboxWidget)
        self.WindowsExtensionComboboxLabel.setObjectName("WindowsExtensionComboboxLabel")

        self.WindowsExtensionComboBox = rq.CheckableListWidget()
        self.WindowsExtensionComboBox.setObjectName("WindowsExtensionComboBox")
        self.WindowsExtensionComboBoxScrollbar = self.WindowsExtensionComboBox.verticalScrollBar()

        self.WindowsExtensionComboboxLabel2 = QLabel(self.WindowsComboboxWidget)
        self.WindowsExtensionComboboxLabel2.setObjectName("WindowsExtensionComboboxLabel2")


        self.WindowsComboboxLayout.addWidget(self.WindowsExtensionComboboxLabel, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.WindowsComboboxLayout.addWidget(self.WindowsExtensionComboBox, alignment= Qt.AlignmentFlag.AlignHCenter)
        self.WindowsComboboxLayout.addWidget(self.WindowsExtensionComboboxLabel2)

        self.WindowsComboboxLayout.setStretch(0,2)
        self.WindowsComboboxLayout.setStretch(1,7)
        self.WindowsComboboxLayout.setStretch(2,1)


        # Addinf items in Windows Path Widget Layout
        self.WindowsPathWidgetLayout.addLayout(self.WindowsPathSearchLayout)
        self.WindowsPathWidgetLayout.addLayout(self.WindowsResultFileLayout)
        self.WindowsPathWidgetLayout.addWidget(self.WindowsComboboxWidget)
        self.WindowsPathWidgetLayout.setStretch(0,2)
        self.WindowsPathWidgetLayout.setStretch(1,2)
        self.WindowsPathWidgetLayout.setStretch(2,6)


        # Search button to search the reports
        self.RepositorySearchButton = QPushButton(self.ChildWidget2FormWidget)
        self.RepositorySearchButton.setObjectName("RepositorySearchButton")
        self.RepositorySearchButton.setMinimumSize(100, 40)

        # A horizontal layout to center the button inside VLayout
        self.RepositorySearchButtonLayout = QHBoxLayout(self.ChildWidget2FormWidget)
        self.RepositorySearchButtonLayout.addWidget(self.RepositorySearchButton, alignment=Qt.AlignmentFlag.AlignHCenter)

        # # List Widget to hold radio buttons
        self.ChildWidget2ListWidget = QListWidget(self.ChildWidget2FormWidget)
        self.ChildWidget2ListWidget.setSpacing(7)
        self.ChildWidget2ListWidget.setContentsMargins(0, 0, 2, 0)
        self.ChildWidget2ListWidget.setMinimumHeight(140)
        self.ChildWidget2ListWidget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        # Set a fixed width for the QListWidget if needed
        # self.ChildWidget2ListWidget.setFixedWidth(self.ChildWidget2ListWidget.sizeHint().width())

        # Optionally, you can set the height based on the content
        # self.ChildWidget2ListWidget.setFixedHeight(self.ChildWidget2ListWidget.sizeHint().height())
        #
        # Disable horizontal scrollbar for QListWidget
        self.ChildWidget2ListWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Radio Button to choose GitHub and Windows Repository
        self.RadioButton1 = QRadioButton(self.ChildWidget2ListWidget)
        self.RadioButton2 = QRadioButton(self.ChildWidget2ListWidget)
        self.RadioButton3 = QRadioButton(self.ChildWidget2ListWidget)

        self.RadioButton1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.RadioButton2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.RadioButton3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.RadioButton1.setMinimumHeight(40)
        self.RadioButton2.setMinimumHeight(40)
        self.RadioButton3.setMinimumHeight(40)

        # Create the QListWidgetItems
        item1 = QListWidgetItem()
        item2 = QListWidgetItem()
        item3 = QListWidgetItem()

        # Add the items to the list widget
        self.ChildWidget2ListWidget.addItem(item1)
        self.ChildWidget2ListWidget.addItem(item2)
        self.ChildWidget2ListWidget.addItem(item3)

        # Set the widgets for each list item
        self.ChildWidget2ListWidget.setItemWidget(item1, self.RadioButton1)
        self.ChildWidget2ListWidget.setItemWidget(item2, self.RadioButton2)
        self.ChildWidget2ListWidget.setItemWidget(item3, self.RadioButton3)

        # Set size hints for each item based on the radio button's size
        item1.setSizeHint(self.RadioButton1.sizeHint())
        item2.setSizeHint(self.RadioButton2.sizeHint())
        item3.setSizeHint(self.RadioButton3.sizeHint())

        self.RadioButton3.setChecked(True)

        # Adding status label to show error messages
        # self.StatusWidget = QWidget(self.ChildWidget2FormWidget)
        # self.StatusWidget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        # self.StatusWidget.setMaximumHeight(0)
        # self.StatusWidget.setObjectName("StatusWidget")
        #
        # # Layout of Child Widget 2 to show error messages
        # self.StatusLayout = QHBoxLayout(self.StatusWidget)
        # self.StatusLayout.setContentsMargins(2, 2, 2, 2)
        # self.StatusLayout.setSpacing(0)

        # Status label to show error messages
        # self.StatusLabel = QLabel(self.StatusWidget)
        self.StatusLabel = QLabel(self.ChildWidget2FormWidget)
        self.StatusLabel.setObjectName("StatusLabel")
        self.StatusLabel.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.StatusLabel.setVisible(True)

        # Adding blank widget as a placeholder after Radio Buttons
        # self.blankWidget = QWidget(self.ChildWidget2FormWidget)
        # self.blankWidget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        # self.blankWidget.setObjectName("blankWidget")
        #
        # # Layout of Child Widget 1 for mark reports done button
        # self.blankLayout = QHBoxLayout(self.blankWidget)
        # self.blankLayout.setContentsMargins(0, 0, 0, 0)
        # self.blankLayout.setSpacing(0)
        # self.blankWidget.setLayout(self.blankLayout)
        #
        # self.blankLabel = QLabel(self.blankWidget)
        # self.blankLayout.addWidget(self.blankLabel)


        # Adding items in Form Widget inside Child Widget 2
        self.ChildWidget2FormWidgetLayout.addWidget(self.ChildWidget2WidgetForSearch)       #string search widget
        self.ChildWidget2FormWidgetLayout.addWidget(self.ChildWidget2ListWidget)                # Radio Button List widget
        self.ChildWidget2FormWidgetLayout.addWidget(self.WindowsPathWidget)                     # Windows Path widget
        self.ChildWidget2FormWidgetLayout.addWidget(self.StatusLabel)
        self.ChildWidget2FormWidgetLayout.addLayout(self.RepositorySearchButtonLayout)


        # Child Widget 3 for Airflow reports button
        self.ChildWidget3 = QWidget(self.widget_2)
        self.ChildWidget3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.ChildWidget3.setVisible(False)
        self.ChildWidget3.setObjectName("ChildWidget3")
        self.widget_2_Layout.addWidget(self.ChildWidget3)

        # Layout of Child Widget 1 for Airflow reports button
        self.ChildWidget3Layout = QHBoxLayout(self.ChildWidget3)
        self.ChildWidget3Layout.setContentsMargins(0, 0, 0, 0)
        self.ChildWidget3Layout.setSpacing(2)

        # Child Widget 1 Label for Airflow reports button
        self.ChildWidget3Label = QLabel(self.ChildWidget3)
        self.ChildWidget3Label.setObjectName("ChildWidget3Label")
        self.ChildWidget3Layout.addWidget(self.ChildWidget3Label)

        #  Child Widget 4 for Query History button
        self.ChildWidget4 = QWidget(self.widget_2)
        self.ChildWidget4.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.ChildWidget4.setVisible(False)
        self.ChildWidget4.setObjectName("ChildWidget4")
        self.widget_2_Layout.addWidget(self.ChildWidget4)

        # Layout of Child Widget 4 for Query History button
        self.ChildWidget4Layout = QHBoxLayout(self.ChildWidget4)
        self.ChildWidget4Layout.setContentsMargins(0, 0, 0, 0)
        self.ChildWidget4Layout.setSpacing(2)

        # Child Widget 4 Label for Query History button
        self.ChildWidget4Label = QLabel(self.ChildWidget4)
        self.ChildWidget4Label.setObjectName("ChildWidget4Label")
        self.ChildWidget4Layout.addWidget(self.ChildWidget4Label)


        # self.Label = QLabel(self.central_widget)
        self.Label = QLabel(self.ScrollAreaWidget)
        self.Label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Label.setStyleSheet("font-size: 20px; font-weight: bold; color: white; background-color:green;")
        self.ScrollAreaWidgetLayout.addWidget(self.Label)

        #  Widget to show windows search result
        self.widget_3 = QWidget(self.ScrollAreaWidget)
        self.widget_3.setObjectName("widget_3")
        self.widget_3.setContentsMargins(2, 2, 2, 2)
        self.widget_3.setMinimumHeight(120)
        self.ScrollAreaWidgetLayout.addWidget(self.widget_3)


        self.Label_2 = QLabel(self.ScrollAreaWidget)
        self.Label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Label_2.setStyleSheet("font-size: 20px; font-weight: bold; color: white; background-color:white;")
        self.ScrollAreaWidgetLayout.addWidget(self.Label_2)

        # ✅ Animation setup
        self.animation = QPropertyAnimation(self.dropdown_menu, b"maximumHeight")
        self.animation.setDuration(400)  # Animation time in milliseconds
        self.menu_expanded = False  # Menu state flag

        # Button Clicked functions
        self.toggle_button.clicked.connect(self.toggle_menu)
        self.button1.clicked.connect(self.displayText)
        self.button2.clicked.connect(self.displayText)

        self.MarkReportsDoneButton.clicked.connect(
            lambda: self.HandleItemPressed(self.MarkReportsDoneButton, self.widget_2))
        self.SearchButton.clicked.connect(lambda: self.HandleItemPressed(self.SearchButton, self.widget_2))
        self.AirflowReportsButton.clicked.connect(
            lambda: self.HandleItemPressed(self.AirflowReportsButton, self.widget_2))
        self.QueryHistoryButton.clicked.connect(lambda: self.HandleItemPressed(self.QueryHistoryButton, self.widget_2))

        # Connect radio buttons to the function
        self.RadioButton1.clicked.connect(lambda: self.RadioButtonClicked(int(1)))
        self.RadioButton2.clicked.connect(lambda: self.RadioButtonClicked(int(2)))
        self.RadioButton3.clicked.connect(lambda: self.RadioButtonClicked(int(3)))

        self.RepositorySearchButton.clicked.connect(self.SearchReports)
        self.LoadExtensionList()

        self.StringSearchInput.textChanged.connect(self.SearchInputTextChanged)

        self.WindowsPathSearchInput.textChanged.connect(self.WindowsSearchInputTextChanged)
        self.WindowsFilePathButton.clicked.connect(self.ChooseWindowsSearchFilePath)

        self.WindowsResulFileInput.textChanged.connect(self.WindowsResultFileInputTextChanged)
        self.WindowsResultFilePathButton.clicked.connect(self.ChooseWindowsResultSaveFilePath)







        # StyleSheet Properties
        self.MainHeadingLabel.setStyleSheet(
            "QLabel {"
            "color: rgb(0, 0, 0); /* Set your desired text color */"
            "font-family: Georgia, serif;"
            "font-size: 45px; /* Set your desired font size */"
            "text-decoration: underline;"
            "/*	border-bottom: 0.5px solid black;/*/"
            "border: 2px solid black;"
            "}")

        self.MainHeadingWidget.setStyleSheet("QWidget{background-color: rgb(237, 234, 222);}")

        self.MainHeadingLabel_1.setStyleSheet("QLabel {"
                                              "color: rgb(0, 0, 0); /* Set your desired text color */"
                                              "font-family: Georgia, serif;"
                                              "font-size: 45px; /* Set your desired font size */"
                                              "/*text-decoration: underline;*/"
                                              "/*	border-bottom: 0.5px solid black;/*/"
                                              "border: 2px solid black;"
                                              "}")

        self.MainHeadingLabel_2.setStyleSheet("QLabel {"
                                              "color: rgb(0, 0, 0); /* Set your desired text color */"
                                              "font-family: Georgia, serif;"
                                              "font-size: 45px; /* Set your desired font size */"
                                              "text-decoration: underline;"
                                              "/*	border-bottom: 0.5px solid black;/*/"
                                              "}")

        self.dropdown_menu.setStyleSheet("background-color: lightgray; border-radius: 5px;")

        self.widget_1.setStyleSheet("QWidget{background-color: transparent;}")

        self.MarkReportsDoneButton.setStyleSheet("QPushButton{\n"
                                                 "background-position: center;\n"
                                                 "background-color: transparent;\n"
                                                 # "background-color:rgb(99, 89, 145);\n"
                                                 "border-radius: 15px; /* Set your desired border radius */\n"
                                                 "color:rgb(89, 50, 25);\n"
                                                 "font-family: Georgia, serif;\n"
                                                 "font-size: 19px; /* Set your desired font size */\n"

                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 # "background-color: rgb(53, 50, 76);\n"
                                                 "background-color: rgb(115, 198, 182);\n"
                                                 "border-style: outset;\n"
                                                 "border-width: 0.5px;\n"
                                                 "color:rgb(89, 50, 25);\n"
                                                 "font-family: Georgia, serif;\n"
                                                 "font-size: 19px; /* Set your desired font size */\n"
                                                 "}\n"

                                                 "QPushButton:pressed {\n"
                                                 "background-color: rgb(115, 198, 182);\n"
                                                 "border-style: none;\n"
                                                 "}\n"
                                                 )
        self.SearchButton.setStyleSheet("QPushButton{\n"
                                        "background-position: center;\n"
                                        "background-color: transparent;\n"
                                        # "background-color:rgb(99, 89, 145);\n"
                                        "border-radius: 15px; /* Set your desired border radius */\n"
                                        "color:rgb(89, 50, 25);\n"
                                        "font-family: Georgia, serif;\n"
                                        "font-size: 19px; /* Set your desired font size */\n"

                                        "}\n"
                                        "QPushButton:hover {\n"
                                        # "background-color: rgb(53, 50, 76);\n"
                                        "background-color: rgb(115, 198, 182);\n"
                                        "border-style: outset;\n"
                                        "border-width: 0.5px;\n"
                                        "color:rgb(89, 50, 25);\n"
                                        "font-family: Georgia, serif;\n"
                                        "font-size: 19px; /* Set your desired font size */\n"
                                        "}\n"

                                        "QPushButton:pressed {\n"
                                        "background-color: rgb(115, 198, 182);\n"
                                        "border-style: none;\n"
                                        "}\n"
                                        )

        self.AirflowReportsButton.setStyleSheet("QPushButton{\n"
                                                "background-position: center;\n"
                                                "background-color: transparent;\n"
                                                # "background-color:rgb(99, 89, 145);\n"
                                                "border-radius: 15px; /* Set your desired border radius */\n"
                                                "color:rgb(89, 50, 25);\n"
                                                "font-family: Georgia, serif;\n"
                                                "font-size: 19px; /* Set your desired font size */\n"

                                                "}\n"
                                                "QPushButton:hover {\n"
                                                # "background-color: rgb(53, 50, 76);\n"
                                                "background-color: rgb(115, 198, 182);\n"
                                                "border-style: outset;\n"
                                                "border-width: 0.5px;\n"
                                                "color:rgb(89, 50, 25);\n"
                                                "font-family: Georgia, serif;\n"
                                                "font-size: 19px; /* Set your desired font size */\n"
                                                "}\n"

                                                "QPushButton:pressed {\n"
                                                "background-color: rgb(115, 198, 182);\n"
                                                "border-style: none;\n"
                                                "}\n"
                                                )
        self.QueryHistoryButton.setStyleSheet("QPushButton{\n"
                                              "background-position: center;\n"
                                              "background-color: transparent;\n"
                                              # "background-color:rgb(99, 89, 145);\n"
                                              "border-radius: 15px; /* Set your desired border radius */\n"
                                              "color:rgb(89, 50, 25);\n"
                                              "font-family: Georgia, serif;\n"
                                              "font-size: 19px; /* Set your desired font size */\n"

                                              "}\n"
                                              "QPushButton:hover {\n"
                                              # "background-color: rgb(53, 50, 76);\n"
                                              "background-color: rgb(115, 198, 182);\n"
                                              "border-style: outset;\n"
                                              "border-width: 0.5px;\n"
                                              "color:rgb(89, 50, 25);\n"
                                              "font-family: Georgia, serif;\n"
                                              "font-size: 19px; /* Set your desired font size */\n"
                                              "}\n"

                                              "QPushButton:pressed {\n"
                                              "background-color: rgb(115, 198, 182);\n"
                                              "border-style: none;\n"
                                              "}\n"
                                              )
        self.widget_2.setStyleSheet("QWidget{background-color: transparent;\n"
                                    "border-radius: 15px;\n"
                                    "}")


        self.ChildWidget1.setStyleSheet("QWidget{\n"
                                        "    background-color: rgb(53, 50, 76);\n"
                                        "    border-radius: 15px;\n"
                                        "    padding:8px;\n"
                                        "    }"
                                        )
        self.ChildWidget2.setStyleSheet("QWidget{\n"
                                        "    background-color: rgb(115, 198, 182);\n"
                                        # "    background-color: transparent;\n"
                                        "    border-radius: 15px;\n"
                                        "    padding:8px;\n"
                                        "    }"
                                        )
        self.ChildWidget3.setStyleSheet("QWidget{\n"
                                        "    background-color: rgb(53, 50, 76);\n"
                                        "    border-radius: 15px;\n"
                                        "    padding:8px;\n"
                                        "    }"
                                        )
        self.ChildWidget4.setStyleSheet("QWidget{\n"
                                        "    background-color: rgb(53, 50, 76);\n"
                                        "    border-radius: 15px;\n"
                                        "    padding:8px;\n"
                                        "    }"
                                        )
        self.ChildWidget1Label.setStyleSheet("QLabel{\n"
                                             "    background-image: transparent;\n"
                                             "    background-repeat: no-repeat;\n"
                                             # "    color: rgb(42, 38, 62);\n"
                                             # "    font-size:20px;\n"
                                             "border-radius: 15px;\n"
                                             "}")

        self.ChildWidget1Label.setStyleSheet("QLabel{\n"
                                             "    background-image: transparent;\n"
                                             "    background-repeat: no-repeat;\n"
                                             # "    color: rgb(42, 38, 62);\n"
                                             # "    font-size:20px;\n"
                                             "border-radius: 15px;\n"
                                             "}")
        self.StingSearchLabel.setStyleSheet("QLabel{\n"
                                        "    color: rgb(89, 50, 25);\n"
                                        "    font-size:14px;\n"
                                        "    font-family: Georgia, serif;\n"
                                        "}")
        self.StringSearchInput.setStyleSheet("QLineEdit{\n"
                                        "    background-color: rgb(117,178,165);/* Set your desired background color */\n"
                                        "    color: rgb(89, 50, 25);/* Set your desired text color */\n"
                                        "    font-family: Georgia, serif;\n"
                                        "    font-size: 14px; /* Set your desired font size */\n"
                                        "    border-style: none;\n"
                                        "    border-radius: 8px; /* Set your desired border radius */\n"
                                        "    padding: 8px; /* Set your desired padding */\n"
                                        "    }")

        self.ChildWidget2FormWidget.setStyleSheet("QWidget#ChildWidget2FormWidget {\n"
                                                  # "    background-color: red;\n"
                                                  "    background-color: transparent;\n"
                                                  "    border-radius: 15px;\n"
                                                  "    border: 1px solid rgb(237, 234, 222);\n"
                                                  "    padding:8px;\n"
                                                  "font-family: Georgia, serif;\n"
                                                  "font-size: 15px; /* Set your desired font size */\n"
                                                  "    }"
                                                  "QWidget#ChildWidget2FormWidget * {\n"
                                                  "border: none; \n"
                                                  "}"
                                                  )

        self.RepositorySearchButton.setStyleSheet("QPushButton{\n"
                                         "background-position: center;\n"
                                         # "background-color: rgb(117, 130, 178);\n"
                                         #   "background-color: rgb(151, 164, 208);\n"
                                         # "background-color: transparent;\n"
                                         # "background-color: rgb(184,216,190);\n"
                                                  "background-color: rgb(184,219,211);\n"

                                         "border-style: outset;\n"
                                         "border-width: 0.5px;\n"
                                         "border-radius: 15px; /* Set your desired border radius */\n"
                                         "color:rgb(89, 50, 25);\n"
                                         "font-family: Georgia, serif;\n"
                                         "font-size: 19px; /* Set your desired font size */\n"

                                         "}\n"
                                         "QPushButton:hover {\n"
                                         # "background-color: rgb(184,219,211);\n"
                                         # "background-color: rgb(117,178,165);\n"
                                         #  "background-color: rgb(212, 239, 223);\n"
                                                  "background-color: rgb(184,216,190);\n"
                                         "border-style: outset;\n"
                                         "border-width: 0.5px;\n"
                                         "color:rgb(89, 50, 25);\n"
                                         "font-family: Georgia, serif;\n"
                                         "font-size: 19px; /* Set your desired font size */\n"
                                         "}\n"

                                         "QPushButton:pressed {\n"
                                         "background-color: rgb(184,219,211);\n"
                                         "border-style: none;\n"
                                         "}\n"
                                                  )

        self.ChildWidget2ListWidget.setStyleSheet("QListWidget{\n"
                                                  # "    background-color: rgb(53, 50, 76);\n"
                                                  "    background-color: rgb(117,178,165);\n"
                                                  # "    background-color: transparent;\n"
                                                  "    border-radius: 15px;\n"
                                                  "    }")

        self.RadioButton1.setStyleSheet("QRadioButton{\n"
                                        "    background-color: rgb(117,178,165);\n"
                                        "    color: rgb(89, 50, 25);/* Set your desired text color */\n"
                                        "    font-family: Georgia, serif;\n"
                                        "    font-size: 16px; /* Set your desired font size */\n"
                                        "    border-radius: 25px; /* Set your desired border radius */\n"
                                        # "    height:30;\n"
                                        "    }")

        self.RadioButton2.setStyleSheet("QRadioButton{\n"
                                        "    background-color: rgb(117,178,165);\n"
                                        "    color: rgb(89, 50, 25);/* Set your desired text color */\n"
                                        "    font-family: Georgia, serif;\n"
                                        "    font-size: 16px; /* Set your desired font size */\n"
                                        "    border-radius: 25px; /* Set your desired border radius */\n"
                                        # "    height:30;\n"
                                        "    }")
        self.RadioButton3.setStyleSheet("QRadioButton{\n"
                                        "    background-color: rgb(117,178,165);\n"
                                        "    color: rgb(89, 50, 25);/* Set your desired text color */\n"
                                        "    font-family: Georgia, serif;\n"
                                        "    font-size: 16px; /* Set your desired font size */\n"
                                        "    border-radius: 25px; /* Set your desired border radius */\n"
                                        # "    height:30;\n"
                                        "    }")

        self.WindowsPathSearchLabel.setStyleSheet("QLabel{\n"
                                                "    color: rgb(89, 50, 25);\n"
                                                "    font-size:14px;\n"
                                                "    font-family: Georgia, serif;\n"
                                                "}")
        self.WindowsPathSearchInput.setStyleSheet("QLineEdit{\n"
                                                "    background-color: rgb(117,178,165);/* Set your desired background color */\n"
                                                "    color: rgb(89, 50, 25);/* Set your desired text color */\n"
                                                "    font-family: Georgia, serif;\n"
                                                "    font-size: 14px; /* Set your desired font size */\n"
                                                "    border-style: none;\n"
                                                "    border-radius: 8px; /* Set your desired border radius */\n"
                                                "    padding: 8px; /* Set your desired padding */\n"
                                                "    }")

        self.WindowsPathWidget.setStyleSheet("QWidget{background-color: transparent;}")

        self.ChildWidget2WidgetForSearch.setStyleSheet("QWidget{background-color: transparent;}")

        self.WindowsExtensionComboboxLabel.setStyleSheet("QLabel{\n"
                                                            "    color: rgb(89, 50, 25);\n"
                                                            "    font-size:14px;\n"
                                                            "    font-family: Georgia, serif;\n"
                                                            "}")
        self.WindowsExtensionComboboxLabel2.setStyleSheet("QLabel{\n"
                                                          "background-color: transparent;"
                                                         # "    color: rgb(89, 50, 25);\n"
                                                         # "    font-size:14px;\n"
                                                         # "    font-family: Georgia, serif;\n"
                                                         "}")

        self.WindowsExtensionComboBox.setStyleSheet("QListWidget{\n"
                                                       "color: rgb(89, 50, 25); \n"
                                                       "background-color: rgb(117,178,165);\n"
                                                       "}"
                                                    )

        self.WindowsExtensionComboBoxScrollbar.setStyleSheet("QScrollBar{\n"
                                                                 "color: rgb(89, 50, 25); \n"
                                                                 "background-color: rgb(151,208,196);\n"
                                                                 "  font-size:13px;\n"
                                                                 "    font-family: Georgia, serif;\n"
                                                                 "}"

                                                                 " QScrollBar: vertical{\n"
                                                                 " border: 2px Solid;\n"
                                                                 "background: rgb(89, 50, 25);\n"
                                                                 "width: 25px;\n"
                                                                 "margin: 2px 0 2px 0;\n"
                                                                 "}"
                                                                 "  QScrollBar::handle: vertical {\n"
                                                                 "background:  rgb(89, 50, 25);\n"
                                                                 "min - height: 20px;\n"
                                                                 "border - radius: 5px;\n"
                                                                 "}"
                                                                 " QScrollBar::add - line: vertical,\n"
                                                                 " QScrollBar::sub - line: vertical{\n"
                                                                 " background: none;\n"
                                                                 "border :none;\n"
                                                                 "}"
                                                             )

        # self.StatusWidget.setStyleSheet("QWidget{\n"
        #                                 "    background-color: rgb(53, 50, 76);\n"
        #                                 # "    background-color: transparent;\n"
        #                                 # "    border-radius: 5px;\n"
        #                                 # "    padding:2px;\n"
        #                                 "    }"
        #                                 )

        self.StatusLabel.setStyleSheet("QLabel{\n"
                                       "    background-color: transparent;\n"
                                       "    color: red;\n"
                                       "    font-size:16px;\n"
                                       "    font-family: Georgia, serif;\n"
                                       "    padding:2px;\n"
                                       "}")
        self.WindowsFilePathButton.setStyleSheet("QPushButton{\n"
                                                    "background-position: center;\n"
                                                    "background-color: transparent;\n"
                                                    "border-style: outset;\n"
                                                    "border-width: 0.5px;\n"
                                                    "border-radius: 10px; /* Set your desired border radius */\n"
                                                    "color:rgb(89, 50, 25);\n"
                                                    "font-family: Georgia, serif;\n"
                                                    "font-size: 19px; /* Set your desired font size */\n"

                                                    "}\n"
                                                    "QPushButton:hover {\n"
                                                    "background-color: rgb(184,216,190);\n"
                                                    "border-style: outset;\n"
                                                    "border-width: 0.5px;\n"
                                                    "border-radius: 10px;\n"
                                                    "color:rgb(89, 50, 25);\n"
                                                    "font-family: Georgia, serif;\n"
                                                    "font-size: 19px; /* Set your desired font size */\n"
                                                    "}\n"

                                                    "QPushButton:pressed {\n"
                                                    "background-color: rgb(184,219,211);\n"
                                                    "border-style: none;\n"
                                                    "}\n"
                                                 )

        self.WindowsResultFileLabel.setStyleSheet("QLabel{\n"
                                                "    color: rgb(89, 50, 25);\n"
                                                "    font-size:14px;\n"
                                                "    font-family: Georgia, serif;\n"
                                                "}")
        self.WindowsResulFileInput.setStyleSheet("QLineEdit{\n"
                                                "    background-color: rgb(117,178,165);/* Set your desired background color */\n"
                                                "    color: rgb(89, 50, 25);/* Set your desired text color */\n"
                                                "    font-family: Georgia, serif;\n"
                                                "    font-size: 14px; /* Set your desired font size */\n"
                                                "    border-style: none;\n"
                                                "    border-radius: 8px; /* Set your desired border radius */\n"
                                                "    padding: 8px; /* Set your desired padding */\n"
                                                "    }")

        self.WindowsResultFilePathButton.setStyleSheet("QPushButton{\n"
                                                    "background-position: center;\n"
                                                    "background-color: transparent;\n"
                                                    "border-style: outset;\n"
                                                    "border-width: 0.5px;\n"
                                                    "border-radius: 10px; /* Set your desired border radius */\n"
                                                    "color:rgb(89, 50, 25);\n"
                                                    "font-family: Georgia, serif;\n"
                                                    "font-size: 19px; /* Set your desired font size */\n"

                                                    "}\n"
                                                    "QPushButton:hover {\n"
                                                    "background-color: rgb(184,216,190);\n"
                                                    "border-style: outset;\n"
                                                    "border-width: 0.5px;\n"
                                                    "border-radius: 10px;\n"
                                                    "color:rgb(89, 50, 25);\n"
                                                    "font-family: Georgia, serif;\n"
                                                    "font-size: 19px; /* Set your desired font size */\n"
                                                    "}\n"

                                                    "QPushButton:pressed {\n"
                                                    "background-color: rgb(184,219,211);\n"
                                                    "border-style: none;\n"
                                                    "}\n"
                                                       )

        self.widget_3.setStyleSheet("QWidget{background-color: red;\n"
                                    "border-radius: 15px;\n"
                                    "}")
        self.WindowsComboboxWidget.setStyleSheet("QWidget{background-color: transparent;\n"
                                    "border-radius: 15px;\n"
                                    "}")


        # Retranslate UI Function Call
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.MainHeadingLabel_1.setText("GNA ALL IN ONE APP")
        self.MarkReportsDoneButton.setText("Mark Reports Done")
        self.SearchButton.setText("Search Reports in \nGitHub && Report Repository")
        # self.SearchButton.setText("<html><body>Search Reports<br><span style='font-size: 12px;'>(GitHub & Report Repository)</span></body></html>")
        self.AirflowReportsButton.setText("List of Airflow Reports")
        self.QueryHistoryButton.setText("Query History of Generic ID")
        self.ChildWidget1Label.setText("Hi button 1 pressed")
        self.StingSearchLabel.setText("Enter the String to Search:")
        self.ChildWidget3Label.setText("Hi button 3 pressed")
        self.ChildWidget4Label.setText("Hi button 4 pressed")
        self.Label.setText("")
        self.RepositorySearchButton.setText("Search")
        self.RadioButton1.setText("GitHub Repository Only")
        self.RadioButton2.setText("Windows Repository Only")
        self.RadioButton3.setText("Both")
        self.WindowsPathSearchLabel.setText("Choose the Windows Search Directory: ")
        self.WindowsExtensionComboboxLabel.setText("Choose File Types to Search in:  ")
        self.WindowsFilePathButton.setToolTip("Choose File Path")
        self.WindowsResultFileLabel.setText("Choose the Windows Directory  \nto Save the Result File:")
        self.WindowsResultFilePathButton.setToolTip("Choose File Path")



    def toggle_menu(self):
        """Expand/Collapse dropdown menu with animation"""
        if self.menu_expanded:
            self.animation.setStartValue(100)  # Current height
            self.animation.setEndValue(0)  # Collapse
        else:
            self.animation.setStartValue(0)  # Current height
            self.animation.setEndValue(100)  # Expand

        self.animation.start()
        self.menu_expanded = not self.menu_expanded  # Toggle state

    def displayText(self):
        self.Label.setText("Clicked Option 1")
        self.Label_2.setText("Clicked Option 2")

    def HandleItemPressed(self, buttonClicked, widget):
        self.AnimationWidgetShow(widget)
        self.ToggleWidget(buttonClicked, widget)

    def AnimationWidgetShow(self, widget):
        # Animation setup
        self.animationWidget = QPropertyAnimation(widget, b"maximumHeight")
        self.animationWidget.setDuration(600)  # Animation time in milliseconds
        self.Expanded = False  # Menu state flag

        """Expand/Collapse dropdown menu with animation"""
        if self.Expanded:
            self.animationWidget.setStartValue(500)  # Current height
            self.animationWidget.setEndValue(0)  # Collapse
        else:
            widget.setMaximumHeight(10)
            self.animationWidget.setStartValue(10)  # Current height

            self.animationWidget.setEndValue(500)  # Expand

        self.animationWidget.start()
        self.Expanded = not self.Expanded  # Toggle state

    def AnimationWidgetHide(self, widgetToBeHidden):
        # Animation setup
        self.animationWidget = QPropertyAnimation(widgetToBeHidden, b"minimumHeight")
        self.animationWidget.setDuration(600)  # Animation time in milliseconds
        self.Expanded = True  # Menu state flag
        """Expand/Collapse dropdown menu with animation"""
        if self.Expanded:
            self.animationWidget.setStartValue(50)  # Current height
            self.animationWidget.setEndValue(0)  # Collapse
        else:
            self.animationWidget.setStartValue(0)  # Current height
            self.animationWidget.setEndValue(50)  # Expand

        self.animationWidget.start()
        self.Expanded = not self.Expanded  # Toggle state

    def ToggleWidget(self, buttonClicked, widgetToBeDisplayed):
        """Expand/Collapse dropdown menu with animation"""
        if buttonClicked.objectName() == 'MarkReportsDoneButton':
            if self.ChildWidget1.isVisible():
                self.AnimationWidgetHide(widgetToBeDisplayed)
                self.ChildWidget1.setVisible(False)
            else:
                self.ChildWidget1.setVisible(True)
                self.ChildWidget2.setVisible(False)
                self.ChildWidget3.setVisible(False)
                self.ChildWidget4.setVisible(False)

        elif buttonClicked.objectName() == 'SearchButton':
            if self.ChildWidget2.isVisible():
                self.AnimationWidgetHide(widgetToBeDisplayed)
                self.ChildWidget2.setVisible(False)
            else:
                self.ChildWidget1.setVisible(False)
                self.ChildWidget2.setVisible(True)
                self.ChildWidget3.setVisible(False)
                self.ChildWidget4.setVisible(False)

        if buttonClicked.objectName() == 'AirflowReportsButton':
            if self.ChildWidget3.isVisible():
                self.AnimationWidgetHide(widgetToBeDisplayed)
                self.ChildWidget3.setVisible(False)
            else:
                self.ChildWidget1.setVisible(False)
                self.ChildWidget2.setVisible(False)
                self.ChildWidget3.setVisible(True)
                self.ChildWidget4.setVisible(False)
        if buttonClicked.objectName() == 'QueryHistoryButton':
            if self.ChildWidget4.isVisible():
                self.AnimationWidgetHide(widgetToBeDisplayed)
                self.ChildWidget4.setVisible(False)
            else:
                self.ChildWidget1.setVisible(False)
                self.ChildWidget2.setVisible(False)
                self.ChildWidget3.setVisible(False)
                self.ChildWidget4.setVisible(True)

    def SearchReports(self):
        global ClickedRadioButton

        # Validations
        validationFlag = self.FieldsValidation()

        if validationFlag:
            self.StatusLabel.setText("")
            self.ResettingInputFieldsStyleSheet(True, [1,2,3])
            if ClickedRadioButton[0][0] == 2:  # Windows button clicked
                self.SearchWindowsRepository()
            elif ClickedRadioButton[0][0] == 1:
                self.SearchGitHubRepository()
            else:
                self.SearchGitHubAndWindowsRepository()

    # Radio button Clicked function
    def RadioButtonClicked(self, val):
        global ClickedRadioButton

        ClickedRadioButton.clear()
        if val == 1:
            ClickedRadioButton.append([val, "GitHub Repo Only"])
        elif val == 2:
            ClickedRadioButton.append([val, "Windows Repo Only"])
        elif val == 3:
            ClickedRadioButton.append([val, "Both"])

        if ClickedRadioButton[0][0] == 2:
            if self.WindowsPathWidget.height() == 0:
                #  Widget expanding for the fist time
                self.StatusLabel.setText("")
                self.ResettingInputFieldsStyleSheet(True, [1])
                self.WindowsPathWidget.setMaximumHeight(250)
                self.WindowsPathWidget.updateGeometry()
                self.WindowsComboboxWidget.setMinimumHeight(90)
            else:
                #  Widget already expanded
                if len(self.StatusLabel.text()) > 0:             # There is an error message already
                    self.StatusLabel.setVisible(True)
        else:
            self.StatusLabel.setText("")
            self.ResettingInputFieldsStyleSheet(True, [1])
            if self.WindowsPathWidget.height() > 0:
                self.WindowsPathWidget.setMaximumHeight(0)
                self.WindowsPathSearchInput.setText("")
                self.WindowsResulFileInput.setText("")
                self.WindowsExtensionComboBox.SetAllItemsChecked()

    # Search Windows Repository function
    def SearchWindowsRepository(self):
        SearchString = self.StringSearchInput.text()
        SearchDirectory = self.WindowsPathSearchInput.text()
        SearchFileTypesExtensions = self.WindowsExtensionComboBox.ReturnCheckedValues()
        ResultDirectory = self.WindowsResulFileInput.text()
        # print("Windows Dir Thread Calling")
        self.thread = SearchWindowsRepositoryThread(SearchDirectory, SearchString, SearchFileTypesExtensions, ResultDirectory )
        self.thread.progress.connect(self.update_status_label)
        self.thread.finished.connect(self.show_results)
        self.thread.start()

    def update_status_label(self, message):
        self.StatusLabel.setText(message)

    def show_results(self, results):
        self.StatusLabel.setText(f"Search complete. {len(results)} results found.")


    # Search GitHub Repository function
    def SearchGitHubRepository(self):
        # extensions = (".sql", ".py", ".txt", ".xlsx")
        print("GitHub")

    # Search GitHubAndWindows Repository function
    def SearchGitHubAndWindowsRepository(self):
        # extensions = (".sql", ".py", ".txt", ".xlsx")
        print("Both")

    # Form Fields validation function
    def FieldsValidation(self):
        self.StatusLabel.setText("")
        currentText = self.StatusLabel.text()
        validationFlag = True

        if len(self.StringSearchInput.text()) == 0:
            self.StatusLabel.setText("<sup>**</sup>Search String Required")
            self.StatusLabel.setVisible(True)
            # self.StringSearchInput.setStyleSheet("border: 0.5px solid red; background-color: rgb(117,178,165);")
            self.ResettingInputFieldsStyleSheet(False, [1])
            currentText = self.StatusLabel.text()
            validationFlag = False

        if validationFlag:
            ## Windows Repository Button Selected
            if ClickedRadioButton[0][0] == 2:
                # Validations
                if len(self.WindowsPathSearchInput.text()) == 0:
                    self.StatusLabel.setText(currentText + "<sup>**</sup>Search Directory Required.")
                    self.StatusLabel.setVisible(True)
                    # self.WindowsPathSearchInput.setStyleSheet("border: 0.5px solid red; background-color: rgb(117,178,165);")
                    self.ResettingInputFieldsStyleSheet(False, [2])
                    currentText = self.StatusLabel.text()
                    validationFlag = False

                if len(self.WindowsPathSearchInput.text()) > 0:
                    SearchDir = self.WindowsPathSearchInput.text()
                    # Checking if Directory exists
                    if not (os.path.isdir(SearchDir)):
                        print("Folder does not exist")
                        self.StatusLabel.setText(currentText + '\n' + "<sup>**</sup>Search Directory Is Not Correct Or Directory Does Not Exists.")
                        # self.WindowsPathSearchInput.setStyleSheet("border: 0.5px solid red; background-color: rgb(117,178,165);")
                        self.ResettingInputFieldsStyleSheet(False, [2])
                        currentText = self.StatusLabel.text()
                        validationFlag = False

                # DIR should not be blank
                if len(self.WindowsResulFileInput.text()) == 0:
                    self.StatusLabel.setText(currentText + "<sup>**</sup>Result Directory Required.")
                    self.StatusLabel.setVisible(True)
                    # self.WindowsResulFileInput.setStyleSheet("border: 0.5px solid red; background-color: rgb(117,178,165);")
                    self.ResettingInputFieldsStyleSheet(False, [3])
                    currentText = self.StatusLabel.text()
                    validationFlag = False

                # DIR should exists
                if len(self.WindowsResulFileInput.text()) > 0:
                    # SearchDir = self.WindowsResulFileInput.text()
                    SearchDir = os.path.dirname(self.WindowsResulFileInput.text())
                    print(SearchDir)
                    # Checking if Directory exists
                    if not (os.path.isdir(SearchDir)):
                        print("Save Folder does not exist")
                        self.StatusLabel.setText(currentText + '\n' + "<sup>**</sup>Result Directory Is Not Correct Or Directory Does Not Exists.")
                        # self.WindowsResulFileInput.setStyleSheet("border: 0.5px solid red; background-color: rgb(117,178,165);")
                        self.ResettingInputFieldsStyleSheet(False, [3])
                        currentText = self.StatusLabel.text()
                        validationFlag = False

                Checkedvalues = self.WindowsExtensionComboBox.ReturnCheckedValues()
                if len(Checkedvalues) == 0:
                    newText = "<sup>**</sup>File Types should not be blank."
                    self.StatusLabel.setText(currentText + '\n' + newText)
                    self.StatusLabel.setVisible(True)
                    self.WindowsExtensionComboboxLabel.setStyleSheet(
                        "border: 0.5px solid red; background-color: rgb(117,178,165);")
                    currentText = self.StatusLabel.text()
                    validationFlag = False

        return validationFlag

    # Load Extension List function
    def LoadExtensionList(self):
        extensions = ["All", ".sql", ".py", ".txt", ".xlsx"]
        self.WindowsExtensionComboBox.addItems(extensions)
        self.WindowsExtensionComboBox.SetAllItemsChecked()

    # Clear error message function
    def SearchInputTextChanged(self):
        # Clear Status Label only when there was error
        if self.StatusLabel.text().__contains__("Search String"):
            self.StatusLabel.setText("")
            self.StringSearchInput.setStyleSheet("QLineEdit{\n"
                                                 "    background-color: rgb(117,178,165);/* Set your desired background color */\n"
                                                 "    color: rgb(89, 50, 25);/* Set your desired text color */\n"
                                                 "    font-family: Georgia, serif;\n"
                                                 "    font-size: 14px; /* Set your desired font size */\n"
                                                 "    border-style: none;\n"
                                                 "    border-radius: 8px; /* Set your desired border radius */\n"
                                                 "    padding: 8px; /* Set your desired padding */\n"
                                                 "    }")

    # Clear error message function
    def WindowsSearchInputTextChanged(self):
        # Clear Status Label only when there was error
        if self.StatusLabel.text().__contains__("Search Directory Required"):
            self.StatusLabel.setText("")
            # text = self.StatusLabel.text().split('<sup>**</sup>',1)[0]
            self.WindowsPathSearchInput.setStyleSheet("QLineEdit{\n"
                                                      "    background-color: rgb(117,178,165);/* Set your desired background color */\n"
                                                      "    color: rgb(89, 50, 25);/* Set your desired text color */\n"
                                                      "    font-family: Georgia, serif;\n"
                                                      "    font-size: 14px; /* Set your desired font size */\n"
                                                      "    border-style: none;\n"
                                                      "    border-radius: 8px; /* Set your desired border radius */\n"
                                                      "    padding: 8px; /* Set your desired padding */\n"
                                                      "    }")

    def WindowsResultFileInputTextChanged(self):
        # Clear Status Label only when there was error
        if self.StatusLabel.text().__contains__("Result Directory Required"):
            self.StatusLabel.setText("")
            self.WindowsResulFileInput.setStyleSheet("QLineEdit{\n"
                                                      "    background-color: rgb(117,178,165);/* Set your desired background color */\n"
                                                      "    color: rgb(89, 50, 25);/* Set your desired text color */\n"
                                                      "    font-family: Georgia, serif;\n"
                                                      "    font-size: 14px; /* Set your desired font size */\n"
                                                      "    border-style: none;\n"
                                                      "    border-radius: 8px; /* Set your desired border radius */\n"
                                                      "    padding: 8px; /* Set your desired padding */\n"
                                                      "    }")



    # Choose windows folder to search in function
    def ChooseWindowsSearchFilePath(self):
        dialog = QFileDialog()
        dialog.setStyleSheet("QFileDialog{ background-color: #F0F0F0;}")
        # file_path: The full path of the selected  file( as a string).
        # _ : The selected file type filter (not used, so it's assigned to _ as a throwaway variable
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.WindowsPathSearchInput.setText(folder_path)

    # Choose windows folder to save result file function
    def ChooseWindowsResultSaveFilePath(self):
        dialog = QFileDialog()
        dialog.setStyleSheet("QFileDialog{ background-color: #F0F0F0;}")
        # file_path: The full path of the selected  file( as a string).
        # _ : The selected file type filter (not used, so it's assigned to _ as a throwaway variable
        folder_path = QFileDialog.getSaveFileName(self, "Select Folder", "" , "Text Files (*.txt)")        # Dialog Title, Default Directory, File type to save result
        # print(folder_path)            # Folder_path is a Tuple: ('C:/Users/ayushit/Pictures/Sweaters/SaveFile.txt', 'Text Files (*.txt)')
        fileName = folder_path[0]
        print('fileName:', fileName)
        print('folderPath:', folder_path)
        base_name = os.path.basename(fileName)
        print('BaseName:', base_name)
        if folder_path != "":
            if fileName.split('.')[-1].lower() == 'txt':
                self.WindowsResulFileInput.setText(fileName)
            else:
                fileName += str('.txt')
                self.WindowsResulFileInput.setText(fileName)

    # Resetting Input fields Style Sheet
    def ResettingInputFieldsStyleSheet(self, val, fieldIndex):

        Indexes = fieldIndex            # list variable

        if val:
            for i in range(0, len(Indexes)):
                if Indexes[i] == 1:
                    self.StringSearchInput.setStyleSheet("QLineEdit{\n"
                                                         "    background-color: rgb(117,178,165);/* Set your desired background color */\n"
                                                         "    color: rgb(89, 50, 25);/* Set your desired text color */\n"
                                                         "    font-family: Georgia, serif;\n"
                                                         "    font-size: 14px; /* Set your desired font size */\n"
                                                         "    border-style: none;\n"
                                                         "    border-radius: 8px; /* Set your desired border radius */\n"
                                                         "    padding: 8px; /* Set your desired padding */\n"
                                                         "    }")
                elif Indexes[i] == 2:
                    self.WindowsPathSearchInput.setStyleSheet("QLineEdit{\n"
                                                              "    background-color: rgb(117,178,165);/* Set your desired background color */\n"
                                                              "    color: rgb(89, 50, 25);/* Set your desired text color */\n"
                                                              "    font-family: Georgia, serif;\n"
                                                              "    font-size: 14px; /* Set your desired font size */\n"
                                                              "    border-style: none;\n"
                                                              "    border-radius: 8px; /* Set your desired border radius */\n"
                                                              "    padding: 8px; /* Set your desired padding */\n"
                                                              "    }")
                elif Indexes[i] == 3:
                    self.WindowsResulFileInput.setStyleSheet("QLineEdit{\n"
                                                             "    background-color: rgb(117,178,165);/* Set your desired background color */\n"
                                                             "    color: rgb(89, 50, 25);/* Set your desired text color */\n"
                                                             "    font-family: Georgia, serif;\n"
                                                             "    font-size: 14px; /* Set your desired font size */\n"
                                                             "    border-style: none;\n"
                                                             "    border-radius: 8px; /* Set your desired border radius */\n"
                                                             "    padding: 8px; /* Set your desired padding */\n"
                                                             "    }")

        elif not val:
            for i in range(0, len(Indexes)):
                if Indexes[i] == 1:
                    self.StringSearchInput.setStyleSheet("border: 0.5px solid red; background-color: rgb(117,178,165);")

                elif Indexes[i] == 2:
                    self.WindowsPathSearchInput.setStyleSheet("border: 0.5px solid red; background-color: rgb(117,178,165);")

                elif Indexes[i] == 3:
                    self.WindowsResulFileInput.setStyleSheet("border: 0.5px solid red; background-color: rgb(117,178,165);")




# Windows Directory Search Thread
class SearchWindowsRepositoryThread(QThread):
    progress = pyqtSignal(str)       # Emit messages to update UI
    finished = pyqtSignal(list)      # Emit results when done

    def __init__(self, search_dir, search_text, ext, ResultDirectory):
        super().__init__()
        self.search_directory = search_dir
        self.search_text = search_text
        self.result_directory = ResultDirectory
        self.results = []
        self.hidden_files = []
        self.searchable_files = []
        self.unread_files = []
        self.oversized_files = []
        self.skipped_dirs = []
        print(ext)
        print(type(ext))
        self.extensions = tuple(ext)
        self.skip_dirs = ["decommissioned", "bkp", "backup", "bckp", "decommission", "decomm", "decom"]

        self.search_pattern = re.compile(re.escape(self.search_text), re.IGNORECASE)

    def run(self):
        self.scan_directory(self.search_directory, self.extensions)
        print('SearchableFileList: ', self.searchable_files)
        self.search_in_file(self.searchable_files)
        self.WriteOutputResultsInFile(self.result_directory)
        self.finished.emit(self.results)


    def scan_directory(self, path, extensionsValues):
        self.progress.emit('Scanning Directories to Search In !!')
        print("inside scan_directory")
        with os.scandir(path) as entries:
            for entry in entries:
                print(os.path.normpath(entry.path))
                # print(type(extensionsValues))
                if entry.is_file() and entry.name.endswith(extensionsValues):
                    if entry.name.startswith("~$"):                 # to add ~ press shift + tilde sign
                        self.hidden_files.append(os.path.normpath(entry.path))
                    elif os.path.getsize(os.path.normpath(entry.path)) > 100 * 1024 * 1024:  # 100MB   i.e. 100000 kb  1 kb = 1024 bytes , 1 MB= 1024 kb = 1024*1024 and 100 mb = 100 * 1024 * 1024
                        self.oversized_files.append(os.path.normpath(entry.path))
                    else:
                        self.searchable_files.append(os.path.normpath(entry.path))
                elif entry.is_dir():
                    if any(skip_word in entry.name.lower() for skip_word in self.skip_dirs):                # we don't want to search in decommissioned or backup directories
                        self.skipped_dirs.append(os.path.abspath(os.path.normpath(entry.path)))                           # Log skipped directory
                        continue
                    self.scan_directory(os.path.normpath(entry.path), extensionsValues)


    def search_in_file(self, files):
        self.progress.emit('Searching Started....')
        for file_path in files:
            try:
                if file_path.endswith((".sql", ".py", ".txt")):
                    # print("Inside search_in_file function , filepath is: ", file_path)
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        for line_number, line in enumerate(f, 1):
                            if self.search_pattern.search(line):
                                self.results.append(f"Match found in {file_path} at line {line_number}: {line.strip()}")

                elif file_path.endswith(".xlsx"):
                    try:
                        wb = openpyxl.load_workbook(file_path, data_only=True)
                        for sheet in wb.worksheets:
                            for row in sheet.iter_rows():
                                for cell in row:
                                    if cell.value and self.search_pattern.search(str(cell.value)):
                                        self.results.append(f"Match found in {file_path} (Sheet: {sheet.title}, Cell: {cell.coordinate}): {cell.value}")
                    except Exception as e:
                        # print(f"Could not open Excel file {file_path}: {e}")
                        self.unread_files.append(file_path)

            except Exception as e:
                print(f"Could not read {file_path}: {e}")
                self.unread_files.append(file_path)


    def WriteOutputResultsInFile(self, result_dir):
        self.progress.emit('Searching Completed. Writing Results in Output File....')
        output_path = result_dir
        with open(output_path, 'w', encoding="utf-8") as file:
            for line in self.results:
                file.write(line + "\n")

            if self.unread_files:
                file.write("\n----- Unable to Open Files: Check Manually -------\n")
                for i, unread in enumerate(self.unread_files):
                    file.write(f"{i} - {unread}\n")

            if self.oversized_files:
                file.write("\n----- Files Skipped (Over 100MB) -------\n")
                for i, big_file in enumerate(self.oversized_files):
                    file.write(f"{i} - {big_file}\n")

            if self.skipped_dirs:
                file.write("\n----- Skipped Folders (Decommissioned/Backup/etc.) -------\n")
                for i, folder in enumerate(self.skipped_dirs, 1):
                    file.write(f"{i} - {folder}\n")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnimatedDropdown()
    window.show()
    sys.exit(app.exec())
