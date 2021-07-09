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

	def insertSql(self, sumLedger):
		cursor.execute("INSERT INTO general_ledger (account, value) VALUES" + sumLedger)
		banco.commit()