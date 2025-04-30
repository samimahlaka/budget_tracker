from flask import Flask ,request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_transaction')
def insert_transactio():
    date = request.form['date']
    description = request.form['description']
    amount = request.form['amount']

    print (f'Date : {date}, Description: {description}, Amount: {amount}')

    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO transactions (date, description, amount) VALUES (?,?,?)' , 
                   (date, description, amount) )
    
    conn.commit()
    conn.close()

    return ('Transaction added successfully')

if __name__ == '__main__':
    app.run(debug=True)
