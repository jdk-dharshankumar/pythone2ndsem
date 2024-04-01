import mysql.connector as sqltor


gpass = input("Enter root password: ")

db = input("Enter Class: ")

Connection = sqltor.connect(host = "localhost" , user = "root" , passwd = gpass , database = db)

Cursor = Connection.cursor()

Cursor.execute("""CREATE TABLE IF NOT EXISTS Chemistry(
                    Admno int,
                    Name varchar(25),
                    Marks int)""")

Cursor.execute("""CREATE TABLE IF NOT EXISTS Physics(
                    Admno int,
                    Name varchar(25),
                    Marks int)""")

Cursor.execute("""CREATE TABLE IF NOT EXISTS Maths(
                    Admno int,
                    Name varchar(25),
                    Marks int)""")

Cursor.execute("""CREATE TABLE IF NOT EXISTS English(
                    Admno int,
                    Name varchar(25),
                    Marks int)""")

Cursor.execute("""CREATE TABLE IF NOT EXISTS CS(
                    Admno int,
                    Name varchar(25),
                    Marks int)""")

Connection.commit()

Connection.close()
