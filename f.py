import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="tomo",
  passwd="waw",
  database="toko_mainan"
)

cursor = db.cursor()
sql = "SELECT * FROM employees"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
  print(data)