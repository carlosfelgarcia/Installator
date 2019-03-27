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

    def __init__(self, url, key=None, ui=None):
        """Constructor.

        Args:
            url (str): The url to download the files.
            key (str): The key to use for web auth. Defaults to None
            ui (InstallatorUI): User Interface connection. Defaults to None.
        """
        self.setUrl(url)
        self.__fileDownloaded = None
        self.__extractedPath = None
        self.__key = key
        self.__ui = ui

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
        if self.__ui:
            self.__ui.progressText.append('Downloading {url}'.format(url=self.__url))
            self.__ui.progressBar.setValue(1)

        with urllib.request.urlopen(req) as response, open(fileDownloaded, 'wb') as out_file:
            # 2 MB buffer size
            bufferSize = 16384
            dataDownloaded = 0
            contentLength = response.getheader('Content-Length')
            fileSize = int(contentLength) if contentLength else None
            while True:
                buffer = response.read(bufferSize)
                if not buffer:
                    break
                dataDownloaded += len(buffer)
                out_file.write(buffer)
                if self.__ui:
                    if not fileSize:
                        continue
                    binaryFileSize = fileSize * (1024**-2)
                    dataDownloadedBinary = dataDownloaded * (1024**-2)
                    percentageDownloaded = dataDownloaded * 100 / fileSize
                    status = 'Downloading {:3.2f}% ({:.2f}) - Total size {:.2f}'.format(percentageDownloaded, dataDownloadedBinary, binaryFileSize)
                    self.__ui.progressText.append(status)
                    processedValue = percentageDownloaded * 0.5
                    self.__ui.progressBar.setValue(processedValue)

        return fileDownloaded

    def extractFile(self, filePath):
        """Extract the downloaded file.

        Args:
            filePath (str): The file path to be extract.

        Return:
            str: The folder where the file was extracted.
        """
        self.__extractor = Extractor.Extractor(self.__fileExt)
        uniqueName = str(uuid.uuid4())
        extractedPath = os.path.join(tempfile.gettempdir(), uniqueName)
        self.__extractor.getFunction()(self.__fileDownloaded, extractedPath)

        return extractedPath

    def setUrl(self, url):
        """Set the URL to download the files and get the extension of the download file.

        Args:
            url (str): The url to download the files.
        """
        self.__url = url
        self.__fileExt = url.split('.')[-1]

    def setKey(self, key):
        """Set the key for the authentication if need it.

        Args:
            key (str): The key to use for web auth.
        """
        self.__key = key

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
