import sqlite3


class Database:
	def __init__(self, databaseName):
		self.connection = sqlite3.connect("../databases/" + str(databaseName))
		self.cursor = self.connection.cursor()

	def execute(self, string):
		print(string)
		self.cursor.execute(string)
		self.connection.commit()
		results = self.cursor.fetchall()

		return results

connection = sqlite3.connect('../databases/jacobstest.db')
cursor = connection.cursor()
currentDatabase = ""
