import pandas as pd
from pandas import DataFrame

def readFile(file: str) -> DataFrame:
    df = pd.read_excel(file)
    return df

    def readTableFromFile(file: str,table: str) -> DataFrame:
        df = pd.read_excel(file,table)
        return df