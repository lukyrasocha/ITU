import math

def calculate_balance(transactions):
	balance = 0
	for i in transactions:
		balance = balance + i

	return balance

def calculate_compound(account_balance, rate, years):
	compound_balance = account_balance*((rate + 1)**years)

	return round(compound_balance,2)

def filter_withdrawals(transactions):
	myList = []
	for i in transactions:
		if i < 0:
			myList.append(i)

	return myList

def risk_analysis(transactions):
	

	return min(transactions)

def join_records(names, transactions):
	myList = []
	if len(names) == len(transactions):
		for i in range(len(names)):
			myList.append((names[i],transactions[i]))
	else:
		print("Error, names and transactions need to have the same size")


	return myList

def unique_deposit_names(joined_transactions):
	myList = []
	for i in joined_transactions:
		if i[0].islower() and i[1] > 0:
			myList.append(i[0])

	return myList

def main():
	#calculate balance example
	transactions = [100 , 5000 , -30, -1200]
	balance = calculate_balance(transactions)
	print(balance) #Expected output: 3870

	#calculate compound example
	compound_balance = calculate_compound(500 , 0.05 , 25)
	print(compound_balance) #Expected outuput: 1693.17[...]

	#filter withdrawals example
	withdrawals = filter_withdrawals(transactions)
	print(withdrawals) #Expected outuput: [-30, -1200]

	#risk analysis example 
	transactions = [-5000, 200, 120, -99999] 
	risk = risk_analysis(transactions)
	print(risk)#Expected outuput: -99999

	#join records example
	names = ['Muhammed', 'emma', 'Emma', 'julie']
	joined_transactions = join_records(names, transactions)
	print(joined_transactions)#Expected outuput: [( ’Muhammed’ , −5000), ( ’emma’ , 200), ( ’Emma’ , 120), ( ’ julie ’ , −99999)]

	#unique deposit names example
	unique_names = unique_deposit_names(joined_transactions)
	print(unique_names) #Expected outuput: ['emma']


if __name__ == "__main__":
	# execute only if run as a script
	main()
	#Expected output:
	#3870
	#1693.17[...]
	#-99999
	#[( ’Muhammed’ , −5000), ( ’emma’ , 200), ( ’Emma’ , 120), ( ’ julie ’ , −99999)]
	#['emma']


	

