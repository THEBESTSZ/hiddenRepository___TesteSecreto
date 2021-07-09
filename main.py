import numpy as np
import os
import time
import sys
from pathlib import Path

import xlsxFunctions as xlsxf
import sqlFunctions as sqlf
import ledgerFunctions as ledgerf

filedir = os.path.join(Path().absolute())

xlsxO = xlsxf.xlsxFunctions()
sqlO = sqlf.sqlFunctions()
ledgerO = ledgerf.ledgerFunctions()

# sql scope

def do_reader_sql():
	try:
		dataBaseFile = input('Type a database file, without the ".sql", that contains the tables general_ledger and chart_of_accounts: ')
		dataBaseFile = dataBaseFile + ".sql"
		if os.path.exists(os.path.join(filedir, "sql", dataBaseFile)):
			ledgerTuple, chartUnpopuled = sqlO.readerSql(filedir, dataBaseFile)
			print("general_ledger:", ledgerTuple, "\n\n\n")
			print("chart_of_accounts:", chartUnpopuled, "\n\n\n")
		else:
			print("The typed file does not exist!!!\n\n\n")
	except OSError as e:
		print("\n\n\nOS error: {0}".format(e), "\n\n\n")
	except:
		print("\n\n\nUnexpected error:", sys.exc_info()[0], "\n\n\n")
	finally:
		time.sleep(2)

def do_populate_sql():
	try:
		dataBaseFile = input('Type a database file, without the ".sql", that contains the tables general_ledger and chart_of_accounts: ')
		dataBaseFile = dataBaseFile + ".sql"
		if os.path.exists(os.path.join(filedir, "sql", dataBaseFile)):
			ledgerTuple, chartUnpopuled = sqlO.readerSql(filedir, dataBaseFile)
			chartPopuled = ledgerO.sumLedgerValues(ledgerTuple)
			sqlO.verifyChartSql(chartUnpopuled, chartPopuled, filedir, dataBaseFile)
		else:
			print("The typed file does not exist!!!\n\n\n")
			time.sleep(2)
	except OSError as e:
		print("\n\n\nOS error: {0}".format(e), "\n\n\n")
		time.sleep(2)
	except:
		print("\n\n\nUnexpected error:", sys.exc_info()[0], "\n\n\n")
		time.sleep(2)

def do_sql():
	try:
		while True:
			print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
			print("                                           Sql Menu:\n")
			print("Type 1 to populate a general_ledger table and a chart_of_accounts table")
			print("Type 2 to select all a general_ledger table and a chart_of_accounts table")
			print("Type any other bottom not listed to back to main menu")
			print("\n\n#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
			command = input("Digite o comando desejado: ")
			if(command not in acceptCommandsSql):
				break
			else:
				acceptCommandsSql[command]()
	except:
		print("\n\n\nUnexpected error:", sys.exc_info()[0], "\n\n\n")
		time.sleep(2)

# end sql scope

# xlsx scope

def do_populate_xlsx():
	try:
		ledgerFile = input('Type a xlsx general_ledger file without the ".xlsx": ')
		ledgerFile = ledgerFile + ".xlsx"
		chartUnpopuledFile = input('Type a xlsx chart_of_accounts file file without the ".xlsx": ')
		chartUnpopuledFile = chartUnpopuledFile + ".xlsx"
		if os.path.exists(os.path.join(filedir, "input", ledgerFile)) and os.path.exists(os.path.join(filedir, "input", chartUnpopuledFile)):
			ledgerTuple = xlsxO.readerXlsx(filedir, ledgerFile)
			chartPopuled = ledgerO.sumLedgerValues(ledgerTuple)
			xlsxO.verifyChartXlsx(chartPopuled, filedir, chartUnpopuledFile)
		else:
			print("The typed file does not exist!!!\n\n\n")
			time.sleep(2)
	except OSError as e:
		print("\n\n\nOS error: {0}".format(e), "\n\n\n")
		time.sleep(2)
	except:
		print("\n\n\nUnexpected error:", sys.exc_info()[0], "\n\n\n")
		time.sleep(2)

			

def do_xlsx():
	try:
		while True:
			print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
			print("                                           Xlsx Menu:\n")
			print("Type 1 to populate from a general_ledger file and a chart_of_accounts file")
			print("Type any other bottom not listed to back to main menu")
			print("\n\n#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
			command = input("Digite o comando desejado: ")
			if(command not in acceptCommandsXlsx):
				break
			else:
				acceptCommandsXlsx[command]()
	except:
		print("\n\n\nUnexpected error:", sys.exc_info()[0], "\n\n\n")
		time.sleep(2)


# end xlsx scope

# create test scope
def do_test_xlsx():
	try:
		ledgerFile = input('Type a name file to the general_ledger file without the ".xlsx": ')
		chartUnpopuledFile = input('Type a name file to the chart_of_accounts file without the ".xlsx": ')
		ledgerTuple = ledgerO.generateRandomLedger()
		ledgerSum = ledgerO.sumLedgerValues(ledgerTuple)
		chartUnpopuled = ledgerO.generateChartFromLedgerSum(ledgerSum)
		xlsxO.saveLedgerTupleXlsx(ledgerTuple , filedir, ledgerFile + ".xlsx")
		xlsxO.saveChartUnpopuledXlsx(chartUnpopuled , filedir, chartUnpopuledFile + ".xlsx")
	except:
		print("\n\n\nUnexpected error:", sys.exc_info()[0], "\n\n\n")
		time.sleep(2)

def do_test_sql():
	try:
		dataBaseFile = input('Type a name file to the database without the ".sql": ')
		ledgerTuple = ledgerO.generateRandomLedger()
		ledgerSum = ledgerO.sumLedgerValues(ledgerTuple)
		chartUnpopuled = ledgerO.generateChartFromLedgerSum(ledgerSum)
		sqlO.createSql(filedir, dataBaseFile + ".sql")
		sqlO.insertSql(ledgerTuple, chartUnpopuled, filedir, dataBaseFile + ".sql")
	except:
		print("\n\n\nUnexpected error:", sys.exc_info()[0], "\n\n\n")
		time.sleep(2)

def do_test():
	try:
		while True:
			print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
			print("                                           Test Menu:\n")
			print("Type 1 to create to create a random test and save in xlsx format")
			print("Type 2 to create to create a random test and save in sql database")
			print("Type any bottom not listed to back to main menu")
			print("\n\n#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
			command = input("Digite o comando desejado: ")
			if(command not in acceptCommandsTest):
				break
			else:
				acceptCommandsTest[command]()
	except:
		print("\n\n\nUnexpected error:", sys.exc_info()[0], "\n\n\n")
		time.sleep(2)

# end test scope

def do_exit():
    exit()

acceptCommandsXlsx = {
	"1": do_populate_xlsx,
}

acceptCommandsSql = {
	"1": do_populate_sql,
	"2": do_reader_sql,
}

acceptCommandsTest = {
	"1": do_test_xlsx,
	"2": do_test_sql,
}

acceptCommands = {
	"1": do_xlsx,
	"2": do_sql,
	"3": do_test,
	"4": do_exit
}

def run():
	try:
		print("Welcome to Ledger Processing Program!!!\n")
		while True:
			print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
			print("                                           Main Menu:\n")
			print("Type 1 to process through an xlsx")
			print("Type 2 to process through an sql")
			print("Type 3 to generate a test")
			print("Type 4 to exit")
			print("\n\n#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
			command = input("Digite o comando desejado: ")
			if(command not in acceptCommands):
				print("\n\n\nComando não encontrado!\n\n\n")
				time.sleep(2)
			else:
				acceptCommands[command]()
	except KeyboardInterrupt:
		exit()
	except:
		print("\n\n\nUnexpected error:", sys.exc_info()[0], "\n\n\n")
		time.sleep(2)


if __name__ == '__main__':
	run()
