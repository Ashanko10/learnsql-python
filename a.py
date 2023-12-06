# cek konek apa kaga
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="tomo",
  passwd="waw"
)

if db.is_connected():
  print("Berhasil terhubung ke database")
cursor = db.cursor()
# cursor.execute("CREATE DATABASE toko_mainan")

# print("Database berhasil dibuat!")