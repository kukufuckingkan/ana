from sqlalchemy import create_engine, Engine , Connection
from pandas import DataFrame,ExcelFile
import logging as log

class Memory:
    def __init__(self) -> None:
        pass
    
    def setup(self,folder: str, subfolder:str) -> Engine :
        url = 'sqlite:///{folder}_{subfolder}_ana.db'.format(folder= folder,subfolder= subfolder)
        self.database = create_engine(url)  

    def connection(self) -> Connection:
        return self.database.connect()
              


    def create(self,book: ExcelFile, bookName: str)-> Dict[str,any]:
        sheetNames = book.sheet_names
        
        log.info(f'Sheet names: {sheetNames}')
        for sheetName in book.sheet_names:
            capSheetName = sheetName.upper()
            if 'english'.__eq__(bookName.casefold()):
                match capSheetName:
                    case 'WORD':
                        df = book.parse(sheet_name= sheetName)
                        db = self.populate(tableName= sheetName,dataframe=df)
                        return {
                            'db': db,
                            'bookName': bookName
                        }
                    case _:
                        return
            elif 'ߒߞߏ'.__eq__(bookName.casefold()):
                match capSheetName:
                    case 'WORD':
                        df = book.parse(sheet_name= sheetName)
                        return self.populate(tableName= sheetName,dataframe=df)
                    case _:
                        return  

    def populate(self,dataframe: DataFrame,tableName: str) -> (int | None):
        # todo add indexes
        rowCount = dataframe.to_sql(name=tableName,con=self.database, if_exists= 'replace')
        log.info(f'number of affecred rows: {rowCount}')        
        
        return rowCount,tableName                    