import pandas as pd
import numpy as np

def extractEP(txt):
    start = txt.find('(')
    end = txt.find(')')
    ans = txt[start+1:end]
    return ans

file = pd.read_csv(r'37.anime.csv')
# print(file)

#make a column for episode count
file['Episode'] = file['Title'].apply(extractEP)
print(file)