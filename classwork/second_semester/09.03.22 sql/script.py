import sqlite3

connection = sqlite3.connect(database = '/home/arseny/python_bd')
cursor = connection.cursor()
# cursor.execute('drop table "Languages";')
cursor.execute('create table "Languages" (name text, quality text);')
cursor.execute('insert into "Languages" values ("python", "great"), ("haskell", "for geniuses");')
cursor.execute('select * from Languages')
print(cursor.fetchall())

connection.commit()

cursor.close()
connection.close()