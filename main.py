import csv

atm = []
gas = []
groceries = []
car = [] 
business = []
misc = []
income = [] 

atm_keywords = ['atm ', 'atm withdrawal']
gas_keywords = ['speedway', 'exxon', 'chevron', 'shell', 'gas', 'petroleum', 'arco', ' 76 ', 'safeway fuel']
grocery_keywords = ['sprouts', 'glacier', 'walmart' 'grocery', 'groceries', 'safeway', 'wal-mart', 'costco']
car_keywords = ['volkswagen', 'statefarm', 'ally']
business_keywords = ['apple.com', 'amazon', 'homedepot', 'itunes', 'ebay', 'home depot', 'amzn.com']

with open('checking1.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for transaction in csv_reader:
        transaction.pop(2)
        transaction.pop(2)
        statement = transaction[2].lower()
        amount = transaction[1].lower()
        status='unused'
        transaction[1] = float(transaction[1])
        amount = transaction[1]

        if amount > 0:
            income.append(transaction)
        else:    
            for kw in atm_keywords:
                if kw in statement:
                    atm.append(transaction)
                    status='used'
                else:
                    for kw in gas_keywords:
                        if kw in statement:
                            gas.append(transaction)
                            status='used'
                        else:
                            for kw in grocery_keywords:
                                if kw in statement:
                                    groceries.append(transaction)
                                    status='used'
                                else:
                                    for kw in car_keywords:
                                        if kw in statement:
                                            car.append(transaction)
                                            status='used'              
                                        else:
                                            for kw in business_keywords:
                                                if kw in statement:
                                                    business.append(transaction)
                                                    status='used'

            for transaction in income:
                if 'OVERDRAFT' in transaction[2]:
                    income.remove(transaction)
                if 'PURCHASE RETURN AUTHORIZED' in transaction[2]:
                    income.remove(transaction)

            if status=='unused':
                misc.append(transaction)

print(income)