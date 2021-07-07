import numpy as np
import pandas as pd
import os
from pathlib import Path

filedir = os.path.join(Path().absolute())
filename = "general_ledger.xlsx"

def reader(): 
	general_ledger = pd.read_excel(os.path.join(filedir,"input",filename))
	general_dict = dict(zip(general_ledger.account, general_ledger.value))
	return general_dict

ledger = reader()

chart = {}
for key in list(ledger):
	print(key)
	chart[key] = ledger[key]
	k = key.rfind(".")
	while(k > 0):
		ancestor = key[:k]
		if ancestor in ledger:
			chart[ancestor] = chart[ancestor] + ledger[key]
		else:
			chart[ancestor] = ledger[key]
		print(ancestor)		
		k = ancestor.rfind(".")
	print(chart)
	break
	removido = ledger.pop(key)
	#print(removido)
	#print(key)


# print(ledger)

