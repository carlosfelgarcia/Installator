"""Main module that will orchestate the installation process."""
import Download
import Install
import Update


class Installator(object):
    """Main class."""

    def install(self, url, targetPath, key=None, ui=None):
        """Install the file located in the url given.

        Args:
            url (str):  The url to download the package to install.
            targetPath (str): Where to install the package.
            key (str): If the system needs a key to access. Defaults to None.
            ui (InstallatorUI): User Interface connection. Defaults to None.
        """
        if ui:
            ui.progressText.append('Starting downloading files...')
        download = Download.Download(url, key, ui=ui)
        download.download()
        downloadedPath = download.getExtractedPath() or download.getFileDownloaded()
        if ui:
            ui.progressText.append('Installing the files...')
        install = Install.Install(downloadedPath, targetPath, ui=ui)
        install.install()
        if ui:
            ui.progressText.append('Installation successful')
            ui.progressBar.setValue(100)

    def update(self, url, currentVersion, key=None, fileName=None, targetPath=None, install=False):
        """Search for updates.

        If an update is found, it can notify the user or install the update and notify the end user that the update
        has been installed.

        Args:
            url (str):  The url to download the package to install.
            currentVersion (str): The current version of the app running.
            key (str): If the system needs a key to access. Defaults to None.

        Return:
            str or None: The url found if install flag is False or None if no update is found.
        """
        update = Update.Update(url, currentVersion)
        updateUrl = update.checkUpdates()
        if not updateUrl:
            return

        return updateUrl
