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

		print(set(list(zip(*chartUnpopuled))))

		print("-------------------------")

		print(set(chartPopuled.keys()))

		if(set(chartUnpopuled) == set(chartPopuled.keys())):
			print("vc eh o bixao mesmo")
			self.chartReturnXlsx(chartPopuled, filedir, filename)
		else:
			print("vc nao eh o bixao")

	def chartReturnXlsx(self, chartVerified, filedir, filename):
		df = pd.DataFrame(chartVerified.items(), columns=['account', 'value']).sort_values(by = 'account').round(2)
		if not os.path.exists(os.path.join(filedir, "output")):
			os.makedirs(os.path.join(filedir, "output"))
		with pd.ExcelWriter(os.path.join(filedir, "output", filename)) as writer:
			df.to_excel(writer, sheet_name="Sheet1", index=False)