import pandas as pd

from pandas import ExcelFile

def read(data: bytes) -> ExcelFile:
    pd.ExcelFile(data)
