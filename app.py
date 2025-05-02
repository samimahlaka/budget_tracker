from flask import Flask ,request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

def create_table():
    conn= sqlite3.connect('data/budget.db')
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    description TEXT NOT NULL,
                    amount REAL NOT NULL CHECK (amount > 0)   )
                   ''')
    conn.commit()
    conn.close()

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    date = request.form['date']
    description = request.form['description']
    amount = request.form['amount']

    print (f'Date : {date}, Description: {description}, Amount: {amount}')

    conn = sqlite3.connect('data/budget.db')
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO transactions(date,description,amount)
                   VALUES(?,?,?)''',
                   (date,description,amount))
    
    conn.commit()
    conn.close()

    return ('Transaction added successfully')

@app.route('/transactions', methods = ['GET'])
def transactions():
    conn=sqlite3.connect('data/budget.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions')
    transactions = cursor.fetchall()
    conn.close()
    return render_template('transaction.html', transactions=transactions)



if __name__ == '__main__':
    create_table()
    app.run(debug=True)
