# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Installator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtWidgets, QtGui

class UiWizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName("Installator Wizard")
        Wizard.resize(850, 625)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Wizard.sizePolicy().hasHeightForWidth())
        Wizard.setSizePolicy(sizePolicy)
        Wizard.setAcceptDrops(False)
        Wizard.setWizardStyle(QtWidgets.QWizard.AeroStyle)
        Wizard.setOptions(QtWidgets.QWizard.NoBackButtonOnLastPage)
        Wizard.setOptions(QtWidgets.QWizard.HaveCustomButton1)
        self.InfoPage = InfoPage(Wizard, self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InfoPage.sizePolicy().hasHeightForWidth())
        self.InfoPage.setSizePolicy(sizePolicy)
        self.InfoPage.setMinimumSize(QtCore.QSize(0, 0))
        self.InfoPage.setObjectName("InfoPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.InfoPage)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mainLayoutInfo = QtWidgets.QVBoxLayout()
        self.mainLayoutInfo.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.mainLayoutInfo.setObjectName("mainLayoutInfo")
        self.logo = QtWidgets.QLabel(self.InfoPage)
        self.logo.setObjectName("logo")
        self.mainLayoutInfo.addWidget(self.logo)
        pixmap = QtGui.QPixmap("GenericUI\\your-logo-here.jpg")
        self.logo.setPixmap(pixmap)
        self.infoLayout = QtWidgets.QVBoxLayout()
        self.infoLayout.setObjectName("infoLayout")
        self.urlLayout = QtWidgets.QHBoxLayout()
        self.urlLayout.setObjectName("urlLayout")
        self.urlLabel = QtWidgets.QLabel(self.InfoPage)
        self.urlLabel.setObjectName("urlLabel")
        self.urlLayout.addWidget(self.urlLabel)
        self.urlLineEdit = QtWidgets.QLineEdit(self.InfoPage)
        self.urlLineEdit.setObjectName("urlLineEdit")
        self.urlLayout.addWidget(self.urlLineEdit)
        self.infoLayout.addLayout(self.urlLayout)
        self.destLayout = QtWidgets.QHBoxLayout()
        self.destLayout.setObjectName("destLayout")
        self.destLabel = QtWidgets.QLabel(self.InfoPage)
        self.destLabel.setObjectName("destLabel")
        self.destLayout.addWidget(self.destLabel)
        self.destLineEdit = QtWidgets.QLineEdit(self.InfoPage)
        self.destLineEdit.setObjectName("destLineEdit")
        self.destLayout.addWidget(self.destLineEdit)
        self.browseBtn = QtWidgets.QPushButton(self.InfoPage)
        self.browseBtn.setObjectName("browseBtn")
        self.destLayout.addWidget(self.browseBtn)
        self.infoLayout.addLayout(self.destLayout)
        self.mainLayoutInfo.addLayout(self.infoLayout)
        self.verticalLayout_3.addLayout(self.mainLayoutInfo)
        Wizard.addPage(self.InfoPage)
        self.installPage = IntallPage(Wizard, self)
        self.installPage.setObjectName("installPage")
        self.gridLayout = QtWidgets.QGridLayout(self.installPage)
        self.gridLayout.setObjectName("gridLayout")
        self.mainLayoutInstall = QtWidgets.QVBoxLayout()
        self.mainLayoutInstall.setObjectName("mainLayoutInstall")
        self.progressText = QtWidgets.QTextEdit(self.installPage)
        self.progressText.setEnabled(True)
        self.progressText.setReadOnly(True)
        self.progressText.setObjectName("progressText")
        self.mainLayoutInstall.addWidget(self.progressText)
        self.progressLabel = QtWidgets.QLabel(self.installPage)
        self.progressLabel.setText("")
        self.progressLabel.setObjectName("progressLabel")
        self.mainLayoutInstall.addWidget(self.progressLabel)
        self.progressBar = QtWidgets.QProgressBar(self.installPage)
        self.progressBar.setObjectName("progressBar")
        self.mainLayoutInstall.addWidget(self.progressBar)
        self.gridLayout.addLayout(self.mainLayoutInstall, 0, 0, 1, 1)

        # Rename Next button
        Wizard.addPage(self.installPage)

        # Add new button
        self.intallBtn = QtWidgets.QPushButton("Install")
        Wizard.setButton(Wizard.CustomButton1, self.intallBtn)
        Wizard.button(Wizard.CustomButton1).setVisible(False)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

        # Set signals
        self.progressBar.valueChanged.connect(self.installPage.complete)
        self.destLineEdit.textChanged.connect(self.InfoPage.complete)

    def retranslateUi(self, Wizard):
        _translate = QtCore.QCoreApplication.translate
        Wizard.setWindowTitle(_translate("Wizard", "Installator Wizard"))
        self.InfoPage.setTitle(_translate("Wizard", "Installator UI Example"))
        self.urlLabel.setText(_translate("Wizard", "Url"))
        self.destLabel.setText(_translate("Wizard", "Where To Install"))
        self.browseBtn.setText(_translate("Wizard", "Browse"))
        self.installPage.setTitle(_translate("Wizard", "Installation Process"))


class InfoPage(QtWidgets.QWizardPage):
    def __init__(self, parent, window):
        super(InfoPage, self).__init__(parent)
        self.__window = window

    def isComplete(self):
        text = self.__window.destLineEdit.text()
        if text:
            return True
        return False

    def complete(self):
        self.completeChanged.emit()


class IntallPage(QtWidgets.QWizardPage):
    def __init__(self, parent, window):
        super(IntallPage, self).__init__(parent)
        self.__window = window

    def isComplete(self):
        progress = self.__window.progressBar.value()
        if progress >= 100:
            return True
        return False

    def complete(self):
        self.completeChanged.emit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Wizard = QtWidgets.QWizard()
    ui = UiWizard()
    ui.setupUi(Wizard)
    Wizard.show()
    sys.exit(app.exec_())
