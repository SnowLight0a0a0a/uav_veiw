from PyQt5 import QtCore, QtGui, QtWidgets
import config.apprcc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1036, 600)

        #程序图标
        icon = QtGui.QIcon(":img/icon/图片1.png")
        icon.addPixmap(QtGui.QPixmap(":img/icon/图片1.png"))
        MainWindow.setWindowIcon(icon)

        #布局
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        #自动随窗口拉伸
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)


        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)

        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("background:transparent")
        self.horizontalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setEnabled(False)

        #self.label_2.setStyleSheet("background:transparent")
        #self.label.setStyleSheet("background:transparent")


        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label,0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_raw = QtWidgets.QLabel(self.groupBox)
        self.label_raw.setAutoFillBackground(False)
        self.label_raw.setText("")
        self.label_raw.setScaledContents(False)
        self.label_raw.setAlignment(QtCore.Qt.AlignCenter)
        self.label_raw.setObjectName("label_raw")
        self.horizontalLayout_2.addWidget(self.label_raw)
        self.label_result = QtWidgets.QLabel(self.groupBox)
        self.label_result.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_result.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_result.setText("")
        self.label_result.setScaledContents(False)
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.horizontalLayout_2.addWidget(self.label_result)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.setStretch(1, 10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        #self.label_raw.setStyleSheet("background:transparent")
        #self.label_result.setStyleSheet("background:transparent")

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)

        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background:transparent")
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setProperty("showDropIndicator", True)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setFlow(0)
        self.listWidget.setMaximumHeight(20)

        self.horizontalLayout_3.setStretch(0, 9)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setStyleSheet("background:#F5F5F5;border-color:#F5F5F5")
        self.SelModel = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":img/icon/数据探索.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.SelModel.setIcon(icon1)
        self.SelModel.setObjectName("SelModel")
        self.SelFile = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":img/icon/打开.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.SelFile.setIcon(icon2)
        self.SelFile.setObjectName("SelFile")

        self.mark = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":img/icon/打开.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.mark.setIcon(icon4)
        self.mark.setObjectName("mark")

        self.RunProgram = QtWidgets.QAction(MainWindow)
        self.RunProgram.setCheckable(True)
        self.RunProgram.setChecked(False)
        self.RunProgram.setEnabled(True)

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":img/icon/暂停.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap(":img/icon/开始.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":img/icon/暂停.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.RunProgram.setIcon(icon3)
        self.RunProgram.setObjectName("RunProgram")



        self.Exit = QtWidgets.QAction(MainWindow)
        self.Exit.setObjectName("Exit")
        self.toolBar.addAction(self.SelModel)
        self.toolBar.addAction(self.SelFile)
        self.toolBar.addAction(self.RunProgram)
        #self.toolBar.addAction(self.mark)

        #./icon/background.jpg
        self.verticalLayout.addWidget(self.listWidget)
        self.listWidget.setStyleSheet("background:#FFFFFF;  border-image:none; border: 1px solid #E4E4E4; border-radius: 2px;")
        self.centralwidget.setStyleSheet("background:#F5F5F5")
        self.groupBox.setStyleSheet("background:#FFFFFF;")
        #self.groupBox.setStyleSheet("#groupBox{border-image: url(:/img/icon/background.jpg);\n"
        #                               "border: 0px solid #42adff;\n"
        #                               "border-radius:5px;}")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YOLOV5_search"))
        MainWindow.setWindowOpacity(1)
        self.label_2.setText(_translate("MainWindow", "Input Image"))
        self.label.setText(_translate("MainWindow", "Output Image"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.SelModel.setText(_translate("MainWindow", "Select Model"))
        self.SelModel.setToolTip(_translate("MainWindow", "Select Model"))
        self.SelFile.setText(_translate("MainWindow", "Select File"))
        self.SelFile.setToolTip(_translate("MainWindow", "Select File"))
        self.RunProgram.setText(_translate("MainWindow", "Run"))
        self.mark.setText(_translate("MainWindow", "mark"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
