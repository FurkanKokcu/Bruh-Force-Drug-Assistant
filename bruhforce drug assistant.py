from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 258)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 771, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 131, 31))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 771, 18))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 771, 18))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 771, 18))
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuDosya = QtWidgets.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuDosya.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.info = self.csvread()
        self.alpha = self.info.sort_values(by="İlaç")
        self.comboBox.addItems(self.alpha["İlaç"].tolist())
        self.comboBox.currentIndexChanged.connect(self.setdrug)

    def csvread(self):
        df = pd.read_csv("sample.csv")
        return df


    def setdrug(self, index):
        drug = self.comboBox.currentText()
        selected = self.info[self.info["İlaç"] == drug]

        if not selected.empty:
            self.label.setText(f"Kategori: {selected["Kategori"].values[0]}")
            self.label_2.setText(f"Kontrendikasyonları: {selected["Kontrendikasyonlar"].values[0]}")
            self.label_3.setText(f"Yan Etkileri : {selected["Yan Etkiler"].values[0]}")
            self.label_4.setText(f"Doz: {selected["Doz"].values[0]}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bruh Force Drug Assistant Alpha 0.1"))
        self.comboBox.setItemText(0, _translate("MainWindow", "İlaç Seç"))
        self.label.setText(_translate("MainWindow", "İlaç Kategorisi"))
        self.label_2.setText(_translate("MainWindow", "Kontrendikasyonları: "))
        self.label_3.setText(_translate("MainWindow", "Yan Etkileri"))
        self.label_4.setText(_translate("MainWindow", "Önerilen doz"))
        self.menuDosya.setTitle(_translate("MainWindow", "Hakkında"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
