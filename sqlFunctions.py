import pandas as pd
import sqlite3
import os

class sqlFunctions:
	
	def createSql(self, filedir, nameData): 
		base = sqlite3.connect(os.path.join(filedir, "sql", nameData))
		cursor = base.cursor()
		cursor.execute("CREATE TABLE general_ledger(account TEXT, value FLOAT)")
		cursor.execute("CREATE TABLE chart_of_accounts(account TEXT)")
		base.commit()

	def readerSql(self, filedir, nameData): 
		base = sqlite3.connect(os.path.join(filedir, "sql", nameData))
		cursor = base.cursor()

		cursor.execute("SELECT * FROM general_ledger")
		ledgerTuple = cursor.fetchall()

		cursor.execute("SELECT * FROM chart_of_accounts")
		chartUnpopuled = cursor.fetchall()
		return ledgerTuple, chartUnpopuled

	def insertSql(self, ledgerTuple, chartUnpopuled, filedir, nameData):
		base = sqlite3.connect(os.path.join(filedir, "sql", nameData))
		cursor = base.cursor()
		cursor.executemany("INSERT INTO general_ledger (account, value) VALUES (?, ?)", list(ledgerTuple))
		cursor.executemany("INSERT INTO chart_of_accounts (account) VALUES (?)", list(zip(*[iter(chartUnpopuled)]*1)))
		base.commit()

	def verifyChartSql(self, chartUnpopuled, chartPopuled, filedir, filename):
		if(set(*(map(set, zip(*chartUnpopuled)))) == set(chartPopuled.keys())):
			self.chartReturnXlsx(chartPopuled, filedir, filename + ".xlsx")
			print('\n\n\nSuccess!!! the file was saved with the name: "'+ filename+'" in the "output" folder\n\n\n')
		else:
			print('\n\n\nThe column "chart_of_accounts" does not match with the column "general_ledger"\n\n\n')

	def chartReturnXlsx(self, chartVerified, filedir, filename):
		df = pd.DataFrame(chartVerified.items(), columns=['account', 'value']).sort_values(by = 'account').round(2)
		if not os.path.exists(os.path.join(filedir, "output")):
			os.makedirs(os.path.join(filedir, "output"))
		with pd.ExcelWriter(os.path.join(filedir, "output", filename)) as writer:
			df.to_excel(writer, sheet_name="Sheet1", index=False)