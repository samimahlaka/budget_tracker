from flask import Flask ,request, render_template, redirect, url_for, flash
import sqlite3
from forms import transactionForm

app = Flask(__name__)
app.secret_key = 'dev123'

@app.route('/')
def home():
    form = transactionForm()
    return render_template('home.html', form=form)


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

@app.route('/insert_transaction', methods=['POST'])
def insert_transactions():
    form = transactionForm()
    if form.validate_on_submit():
        date = form.date.data
        description = form.description.data
        amount = form.amount.data
        
        conn = sqlite3.connect('data/budget.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO transactions(date,description,amount)
                   VALUES(?,?,?)''', (date,description,amount))
        conn.commit()
        conn.close()
        
        flash("Transaction added successfully")
        return redirect('/view_transactions')
    else:
        return render_template('home.html', form=form)
    

@app.route('/view_transactions', methods = ['GET'])
def transactions():
    conn=sqlite3.connect('data/budget.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions')
    transactions = cursor.fetchall()
    conn.close()
    total_spending =float(0)
    try:
        for x in transactions:
            total_spending = total_spending + float(x[3])
    except ValueError:
        pass
    
    return render_template('transaction.html', transactions=transactions, Total_Amount = total_spending)


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
