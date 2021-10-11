import csv
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1234', db='test2', charset='utf8') 
cursor = conn.cursor() 

print("dbconnection!!")

with open('mapo.csv',"rt",encoding="UTF8") as file:
    reader = csv.reader(file)

    for row in reader:
        id = row[0]
        restaurant_name = (row[1])
        restaurant_address = (row[2])
        restaurant_phone_number = (row[3])
        hygiene_level = (row[4])
        is_franchise = (row[5])
        menu = (row[6])
        menu_main_category = (row[7])
        grade = (row[8])
        opening_hours = (row[9])
        holiday = (row[10])
        sql = f'''
            INSERT INTO RESTAURANT(restaurant_name, restaurant_address, restaurant_phone_number, hygiene_level,
     is_franchise, menu, menu_main_category, grade, opening_hours, holiday)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
        cursor.execute(sql,(restaurant_name, restaurant_address, restaurant_phone_number, hygiene_level,
     is_franchise, menu, menu_main_category, grade, opening_hours, holiday)) 

        # print(restaurant_address)
        

# sql = f'''
#     INSERT INTO RESTAURANT(restaurant_name, restaurant_address, restaurant_phone_number, hygiene_level,
#     is_franchise, menu, menu_main_category, grade, opening_hours, holiday)
#     VALUES({restaurant_name}, {restaurant_address}, {restaurant_phone_number}, {hygiene_level},
#     {is_franchise}, {menu}, {menu_main_category}, {grade}, {opening_hours}, {holiday})
# '''

conn.commit() 
conn.close() 