import pandas as pd

data = [(1, 8302643107729554, 813524, 213123213.0, 'Clement', 'Lee'), (2, 398759476402815, 174965, 12763871263.0, 'Chia', 'Hao')]

df = pd.DataFrame(data, columns=["1","2","3","4","5","6"])
print(df)