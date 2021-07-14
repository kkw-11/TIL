import sqlite3

# sqlite3.Connection
conn = sqlite3.connect('db.sqlite3')

# Cursor
cur = conn.cursor()

# cur.execute(sql문)

str1 =    '''
    DROP TABLE IF EXISTS user
    '''
cur.execute(str1)

cur.execute(
    '''
    CREATE TABLE user (
        pk_user_id INTEGER,
        name TEXT,
        PRIMARY KEY (pk_user_id)
    )
    '''
)



# 데이터베이스의 CRUD

# CREATE 데이터 생성

# INSERT
cur.execute(
    '''
    INSERT INTO user
    VALUES (1, '승한')
    '''
)


user_list = [
    (2, '철수'),
    (3, '영희'),
]

cur.execute(
    '''
    INSERT INTO user
    VALUES (?, ?)
    ''',
    (2, '철수')
)


user_list = [
    (3, '영희'),
    (4, '영수'),
]

cur.executemany(
    '''
    INSERT INTO user
    VALUES (?, ?)
    ''',
    user_list
)

#READ
cur.execute(
    '''
    SELECT *
    FROM user
    '''
)



#UPDATE


# row = cur.fetchone()
# print(row)

# row = cur.fetchone()
# print(row)


# row = cur.fetchmany(size=2)
# print(row)


rows = cur.fetchall()

print(rows)

# UPDATE
cur.execute(
    '''
    UPDATE user
    SET name = '한영'
    WHERE pk_user_id = '1'
    '''

)


# DELETE

cur.execute(
    '''
    DELETE 
    FROM user
    WHERE pk_user_id = '2'
    '''

)

conn.commit()

