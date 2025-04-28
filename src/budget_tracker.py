import sqlite3
def create_table():
    conn = sqlite3.connect('data/budget.db')
    cursor= conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTs transactions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            description TEXT NOT NULL,
            amount REAL NOT NULL            
        )
    ''')
    print("Table 'transactions' created successfully or already exists.")
    conn.commit()
    conn.close()

def insert_transactions(date,description,amount):
    conn = sqlite3.connect('data/budget.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (date, description, amount)
        VALUES (?,?,?)
    ''', 
        (date, description,amount))
    conn.commit()
    print('Transaction added successfully')
    conn.close()


def view_transactions():
    conn = sqlite3.connect('data/budget.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions')
    transactions = cursor.fetchall()
    if transactions:
        for transaction in transactions:
            print (transaction)
    else:
        print('no transaction found')
    conn.close()
    
def main():

    print('Welcome to the budget tracker')

    #create the table
    create_table()

    #ask user for the input
    date= input ('Enter the date (YY, MM, DD)')
    description = input ('Enter a description')
    amount = input('Enter the amount')

    insert_transactions(date,description,amount)

    view_transactions()

if __name__ == '__main__':
    main()