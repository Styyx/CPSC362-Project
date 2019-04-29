import mysql.connector
from mysql.connector import Error
from tkinter import Tk, Label, Entry, Button, E, W
from tkinter import *
   
class logscreen:
    
    def __init__(self, master):
        
        self.master = master
        master.title("Books Advantage Web App")

        self.title = Label(master, text="Welcome to Books Advantage! Please sign in.")
        
        #self.username = Entry(master)
        #self.text1 = Label(master, text="username")

        #self.password = Entry(master)
        #self.text2 = Label(master, text="password")
        
        self.student_login_button = Button(master, text="Student Login")
        self.teacher_login_button = Button(master, text="Teacher Login")
        self.account_register = Button(master, text="Register Account")

        self.title.grid(row=0, column=0, sticky=W)
        #self.text1.grid(row=1, column=0, sticky=W)
        #self.username.grid(row=1, column=1, sticky=E)
        #self.text2.grid(row=2, column=0, sticky=W)
        #self.password.grid(row=2, column=1, sticky=E)
        self.student_login_button.grid(row=3, column=0, sticky=W+E)
        self.teacher_login_button.grid(row=4, column=0, sticky=W+E)
        self.account_register.grid(row=5, column=0, sticky=W+E)
    
    def login(self):
        print("~")

class logscreen:
    
    def __init__(self, master):
        
        self.master = master
        master.title("Books Advantage Web App")

        self.title = Label(master, text="Welcome to Books Advantage! Please sign in.")
        
        #self.username = Entry(master)
        #self.text1 = Label(master, text="username")

        #self.password = Entry(master)
        #self.text2 = Label(master, text="password")
        
        self.student_login_button = Button(master, text="Student Login")
        self.teacher_login_button = Button(master, text="Teacher Login", command = self.new_window)
        self.account_register = Button(master, text="Register Account")

        self.title.grid(row=0, column=0, sticky=W)
        #self.text1.grid(row=1, column=0, sticky=W)
        #self.username.grid(row=1, column=1, sticky=E)
        #self.text2.grid(row=2, column=0, sticky=W)
        #self.password.grid(row=2, column=1, sticky=E)
        self.student_login_button.grid(row=3, column=0, sticky=W+E)
        self.teacher_login_button.grid(row=4, column=0, sticky=W+E)
        self.account_register.grid(row=5, column=0, sticky=W+E)
    
    def login(self):
        print("~") 

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.my_gui = teacherWindow(self.newWindow)

class teacherWindow:

    def __init__(self, master):
        username = StringVar()

        password = StringVar()
    


        Label(text = "Username * ").pack()

        Entry(textvariable = username)

        Label(text = "Password * ").pack()

        Entry(textvariable = password)


    
try:
    conn = mysql.connector.connect(host='127.0.0.1',
                             database='student',
                             user='root',
                             password='password')
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
        
global my_gui
root = Tk()
my_gui = logscreen(root)
root.mainloop()
