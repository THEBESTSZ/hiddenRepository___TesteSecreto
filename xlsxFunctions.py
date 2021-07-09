import pandas as pd
import os
import random
import sys
import time

class xlsxFunctions:

	def readerXlsx(self, filedir, filename): 
		general_ledger = pd.read_excel(os.path.join(filedir, "input", filename))
		general_tuple = tuple(zip(general_ledger.account, general_ledger.value))
		return general_tuple

	def verifyChartXlsx(self, chartPopuled, filedir, filename):
		try:
			chart_accounts = pd.read_excel(os.path.join(filedir, "input", filename))
			list_accounts = list(chart_accounts.account)
			if(set(list_accounts) == set(chartPopuled.keys())):
				self.chartReturnXlsx(chartPopuled, filedir, filename)
			else:
				print('\n\n\nThe file "chart_accounts" does not match the file "ledger" passed\n\n\n')
		except PermissionError:
			print("\n\n\nYou don't seem to have the rights to do that or the file is open")
		except OSError as e:
			print("\n\n\nOS error: {0}".format(e))
		except:
			print("\n\n\nUnexpected error:", sys.exc_info()[0])
		finally:
			time.sleep(2)

	def chartReturnXlsx(self, chartVerified, filedir, filename):
		try:
			df = pd.DataFrame(chartVerified.items(), columns=['account', 'value']).sort_values(by = 'account').round(2)
			if not os.path.exists(os.path.join(filedir, "output")):
				os.makedirs(os.path.join(filedir, "output"))
			with pd.ExcelWriter(os.path.join(filedir, "output", filename)) as writer:
				df.to_excel(writer, sheet_name="Sheet1", index=False)
			print('\n\n\nSuccess!!! the file was saved with the name: "'+ filename+'" in the "output" folder\n\n\n')
		except PermissionError:
			print("\n\n\nYou don't seem to have the rights to do that or the file is open")
		except OSError as e:
			print("\n\n\nOS error: {0}".format(e))
		except:
			print("\n\n\nUnexpected error:", sys.exc_info()[0])
		finally:
			time.sleep(2)

	def saveLedgerTupleXlsx(self, ledgerTuple, filedir, filename):
		try:
			df = pd.DataFrame(list(ledgerTuple), columns=['account', 'value'])
			if not os.path.exists(os.path.join(filedir, "input")):
				os.makedirs(os.path.join(filedir, "input"))
			with pd.ExcelWriter(os.path.join(filedir, "input", filename)) as writer:
				df.to_excel(writer, sheet_name="Sheet1", index=False)
		except PermissionError:
			print("\n\n\nYou don't seem to have the rights to do that or the file is open")
		except OSError as e:
			print("\n\n\nOS error: {0}".format(e))
		except:
			print("\n\n\nUnexpected error:", sys.exc_info()[0])
		finally:
			time.sleep(2)

	def saveChartUnpopuledXlsx(self, chartUnpopuled, filedir, filename):
		try:
			df = pd.DataFrame(chartUnpopuled, columns=['account']).sort_values(by = 'account')
			if not os.path.exists(os.path.join(filedir, "input")):
				os.makedirs(os.path.join(filedir, "input"))
			with pd.ExcelWriter(os.path.join(filedir, "input", filename)) as writer:
				df.to_excel(writer, sheet_name="Sheet1", index=False)
		except PermissionError:
			print("\n\n\nYou don't seem to have the rights to do that or the file is open")
		except OSError as e:
			print("\n\n\nOS error: {0}".format(e))
		except:
			print("\n\n\nUnexpected error:", sys.exc_info()[0])
		finally:
			time.sleep(2)