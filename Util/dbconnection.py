import mysql.connector as sql
class Connect:
    def __init__(self):
        self.conn = None
        self.stmt = None
    def dbconnect(self):
        host = input("Enter host: ")
        user = input("Enter user: ")
        database = input("Enter database name: ")
        password = input("Enter password: ")

        try:
            self.conn = sql.connect(host=host, database=database, user=user, password=password)
            if self.conn.is_connected():
                self.stmt = self.conn.cursor()
                print("Database is connected")



        except Exception as e:
            print("Error:", e)
            self.stmt=None

    def perform_database_operation(self, query, data=None):
        try:
            if not self.stmt:
                raise Exception("No database connection established.")

            if data:
                # If data is provided, assume executemany
                self.stmt.executemany(query, data)
            else:
                if query.lower().startswith("select"):
                    self.stmt.execute(query)
                    results=self.stmt.fetchall()
                    return results
                else:
                    self.stmt.execute(query)
                    self.stmt.fetchall()

            self.conn.commit()

        except Exception as e:
            print("Error during database operation:", e)
mdb=Connect()
mdb.dbconnect()
