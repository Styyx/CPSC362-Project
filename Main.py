import mysql.connector
from mysql.connector import Error
try:
    conn = mysql.connector.connect(host='127.0.0.1',
                             database='test',
                             user='root',
                             password='123')
    if conn.is_connected():
        db_Info = conn.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ",db_Info)
   
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print ("You're connected to - ", record)
        
        mycursor = conn.cursor();
        
        #Adding to Student
        mycursor.execute("INSERT INTO Students (studentID, studentName, checkoutBook) VALUES (0001, 'Steven Alvarez', FALSE)")

        #Displaying Students
        mycursor.execute("SELECT * FROM Students")
        
        myresult = mycursor.fetchall()        
        
        for x in myresult:
            print(x)        
        
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(conn.is_connected()):
        cursor.close()
        conn.close()
        print("MySQL connection is closed")