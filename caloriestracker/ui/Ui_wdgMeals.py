# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caloriestracker/ui/wdgMeals.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgMeals(object):
    def setupUi(self, wdgMeals):
        wdgMeals.setObjectName("wdgMeals")
        wdgMeals.resize(1012, 669)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(wdgMeals)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl = QtWidgets.QLabel(wdgMeals)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout.addWidget(self.lbl)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.calendar = QtWidgets.QCalendarWidget(wdgMeals)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendar.sizePolicy().hasHeightForWidth())
        self.calendar.setSizePolicy(sizePolicy)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar.setObjectName("calendar")
        self.horizontalLayout.addWidget(self.calendar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tblMeals = myQTableWidget(wdgMeals)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblMeals.sizePolicy().hasHeightForWidth())
        self.tblMeals.setSizePolicy(sizePolicy)
        self.tblMeals.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblMeals.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblMeals.setAlternatingRowColors(True)
        self.tblMeals.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblMeals.setObjectName("tblMeals")
        self.tblMeals.setColumnCount(0)
        self.tblMeals.setRowCount(0)
        self.tblMeals.horizontalHeader().setStretchLastSection(False)
        self.tblMeals.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tblMeals)
        self.lblFound = QtWidgets.QLabel(wdgMeals)
        self.lblFound.setObjectName("lblFound")
        self.verticalLayout.addWidget(self.lblFound)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.actionProductNew = QtWidgets.QAction(wdgMeals)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/caloriestracker/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProductNew.setIcon(icon)
        self.actionProductNew.setObjectName("actionProductNew")
        self.actionProductDelete = QtWidgets.QAction(wdgMeals)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/caloriestracker/list-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProductDelete.setIcon(icon1)
        self.actionProductDelete.setObjectName("actionProductDelete")

        self.retranslateUi(wdgMeals)
        QtCore.QMetaObject.connectSlotsByName(wdgMeals)

    def retranslateUi(self, wdgMeals):
        _translate = QtCore.QCoreApplication.translate
        self.lbl.setText(_translate("wdgMeals", "Your meals"))
        self.lblFound.setText(_translate("wdgMeals", "Registers found"))
        self.actionProductNew.setText(_translate("wdgMeals", "New product"))
        self.actionProductNew.setToolTip(_translate("wdgMeals", "New user product"))
        self.actionProductDelete.setText(_translate("wdgMeals", "Delete product"))
        self.actionProductDelete.setToolTip(_translate("wdgMeals", "Delete user product"))
from caloriestracker.ui.myqtablewidget import myQTableWidget
import caloriestracker.images.caloriestracker_rc