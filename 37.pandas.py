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
# print(file.loc[0]['Title'])
file['EndMth'] = file['Title'].apply(extractEndMonth)
# print(file)



#which anime has the highest score
print("the anime with the highest score is ----")
print(file[(file['Score']) == (file['Score'].max())])


#top 5 highest scoring anime
print("\n\nthe top 5 highest scoring animes are --- ")
print(file.head())


#which anime has the highest ep count
print("\n\nthe anime which has the highest EP count is ----")
print(file[(file['Episode'] == (file['Episode'].max()))])

#anime with top 5 episode count
print("\n\nthe anime with top 5 episode count are---")
print(file.sort_values(by='Episode',ascending=False).head(5))