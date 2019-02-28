"""Handle the IO and installation process."""
import shutil
import os


class Install(object):
    """Module that handle the installation and checks if the instalation is completed."""

    def __init__(self, destinationPath, sourcePath=None):
        """Constructor.

        Args:
            sourcePath (str): The source of the files to get installed.
            destinationPath (str): Where the files are going to be intalled.
        """
        self.__sourcePath = sourcePath
        self.__destinationPath = destinationPath

    def install(self):
        """Install the app base on the source and the destination given.

        It makes sure that the destination folder does not exist.
        It then run the checks to see if the installation is completed.
        """
        if self.checkDestination():
            self.removeDestination()
        self.copyFiles()

    def copyFiles(self):
        """Copy the files from the source to the destination.

        At this point it assume that the destination folder does not exist.
        """
        shutil.copytree(self.__sourcePath, self.__destinationPath)

    def checkDestination(self, removed=True):
        """Check if the destination exist and removed if flag is True.

        Resturn:
            bool: Indicating if the destination path exist in the system or not.
        """
        return os.path.exists(self.__destinationPath)

    def removeDestination(self, removeVerbose=False):
        """Remove the destination directory.

        It have the option to have a verbose if what to expouse information.

        Args:
            removeVerbose (bool): It use a walk method to removed file by file. Defaults to False.
        """
        if not removeVerbose:
            shutil.rmtree(self.__destinationPath)
        else:
            for root, dirs, files in os.walk(self.__destinationPath, topdown=False):
                for name in files:
                    fileToRemove = os.path.join(root, name)
                    print('Removing file ', fileToRemove)
                    os.remove(fileToRemove)
                for name in dirs:
                    dirToRemove = os.path.join(root, name)
                    print('Removing directory ', dirToRemove)
                    os.rmdir(dirToRemove)
            print('Removing directory ', self.__destinationPath)
            os.rmdir(self.__destinationPath)

    def setSourcePath(self, sourcePath):
        """Set the source path.

        Args:
            sourcePath (str): The path of the source folder.
        """
        self.__sourcePath = sourcePath
