import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai', 'campus'])
ser.str.capitalize().str.cat(sep=' ')
print(ser.str.capitalize().str.cat(sep=' '))