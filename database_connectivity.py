import mysql.connector

def updatevalue(email,phone_number,feedback):

    mydb = mysql.connector.connect(host="localhost",port="3306",user="root",password="Icarius01",database="rasa")
    cursor = mydb.cursor()

    sql='insert into userinfo (id,email,phone_numnber,feedback) values(2,"{0}","{1}","{2}");'.format(email,phone_number,feedback)
    cursor.execute(sql)
    mydb.commit()