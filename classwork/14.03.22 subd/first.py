import psycopg2


def select(table, cond):
    return 'Select * from {0} Where {1}'.format(table, cond)

def update(table, atr, values, cond):
    return 'Update {0} set {1} = {2} where {3}'.format(table, atr, values, cond)

def delete(table, cond):
    return 'Delete * from {0} Where {1}'.format(table, cond)

def insert(table, values):
    return 'Insert * into {0} values ({1})'.format(table, ', '.join(values))

connection = psycopg2.connect()
cursor = connection.cursor()

table = ''
level = 1
menus = [
    '1. Выбор таблицы \n 2. EXIT',
    '1. SELECT \n 2. UPDATE \n 3. DELETE \n 4. INSERT \n 5. EXIT'
]
while True:
    ans = input(menus[level - 1])
    if level == '2':
        def execute(query):
            cursor.execute(query)
            return cursor.fetchall()
        if ans == '1':
            cond = input('Введите условие для запроса: ')
            req = execute(select(table, cond))
            print('')
        if ans == '2':
            pass
        if ans == '5':
            level == '2'