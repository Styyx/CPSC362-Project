import tkinter
from tkinter import Entry

def stuLoginPg():
    stuLoginPgBtn.pack_forget()
    teaLoginPgBtn.pack_forget()
    adminLoginPgBtn.pack_forget()
    regAccPgBtn.pack_forget()
    emaillabel.pack()
    email.pack()
    passwordlabel.pack()
    password.pack()
    stuLoginBtn.pack()
    stuCancelBtn.pack()

def teaLoginPg():
    stuLoginPgBtn.pack_forget()
    teaLoginPgBtn.pack_forget()
    adminLoginPgBtn.pack_forget()
    regAccPgBtn.pack_forget()
    emaillabel.pack()
    email.pack()
    passwordlabel.pack()
    password.pack()
    teaLoginBtn.pack()
    teaCancelBtn.pack()

def adminLoginPg():
    stuLoginPgBtn.pack_forget()
    teaLoginPgBtn.pack_forget()
    adminLoginPgBtn.pack_forget()
    regAccPgBtn.pack_forget()
    emaillabel.pack()
    email.pack()
    passwordlabel.pack()
    password.pack()
    adminLoginBtn.pack()
    adminCancelBtn.pack()

def regAccPg():
    stuLoginPgBtn.pack_forget()
    teaLoginPgBtn.pack_forget()
    adminLoginPgBtn.pack_forget()
    regAccPgBtn.pack_forget()
    emaillabel.pack()
    email.pack()
    passwordlabel.pack()
    password.pack()
    cPasswordLabel.pack()
    cPassword.pack()
    regStuBtn.pack()
    regTeaBtn.pack()
    regAdminBtn.pack()
    regAccCancelBtn.pack()
    

def stuCancel():
    emaillabel.pack_forget()
    email.pack_forget()
    passwordlabel.pack_forget()
    password.pack_forget()
    stuLoginBtn.pack_forget()
    stuCancelBtn.pack_forget()
    stuLoginPgBtn.pack()
    teaLoginPgBtn.pack()
    adminLoginPgBtn.pack()
    regAccPgBtn.pack()

def teaCancel():
    emaillabel.pack_forget()
    email.pack_forget()
    passwordlabel.pack_forget()
    password.pack_forget()
    teaLoginBtn.pack_forget()
    teaCancelBtn.pack_forget()
    stuLoginPgBtn.pack()
    teaLoginPgBtn.pack()
    adminLoginPgBtn.pack()
    regAccPgBtn.pack()

def adminCancel():
    emaillabel.pack_forget()
    email.pack_forget()
    passwordlabel.pack_forget()
    password.pack_forget()
    adminLoginBtn.pack_forget()
    adminCancelBtn.pack_forget()
    stuLoginPgBtn.pack()
    teaLoginPgBtn.pack()
    adminLoginPgBtn.pack()
    regAccPgBtn.pack()

def regAccCancel():
    emaillabel.pack_forget()
    email.pack_forget()
    passwordlabel.pack_forget()
    password.pack_forget()
    cPasswordLabel.pack_forget()
    cPassword.pack_forget()
    regStuBtn.pack_forget()
    regTeaBtn.pack_forget()
    regAdminBtn.pack_forget()
    regAccCancelBtn.pack_forget()
    stuLoginPgBtn.pack()
    teaLoginPgBtn.pack()
    adminLoginPgBtn.pack()
    regAccPgBtn.pack()

def stuLogin():
    emaillabel.pack_forget()
    email.pack_forget()
    passwordlabel.pack_forget()
    password.pack_forget()
    stuLoginBtn.pack_forget()
    stuCancelBtn.pack_forget()
    stuPg.pack()
    stuLogoutBtn.pack()

def teaLogin():
    emaillabel.pack_forget()
    email.pack_forget()
    passwordlabel.pack_forget()
    password.pack_forget()
    teaLoginBtn.pack_forget()
    teaCancelBtn.pack_forget()
    teaPg.pack()
    teaLogoutBtn.pack()

def adminLogin():
    emaillabel.pack_forget()
    email.pack_forget()
    passwordlabel.pack_forget()
    password.pack_forget()
    adminLoginBtn.pack_forget()
    adminCancelBtn.pack_forget()
    adminPg.pack()
    adminLogoutBtn.pack()

def stuLogout():
    stuPg.pack_forget()
    stuLogoutBtn.pack_forget()
    emaillabel.pack()
    email.pack()
    passwordlabel.pack()
    password.pack()
    stuLoginBtn.pack()
    stuCancelBtn.pack()

def teaLogout():
    teaPg.pack_forget()
    teaLogoutBtn.pack_forget()
    emaillabel.pack()
    email.pack()
    passwordlabel.pack()
    password.pack()
    teaLoginBtn.pack()
    teaCancelBtn.pack()

def adminLogout():
    adminPg.pack_forget()
    adminLogoutBtn.pack_forget()
    emaillabel.pack()
    email.pack()
    passwordlabel.pack()
    password.pack()
    adminLoginBtn.pack()
    adminCancelBtn.pack()
    

window = tkinter.Tk()

#the following buttons need logic assigned to them, stuLoginBtn, teaLoginBtn, regStuBtn, and regTeaBtn

stuLoginPgBtn = tkinter.Button(window, text="Student Login", command=stuLoginPg)
teaLoginPgBtn = tkinter.Button(window, text="Teacher Login", command=teaLoginPg)
adminLoginPgBtn = tkinter.Button(window, text="Admin Login", command=adminLoginPg)
regAccPgBtn = tkinter.Button(window, text="Register an Account", command=regAccPg)

stuLoginBtn = tkinter.Button(window, text="Login", command=stuLogin)
teaLoginBtn = tkinter.Button(window, text="Login", command=teaLogin)
adminLoginBtn = tkinter.Button(window, text="Login", command=adminLogin)

stuLogoutBtn = tkinter.Button(window, text="Logout", command=stuLogout)
teaLogoutBtn = tkinter.Button(window, text="Logout", command=teaLogout)
adminLogoutBtn = tkinter.Button(window, text="Logout", command=adminLogout)

stuCancelBtn = tkinter.Button(window, text="Cancel", command=stuCancel)
teaCancelBtn = tkinter.Button(window, text="Cancel", command=teaCancel)
adminCancelBtn = tkinter.Button(window, text="Cancel", command=adminCancel)
regAccCancelBtn = tkinter.Button(window, text="Cancel", command=regAccCancel)

regStuBtn = tkinter.Button(window, text="Register as Student") 
regTeaBtn = tkinter.Button(window, text="Register as Teacher")
regAdminBtn =tkinter.Button(window, text="Register as Admin")


email = Entry(window)
emaillabel = tkinter.Label(window, text="Email:")
password = Entry(window)
passwordlabel = tkinter.Label(window, text="Password:")
cPassword = Entry(window)
cPasswordLabel = tkinter.Label(window, text="Confirm Password:")

stuPg = tkinter.Label(window, text="Welcome to the student page. (This is a placeholder)")
teaPg = tkinter.Label(window, text="Welcome to the teacher page. (This is a placeholder)")
adminPg = tkinter.Label(window, text="Welcome to the admin page. (This is a placeholder)")

stuLoginPgBtn.pack()
teaLoginPgBtn.pack()
adminLoginPgBtn.pack()
regAccPgBtn.pack()
