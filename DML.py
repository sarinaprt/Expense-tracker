from mysql.connector import connection , Error

def datebase_exist(DATABASE):
    try:
        config={"user":"root","host":"localhost","password":"belive_god1527"}
        conn=connection.MySQLConnection(**config)
        cur=conn.cursor()
        cur.execute(F"DROP DATABASE IF EXISTS {DATABASE}")
        cur.execute(f"CREATE DATABASE {DATABASE}")
        conn.commit()
        cur.close()
        conn.close()
    except:
        print("database (drop or create ) faild")
def users():
    config={'user':'root','host':'localhost','password':'belive_god1527','database':'Expense_tracker'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE USERS(
                USERID     INT AUTO_INCREMENT PRIMARY KEY,
                USERNAME   VARCHAR(100) NOT NULL UNIQUE,
                EMAIL      VARCHAR(150) UNIQUE,
                PASSWORD   VARBINARY(50) NOT NULL UNIQUE,
                CREAT_AT   DATETIME DEFAULT CURRENT_TIMESTAMP,
                LAST_ACTIV DATETIME DEFAULT CURRENT_TIMESTAMP           
    )""")


if __name__=="__main__":
    DATABASE="Expense_tracker"
    datebase_exist(DATABASE)
    users()
