"""Handle the user interface."""
import PyQt5.QtWidgets as qtw
import sys

from Installator import Installator
from GenericUI import UiWizard


class InstallatorUI(qtw.QWizard):
    """Main window of the installator."""

    def __init__(self):
        """Constructor."""
        super(InstallatorUI, self).__init__()
        self.ui = UiWizard()
        self.__installator = Installator()
        self.ui.setupUi(self)

        # Initial values
        self.ui.urlLineEdit.setText('https://yourURL.com/file.exe')
        self.ui.urlLineEdit.setEnabled(False)

        # Connect the signals
        self.ui.browseBtn.clicked.connect(self.__showBrowseDialog)
        self.currentIdChanged.connect(self.__pageChange)
        self.ui.intallBtn.clicked.connect(self.__install)

        # self.ui.
    def __showBrowseDialog(self):
        """Show the file browser dialog."""
        dirPath = qtw.QFileDialog.getExistingDirectory(options=qtw.QFileDialog.ShowDirsOnly)
        urlFile = self.ui.urlLineEdit.text().split('/')[-1]
        self.ui.destLineEdit.setText('{dirPath}/{urlFile}'.format(dirPath=dirPath, urlFile=urlFile))

    def __pageChange(self, idPage):
        """Handle the signal when a page change."""
        # ID 1 going to the install page
        if idPage == 1:
            self.button(self.CustomButton1).setVisible(True)

    def __install(self):
        """Start the installation process."""
        self.ui.intallBtn.setEnabled(False)
        url = self.ui.urlLineEdit.text()
        destination = self.ui.destLineEdit.text()
        try:
            self.__installator.install(url, destination, ui=self.ui)
            self.ui.intallBtn.setEnabled(True)
            self.ui.intallBtn.setText('Re-Install')
        except Exception as err:
            import traceback
            _, _, ex_traceback = sys.exc_info()
            stack = "".join(traceback.extract_tb(ex_traceback).format())
            self.ui.progressText.append('Installation fatal Error:\n{error}\n\n{e}'.format(error=err, e=stack))


def main():
    """Main function."""
    app = qtw.QApplication(sys.argv)
    ui = InstallatorUI()
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
