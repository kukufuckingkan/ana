#!/usr/bin/env python3


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
@author Ana
"""
import pandas as pd
from pandas import DataFrame,ExcelFile
from sqlalchemy import create_engine
#psycopg2
# sqlalchemy
import pandasql as ps
import logging as log
#from overloading import overload


from sqlalchemy import create_engine,Engine,Connection
from typing import Optional

class Dictionary:

    def __init__(self, bookName:str, database: Optional[Engine] = None, connection: Optional[Connection] = None) -> None:
        # Define the file path
        self.ߒߞߏ = '/Users/moridjarakeita/Documents/Kukukan/git/ana/conda/books/ߒߞߏ.xlsx'
        self.pathEnglish = '/Users/moridjarakeita/Documents/Kukukan/git/ana/conda/dictionary.py'
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

            

    def createDatabases(self,book: ExcelFile):
        sheetNames = book.sheet_names
        log.info(f'Sheet names: {sheetNames}')
        for sheetName in book.sheet_names:
            capSheetName = sheetName.upper()
            match capSheetName:
                case 'WORD':
                    df = book.parse(sheet_name= sheetName)
                    return self.populateDb(tableName= sheetName,dataframe=df)
                case _:
                    return
                
    def populateDb(self,dataframe: DataFrame,tableName: str):
        # todo add indexes
        rowCount = dataframe.to_sql(name=tableName,con=self.database, if_exists= 'replace',index= True)
        log.info(f'number of affecred rows: {rowCount}')        
        
        return rowCount

    

    # retrive workbook    
    def retriveFile(self) -> ExcelFile:
        file = pd.ExcelFile(self.file)
        return file
    
    def query(mapping: dict):
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
    dic = Dictionary(bookName= 'english')
    book = dic.retriveFile()
    dic.createDatabases(book)
  
    #df = dic.readFile()
    #dic.readTableFromFile()
    #df =  dic.readTableFromFile('english')
    
    #print(df)
    #engine = dic.createDatabase('english')
    
    #table = 'word'
    #df2 = dic.readFileTable('words')
    
   
   
   