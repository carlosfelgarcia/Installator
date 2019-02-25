"""This module handle the connection and download of the files."""
import tempfile
import urllib.request
import os
import uuid

import Extractor


class Download(object):
    """Download module."""

    def __init__(self, url):
        """Constructor.

        Args:
            url (str): The url to connect and download the files.
        """
        self.__url = url
        self.__fileDownloaded = None
        self.__fileExt = None
        self.__extractedFolders = {}

    def downloadFile(self):
        """Download the file to be intall."""
        self.__fileExt = self.__url.split('/')[-1]
        uniqueName = str(uuid.uuid4())
        self.__fileDownloaded = os.path.join(tempfile.gettempdir(), uniqueName, '.{ext}'.format(ext=self.__fileExt))
        with urllib.request.urlopen(self.__url) as response, open(self.__fileDownloaded, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

    def extractFile(self):
        """Extract the downloaded file."""
        extractor = Extractor.Extractor(self.__fileExt)
        uniqueName = str(uuid.uuid4())
        whereToExtract = os.path.join(tempfile.gettempdir(), uniqueName)
        self.__extractedFolders[self.__fileDownloaded] = whereToExtract
        extractor.getFunction()(self.__fileDownloaded, whereToExtract)

    def getFileDownloaded(self):
        """Get the file base on the url provided.

        Return:
            str: The path where the downloaded file is.
        """
        return self.__fileDownloaded
