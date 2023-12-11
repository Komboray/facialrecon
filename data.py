import mariadb
import sys

class Data:
  # def __init__(self, admin, name):
  #   self.name = name
  #   self.admin = admin


  def sendDetails(self, admin, name):
        # database operations
        try:
          conn = mariadb.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="university"
          )
        except mariadb.Error as e:
          print(f"Error connecting to MariaDb PLatform: {e}")
          sys.exit(1)

        mycursor = conn.cursor()

        mycursor.execute("INSERT INTO students (admin, name) VALUES ('admin', 'name')", (admin, name))

        if (mycursor):
          print("Success")

        else:
          # Close Connection
          conn.close()
