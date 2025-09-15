import pandas as pd
import numpy as np

def extractEP(txt):
    start = txt.find('(')
    end = txt.find(' eps')
    ans = txt[start+1:end]
    return ans

def extractTS(txt):
    start = txt.find(')')
    # end = txt.find(' eps')
    ans = txt[start+1:start+20]
    return ans


def extractStartMonth(txt):
    start = txt.find(')')
    # end = txt.find(' eps')
    ans = txt[start+1:start+4]
    return ans


def extractEndMonth(txt):
    start = txt.find(')')
    # end = txt.find(' eps')
    ans = txt[start+12:start+16]
    return ans

file = pd.read_csv(r'37.anime.csv')
# print(file)

#make a column for episode count
file['Episode'] = file['Title'].apply(extractEP).astype(int)
# print((file))


#make a new column for timestamps
file['Timestamp'] = file['Title'].apply(extractTS)
# print(file)


#extract start month
# print(file.loc[0]['Title'])
file['StartMth'] = file['Title'].apply(extractStartMonth)
# print(file)


#extract start month
print(file.loc[0]['Title'])
file['EndMth'] = file['Title'].apply(extractEndMonth)
print(file)

