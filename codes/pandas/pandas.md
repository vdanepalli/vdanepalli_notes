
```python
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    row,col=players.shape
    return[row,col]
    
```

```python
df.head(3)

df.tail(3)

students[students['student_id'] == 101][['name', 'age']]

employees['bonus'] = employees['salary'] * 2

animals[animals['weight'] > 100].sort_values('weight', ascending = False)[['name']] # [[dataframe]]; [series]

customers.drop_duplicates(subset='email', keep='first', inplace=True)
# keep -- first, last, False

DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
# axis -- 0 rows; 1 columns
# how -- all | any
# thresh -- these many non-null values are required to keep row or col
# subset -- labels along other axis to consider

students.dropna(subset=['name'], inplace=True)
students = students[students['name'].notnull()]
students.loc[students['name'].notna()]
students.loc[students['name'].notnull()]


employees['salary'] = [int(i) * 2 for i in employees['salary']]
employees['salary'] = employees['salary'] * 2

DataFrame.rename(mapper=None, index=None, columns=None, axis=None, copy=True, inplace=False, level=None, errors='raise')
# axis -- index | columns
# copy -- if set, returns new dataframe
# inplace -- if set, modifies inplace
# level -- for data frames with multi level index, level from which label should be renamed
# errors = raise | ignore




```