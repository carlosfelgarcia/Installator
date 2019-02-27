"""Main module that will orchestate the installation process."""
import sys
import os
import Download


class Installator(object):
    """Main class."""

    def __init__(self, url, destination, currentVersion=0, key=None):
        """Constructor.

        Args:
            url (str):  The url to download the package to install.
            destination (str): Where to install the package.
            currentVersion (int): Current version of the app to be compared with the downloaded package. Defaults to 0.
            key (type): If the system needs a key to access. Defaults to None.
        """
        self.__destination = destination
        self.__currentVersion = currentVersion

        self.__downloadModule = Download.Download(url, key)

    def install(self):
        """Install the file located in the url given."""
        self.__downloadModule.download()
        print('Downloaded Files ----> ', self.__downloadModule.getDownloadedFiles())


if __name__ == '__main__':
    args = sys.argv
    removeTmp = False
    # --------------------------------------------- Removed when done --------------------------------------------------<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    with open('/tmp/key.txt', 'r') as f:
        key = f.read().rstrip('\n')
    # --------------------------------------------- Removed when done --------------------------------------------------<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if len(args) == 1:
        url = 'https://github.com/carlosfelgarcia/testPrivate/archive/0.1.zip'
        dest = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tmp')
        removeTmp = True
    else:
        url = args[1]
        dest = args[2]
    print('URL - {url}'.format(url=url))
    print('Dest - {dest}'.format(dest=dest))
    # print('Version - {ver}'.format(ver=args[3]))
    app = Installator(url, dest, key=key)
    app.install()
