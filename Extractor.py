"""A factory that base on the file it extracts it's contents."""
import zipfile


class NoFunctionFound(Exception):
    """Custom expection to be raise when there is no function associated to the file extension."""

    pass


class Extractor(object):
    """Extract contents from compressed files."""

    def __init__(self, fileExtension):
        """Constructor.

        Args:
            fileExtension (str): The extension of the file to be extracted.

        Raise: NoFunctionFound: No function was found.
        """
        self.__fileExt = fileExtension
        self.__functions = {'zip': self.zipFile}

        if self.__fileExt not in self.__functions:
            raise NoFunctionFound("Extension file is not supported {ext}".format(ext=self.__fileExt))

    def getFunction(self):
        """Get the function that can extract the given file extension.

        Return:
            Extractor.func: The function that extract can extract the file.
        """
        return self.__functions[self.__fileExt]

    def zipFile(self, filePath, whereToExtract):
        """Extract zip files.

        Args:
            filePath (str): The zip file to extract.
            whereToExtract (str): Where the zip file is going to be extracted.

        Return:
            str: Folder where the zip file was extracted.
        """
        zip_ref = zipfile.ZipFile(filePath, 'r')
        zip_ref.extractall(whereToExtract)
        zip_ref.close()
