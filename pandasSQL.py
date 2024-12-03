import pandas as pd
from sqlite3 import connect
import mysql.connector

conn = connect(':memory:')
df = pd.DataFrame(data=[[0,'10-11-12'],[1,'12-11-10']],
                  columns=['int_column','date_column'])

print(df.to_sql(name='test_data',con=conn))


print(pd.read_sql('SELECT int_column, date_column FROM test_data',conn))

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database='takatambaza')
print(pd.read_sql('SELECT * FROM student',con=db))
