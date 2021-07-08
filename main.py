import numpy as np
import pandas as pd
import os
import sqlite3
from pathlib import Path

filedir = os.path.join(Path().absolute())
filename = "general_ledger.xlsx"
fileReturn = "chart_return.xlsx"

def readerXlsx(): 
	general_ledger = pd.read_excel(os.path.join(filedir, "input", filename))
	general_dict = dict(zip(general_ledger.account, general_ledger.value))
	return general_dict

def chartReturnXlsx(chart):
	df1 = pd.DataFrame(chart.items(), columns=['account', 'value']).sort_values(by = 'account')
	if not os.path.exists(os.path.join(filedir, "output")):
		os.makedirs(os.path.join(filedir, "output"))
	with pd.ExcelWriter(os.path.join(filedir, "output","path_to_file.xlsx")) as writer:
		df1.to_excel(writer, sheet_name="Sheet1", index=False)
	print(df1)

def createSql(): 
	banco = sqlite3.connect('deepesg.sql')
	cursor = banco.cursor()
	cursor.execute("CREATE TABLE general_ledger(account TEXT, value FLOAT)")
	banco.commit()

def readerSql(): 
	banco = sqlite3.connect('deepesg.sql')
	cursor = banco.cursor()
	cursor.execute("SELECT * FROM general_ledger")
	general_dict = dict(cursor.fetchall())
	print(general_dict)

def insertSql():
	banco = sqlite3.connect('deepesg.sql')
	cursor = banco.cursor()
	cursor.execute("INSERT INTO general_ledger (account, value) VALUES('03.1.5.001', 494.36), ('03.1.5', 49.36)")
	banco.commit()

ledger = readerXlsx()

chart = {}
for key in list(ledger):
	print(key)
	if key in chart:
		chart[key] = chart[key] + ledger[key]
	else:
		chart[key] = ledger[key]
	k = key.rfind(".")
	while(k > 0):
		ancestor = key[:k]
		if ancestor in chart:
			chart[ancestor] = chart[ancestor] + ledger[key]
		else:
			chart[ancestor] = ledger[key]
		print(ancestor)		
		k = ancestor.rfind(".")
	removido = ledger.pop(key)
# print(chart)

chartReturnXlsx(chart)

insertSql()

readerSql()


