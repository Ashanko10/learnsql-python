import mysql.connector
from mysql.connector import errorcode

db = mysql.connector.connect(
  host="localhost",
  user="tomo",
  passwd="waw",
  database="toko_mainan"
)

cursor = db.cursor()
# cursor.execute("CREATE DATABASE toko_mainan")

# print("Database berhasil dibuat!")
sql1 = ("CREATE TABLE `employees` ("
      "`customer_id` INT,"
      "`name` VARCHAR(255),"
      "`address` Varchar(255)) ENGINE=InnoDB")
sql2 = ("ALTER TABLE `employees` "
      " CHANGE COLUMN `employee_id` `employee_id` INT AUTO_INCREMENT PRIMARY KEY")            

sql = """CREATE TABLE customers (
          customer_id INT AUTO_INCREMENT PRIMARY KEY,
          name VARCHAR(255),
          address Varchar(255))"""
cursor.execute(sql2)
# for table_name in TABLES:
#     table_description = TABLES[table_name]
#     try:
#         print("Creating table {}: ".format(table_name), end='')
#         cursor.execute(table_description)
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#             print("already exists.")
#         else:
#             print(err.msg)
#     else:
#         print("OK")