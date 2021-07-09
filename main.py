import numpy as np
import os
import time
from pathlib import Path

import xlsxFunctions as xlsxf
import sqlFunctions as sqlf
import ledgerFunctions as ledgerf

filedir = os.path.join(Path().absolute())
filename = "general_ledger.xlsx"
fileReturn = "chart_return.xlsx"
filenamechart = "chart_of_accounts.xlsx"

xlsxO = xlsxf.xlsxFunctions()
sqlO = sqlf.sqlFunctions()
ledgerO = ledgerf.ledgerFunctions()

# xlsx scope

def do_populate_xlsx():
	repeat = True
	while(repeat):
		ledgerFile = input('Type a xlsx general_ledger file whith the ".xlsx": ')
		chartUnpopuledFile = input('Type a xlsx chart_of_accounts file file whith the ".xlsx": ')
		if os.path.exists(os.path.join(filedir, "input", ledgerFile)) and os.path.exists(os.path.join(filedir, "input", chartUnpopuledFile)):
			ledgerTuple = xlsxO.readerXlsx(filedir, ledgerFile)
			chartPopuled = ledgerO.sumLedgerValues(ledgerTuple)
			xlsxO.verifyChartXlsx(chartPopuled, filedir, chartUnpopuledFile)
			repeat = False

def do_xlsx():
	while True:
		print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
		print("Xlsx Menu:\n")
		print("Type 1 to populate from a general_ledger file and a chart_of_accounts file")
		print("Type any other options not listed to back to main menu")
		print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
		command = input("Digite o comando desejado: ")
		if(command not in acceptCommandsXlsx):
			break
		else:
			acceptCommandsXlsx[command]()

# end xlsx scope

# create test scope
def do_test_xlsx():
	ledgerFile = input('Type a name file to the general_ledger whithout the ".xlsx": ')
	ledgerTuple = ledgerO.generateRandomLedger()
	chartUnpopuled = ledgerO.generateChartFromLedgerTuple(ledgerTuple)
	xlsxO.saveLedgerTuple(ledgerTuple , filedir, ledgerFile + ".xlsx")

def do_test():
	while True:
		print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
		print("Test Menu:\n")
		print("Type 1 to create to create a random test and save in xlsx format")
		print("Type 2 to create to create a random test and save in sql database")
		print("Type any bottom not listed to back to main menu")
		print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
		command = input("Digite o comando desejado: ")
		if(command not in acceptCommandsTest):
			break
		else:
			acceptCommandsTest[command]()

# end test scope

def do_back():
	return

def do_exit():
    exit()

acceptCommandsXlsx = {
	"1": do_populate_xlsx,
	"2": "Mustang",
	"3": do_back
}

acceptCommandsSql = {
	"1": do_populate_xlsx,
	"2": "Mustang",
	"3": do_back
}

acceptCommandsTest = {
	"1": do_test_xlsx,
	"2": "do_test_sql",
	"3": do_back
}

acceptCommands = {
	"1": do_xlsx,
	"2": "do_sql",
	"3": do_test,
	"4": do_exit
}

def run():
	print("Welcome to Ledger Processing Program!!!\n")
	while True:
		print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
		print("Main Menu:\n")
		print("Type 1 to process through an xlsx")
		print("Type 3 to generate a test")
		print("Type 4 to exit")
		print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
		command = input("Digite o comando desejado: ")
		if(command not in acceptCommands):
			print("\n\n\nComando não encontrado!\n\n\n")
			time.sleep(1)
		else:
			acceptCommands[command]()


if __name__ == '__main__':
	run()
