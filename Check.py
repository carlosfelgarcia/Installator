"""Open module for checks, it ships with the basics but you can add more if necesary."""
import os


class Checks(object):
    """Open module to do checks on the installataion."""

    @classmethod
    def checksFilesInstalled(cls, installedFolder, ignoreFileNames=None, verbose=False):
        """Check the instegrity of the files installed.

        Base on the size of the file, it checks if the files installed have some data in it.

        Args:
            installedFolder (str): The folders to check the files integrity.
            ignoreFileNames (list or None): The list of files names with extension to be ingore.
            verbose (bool): Flag to indicate the level of verbose wanted.

        Return:
            bool: True if passed the check, False if it fails.
        """
        for root, dirs, files in os.walk(installedFolder, topdown=False):
            for name in files:
                if verbose:
                    print('Checking file ---> ', name)
                if ignoreFileNames and name in ignoreFileNames:
                    continue
                fileSize = os.path.getsize(os.path.join(root, name))
                if fileSize == 0:
                    return False

        return True
