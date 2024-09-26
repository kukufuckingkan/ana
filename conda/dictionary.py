#!/usr/bin/env python3


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
@author Ana
"""
import pandas as pd
#psycopg2
# sqlalchemy
import pandasql as ps
def read():
    file = '/Users/moridjarakeita/Documents/Kukukan/git/ana/dictionary.xlsx'
    
    df = pd.read_excel(file)
    return df

def findWord(word):
    df = read()

    result = df.query('text == @word')
    return result

def findRoot(word):
    df = read()
    result = df.query('text == @word')
    
    


    
if __name__ == "__main__":
    
    result = findWord('kalama')
    print(result)
    