import csv
import psycopg2

keywords= {
    'atm': ['atm ', 'atm withdrawal'],
    'gas': ['speedway', 'exxon', 'chevron', 'shell', 'gas', 'petroleum', 'arco', ' 76 ', 'safeway fuel', 'valero'],
    'grocery': ['sprouts', 'glacier', 'walmart' 'grocery', 'groceries', 'safeway', 'wal-mart', 'costco'],
    'business': ['apple.com', 'amazon', 'homedepot', 'itunes', 'ebay', 'home depot', 'amzn.com'],
    'car': ['volkswagen', 'statefarm', 'ally', 'geico']
}

def sort_transactions():
    global transactions
    transactions = {'atm': atm, 'gas': gas, 'groceries': groceries, 'car': car, 'business': business, 'misc': misc, 'income': income}

    with open('checking1.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for transaction in csv_reader:
            transaction.pop(2)
            transaction.pop(2)
            statement = transaction[2].lower()
            amount = transaction[1].lower()
            status = 'unused'
            transaction[1] = float(transaction[1])
            amount = transaction[1]

            if amount > 0:
                transactions['income'].append(transaction)
            else:    
                for kw in keywords['atm']:
                    if kw in statement:
                        transactions['atm'].append(transaction)
                        status='used'
                    else:
                        for kw in keywords['gas']:
                            if kw in statement:
                                transactions['gas'].append(transaction)
                                status='used'
                            else:
                                for kw in keywords['grocery']:
                                    if kw in statement:
                                        transactions['groceries'].append(transaction)
                                        status='used'
                                    else:
                                        for kw in keywords['car']:
                                            if kw in statement:
                                                transactions['car'].append(transaction)
                                                status='used'              
                                            else:
                                                for kw in keywords['business']:
                                                    if kw in statement:
                                                        transactions['business'].append(transaction)
                                                        status='used'

            for transaction in transactions['income']:
                if 'OVERDRAFT' in transaction[2]:
                    transactions['income'].remove(transaction)
                if 'PURCHASE RETURN AUTHORIZED' in transaction[2]:
                    transactions['income'].remove(transaction)

            if status=='unused':
                misc.append(transaction)
            
    del atm, gas, groceries, car, business, misc, income

def get_category_id(category_name):
    connection = psycopg2.connect(user="postgres",
                                    password=r"",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="finance_tracker")
    cursor = connection.cursor()
    query = "SELECT exp_cat_id FROM expense_category WHERE exp_cat_name = " + "'" + name + "'"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

def insert_expenses():
    connection = psycopg2.connect(user="postgres",
                                    password=r"",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="finance_tracker")
    cursor = connection.cursor()
    
    for key, value in transactions.items():
        for transaction in value:
            query = "INSERT INTO expense (exp_cat_id, exp_statement, exp_amount, exp_datetime) VALUES(" + str(get_category_id(key)[0]) + ",'" + str(transaction[2]) + "'," + str(transaction[1]) + ",'" + str(transaction[0]) + "')"
            cursor.execute(query)
            connection.commit()

    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

insert_expenses()



