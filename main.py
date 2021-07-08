import mariadb 

conn = mariadb.connect(
    user="root",
    password="root",
    host="localhost",
    port=3306,
    database="agenda")
cur = conn.cursor() 

cur.execute("SELECT * FROM usuario") 

for id,nome,telefone in cur: 
    print(f"Id: {id}, Nome: {nome}, Telefone: {telefone}")    
conn.close()
