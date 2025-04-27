import sqlite3


def main():
    print('Welcome to the budget tracker')

    conn = sqlite3.connect('data/budget.db')
    cursor = conn.cursor()
    conn.close()

    
if __name__ == 'main':
    main()