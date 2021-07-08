import sqlite3

class sqlFunctions:
	banco = sqlite3.connect('deepesg.sql')
	cursor = banco.cursor()
	
	def createSql(self): 
		cursor.execute("CREATE TABLE general_ledger(account TEXT, value FLOAT)")
		banco.commit()

	def readerSql(self): 
		cursor.execute("SELECT * FROM general_ledger")
		general_tuple = cursor.fetchall()
		return general_tuple

	def insertSql(self):
		cursor.execute("INSERT INTO general_ledger (account, value) VALUES('03.1.5.001', 494.36), ('03.1.5', 49.36)")
		banco.commit()