# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(400, 573)
        mainWindow.setFixedSize(400, 573)
        mainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 518))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_record = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_record.setFont(font)
        self.btn_record.setStyleSheet("padding: 4px;")
        self.btn_record.setObjectName("btn_record")
        self.horizontalLayout.addWidget(self.btn_record)
        self.btn_select_file = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_select_file.setFont(font)
        self.btn_select_file.setStyleSheet("padding: 4px;")
        self.btn_select_file.setObjectName("btn_select_file")
        self.horizontalLayout.addWidget(self.btn_select_file)
        self.btn_execute = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_execute.setFont(font)
        self.btn_execute.setStyleSheet("padding: 4px;")
        self.btn_execute.setObjectName("btn_execute")
        self.horizontalLayout.addWidget(self.btn_execute)
        self.label_times = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_times.setFont(font)
        self.label_times.setStyleSheet("margin-left: 6px")
        self.label_times.setObjectName("label_times")
        self.horizontalLayout.addWidget(self.label_times)
        self.spin_times = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spin_times.setStyleSheet("padding: 4px")
        self.spin_times.setPrefix("")
        self.spin_times.setProperty("value", 1)
        self.spin_times.setObjectName("spin_times")
        self.horizontalLayout.addWidget(self.spin_times)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setObjectName("formLayout")
        self.radio_one = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radio_one.setFont(font)
        self.radio_one.setStyleSheet("margin: 6px;")
        self.radio_one.setChecked(True)
        self.radio_one.setObjectName("radio_one")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radio_one)
        self.radio_assign = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radio_assign.setFont(font)
        self.radio_assign.setStyleSheet("margin: 6px;")
        self.radio_assign.setObjectName("radio_assign")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radio_assign)
        self.edit_assign = QtWidgets.QDateTimeEdit(self.verticalLayoutWidget)
        self.edit_assign.setMinimumSize(QtCore.QSize(160, 0))
        self.edit_assign.setStyleSheet("padding: 4px")
        self.edit_assign.setReadOnly(False)
        self.edit_assign.setCalendarPopup(True)
        self.edit_assign.setObjectName("edit_assign")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.edit_assign)
        self.radio_daily = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radio_daily.setFont(font)
        self.radio_daily.setStyleSheet("margin: 6px;")
        self.radio_daily.setObjectName("radio_daily")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radio_daily)
        self.edit_daily = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.edit_daily.setStyleSheet("padding: 4px")
        self.edit_daily.setAccelerated(False)
        self.edit_daily.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.edit_daily.setCalendarPopup(True)
        self.edit_daily.setObjectName("edit_daily")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.edit_daily)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_file_path = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_file_path.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.label_file_path.setFont(font)
        self.label_file_path.setWordWrap(True)
        self.label_file_path.setObjectName("label_file_path")
        self.verticalLayout.addWidget(self.label_file_path)
        self.text_status = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_status.sizePolicy().hasHeightForWidth())
        self.text_status.setSizePolicy(sizePolicy)
        self.text_status.setMinimumSize(QtCore.QSize(0, 290))
        self.text_status.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.text_status.setFont(font)
        self.text_status.setReadOnly(True)
        self.text_status.setObjectName("text_status")
        self.verticalLayout.addWidget(self.text_status)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 18))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setWindowFlags(QtCore.Qt.WindowType.WindowMinimizeButtonHint | QtCore.Qt.WindowType.WindowCloseButtonHint)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Recorder"))
        self.btn_record.setText(_translate("mainWindow", "Record"))
        self.btn_select_file.setText(_translate("mainWindow", "Open File"))
        self.btn_execute.setText(_translate("mainWindow", "Execute"))
        self.label_times.setText(_translate("mainWindow", "執行次數:"))
        self.radio_one.setText(_translate("mainWindow", "立即執行  "))
        self.radio_assign.setText(_translate("mainWindow", "指定時間  "))
        self.radio_daily.setText(_translate("mainWindow", "每天  "))
        self.label_file_path.setText(_translate("mainWindow", "file path:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())