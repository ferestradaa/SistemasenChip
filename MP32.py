# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MP32.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1299, 896)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(170, 560, 301, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PlayButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.PlayButton.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.PlayButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("mp3_imagen/play (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayButton.setIcon(icon)
        self.PlayButton.setIconSize(QtCore.QSize(80, 80))
        self.PlayButton.setObjectName("PlayButton")
        self.horizontalLayout.addWidget(self.PlayButton)
        self.PauseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.PauseButton.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.PauseButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("mp3_imagen/pause (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PauseButton.setIcon(icon1)
        self.PauseButton.setIconSize(QtCore.QSize(80, 80))
        self.PauseButton.setObjectName("PauseButton")
        self.horizontalLayout.addWidget(self.PauseButton)
        self.StopButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.StopButton_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.StopButton_3.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.StopButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("mp3_imagen/stop (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StopButton_3.setIcon(icon2)
        self.StopButton_3.setIconSize(QtCore.QSize(80, 80))
        self.StopButton_3.setObjectName("StopButton_3")
        self.horizontalLayout.addWidget(self.StopButton_3)
        self.NumC = QtWidgets.QLineEdit(self.centralwidget)
        self.NumC.setGeometry(QtCore.QRect(560, 360, 51, 31))
        self.NumC.setStyleSheet("background-color: rgb(134, 134, 134);\n"
"background-color: rgb(193, 193, 193);\n"
"border-top-color: rgb(170, 0, 0);\n"
"border-right-color: rgb(170, 0, 0);\n"
"border-right-color: rgb(170, 0, 0);\n"
"border-bottom-color: rgb(170, 0, 0);")
        self.NumC.setObjectName("NumC")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 320, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: italic 16pt \"Monotype Corsiva\";\n"
"")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(150, 180, 351, 241))
        self.textBrowser.setStyleSheet("background-color: rgb(134, 134, 134);\n"
"background-color: rgb(193, 193, 193);")
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 490, 351, 51))
        self.lineEdit.setStyleSheet("background-color: rgb(134, 134, 134);\n"
"background-color: rgb(193, 193, 193);")
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 440, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: italic 16pt \"Monotype Corsiva\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.arriba_button = QtWidgets.QPushButton(self.centralwidget)
        self.arriba_button.setGeometry(QtCore.QRect(920, 240, 91, 81))
        self.arriba_button.setStyleSheet("background-color: rgb(104, 104, 104);")
        self.arriba_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("mp3_imagen/up2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.arriba_button.setIcon(icon3)
        self.arriba_button.setIconSize(QtCore.QSize(100, 100))
        self.arriba_button.setObjectName("arriba_button")
        self.abajo_button = QtWidgets.QPushButton(self.centralwidget)
        self.abajo_button.setGeometry(QtCore.QRect(920, 480, 91, 81))
        self.abajo_button.setStyleSheet("background-color: rgb(104, 104, 104);")
        self.abajo_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("mp3_imagen/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.abajo_button.setIcon(icon4)
        self.abajo_button.setIconSize(QtCore.QSize(100, 100))
        self.abajo_button.setObjectName("abajo_button")
        self.izquierda_button = QtWidgets.QPushButton(self.centralwidget)
        self.izquierda_button.setGeometry(QtCore.QRect(790, 360, 91, 81))
        self.izquierda_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.izquierda_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("mp3_imagen/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.izquierda_button.setIcon(icon5)
        self.izquierda_button.setIconSize(QtCore.QSize(100, 100))
        self.izquierda_button.setObjectName("izquierda_button")
        self.derecha_button = QtWidgets.QPushButton(self.centralwidget)
        self.derecha_button.setGeometry(QtCore.QRect(1050, 360, 91, 81))
        self.derecha_button.setStyleSheet("background-color: rgb(104, 104, 104);")
        self.derecha_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("mp3_imagen/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.derecha_button.setIcon(icon6)
        self.derecha_button.setIconSize(QtCore.QSize(100, 100))
        self.derecha_button.setObjectName("derecha_button")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 170, 371, 261))
        self.label_6.setStyleSheet("background-image: url(mp3_imagen/degradadooo.jpg);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(140, 480, 371, 71))
        self.label_10.setStyleSheet("background-image: url(mp3_imagen/degradadooo.jpg);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(780, 350, 111, 101))
        self.label_7.setStyleSheet("background-image: url(mp3_imagen/degradadooo.jpg);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(910, 230, 111, 101))
        self.label_8.setStyleSheet("background-image: url(mp3_imagen/degradadooo.jpg);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(910, 470, 111, 101))
        self.label_9.setStyleSheet("background-image: url(mp3_imagen/degradadooo.jpg);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1040, 350, 111, 101))
        self.label_11.setStyleSheet("background-image: url(mp3_imagen/degradadooo.jpg);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.detener_button = QtWidgets.QPushButton(self.centralwidget)
        self.detener_button.setGeometry(QtCore.QRect(920, 360, 91, 81))
        self.detener_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.detener_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("mp3_imagen/detener.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.detener_button.setIcon(icon7)
        self.detener_button.setIconSize(QtCore.QSize(100, 100))
        self.detener_button.setObjectName("detener_button")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(910, 350, 111, 101))
        self.label_12.setStyleSheet("background-image: url(mp3_imagen/degradadooo.jpg);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 1291, 851))
        self.label_3.setStyleSheet("background-image: url(mp3_imagen/fondo.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 50, 251, 111))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 72pt \"Algerian\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(810, 60, 331, 111))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 72pt \"Algerian\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_3.raise_()
        self.label_11.raise_()
        self.label_9.raise_()
        self.label_8.raise_()
        self.label_7.raise_()
        self.label_10.raise_()
        self.label_6.raise_()
        self.horizontalLayoutWidget.raise_()
        self.NumC.raise_()
        self.label.raise_()
        self.textBrowser.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.abajo_button.raise_()
        self.derecha_button.raise_()
        self.izquierda_button.raise_()
        self.arriba_button.raise_()
        self.label_12.raise_()
        self.detener_button.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1299, 26))
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
        self.NumC.setText(_translate("MainWindow", "1"))
        self.label.setText(_translate("MainWindow", "No. Canción"))
        self.label_2.setText(_translate("MainWindow", "Canción Actual"))
        self.label_4.setText(_translate("MainWindow", "MP3"))
        self.label_5.setText(_translate("MainWindow", "MBOT"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())