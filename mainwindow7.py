# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow7.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 568)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 350, 90, 28))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/img/application-wave.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 240, 141, 16))
        self.label.setObjectName("label")
        self.lnCogn = QtWidgets.QLineEdit(self.centralwidget)
        self.lnCogn.setGeometry(QtCore.QRect(60, 40, 113, 28))
        self.lnCogn.setObjectName("lnCogn")
        self.lnNome = QtWidgets.QLineEdit(self.centralwidget)
        self.lnNome.setGeometry(QtCore.QRect(60, 100, 113, 28))
        self.lnNome.setObjectName("lnNome")
        self.lnSesso = QtWidgets.QLineEdit(self.centralwidget)
        self.lnSesso.setGeometry(QtCore.QRect(60, 270, 113, 28))
        self.lnSesso.setObjectName("lnSesso")
        self.lnLuogo = QtWidgets.QLineEdit(self.centralwidget)
        self.lnLuogo.setGeometry(QtCore.QRect(60, 390, 113, 28))
        self.lnLuogo.setObjectName("lnLuogo")
        self.dataNas = QtWidgets.QDateEdit(self.centralwidget)
        self.dataNas.setGeometry(QtCore.QRect(60, 330, 113, 28))
        self.dataNas.setDateTime(QtCore.QDateTime(QtCore.QDate(1900, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dataNas.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dataNas.setCalendarPopup(True)
        self.dataNas.setObjectName("dataNas")
        self.lblCog = QtWidgets.QLabel(self.centralwidget)
        self.lblCog.setGeometry(QtCore.QRect(220, 40, 58, 16))
        self.lblCog.setObjectName("lblCog")
        self.lblNom = QtWidgets.QLabel(self.centralwidget)
        self.lblNom.setGeometry(QtCore.QRect(220, 100, 58, 16))
        self.lblNom.setObjectName("lblNom")
        self.lblSesso = QtWidgets.QLabel(self.centralwidget)
        self.lblSesso.setGeometry(QtCore.QRect(220, 280, 113, 28))
        self.lblSesso.setObjectName("lblSesso")
        self.lblDatNas = QtWidgets.QLabel(self.centralwidget)
        self.lblDatNas.setGeometry(QtCore.QRect(220, 330, 113, 28))
        self.lblDatNas.setObjectName("lblDatNas")
        self.lblLuogo = QtWidgets.QLabel(self.centralwidget)
        self.lblLuogo.setGeometry(QtCore.QRect(220, 390, 113, 28))
        self.lblLuogo.setObjectName("lblLuogo")
        self.grpSesso = QtWidgets.QGroupBox(self.centralwidget)
        self.grpSesso.setGeometry(QtCore.QRect(60, 140, 221, 101))
        self.grpSesso.setObjectName("grpSesso")
        self.rdbFem = QtWidgets.QRadioButton(self.grpSesso)
        self.rdbFem.setGeometry(QtCore.QRect(20, 30, 104, 21))
        self.rdbFem.setObjectName("rdbFem")
        self.rdbMas = QtWidgets.QRadioButton(self.grpSesso)
        self.rdbMas.setGeometry(QtCore.QRect(20, 60, 104, 21))
        self.rdbMas.setObjectName("rdbMas")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "&Ok"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.dataNas.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.lblCog.setText(_translate("MainWindow", "Cognome"))
        self.lblNom.setText(_translate("MainWindow", "<html><head/><body><p>Nome</p></body></html>"))
        self.lblSesso.setText(_translate("MainWindow", "<html><head/><body><p>Sesso</p></body></html>"))
        self.lblDatNas.setText(_translate("MainWindow", "<html><head/><body><p>Data di Nascita</p></body></html>"))
        self.lblLuogo.setText(_translate("MainWindow", "<html><head/><body><p>Luogo di Nascita</p></body></html>"))
        self.grpSesso.setTitle(_translate("MainWindow", "Sesso"))
        self.rdbFem.setText(_translate("MainWindow", "Femmina"))
        self.rdbMas.setText(_translate("MainWindow", "Maschio"))
import risorse_rc
