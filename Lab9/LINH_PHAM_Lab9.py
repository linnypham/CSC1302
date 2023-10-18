import  sqlite3

conn = sqlite3.connect('store_inventory.db')

cursor = conn.cursor()

command = 'CREATE TABLE IF NOT EXISTS GROCERY(ProductID INTEGER PRIMARY KEY, ProductName TEXT, UnitPrice FLOAT, Quantity FLOAT)'
cursor.execute(command)

command = "INSERT INTO GROCERY VALUES(001,'Egg',2.0,23)"
cursor.execute(command)

command = "INSERT INTO GROCERY VALUES(002,'Milk',4.0,30)"
cursor.execute(command)

command = "INSERT INTO GROCERY VALUES(003,'Rice',19.99,10)"
cursor.execute(command)

command = 'SELECT* from GROCERY'
cursor.execute(command)
all_data = cursor.fetchall()
print(all_data)

command = 'SELECT ProductName from GROCERY WHERE UnitPrice BETWEEN 1.0 and 5.0'
cursor.execute(command)
print()
filtered_data = cursor.fetchall()
print(filtered_data)


command = 'SELECT SUM(UnitPrice*Quantity) from GROCERY'
cursor.execute(command)
total_cost  = cursor.fetchall()
print()
print(total_cost)