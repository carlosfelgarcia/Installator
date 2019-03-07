"""This module handle the connection and download of the files."""
import tempfile
import urllib.request
# from urllib import Request, urlopen
import os
import uuid

import Extractor


class Download(object):
    """Download module."""

    BINARY_EXT = ['exe']

    def __init__(self, url, key):
        """Constructor.

        Args:
            url (str): The url to connect and download the files.
        """
        self.__url = url
        self.__fileDownloaded = None
        self.__extractedPath = None
        self.__fileExt = url.split('.')[-1]
        self.__key = key
        if self.__fileExt not in self.BINARY_EXT:
            self.__extractor = Extractor.Extractor(self.__fileExt)

    def download(self):
        """Orchestate the download of a file.

        It downloads a file, and extract it.
        """
        self.__fileDownloaded = self.downloadFile()
        if self.__fileExt not in self.BINARY_EXT:
            tmpExtractedPath = self.extractFile(self.__fileDownloaded)
            self.__extractedPath = os.path.join(tmpExtractedPath, os.listdir(tmpExtractedPath)[0])


    def downloadFile(self):
        """Download the file to be intall from the url given.

        Return:
            str: The path where the downloaded file is.
        """
        uniqueName = str(uuid.uuid4())
        fileDownloaded = os.path.join(
            tempfile.gettempdir(),
            '{uniqueName}.{ext}'.format(uniqueName=uniqueName, ext=self.__fileExt)
        )
        urlHeader = {'Authorization': 'token {key}'.format(key=self.__key)} if self.__key else {}
        req = urllib.request.Request(self.__url, headers=urlHeader)
        print('Downloading {url}....'.format(url=self.__url))
        with urllib.request.urlopen(req) as response, open(fileDownloaded, 'wb') as out_file:
                data = response.read()
                out_file.write(data)

        return fileDownloaded

    def extractFile(self, filePath):
        """Extract the downloaded file.

        Args:
            filePath (str): The file path to be extract.

        Return:
            str: The folder where the file was extracted.
        """
        uniqueName = str(uuid.uuid4())
        extractedPath = os.path.join(tempfile.gettempdir(), uniqueName)
        self.__extractor.getFunction()(self.__fileDownloaded, extractedPath)

        return extractedPath

    def getExtractedPath(self):
        """Get the path where the file was extracted.

        Return:
            str: The path where the extracted file is.
        """
        return self.__extractedPath

    def getFileDownloaded(self):
        """Get the file base on the url provided.

        Return:
            str: The path where the downloaded file is.
        """
        return self.__fileDownloaded
