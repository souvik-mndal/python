import pandas as pd
import numpy as np

dct = {
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [28, 34, 25, 30],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"],
    "salary": [70000, 85000, 60000, 75000]
}

df = pd.DataFrame(dct)
#take a particular portion
print(df.loc[[2,3]][['city','salary']])