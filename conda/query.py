from sqlalchemy import create_engine, CursorResult,Connection,Engine,text,Sequence,Row

class Query:

    def __init__(self,database: Engine) -> None:
        pass
        
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
