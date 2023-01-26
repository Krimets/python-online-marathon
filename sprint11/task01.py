import sqlite3


class TaskDb:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connection(self):
        self.conn = sqlite3.connect('q1.db')
        self.cursor = self.conn.cursor()

    def end_connection(self):
        self.cursor.close()
        self.conn.close()

    def show(self):
        try:
            self.connection()
            self.cursor.execute("""SELECT * FROM customers WHERE grade > 200 ORDER BY id""")
            total_rows = self.cursor.fetchall()
            print(f"""Connected to SQLite
Total rows are:   {len(total_rows)}
Printing each row""")
            for row in total_rows:
                print(f"""Id:  {row[0]}
Name:  {row[1]}
City:  {row[2]}
Grade:  {row[3]}
Seller:  {row[4]}

""")
            print('The SQLite connection is closed')
        except sqlite3.Error as e:
            print(f'Error: {e}')
        finally:
            self.end_connection()


my_db_class = TaskDb()
my_db_class.show()
