"""Main module that will orchestate the installation process."""
import sys
import os
import tempfile
import Download
import Install
import Update


class Installator(object):
    """Main class."""

    def install(self, url, targetPath, key=None):
        """Install the file located in the url given.

        Args:
            url (str):  The url to download the package to install.
            targetPath (str): Where to install the package.
            key (str): If the system needs a key to access. Defaults to None.
        """
        download = Download.Download(url, key)
        download.download()
        downloadedPath = download.getExtractedPath() or download.getFileDownloaded()
        install = Install.Install(downloadedPath, targetPath)
        install.install()

    def update(self, url, currentVersion='0.0.0'):
        """Search for updates.

        If an update is found, it can notify the user or install the update and notify the end user that the update
        has been installed.
        """
        update = Update.Update(url, currentVersion)
        updateUrl = update.checkUpdates()
        print('URL to update found --> ', updateUrl)


if __name__ == '__main__':
    args = sys.argv
    removeTmp = False
    key = None
    # --------------------------------------------- Removed when done --------------------------------------------------<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    try:
        with open('/tmp/key.txt', 'r') as f:
            key = f.read().rstrip('\n')
    except FileNotFoundError:
        print('Key is none')
    # --------------------------------------------- Removed when done --------------------------------------------------<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if len(args) == 1:
        #url = 'https://github.com/carlosfelgarcia/Data-Analysis-Tool/releases/download/0.0.0/UI.exe'
        url = 'https://github.com/carlosfelgarcia/Data-Analysis-Tool/releases/tag/'
        dest = os.path.join(tempfile.gettempdir(), 'DataAnalysis.exe')
        removeTmp = True
    else:
        url = args[1]
        dest = args[2]
    print('URL - {url}'.format(url=url))
    print('Dest - {dest}'.format(dest=dest))
    # print('Version - {ver}'.format(ver=args[3]))
    app = Installator()
    # app.install(url, dest, key)
    app.update(url)
