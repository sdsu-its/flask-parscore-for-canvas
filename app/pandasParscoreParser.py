import sys
import os
import pandas as pd
import datetime
import csv
currDate = datetime.datetime.now()

#run program
def parscoreParser(inputFile):
    newData = readFile(inputFile)
    #changed this line to put changes back into file rather than printing them
    inputConv(newData).to_csv(index=False,path_or_buf=inputFile, quoting=csv.QUOTE_ALL)


#read in file from upser input

def readFile(csvFilePath):
    #produce a DataFrame object from input file
    dataFrame = pd.read_csv(csvFilePath)
    dataFrame.dropna(how ='all', inplace = True)
    dataFrame.head()
    dataFrame.drop([0],axis=0,inplace=True)
    return dataFrame


#convert input DataFrame file into correct format
def inputConv(dataFrame):
    retDf=dataFrame
    cols = dataFrame["Student"].str.partition(" ", True)
    dataFrame["Last Name"]= cols[2]
    dataFrame["First Name"]= cols[0]
    dataFrame.drop(columns =["Student"], inplace = True)
    dataFrame = dataFrame[  dataFrame['Last Name'] != 'Student'] 
    if 'Override Score' in dataFrame:
        convDf = dataFrame[['SIS User ID','Last Name','First Name','Override Score']]
        convDf.rename(columns = {"SIS User ID": "Username",
                                  "Override Score":"Course Letter Grade"})
        convDf.insert(3, "Last Access", currDate.strftime("%Y-%m-%d %H:%M:%S"), True)
        retDf = convDf.reindex(columns=("Last Name","First Name","SIS User ID","Last Access","Override Score"))
        retDf = retDf.rename(columns = {"SIS User ID": "Username","Override Score":"Course Letter Grade"})
        retDf["Course Letter Grade"]=detectMissing(retDf["Course Letter Grade"],dataFrame["Final Score"])
        retDf = retDf.apply(lambda x: seriesIteration(x) if x.name == "Course Letter Grade" else x)
    elif 'Override Grade' in dataFrame:
        convDf = dataFrame[['SIS User ID','Last Name','First Name','Override Grade']]
        convDf.rename(columns = {"SIS User ID": "Username",'Override Grade':'Course Letter Grade'})
        convDf.insert(3, "Last Access", currDate.strftime("%Y-%m-%d %H:%M:%S"), True)
        retDf = convDf.reindex(columns=("Last Name","First Name","SIS User ID","Last Access","Override Grade"))
        retDf = retDf.rename(columns = {"SIS User ID": "Username","Override Grade":"Course Letter Grade"})
        retDf["Course Letter Grade"]=detectMissing(retDf["Course Letter Grade"],dataFrame["Final Grade"])
    elif 'Final Grade' in dataFrame:
        convDf = dataFrame[['SIS User ID','Last Name','First Name','Final Grade']]
        convDf.rename(columns = {"SIS User ID": "Username",'Final Grade':'Course Letter Grade'})
        convDf.insert(3, "Last Access", currDate.strftime("%Y-%m-%d %H:%M:%S"), True)
        retDf = convDf.reindex(columns=("Last Name","First Name","SIS User ID","Last Access","Final Grade"))
        retDf = retDf.rename(columns = {"SIS User ID": "Username","Final Grade":"Course Letter Grade"})
    elif  'Final Score' in dataFrame:
    	convDf = dataFrame[['SIS User ID','Last Name','First Name','Final Score']]
    	convDf.rename(columns = {"SIS User ID": "Username",'Final Score':'Course Letter Grade'})
    	convDf.insert(3, "Last Access", currDate.strftime("%Y-%m-%d %H:%M:%S"), True)
    	retDf = convDf.reindex(columns=("Last Name","First Name","SIS User ID","Last Access","Final Score"))
    	retDf = retDf.rename(columns = {"SIS User ID": "Username","Final Score":"Course Letter Grade"})
    	retDf = retDf.apply(lambda x: seriesIteration(x) if x.name == "Course Letter Grade" else x)
    modDfObj = retDf.apply(lambda x: stripSeries(x) if x.name == "First Name" else x)
    modDfObj = modDfObj.apply(lambda x: stripSeries(x) if x.name == "Last Name" else x)
    modDfObj["Username"] = modDfObj["Username"].astype(int)
    return modDfObj

def detectMissing(overrideSeries,baseSeries):
    return overrideSeries.combine_first(baseSeries)
def stripSeries(inputSeries):
    return inputSeries.apply(stripNonalpha)
def stripNonalpha(inputString):
    return ''.join(filter(str.isalnum, inputString))
def seriesIteration(input):
    return input.apply(toLetterGrade)
def toLetterGrade(percentString):
    letterGrade = 'n/a' 
    percent=float(percentString)
    if percent >= 94 :
        letterGrade='A'
    elif percent >= 90 :
	letterGrade='A-'
    elif percent >= 88 :
        letterGrade='B+'
    elif percent >= 84 :
        letterGrade='B'
    elif percent >= 80 :
        letterGrade='B-'
    elif percent >= 78 :
        letterGrade='C+'
    elif percent >= 74 :
        letterGrade='C'
    elif percent >= 70 :
        letterGrade='C-'
    elif percent >= 68 :
        letterGrade='D+'
    elif percent >= 64 :
        letterGrade='D'
    elif percent >= 60 :
        letterGrade='D-'
    else:
        letterGrade='F'


    return letterGrade
#parscoreParser("canvas/Grades-B_A370-06-Fall2019.csv")
#if __name__ == '__main__':
    #parscoreParser(*sys.arg[1:])
