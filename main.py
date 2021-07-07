import numpy as np
import pandas as pd
import os
from pathlib import Path

filedir = os.path.join(Path().absolute(), "dataset_small")
filename = "general_ledger.xlsx"

def reader(): 
	general_ledger = pd.read_excel(os.path.join(filedir,"input",filename))
	general_dict = dict(zip(general_ledger.account, general_ledger.value))
	return general_dict

ledger = reader()

chart = {}
for key in list(ledger):
	chart[key] = ledger[key]
	k = key.rfind(".")
	while(k > 0):
		ledgerFather = key[:k]
		print(ledgerFather)
		k = ledgerFather.rfind(".")
	#print(key)
	removido = ledger.pop(key)
	#print(removido)
	#print(key)


# print(ledger)

