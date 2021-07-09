import random

class ledgerFunctions:

	def generateRandomLedger(self, quantity = 300, limitAccount = 50, limitComma = 5, limitValue = 10000):
		ledgerTuple = ()
		for i in range(quantity):
			account = (str)(random.randint(1, limitAccount + (limitAccount == 0)))
			for j in range(limitComma):
				if(not bool(random.randint(0, 3))):
					break;
				account = account + "." + (str)(random.randint(1, limitAccount + (limitAccount == 0)))
			value = round((random.randint(0, limitValue)) * 0.01, 2)
			ledgerTuple = ledgerTuple + ((account, value), )
		return ledgerTuple

	def generateChartFromLedgerTuple(self, ledgerTuple):
		accountList = [entry[0] for entry in ledgerTuple]
		chartUnpopuled = list(set(accountList))
		chartUnpopuled.sort()
		return chartUnpopuled

	def sumLedgerValues(self, ledgerTuple):
		ledgerSum = {}
		for element in ledgerTuple:
			key = element[0]
			value = element[1]
			if key in ledgerSum:
				ledgerSum[key] = ledgerSum[key] + value
			else:
				ledgerSum[key] = value
			k = key.rfind(".")
			while(k > 0):
				ancestor = key[:k]
				if ancestor in ledgerSum:
					ledgerSum[ancestor] = ledgerSum[ancestor] + value
				else:
					ledgerSum[ancestor] = value
				k = ancestor.rfind(".")
		return ledgerSum