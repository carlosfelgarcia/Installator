"""Main module that will orchestate the installation process."""


class Installator(object):
    """Main class."""

    def __init__(self, url, destination, currentVersion=0, sshKey=None):
        """Constructor.

        Args:
            url (str):  The url to download the package to install.
            destination (str): Where to install the package..
            currentVersion (int): Current version of the app to be compared with the downloaded package. Defaults to 0.
            sshKey (type): If the system needs a key to access. Defaults to None.
        """
        self.__url = url
        self.__destination = destination
        self.__currentVersion = currentVersion

        
