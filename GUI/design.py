# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Fri Jul 29 01:18:00 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1089, 732)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.lblInputFilename = QtGui.QLabel(self.groupBox_2)
        self.lblInputFilename.setObjectName(_fromUtf8("lblInputFilename"))
        self.verticalLayout_7.addWidget(self.lblInputFilename)
        self.btnBrowse = QtGui.QPushButton(self.groupBox_2)
        self.btnBrowse.setMinimumSize(QtCore.QSize(100, 0))
        self.btnBrowse.setMaximumSize(QtCore.QSize(100, 50))
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.verticalLayout_7.addWidget(self.btnBrowse)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.scrollArea_3 = QtGui.QScrollArea(self.groupBox)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.scrollAreaWidgetContents_9 = QtGui.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 236, 471))
        self.scrollAreaWidgetContents_9.setObjectName(_fromUtf8("scrollAreaWidgetContents_9"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lineEdit_5 = QtGui.QLineEdit(self.scrollAreaWidgetContents_9)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout_3.addWidget(self.lineEdit_5, 3, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents_9)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents_9)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents_9)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.scrollAreaWidgetContents_9)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_3.addWidget(self.lineEdit_4, 2, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.scrollAreaWidgetContents_9)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents_9)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents_9)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents_9)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_10.addWidget(self.label_7)
        self.scrollArea = QtGui.QScrollArea(self.scrollAreaWidgetContents_9)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_6 = QtGui.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 198, 348))
        self.scrollAreaWidgetContents_6.setObjectName(_fromUtf8("scrollAreaWidgetContents_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.checkBox_2 = QtGui.QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout_3.addWidget(self.checkBox_2)
        self.checkBox = QtGui.QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_3.addWidget(self.checkBox)
        self.checkBox_9 = QtGui.QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.verticalLayout_3.addWidget(self.checkBox_9)
        self.checkBox_4 = QtGui.QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.verticalLayout_3.addWidget(self.checkBox_4)
        self.checkBox_3 = QtGui.QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.verticalLayout_3.addWidget(self.checkBox_3)
        self.checkBox_10 = QtGui.QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.verticalLayout_3.addWidget(self.checkBox_10)
        self.checkBox_8 = QtGui.QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.verticalLayout_3.addWidget(self.checkBox_8)
        self.checkBox_12 = QtGui.QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        self.verticalLayout_3.addWidget(self.checkBox_12)
        self.checkBox_6 = QtGui.QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.verticalLayout_3.addWidget(self.checkBox_6)
        self.checkBox_13 = QtGui.QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        self.verticalLayout_3.addWidget(self.checkBox_13)
        self.checkBox_5 = QtGui.QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.verticalLayout_3.addWidget(self.checkBox_5)
        self.checkBox_11 = QtGui.QCheckBox(self.scrollAreaWidgetContents_6)
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.verticalLayout_3.addWidget(self.checkBox_11)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_6)
        self.verticalLayout_10.addWidget(self.scrollArea)
        self.label_8 = QtGui.QLabel(self.scrollAreaWidgetContents_9)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_10.addWidget(self.label_8)
        self.scrollArea_2 = QtGui.QScrollArea(self.scrollAreaWidgetContents_9)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_8 = QtGui.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 198, 152))
        self.scrollAreaWidgetContents_8.setObjectName(_fromUtf8("scrollAreaWidgetContents_8"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.checkBox_7 = QtGui.QCheckBox(self.scrollAreaWidgetContents_8)
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.verticalLayout_4.addWidget(self.checkBox_7)
        self.checkBox_14 = QtGui.QCheckBox(self.scrollAreaWidgetContents_8)
        self.checkBox_14.setObjectName(_fromUtf8("checkBox_14"))
        self.verticalLayout_4.addWidget(self.checkBox_14)
        self.checkBox_16 = QtGui.QCheckBox(self.scrollAreaWidgetContents_8)
        self.checkBox_16.setObjectName(_fromUtf8("checkBox_16"))
        self.verticalLayout_4.addWidget(self.checkBox_16)
        self.checkBox_17 = QtGui.QCheckBox(self.scrollAreaWidgetContents_8)
        self.checkBox_17.setObjectName(_fromUtf8("checkBox_17"))
        self.verticalLayout_4.addWidget(self.checkBox_17)
        self.checkBox_15 = QtGui.QCheckBox(self.scrollAreaWidgetContents_8)
        self.checkBox_15.setObjectName(_fromUtf8("checkBox_15"))
        self.verticalLayout_4.addWidget(self.checkBox_15)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_8)
        self.verticalLayout_10.addWidget(self.scrollArea_2)
        self.verticalLayout_10.setStretch(1, 1)
        self.verticalLayout_10.setStretch(3, 1)
        self.verticalLayout_5.addLayout(self.verticalLayout_10)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_9)
        self.verticalLayout_6.addWidget(self.scrollArea_3)
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_6.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.groupBox)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.listWidget = QtGui.QListWidget(self.groupBox_3)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout_8.addWidget(self.listWidget)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_9.addWidget(self.label_9)
        self.comboBox = QtGui.QComboBox(self.groupBox_4)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_9.addWidget(self.comboBox)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_10.addWidget(self.label_4)
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_10.addWidget(self.lineEdit_3)
        self.horizontalSlider = QtGui.QSlider(self.groupBox_4)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalLayout_10.addWidget(self.horizontalSlider)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        self.graphicsView = PlotWidget(self.groupBox_4)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout_9.addWidget(self.graphicsView)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1089, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Select Spectra", None))
        self.lblInputFilename.setText(_translate("MainWindow", "Select SN File...", None))
        self.btnBrowse.setText(_translate("MainWindow", "Browse", None))
        self.groupBox.setTitle(_translate("MainWindow", "Priors", None))
        self.lineEdit_5.setText(_translate("MainWindow", "50", None))
        self.label_6.setText(_translate("MainWindow", "Max Age", None))
        self.label_5.setText(_translate("MainWindow", "Min Age", None))
        self.label_2.setText(_translate("MainWindow", "Max Redshift", None))
        self.lineEdit_4.setText(_translate("MainWindow", "-50", None))
        self.lineEdit_2.setText(_translate("MainWindow", "0.5", None))
        self.label.setText(_translate("MainWindow", "Min Redshift", None))
        self.lineEdit.setText(_translate("MainWindow", "0", None))
        self.label_7.setText(_translate("MainWindow", "SN Types", None))
        self.checkBox_2.setText(_translate("MainWindow", "Type Ia-norm", None))
        self.checkBox.setText(_translate("MainWindow", "Type Ia-91bg", None))
        self.checkBox_9.setText(_translate("MainWindow", "Type Ia-pec", None))
        self.checkBox_4.setText(_translate("MainWindow", "Type Ib-norm", None))
        self.checkBox_3.setText(_translate("MainWindow", "Type IIb", None))
        self.checkBox_10.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_8.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_12.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_6.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_13.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_11.setText(_translate("MainWindow", "CheckBox", None))
        self.label_8.setText(_translate("MainWindow", "Host Types", None))
        self.checkBox_7.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_14.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_16.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_17.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_15.setText(_translate("MainWindow", "CheckBox", None))
        self.pushButton.setText(_translate("MainWindow", "Re-fit with priors", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Best Matches", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Best Matches", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox_4.setTitle(_translate("MainWindow", "Analyse selection", None))
        self.label_9.setText(_translate("MainWindow", "Template", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "New Item", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "wd", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "dw", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "New Item", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "New Item", None))
        self.comboBox.setItemText(5, _translate("MainWindow", "qd", None))
        self.comboBox.setItemText(6, _translate("MainWindow", "New Item", None))
        self.label_4.setText(_translate("MainWindow", "Redshift", None))
        self.lineEdit_3.setText(_translate("MainWindow", "0", None))

from pyqtgraph import PlotWidget
