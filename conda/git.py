"""
@author Ana
"""
import urllib.request
import pandas as pd
import logging as log
import pathlib
#pathlib.Path or py._path.local.LocalPath
from typing import Dict,Optional,overload
import urllib
from PIL import Image, ImageFile
import io

class Git:
    
    def __init__(self,str,folder: str, subFolder: str) -> None:
        basePath = 'https://github.com/kukufuckingkan/mandenkanMedia/raw/refs/heads/main/'
        self.folder = folder
        self.subfolder = subFolder
        self.path += folder + '/' + subFolder
 

    # retrive all assets in the subfolder
    @overload
    def retrive(self):
        pass
    
    @overload
    def retrive(self,assetName:None| str, extension) -> bytes:
        path = self.path + assetName + '.' + extension

        if self.folder == 'dictionary':
            match self.subfolder:
                case 'english':
                    url += assetName + '.' + extension
                    data = self.response(url=url)
                    return data              
                case 'ߣߞߏ':
                    return None
                case _:
                    return None
                
        # subfolder is image
        else:
            match self.subfolder:
                case 'animal':
                    if assetName and extension:
                        url += assetName + '.' + extension
                        data = self.response(url=url)
                        return data
                    

    
    def response(self,url) -> bytes:
        try:
            with urllib.request.urlopen(url) as response:
                # Read the response data
                data = response.read()
                return io.BytesIO(data)

        except urllib.error.URLError as e:
            print(f"Failed to fetch data: {e.reason}")        
                
