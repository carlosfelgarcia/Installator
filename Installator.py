"""Main module that will orchestate the installation process."""
import sys
import os
import Download
import Install
import tempfile


class Installator(object):
    """Main class."""

    def __init__(self, url, destination, infoFile="0.0.0", key=None):
        """Constructor.

        Args:
            url (str):  The url to download the package to install.
            destination (str): Where to install the package.
            infoFile (str): File that have the information of the project (version veriable is required)
            key (type): If the system needs a key to access. Defaults to None.
        """
        self.__destination = destination
        self.__infoFile = infoFile

        self.__downloadModule = Download.Download(url, key)
        self.__installModule = Install.Install(self.__destination)

    def install(self):
        """Install the file located in the url given."""
        self.__downloadModule.download()
        self.__installModule.setSourcePath(self.__downloadModule.getExtractedPath())
        self.__installModule.install()


if __name__ == '__main__':
    args = sys.argv
    removeTmp = False
    # --------------------------------------------- Removed when done --------------------------------------------------<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    with open('/tmp/key.txt', 'r') as f:
        key = f.read().rstrip('\n')
    # --------------------------------------------- Removed when done --------------------------------------------------<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if len(args) == 1:
        url = 'https://github.com/carlosfelgarcia/rvtools/archive/0.1.2.zip'
        dest = os.path.join(tempfile.gettempdir(), 'testInstall')
        removeTmp = True
    else:
        url = args[1]
        dest = args[2]
    print('URL - {url}'.format(url=url))
    print('Dest - {dest}'.format(dest=dest))
    # print('Version - {ver}'.format(ver=args[3]))
    app = Installator(url, dest, key=key)
    app.install()
