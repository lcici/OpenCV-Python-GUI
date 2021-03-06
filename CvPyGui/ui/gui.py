# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1030, 635)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.h_img_lay = QtWidgets.QHBoxLayout()
        self.h_img_lay.setObjectName("h_img_lay")
        self.original_img_v_lay = QtWidgets.QVBoxLayout()
        self.original_img_v_lay.setObjectName("original_img_v_lay")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.original_img_v_lay.addItem(spacerItem)
        self.original_name_lbl = QtWidgets.QLabel(self.centralwidget)
        self.original_name_lbl.setScaledContents(False)
        self.original_name_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.original_name_lbl.setObjectName("original_name_lbl")
        self.original_img_v_lay.addWidget(self.original_name_lbl)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.original_img_v_lay.addItem(spacerItem1)
        self.original_frame_lbl = QtWidgets.QLabel(self.centralwidget)
        self.original_frame_lbl.setMinimumSize(QtCore.QSize(500, 500))
        self.original_frame_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.original_frame_lbl.setObjectName("original_frame_lbl")
        self.original_img_v_lay.addWidget(self.original_frame_lbl)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.original_img_v_lay.addItem(spacerItem2)
        self.h_img_lay.addLayout(self.original_img_v_lay)
        self.processed_img_v_lay = QtWidgets.QVBoxLayout()
        self.processed_img_v_lay.setObjectName("processed_img_v_lay")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.processed_img_v_lay.addItem(spacerItem3)
        self.processed_name_lbl = QtWidgets.QLabel(self.centralwidget)
        self.processed_name_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.processed_name_lbl.setObjectName("processed_name_lbl")
        self.processed_img_v_lay.addWidget(self.processed_name_lbl)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.processed_img_v_lay.addItem(spacerItem4)
        self.processed_frame_lbl = QtWidgets.QLabel(self.centralwidget)
        self.processed_frame_lbl.setMinimumSize(QtCore.QSize(500, 500))
        self.processed_frame_lbl.setBaseSize(QtCore.QSize(0, 0))
        self.processed_frame_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.processed_frame_lbl.setObjectName("processed_frame_lbl")
        self.processed_img_v_lay.addWidget(self.processed_frame_lbl)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.processed_img_v_lay.addItem(spacerItem5)
        self.h_img_lay.addLayout(self.processed_img_v_lay)
        self.verticalLayout_4.addLayout(self.h_img_lay)
        self.h_btn_lay = QtWidgets.QHBoxLayout()
        self.h_btn_lay.setObjectName("h_btn_lay")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_btn_lay.addItem(spacerItem6)
        self.countours_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.countours_check_box.setObjectName("countours_check_box")
        self.h_btn_lay.addWidget(self.countours_check_box)
        self.filter_select = QtWidgets.QComboBox(self.centralwidget)
        self.filter_select.setObjectName("filter_select")
        self.h_btn_lay.addWidget(self.filter_select)
        self.add_filter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_filter_btn.setObjectName("add_filter_btn")
        self.h_btn_lay.addWidget(self.add_filter_btn)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_btn_lay.addItem(spacerItem7)
        self.verticalLayout_4.addLayout(self.h_btn_lay)
        self.v_filters_lay = QtWidgets.QVBoxLayout()
        self.v_filters_lay.setObjectName("v_filters_lay")
        self.verticalLayout_4.addLayout(self.v_filters_lay)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1030, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_image = QtWidgets.QAction(MainWindow)
        self.actionOpen_image.setObjectName("actionOpen_image")
        self.actionSave_original_image = QtWidgets.QAction(MainWindow)
        self.actionSave_original_image.setObjectName("actionSave_original_image")
        self.actionSave_processed_image = QtWidgets.QAction(MainWindow)
        self.actionSave_processed_image.setObjectName("actionSave_processed_image")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionOpen_image)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_original_image)
        self.menuFile.addAction(self.actionSave_processed_image)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionLicense)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Processing"))
        self.original_name_lbl.setText(_translate("MainWindow", "Original"))
        self.original_frame_lbl.setText(_translate("MainWindow", "TextLabel"))
        self.processed_name_lbl.setText(_translate("MainWindow", "Processed"))
        self.processed_frame_lbl.setText(_translate("MainWindow", "TextLabel"))
        self.countours_check_box.setText(_translate("MainWindow", "Show countours"))
        self.add_filter_btn.setText(_translate("MainWindow", "Add filter"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_image.setText(_translate("MainWindow", "Open image"))
        self.actionSave_original_image.setText(_translate("MainWindow", "Save original image"))
        self.actionSave_processed_image.setText(_translate("MainWindow", "Save processed image"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionLicense.setText(_translate("MainWindow", "License"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

