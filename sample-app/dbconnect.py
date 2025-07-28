import mysql.connector
def Get_Connect_To_Mysql():
    mydb = mysql.connector.connect(host="mysql", user="root", password="123456")
    return mydb

def Get_Connect_To_DatabaseMysql(dbname):
    mydb = mysql.connector.connect(host="mysql", user="root", password="123456", database = dbname)
    return mydb