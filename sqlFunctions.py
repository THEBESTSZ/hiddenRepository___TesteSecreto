import pandas as pd
import sqlite3
import os
import sys
import time

class sqlFunctions:

	# Função para criar o arquivo sql com a tabela general_ledger e a tabela chart_of_accounts (chart não-populado)
	
	def createSql(self, filedir, nameData): 
		try:
			base = sqlite3.connect(os.path.join(filedir, "sql", nameData))
			cursor = base.cursor()
			cursor.execute("CREATE TABLE general_ledger(account TEXT, value FLOAT)")
			cursor.execute("CREATE TABLE chart_of_accounts(account TEXT)")
			base.commit()
			print('\n\n\nSuccess!!! the file was saved with the name: "'+ nameData+'" in the "sql" folder\n\n\n')
		except sqlite3.Error as e:
			print("\n\n\nSQL error: SQL archive", nameData, "already exists\n\n\n")
			print("\n\n\nReplace the archive and reset data? Type yes or no (by typing no, new data will be inserted into the existing table ):", end = '', flush = True)
			repeat = True
			while(repeat):
				try:
					decison = input()
					if(decison == "yes"):
						repeat = False
						cursor.close()
						base.close()
						os.remove(os.path.join(filedir, "sql", nameData))
						self.createSql(filedir, nameData)
						print("Replaced with sucess!!!\n\n\n")
					elif(decison == "no"):
						repeat = False
					else:
						print("\n\n\nType only yes or no:", end = '', flush = True)
				except OSError as e:
					print("\n\n\nOS error: {0}".format(e), "\n\n\n")
				except:
					print("\n\n\nUnexpected error:", sys.exc_info()[0], "\n\n\n")
		except PermissionError:
			print("\n\n\nYou don't seem to have the rights to do that or the file is open")
		except OSError as e:
			print("\n\n\nOS error: {0}".format(e), "\n\n\n")
		except:
			print("\n\n\nUnexpected error:", sys.exc_info()[0], "\n\n\n")
		finally:
			time.sleep(2)

	# Função para ler os tabelas general_ledger e chart_of_accounts, retornando ambas em formato de tupla

	def readerSql(self, filedir, nameData): 
		try:
			base = sqlite3.connect(os.path.join(filedir, "sql", nameData))
			cursor = base.cursor()

			cursor.execute("SELECT * FROM general_ledger")
			ledgerTuple = cursor.fetchall()

			cursor.execute("SELECT DISTINCT account FROM chart_of_accounts")
			chartUnpopuled = cursor.fetchall()
			cursor.close()
			base.close()
			return ledgerTuple, chartUnpopuled
		except sqlite3.Error as e:
			print("\n\n\nSQL error:", e, "\n\n\n")
			time.sleep(2)
		except PermissionError:
			print("\n\n\nYou don't seem to have the rights to do that or the file is open")
			time.sleep(2)
		except OSError as e:
			print("\n\n\nOS error: {0}".format(e), "\n\n\n")
			time.sleep(2)
		except:
			print("\n\n\nUnexpected error:", sys.exc_info()[0], "\n\n\n")
			time.sleep(2)

	# Função para inserir valores em ambas as tabelas, general_ledger e chart_of_accounts, no arquivo de formato sql informado. O arquivo sql deve estar na pasta sql

	def insertSql(self, ledgerTuple, chartUnpopuled, filedir, nameData):
		try:
			base = sqlite3.connect(os.path.join(filedir, "sql", nameData))
			cursor = base.cursor()
			cursor.executemany("INSERT INTO general_ledger (account, value) VALUES (?, ?)", list(ledgerTuple))
			cursor.executemany("INSERT INTO chart_of_accounts (account) VALUES (?)", list(zip(*[iter(chartUnpopuled)]*1)))
			base.commit()

			cursor.close()
			base.close()
		except sqlite3.Error as e:
			print("\n\n\nSQL error:", e, "\n\n\n")
			time.sleep(2)
		except PermissionError:
			print("\n\n\nYou don't seem to have the rights to do that or the file is open")
			time.sleep(2)
		except OSError as e:
			print("\n\n\nOS error: {0}".format(e), "\n\n\n")
			time.sleep(2)
		except:
			print("\n\n\nUnexpected error:", sys.exc_info()[0], "\n\n\n")
			time.sleep(2)

	# Função para verificar se as contas da tabela chart não-populado condiz com as contas encontradas no general_ledger em formato de dicionário
	# Caso seja, a função para salvar na pasta output é chamada (chartReturnXlsx)

	def verifyChartSql(self, chartUnpopuled, chartPopuled, filedir, filename):
		try:
			if(set(*(map(set, zip(*chartUnpopuled)))) == set(chartPopuled.keys())):
				self.chartReturnXlsx(chartPopuled, filedir, filename + ".xlsx")
				print('\n\n\nSuccess!!! the file was saved with the name: "'+ filename + '.xlsx" in the "output" folder\n\n\n')
			else:
				print('\n\n\nThe column "chart_of_accounts" does not match with the column "general_ledger"\n\n\n')
		except:
			print("\n\n\nUnexpected error:", sys.exc_info()[0], "\n\n\n")
		finally:
			time.sleep(2)

	# Função para salvar na pasta output em formato xlsx

	def chartReturnXlsx(self, chartVerified, filedir, filename):
		try:
			df = pd.DataFrame(chartVerified.items(), columns=['account', 'value']).sort_values(by = 'account').round(2)
			if not os.path.exists(os.path.join(filedir, "output")):
				os.makedirs(os.path.join(filedir, "output"))
			with pd.ExcelWriter(os.path.join(filedir, "output", filename)) as writer:
				df.to_excel(writer, sheet_name="Sheet1", index=False)
		except PermissionError:
			print("\n\n\nYou don't seem to have the rights to do that or the file is open")
			time.sleep(2)
		except OSError as e:
			print("\n\n\nOS error: {0}".format(e), "\n\n\n")
			time.sleep(2)
		except:
			print("\n\n\nUnexpected error:", sys.exc_info()[0], "\n\n\n")
			time.sleep(2)
			