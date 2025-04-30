import sqlite3

def create_table():
    # Create the table with a constraint to reject negative amounts in SQLite
    conn = sqlite3.connect('data/budget.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            description TEXT NOT NULL,
            amount REAL NOT NULL CHECK (amount > 0)   )
    ''')
    print("Table 'transactions' created successfully or already exists.")
    conn.commit()
    conn.close()


def insert_transactions():
    date = input('Enter date (YY,MM,DD): ').strip()
    if not date:
       print('Enter valid date')
       return
   
    description=input('Enter description: ').split()
    if len(description) == 0 :
        print('Description cannot be empty')
        return
    amount = input('Enter amount: ')
    if not amount: 
        print("Amount can't be empty")
    try :
        amount = float(amount)
        if amount<=0:
            print("Amount can't be negative")
            return
    except ValueError:
        print('Please enter valid amount')
        return

    conn = sqlite3.connect('data/budget.db')
    cursor = conn.cursor()
    cursor.execute('''
                   INSERT INTO transactions(date,description,amount)
                   VALUES(?,?,?)''',
                   (date,description,amount))
    conn.commit()
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

def delete_transaction():
    
    transaction_id=input('Enter the tranasction_id: ').strip()
    print (transaction_id)
    if not transaction_id.isdigit():
        print('Please enter valid id')
        return
    conn = sqlite3.connect('data/budget.db')
    cursor = conn.cursor()
    cursor.execute(' DELETE FROM transactions WHERE id =?' , (transaction_id))
    if cursor.rowcount == 0:
        print('No transaction found with that ID.')
    else:
        print('Transaction is deleted')
    conn.commit()
    conn.close()
    




def main():

    print('Welcome to the budget tracker')
    #create the table
    create_table()

    while True:
        print('Please choose from following options:')
        print('1. Add a transaction')
        print('2. View transactions')
        print('3. Delete transactions')
        print('4. Exit')
    
        choice = input('Enter your choice : (1/2/3/4)').strip()   
        if choice == '1':
            insert_transactions()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            delete_transaction()
        elif choice == '4':
            print("Good Bye!")
            break

        else:
            print('Invalid choice, please try again ')
   
 

if __name__ == '__main__':
    main()