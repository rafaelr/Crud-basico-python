
from config.database import mydb

cursor = mydb.cursor()

def insert_data(nome=None, acronimo=None):
    sql = "INSERT INTO instituto (nome, acronimo) VALUES (%s, %s)"
    val = (nome, acronimo)
    cursor.execute(sql, val)
    mydb.commit()


def read():
    cursor.execute("SELECT * FROM instituto")
    myresult = cursor.fetchall()
    result = []
    for x in myresult:
        result.append(x)
    return result

def delete(id):
    cursor.execute("DELETE FROM instituto WHERE id = " + str(id))
    mydb.commit()