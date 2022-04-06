'''
MySQL
======
Python can be used in database applications.
One of the most popular databases is MySQL.

'''

# %% Download and install "MySQL Connector" i.e. mysql-connector-python
import mysql.connector
pip install mysql-connector-python

# https://dev.mysql.com/downloads/ OR https://dev.mysql.com/downloads/installer/

# %% Test MySQL Connector

mysql.connector.connect()

# %% creating a connection to the database


myDB = mysql.connector.connect(
    host="localhost",
    user="SunMan",
    password="root"
)

print(myDB)

# %% Creating a Database
myCursor = myDB.cursor()
myQuery = "CREATE DATABASE suppliers"
myCursor.execute(myQuery)

# %% check version of SQL
myCursor = myDB.cursor()
myCursor.execute("SELECT version()")

# The fetchone() method will return the first row of the result:
DB_Version = myCursor.fetchone()

print(DB_Version)

# %% check version of SQL
myCursor = myDB.cursor()

myCursor.execute("SHOW DATABASES")

for x in myCursor:
    print(x)

# %% Connect to your database "suppliers"
myDB = mysql.connector.connect(
    host="localhost",
    user="SunMan",
    password="root",
    database="suppliers"
)

print(myDB)

# %% To create a table in MySQL, use the "CREATE TABLE" statement

myCursor = myDB.cursor()
myQuery = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
myCursor.execute(myQuery)


# %% Check if table exists
myCursor = myDB.cursor()
myCursor.execute("SHOW TABLES")

for x in myCursor:
    print(x)

# %% Primary Key - Create primary key when creating the table
myCursor = myDB.cursor()
myQuery = "CREATE TABLE products (ID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
myCursor.execute(myQuery)


# %% Primary Key - Create primary key on existing table
myCursor = myDB.cursor()
myQuery = "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"
myCursor.execute(myQuery)

# %% Insert into tables

myCursor = myDB.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")

myCursor.execute(sql, val)

myDB.commit()

print(myCursor.rowcount, "record inserted.")

# %% Check tables

myCursor.execute("DESCRIBE customers")
myResult = myCursor.fetchall()
for x in myResult:
    print(x)

# %% INSERT multiple rows
myCursor = myDB.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"

val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]

for item in val:
    myCursor.execute(sql, item)

myDB.commit()

print(myCursor.rowcount, "record inserted.")

# Note: If you insert more than one row, the id of the last inserted row is returned. You can get the id of the row you just inserted by asking the cursor object.

print("1 record inserted, ID:", myCursor.lastrowid)

# %% Select From a Table

'''
USE suppliers;
SELECT * FROM customers;
'''
myDB = mysql.connector.connect(
    host="localhost",
    user="SunMan",
    password="root",
    database="suppliers"
)

print(myDB)
myCursor = myDB.cursor()

myCursor.execute("SELECT * FROM customers")
myResult = myCursor.fetchall()
for x in myResult:
    print(x)

# Note: We use the fetchall() method, which fetches all rows from the last executed statement.

# %% Selecting Columns

myDB = mysql.connector.connect(
    host="localhost",
    user="SunMan",
    password="root",
    database="suppliers"
)

print(myDB)
myCursor = myDB.cursor()

myCursor.execute("SELECT name FROM customers")
myResult = myCursor.fetchall()
for x in myResult:
    print(x)


# %% The fetchone() method will return the first row of the result:
myCursor.execute("SELECT name FROM customers")
myResult = myCursor.fetchone()
for x in myResult:
    print(x)

# %% Select With a Filter
myCursor.execute("SELECT * FROM customers WHERE address ='Park Lane 38'")
myResult = myCursor.fetchall()
for x in myResult:
    print(x)

# %% Use the %  to represent wildcard characters
myCursor.execute("SELECT * FROM customers WHERE address LIKE '%way%'")
myResult = myCursor.fetchall()
for x in myResult:
    print(x)

# %% Escape query values by using the placholder %s method to Prevent SQL Injection
adr = ("Yellow Garden 2", )
myCursor.execute("SELECT * FROM customers WHERE address = %s", adr)

myResult = myCursor.fetchall()
for x in myResult:
    print(x)

# %% Sort the Result
myCursor.execute("SELECT name FROM customers ORDER BY name")
myResult = myCursor.fetchall()
for x in myResult:
    print(x)


# %%
myCursor.execute("SELECT name FROM customers ORDER BY name DESC")
myResult = myCursor.fetchall()
for x in myResult:
    print(x)
# %% Delete Record
query = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

myCursor.execute(query, adr)
myDB.commit()

print(myCursor.rowcount, "record(s) deleted")

# %% Delete a Table
query = "DROP TABLE customers"

myCursor.execute(query)
# %% Drop Only if Exist
query = "DROP TABLE IF EXISTS customers"

myCursor.execute(query)
# %% Update Table
query = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

myCursor.execute(query)
myDB.commit()

print(myCursor.rowcount, "record(s) affected")

# %% Limit the Result

myCursor.execute("SELECT * FROM customers LIMIT 5")
myResult = myCursor.fetchall()
for x in myResult:
    print(x)
# %% If you want to return five records, starting from the third record, you can use the "OFFSET" keyword:

myCursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myResult = myCursor.fetchall()
for x in myResult:
    print(x)

# %% Join Two or More Tables
'''
You can combine rows from two or more tables, based on a related column between them, by using a JOIN statement.
Consider you have a "users" table and a "products" table:
'''

# %% Products table
import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="SunMan",
    password="root",
    database="suppliers"
)

print(myDB)
myCursor = myDB.cursor()

# %% Primary Key - Create primary key when creating the table
myCursor = myDB.cursor()
myQuery = "CREATE TABLE products (ID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
myCursor.execute(myQuery)

# %% Check tables

myCursor.execute("DESCRIBE products")
myResult = myCursor.fetchall()
for x in myResult:
    print(x)

# %% INSERT records INTO products
sql = "INSERT INTO products (name) VALUES (%s)"
# val = [('Chocolate Heaven',),("Tasty Lemons",),("Vanilla Dreams",),]
val = [['Chocolate Heaven'], ['Tasty Lemons'], ['Vanilla Dreams']]

myCursor.executemany(sql, val)

myDB.commit()

print(myCursor.rowcount, "record inserted.")

# %% Verify
myCursor.execute("SELECT * FROM products")
myResult = myCursor.fetchall()
for x in myResult:
    print(x)


# %% users table
import mysql.connector
myDB = mysql.connector.connect(
    host="localhost",
    user="SunMan",
    password="root",
    database="suppliers"
)

print(myDB)
myCursor = myDB.cursor()

# %% Primary Key - Create primary key when creating the table
myCursor = myDB.cursor()
myQuery = "CREATE TABLE users (ID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav INT)"
myCursor.execute(myQuery)

# %% Check tables

myCursor.execute("DESCRIBE users")
myResult = myCursor.fetchall()
for x in myResult:
    print(x)

# %% INSERT records INTO products

sql = "INSERT INTO users (name,fav) VALUES (%s,%s)"

val = [
    ['John', 2],
    ['Peter', 1],
    ['Amy', 3],
    ['Hannah', None],
    ['Michael', 2]
]

myCursor.executemany(sql, val)
myDB.commit()
print(myCursor.rowcount, "record inserted.")

# %% Verify
myCursor.execute("SELECT * FROM users")
myResult = myCursor.fetchall()
for x in myResult:
    print(x)

# %% DROP
# myCursor.execute('DROP TABLE products')
# myCursor.execute('DROP TABLE users')

# %% INNER JOIN only shows the records where there is a match.

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

myCursor.execute(sql)

myResult = myCursor.fetchall()

for x in myResult:
  print(x)


# %% show all users, even if they do not have a favorite product

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"

myCursor.execute(sql)

myResult = myCursor.fetchall()

for x in myResult:
  print(x)


# %% return all products, and the users who have them as their favorite, even if no user have them as their favorite

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"

myCursor.execute(sql)

myResult = myCursor.fetchall()

for x in myResult:
  print(x)


# %%
