"""Handle the IO and installation process."""
import shutil
import os
from Check import Checks


class InstallationError(Exception):
    """Custom error to raise if the installation fails."""

    pass


class Install(object):
    """Module that handle the installation and checks if the instalation is completed."""

    def __init__(self, destinationPath, sourcePath=None, overwrite=True):
        """Constructor.

        Args:
            sourcePath (str): The source of the files to get installed.
            destinationPath (str): Where the files are going to be intalled.
            overwrite (bool): TODO: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """
        self.__sourcePath = sourcePath
        self.__destinationPath = destinationPath

    def install(self):
        """Install the app base on the source and the destination given.

        It makes sure that the destination folder does not exist.
        It then run the checks to see if the installation is completed.
        """
        if self.checkDestination():
            self.removeFiles(self.__destinationPath, verbose=True)
        self.copyFiles()
        if not self.__runChecks():
            raise InstallationError("The installation has fail, it did not pass one of the checks")

        # Clean the tmp folder by removing the source
        self.removeFiles(self.__sourcePath)

    def __runChecks(self):
        """Run the checks to verify the installation.

        Return:
            bool: True if pass all, False if it fails any.
        """
        runnedChecks = []
        runnedChecks.append(Checks.checksFilesInstalled(self.__destinationPath, verbose=True))
        return all(runnedChecks)

    def copyFiles(self):
        """Copy the files from the source to the destination.

        At this point it assume that the destination folder does not exist.
        """
        if os.path.isdir(self.__sourcePath):
            shutil.copytree(self.__sourcePath, self.__destinationPath)
        else:
            shutil.copy2(self.__sourcePath, self.__destinationPath)

    def checkDestination(self):
        """Check if the destination exist.

        Resturn:
            bool: Indicating if the destination path exist in the system or not.
        """
        return os.path.exists(self.__destinationPath)

    def removeFiles(self, pathToRemove, verbose=False):
        """Remove the destination directory.

        It have the option to have a verbose if what to expouse information.

        Args:
            pathToRemove (str): Path to be remove from the file system
            verbose (bool): It use a walk method to removed file by file. Defaults to False.
        """
        if os.path.isdir(pathToRemove):
            if not verbose:
                shutil.rmtree(pathToRemove)
            else:
                for root, dirs, files in os.walk(pathToRemove, topdown=False):
                    for name in files:
                        fileToRemove = os.path.join(root, name)
                        print('Removing file ', fileToRemove)
                        os.remove(fileToRemove)
                    for name in dirs:
                        dirToRemove = os.path.join(root, name)
                        print('Removing directory ', dirToRemove)
                        os.rmdir(dirToRemove)
                print('Removing directory ', pathToRemove)
                os.rmdir(pathToRemove)
        else:
            print('Removing File ', pathToRemove)
            os.remove(pathToRemove)

    def setSourcePath(self, sourcePath):
        """Set the source path.

        Args:
            sourcePath (str): The path of the source folder.
        """
        self.__sourcePath = sourcePath
