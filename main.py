import numpy as np
import os
from pathlib import Path

import xlsxFunctions as xlsxf
import sqlFunctions as sqlf

filedir = os.path.join(Path().absolute())
filename = "general_ledger.xlsx"
fileReturn = "chart_return.xlsx"

xlsxO = xlsxf.xlsxFunctions()
sqlO = sqlf.sqlFunctions()

ledger = xlsxO.readerXlsx(filedir, filename)

chart = {}
for element in ledger:
	key = element[0]
	value = element[1]
	if key in chart:
		chart[key] = chart[key] + value
	else:
		chart[key] = value
	k = key.rfind(".")
	while(k > 0):
		ancestor = key[:k]
		if ancestor in chart:
			chart[ancestor] = chart[ancestor] + value
		else:
			chart[ancestor] = value
		k = ancestor.rfind(".")

# xlsxO.chartReturnXlsx(chart, filedir)
xlsxO.generateRandomLedger()