import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="******",database="reciepe_recon", auth_plugin="mysql_native_password")

mycursor = mydb.cursor()

mycursor.execute("select `name` from reciepe_recon.recipe_rec")

for db in mycursor:
    print(db)

