# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Resource_BinanceConnection.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(564, 105)
        Dialog.setSizeGripEnabled(False)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.label_apiKey = QtWidgets.QLabel(Dialog)
        self.label_apiKey.setObjectName("label_apiKey")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_apiKey)
        self.lineEdit_apiKey = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_apiKey.setObjectName("lineEdit_apiKey")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_apiKey)
        self.label_apiSecret = QtWidgets.QLabel(Dialog)
        self.label_apiSecret.setObjectName("label_apiSecret")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_apiSecret)
        self.lineEdit_apiSecret = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_apiSecret.setObjectName("lineEdit_apiSecret")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_apiSecret)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Configure Binance API"))
        self.label_apiKey.setText(_translate("Dialog", "Binance API key :"))
        self.label_apiSecret.setText(_translate("Dialog", "Binance API secret :"))
