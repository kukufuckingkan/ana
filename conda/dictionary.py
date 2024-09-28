#!/usr/bin/env python3


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
@author Ana
"""
import pandas as pd
from pandas import DataFrame,ExcelFile
from sqlalchemy import create_engine, CursorResult,Connection,Engine,text,Sequence,Row
#psycopg2
# sqlalchemy
import pandasql as ps
import logging as log
#from overloading import overload
import pathlib
import py
#pathlib.Path or py._path.local.LocalPath
from typing import List, Dict, Tuple,Optional


class Dictionary:
    # https://github.com/kukufuckingkan/mandenkanMedia/raw/refs/heads/main/dictionary/english.xlsx
    def __init__(self, bookName:str, database: Optional[Engine] = None) -> None:
        # Define the file path
        bookFolderPath = '/Users/moridjarakeita/Documents/Kukukan/git/ana/books/'
        self.bookPath = bookFolderPath+ bookName +'.xlsx'
        self.mappingkeys = {}
        
        lowerBookName = bookName.lower()
        if not database:
            url = 'sqlite:///{name}.db'.format(name=lowerBookName)
            self.database = create_engine(url)
            self.connection = self.database.connect()  
        
        
    def __delete__(self):
        if self.connection:
            self.disconnect()

    def disconnect(self):
        self.database.disconnect()

    def queryFindText(self,param: str) -> CursorResult:
        query = text("select * from word where text = :param")
        connection = self.database.connect()
        result = connection.execute(query,{'param':param})
        return result
    
    def getRows(self,cursor: CursorResult) -> Sequence[Row]:
        return cursor.fetchall()
    
    def queryByRootId(self,text:str)  -> CursorResult:
        query = "select * from word where rootId == @text".format(text, text)
        connection = self.database.connect()
        result = connection.exec_driver_sql(query)
        return result
    
    def queryFindTextLike(self,text:str):
        query = "select * from words where text like  '%@text%'".format(text, text)
        connection = self.database.connect()
        result = connection.exec_driver_sql(query)
        return result
      
    
    def queryFindTextEndingWith(self,text: str):
        query = "select * from words where text like '@text%'".format(text, text)
        connection = self.database.connect()
        result = connection.exec_driver_sql(query)
        return result
    
 
    def queryFindTextStartingWith(self,text: str):
        query = "select * from words where text like '$@text'".format(text, text)
        connection = self.database.connect()
        result = connection.exec_driver_sql(query)
        return result
       
                            

    def createDatabases(self,book: ExcelFile, bookName: str)-> Dict[str,any]:
        sheetNames = book.sheet_names
        
        log.info(f'Sheet names: {sheetNames}')
        for sheetName in book.sheet_names:
            capSheetName = sheetName.upper()
            if 'english'.__eq__(bookName.casefold()):
                match capSheetName:
                    case 'WORD':
                        df = book.parse(sheet_name= sheetName)
                        db = self.populateDb(tableName= sheetName,dataframe=df)
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
                        return self.populateDb(tableName= sheetName,dataframe=df)
                    case _:
                        return                    
                
    def populateDb(self,dataframe: DataFrame,tableName: str) -> (int | None):
        # todo add indexes
        rowCount = dataframe.to_sql(name=tableName,con=self.database, if_exists= 'replace')
        log.info(f'number of affecred rows: {rowCount}')        
        
        return rowCount,tableName

    

    # retrive workbook    
    def retriveFile(self) -> ExcelFile:
        file = pd.ExcelFile(self.bookPath)
        return file
    
    def query(mapping: dict):
        return
    
    def getBooksPaths(self):
        currPath =  pathlib.Path('.')
        bookPath = currPath / '..'
        absolutePath = bookPath.resolve()
        dir = absolutePath.iterdir()
        return
    
    


    def readFile(self) -> DataFrame:
        df = pd.read_excel(self.file)
        return df
           
    def readTableFromFile(self,table: str) -> DataFrame:
        df = pd.read_excel(self.file,table)
        return df

    
    def addImages():
        return
    
    def display(dataframe: DataFrame):
        print(dataframe)
            
        
        
        
if __name__ == "__main__":
    #dic.getBooksPaths()

    dicEnglish = Dictionary(bookName= 'english')
    dicNko = Dictionary(bookName= 'ߒߞߏ')
    bookEnglish = dicEnglish.retriveFile()
    bookNko = dicNko.retriveFile()   
    
    englishDb =dicEnglish.createDatabases(bookEnglish,'english')
    ߒߞߏߘߓ=dicNko.createDatabases(bookNko,'ߒߞߏ')  

    cur = dicEnglish.queryFindText('ka')
    rows = dicEnglish.getRows(cur)
    print(rows)
    df = pd.DataFrame([rows])
    print(df)

    
   
   
   