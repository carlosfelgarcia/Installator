"""Module that handle the updates."""
import urllib


class Update(object):
    """Handle the update of the application."""

    def __init__(self, url, currentVersion, key=None):
        """Constructor.

        Args:
            url (str): The url to look for the update.
            currentVersion (str): The tag or version to compare.
            key (str): The key to use for web auth. Defaults to None
        """
        self.__url = url
        self.__currrentVersion = currentVersion
        self.__key = key

    def checkUpdates(self):
        """Check if an update exist.

        Concatenate the url given with the current versio adding one to the version for patch, then minor and finally
        mayor.
        e.g. First try x.x.x+1, second try x.x+1.x thrid try x+1.x.x

        Return:
            str: The url found where the update is or None if no update was found.
        """
        try:
            mayor, minor, patch = self.__currrentVersion.split('.')
        except ValueError:
            raise Exception("Version format not supported, "
                            "expected x.x.x got {version}".format(version=self.__currrentVersion))
        versions = [(mayor, minor, int(patch)+1), (mayor, int(minor)+1, patch), (int(mayor)+1, minor, patch)]
        for mayorNum, minorNum, patchNum in versions:
            url = "{url}{mayor}.{minor}.{patch}".format(url=self.__url, mayor=mayorNum, minor=minorNum, patch=patchNum)
            urlHeader = {'Authorization': 'token {key}'.format(key=self.__key)} if self.__key else {}
            req = urllib.request.Request(url, headers=urlHeader)
            try:
                urllib.request.urlopen(req)
                return url
            except urllib.error.HTTPError:
                pass
