# insert data
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="tomo",
  password="waw",
  database="toko_mainan"
)

# -------------------------------
# cursor = db.cursor()
# sql = "INSERT INTO employees ("name", address) VALUES (%s, %s)"
# val = ("Aldo", "Bandung")
# cursor.execute(sql, val)

# db.commit()

# print("{} data ditambahkan".format(cursor.rowcount))

# db.commit()
# -------------------------------

vals = [{"name":"Ayudi","address":"Jogja"},
        {"name":"Prato","address":"Jogja"},
        {"name":"Rotomo","address":"Jogja"}]

for val in vals:
  sql = "INSERT INTO employees (name, address) VALUES (%s, %s)"
  value = (val["name"], val["address"])
  print(val['name'], val['address'])
  cursor = db.cursor()
  cursor.execute(sql, value)

db.commit()