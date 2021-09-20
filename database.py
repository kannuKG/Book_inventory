import sqlite3

def connect():
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("create table if not exists book (id integer PRIMARY KEY, title text, author text, year integer,isbn integer)")
    con.commit()
    con.close()

def insert(title,author,year,isbn):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("insert into book values(NULL,?,?,?,?)",(title,author,year,isbn))
    con.commit()
    con.close()

def view():
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("select * from book")
    rows=cur.fetchall()
    con.close()
    return rows

def search(title="",author="",year="",isbn=""):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("select * from book where title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    con.close()
    return rows

def delete(id):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("delete from book where id=?",(id,))
    rows=cur.fetchall()
    con.close()
    
connect()
insert("the sea","KG",1920,133254657)
delete(3)
print(view())
#print(search(author="KG"))