from urllib.request import urlopen
import os.path
from skyfield.api import load
import certifi
import ssl
class TLELoader:
    """
    TLELoader takes care of downloading or loading 
    the TLE records.
    """
    def __init__(self, url : str, tleFilePath : str):
        
        """
        TLELoader constructor

        @param url: the TLE server URL
        @param tleFilePath: the file where the TLE records will be downloaded
        """
        self._ctx = ssl.create_default_context(cafile=certifi.where())
        self._url = url
        self._tleFilePath = tleFilePath
        self._tleResponse = None
        self._earthSatelliteArray = []
        self._loadIfExists()

    def downloadTLE(self):
        """
        downloadTLE downloads the TLE records from the specified URL.
        if the TLE file already exists it will be overwritten 

        @return the HTTP status code
        """
        rc = self._downloadFile()
        self._loadIfExists()
        return rc
    
    def getSatellites(self):
        """
        getSatellites returns the EarthSatellite array

        @return EarthSatellite array
        """
        return self._earthSatelliteArray

    def _loadIfExists(self):
        """
        _loadIfExists loads the TLE records from a file if the file exists
        """
        if os.path.isfile(self._tleFilePath) == True:
            self._earthSatelliteArray = load.tle_file(self._tleFilePath)
            
    def _downloadFile(self):
        """
        _downloadFile downloads the TLE records from the specified URL
        and stores the results (response body) in the specified file
        (tleFilePath)

        @return the HTTP status code
        """
        returnCode = 0
        with urlopen(self._url, context=self._ctx) as response:
            self._tleResponse = response.read()
            returnCode = response.code

        with open(self._tleFilePath, "wb") as f:
            f.write(self._tleResponse)

        return returnCode
