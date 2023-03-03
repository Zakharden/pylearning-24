import sqlite3

DB_NAME = 'sqlitedb_test.db'
#Создание БД
"""with sqlite3.connect(DB_NAME) as sql_conn:
    print(sql_conn)
    print(sqlite3.version) #создание БД"""

#Создание таблицы
# with sqlite3.connect(DB_NAME) as sql_conn:
#     sql_rec = """CREATE TABLE IF NOT EXISTS courseinfo(
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         students_qty integer,
#         reviews_qty integer
#     );"""
#     sql_conn.execute(sql_rec) #выполнение запроса

courses = [(1, "1course", 11, 1211111),
           (2, "2course", 121, 112111),
           (3, "3 course", 131, 1112),
           (4, "4course", 141, 112)]
#Заполнение таблицы
# with sqlite3.connect(DB_NAME) as sql_conn:
#     sql_request="INSERT INTO courseinfo values (?,?,?,?)"
#     sql_conn.execute(sql_request,(228,"Python course", 100, 12)) #построчно
#     sql_conn.commit()

# with sqlite3.connect(DB_NAME) as sql_conn:
#     sql_request = "INSERT INTO courseinfo values (?,?,?,?)"
#     for course in courses:
#         sql_conn.execute(sql_request, course)
#     sql_conn.commit()


# with sqlite3.connect(DB_NAME) as sql_conn:
#     sql_request = "INSERT or Replace INTO  courseinfo values (?,?,?,?)" #вставить или заменить
#     for i in courses:
#         sql_conn.execute(sql_request,i) #циклом
#     sql_conn.commit()

#ЧТЕНИЕ таблицы
with sqlite3.connect(DB_NAME) as sql_conn:
        sql_reader = 'Select * from courseinfo where reviews_qty>500'
        sql_cursor = sql_conn.execute(sql_reader)
        for record in sql_cursor: #кортежи
            print(record)
        # records = sql_cursor.fetchall() #список кортежей
        # print(records) #так как курсор уже прощел, список пустой