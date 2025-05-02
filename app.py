from flask import Flask ,request, render_template, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/')
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

@app.route('/insert_transaction' , methods = ['POST'] )
def insert_transactions():
    date = request.form['date']
    description = request.form['description']
    amount = request.form['amount']
    if amount:
        amount = float(amount)
    
    if not date or not description or not amount:
        return ("Please enter all the fields")
    try:
        if amount <=0:
            return("Enter valid amount")
    except ValueError:
        return('Please enter valid amount')

    else:
        conn = sqlite3.connect('data/budget.db')
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO transactions(date,description,amount)
                    VALUES(?,?,?)''',
                    (date,description,amount))
        
        conn.commit()
        conn.close()
        return ('Transaction added successfully')

@app.route('/view_transactions', methods = ['GET'])
def transactions():
    conn=sqlite3.connect('data/budget.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions')
    transactions = cursor.fetchall()
    conn.close()
    return render_template('transaction.html', transactions=transactions)


@app.route('/delete_transaction', methods = ['POST'])
def delete_transaction():
    conn = sqlite3.connect('data/budget.db')
    cursor = conn.cursor()
    delete_id = request.form['id']
    cursor.execute('DELETE from transactions WHERE id = ?', (delete_id,))
    conn.commit()
    conn.close()
    return redirect('/view_transactions')

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
