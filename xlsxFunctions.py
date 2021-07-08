import pandas as pd
import os
import random

class xlsxFunctions:

	def readerXlsx(self, filedir, filename): 
		general_ledger = pd.read_excel(os.path.join(filedir, "input", filename))
		general_tuple = tuple(zip(general_ledger.account, general_ledger.value))
		return general_tuple

	def populateChart(self, chart, filedir, filename):
		chart_accounts = pd.read_excel(os.path.join(filedir, "input", filename))
		list_accounts = list(chart_accounts.account)
		if(set(list_accounts) == set(chart.keys())):
			self.chartReturnXlsx(chart, filedir, filename)
		# else: mensagem de erro

		#general_tuple = tuple(zip(general_ledger.account, general_ledger.value))
		#return general_tuple

	def chartReturnXlsx(self, chart, filedir, filename):
		df1 = pd.DataFrame(chart.items(), columns=['account', 'value']).sort_values(by = 'account').round(2)
		if not os.path.exists(os.path.join(filedir, "output")):
			os.makedirs(os.path.join(filedir, "output"))
		with pd.ExcelWriter(os.path.join(filedir, "output", filename)) as writer:
			df1.to_excel(writer, sheet_name="Sheet1", index=False)

	def generateRandomLedger(self, quantity = 200, limitAccount = 50, limitComma = 5, limitValue = 10000):
		for i in range(quantity):
			account = (str)(random.randint(1, limitAccount + (limitAccount == 0)))
			for j in range(limitComma):
				if(bool(random.randint(0, 2))):
					break;
				account = account + "." + (str)(random.randint(1, limitAccount + (limitAccount == 0)))
			value = round((random.randint(0, limitValue)) * 0.01, 2)
			print(account, value)
	        
