import sys
import os
import pandas as pd
import datetime

currDate = datetime.datetime.now()

#run program
def parscoreParser(inputFile):
    newData = readFile(inputFile)
    #changed this line to put changes back into file rather than printing them
    inputConv(newData).to_csv(index=False,path_or_buf=inputFile)


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
    cols = dataFrame["Student"].str.partition(" ", True)
    dataFrame["Last Name"]= cols[2]
    dataFrame["First Name"]= cols[0]
    dataFrame.drop(columns =["Student"], inplace = True)
    convDf = dataFrame[['SIS User ID','Last Name','First Name','Final Score']]
    convDf.rename(columns = {"SIS User ID": "RED ID",
                                  "Final Score":"Course Letter Grade"})
    convDf.insert(3, "Last Access Date", currDate.strftime("%Y-%m-%d %H:%M:%S"), True)
    retDf = convDf.reindex(columns=("Last Name","First Name","SIS User ID","Last Access Date","Final Score"))
    retDf = retDf.rename(columns = {"SIS User ID": "RED ID",
                                  "Final Score":"Course Letter Grade"})
    for ()
    return retDf

def toLetterGrade(percent):
    letterGrade = ' '

    if(percent < 97.5):
        letterGrade = 'A+'
    elif(percent > 92.5 and percent < 97.5 ):
        letterGrade = 'A'
    elif(percent > 90 and percent < 92.5 ):
        letterGrade = 'A-'
    elif(percent > 87.5 and percent < 90 ):
        letterGrade = 'B+'
    elif(percent > 82.5 and percent < 87.5 ):
        letterGrade = 'B'
    elif(percent > 80 and percent < 82.5 ):
        letterGrade = 'B-'
    elif(percent > 77.5 and percent < 80 ):
        letterGrade = 'C+'
    elif(percent > 72.5 and percent < 77.5 ):
        letterGrade = 'C'
    elif(percent > 70 and percent < 72.5 ):
        letterGrade = 'C-'
    elif(percent > 67.5 and percent < 70 ):
        letterGrade = 'D+'
    elif(percent > 62.5 and percent < 67.5 ):
        letterGrade = 'D'
    elif(percent > 60 and percent < 62.5 ):
        letterGrade = 'D-'
    elif(percent < 60 ):
        letterGrade = 'F'
    
    return letterGrade
        
    



#parscoreParser("canvas/Grades-B_A370-06-Fall2019.csv")
#if __name__ == '__main__':
    #parscoreParser(*sys.arg[1:])
