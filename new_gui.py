import tkinter
from tkinter import Entry

def stuLoginPg():
    splash.pack_forget()
    stuLoginPgBtn.pack_forget()
    teaLoginPgBtn.pack_forget()
    adminLoginPgBtn.pack_forget()
    regAccPgBtn.pack_forget()
    studentSplash.pack()
    emaillabel.pack()
    email.pack()
    passwordlabel.pack()
    password.pack()
    stuLoginBtn.pack()
    stuCancelBtn.pack()

def teaLoginPg():
    splash.pack_forget()
    stuLoginPgBtn.pack_forget()
    teaLoginPgBtn.pack_forget()
    adminLoginPgBtn.pack_forget()
    regAccPgBtn.pack_forget()
    teacherSplash.pack()
    emaillabel.pack()
    email.pack()
    passwordlabel.pack()
    password.pack()
    teaLoginBtn.pack()
    teaCancelBtn.pack()

def adminLoginPg():
    splash.pack_forget()
    stuLoginPgBtn.pack_forget()
    teaLoginPgBtn.pack_forget()
    adminLoginPgBtn.pack_forget()
    regAccPgBtn.pack_forget()
    adminSplash.pack()
    emaillabel.pack()
    email.pack()
    passwordlabel.pack()
    password.pack()
    adminLoginBtn.pack()
    adminCancelBtn.pack()

def regAccPg():
    splash.pack_forget()
    stuLoginPgBtn.pack_forget()
    teaLoginPgBtn.pack_forget()
    adminLoginPgBtn.pack_forget()
    regAccPgBtn.pack_forget()
    registerSplash.pack()
    fullnameLabel.pack()
    fullname.pack()
    emaillabel.pack()
    email.pack()
    passwordlabel.pack()
    password.pack()
    cPasswordLabel.pack()
    cPassword.pack()
    regStuBtn.pack()
    regTeaBtn.pack()
    regAccCancelBtn.pack()
    

def stuCancel():
    studentSplash.pack_forget()
    emaillabel.pack_forget()
    email.pack_forget()
    passwordlabel.pack_forget()
    password.pack_forget()
    stuLoginBtn.pack_forget()
    stuCancelBtn.pack_forget()
    splash.pack()
    stuLoginPgBtn.pack()
    teaLoginPgBtn.pack()
    adminLoginPgBtn.pack()
    regAccPgBtn.pack()

def teaCancel():
    teacherSplash.pack_forget()
    emaillabel.pack_forget()
    email.pack_forget()
    passwordlabel.pack_forget()
    password.pack_forget()
    teaLoginBtn.pack_forget()
    teaCancelBtn.pack_forget()
    splash.pack()
    stuLoginPgBtn.pack()
    teaLoginPgBtn.pack()
    adminLoginPgBtn.pack()
    regAccPgBtn.pack()

def adminCancel():
    adminSplash.pack_forget()
    emaillabel.pack_forget()
    email.pack_forget()
    passwordlabel.pack_forget()
    password.pack_forget()
    adminLoginBtn.pack_forget()
    adminCancelBtn.pack_forget()
    splash.pack()
    stuLoginPgBtn.pack()
    teaLoginPgBtn.pack()
    adminLoginPgBtn.pack()
    regAccPgBtn.pack()

def regAccCancel():
    registerSplash.pack_forget()
    fullnameLabel.pack_forget()
    fullname.pack_forget()
    emaillabel.pack_forget()
    email.pack_forget()
    passwordlabel.pack_forget()
    password.pack_forget()
    cPasswordLabel.pack_forget()
    cPassword.pack_forget()
    regStuBtn.pack_forget()
    regTeaBtn.pack_forget()
    regAccCancelBtn.pack_forget()
    splash.pack()
    stuLoginPgBtn.pack()
    teaLoginPgBtn.pack()
    adminLoginPgBtn.pack()
    regAccPgBtn.pack()

def stuLogin():
    #ideally we have some login verification programmed here
    #if the email and password fields are correct we continue to execute the code
    #if not we DO NOT execute the following code
    studentSplash.pack_forget()
    emaillabel.pack_forget()
    email.pack_forget()
    passwordlabel.pack_forget()
    password.pack_forget()
    stuLoginBtn.pack_forget()
    stuCancelBtn.pack_forget()
    stuPg.pack()
    stuLogoutBtn.pack()

def teaLogin():
    #ideally we have some login verification programmed here
    #if the email and password fields are correct we continue to execute the code
    #if not we DO NOT execute the following code
    teacherSplash.pack_forget()
    emaillabel.pack_forget()
    email.pack_forget()
    passwordlabel.pack_forget()
    password.pack_forget()
    teaLoginBtn.pack_forget()
    teaCancelBtn.pack_forget()
    teaPg.pack()
    teaLogoutBtn.pack()

def adminLogin():
    #ideally we have some login verification programmed here
    #if the email and password fields are correct we continue to execute the code
    #if not we DO NOT execute the following code
    adminSplash.pack_forget()
    emaillabel.pack_forget()
    email.pack_forget()
    passwordlabel.pack_forget()
    password.pack_forget()
    adminLoginBtn.pack_forget()
    adminCancelBtn.pack_forget()
    adminPg.grid(row=0,column=0)
    adminLogoutBtn.grid(row=0, column=3)
    studentNameLabel.grid(row=1, column=0)
    studentName1Label.grid(row=2, column=0)
    studentName2Label.grid(row=3, column=0)
    studentName3Label.grid(row=4, column=0)
    studentName4Label.grid(row=5, column=0)
    studentName5Label.grid(row=6, column=0)
    if stuQ1 == True:
        stuDQButton1.grid(row=2, column=2)
    else:
        stuQButton1.grid(row=2, column=1)
    if stuQ2 == True:
        stuDQButton2.grid(row=3, column=2)
    else:
        stuQButton2.grid(row=3, column=1)
    if stuQ3 == True:
        stuDQButton3.grid(row=4, column=2)
    else:
        stuQButton3.grid(row=4, column=1)
    if stuQ4 == True:
        stuDQButton4.grid(row=5, column=2)
    else:
        stuQButton4.grid(row=5, column=1)
    if stuQ5 == True:
        stuDQButton5.grid(row=6, column=2)
    else:
        stuQButton5.grid(row=6, column=1)

def stuLogout():
    stuPg.pack_forget()
    stuLogoutBtn.pack_forget()
    studentSplash.pack()
    emaillabel.pack()
    email.pack()
    passwordlabel.pack()
    password.pack()
    stuLoginBtn.pack()
    stuCancelBtn.pack()

def teaLogout():
    teaPg.pack_forget()
    teaLogoutBtn.pack_forget()
    teacherSplash.pack()
    emaillabel.pack()
    email.pack()
    passwordlabel.pack()
    password.pack()
    teaLoginBtn.pack()
    teaCancelBtn.pack()

def adminLogout():
    adminPg.pack_forget()
    adminLogoutBtn.pack_forget()
    adminSplash.pack()
    emaillabel.pack()
    email.pack()
    passwordlabel.pack()
    password.pack()
    adminLoginBtn.grid_forget()
    adminCancelBtn.grid_forget()

def stuQButton1():
    #have logic here that changes the first student's qualification status to "Qualifed"
    stuQButton1.grid_forget()
    stuDQButton1.grid(row=2,column=2)

def stuDQButton1():
    #have logic here that changes the first student's qualification status to "Disqualifed"
    stuDQButton1.grid_forget()
    stuQButton1.grid(row=2,column=1)

def stuQButton2():
    #have logic here that changes the second student's qualification status to "Qualifed"
    stuQButton2.grid_forget()
    stuDQButton2.grid(row=3,column=2)

def stuDQButton2():
    #have logic here that changes the second student's qualification status to "Disqualifed"
    stuDQButton2.grid_forget()
    stuQButton2.grid(row=3,column=1)

def stuQButton3():
    #have logic here that changes the third student's qualification status to "Qualifed"
    stuQButton3.grid_forget()
    stuDQButton3.grid(row=4,column=2)

def stuDQButton3():
    #have logic here that changes the third student's qualification status to "Disqualifed"
    stuDQButton3.grid_forget()
    stuQButton3.grid(row=4, column=1)

def stuQButton4():
    #have logic here that changes the fourth student's qualification status to "Qualifed"
    stuQButton4.grid_forget()
    stuDQButton4.grid(row=5, column=2)

def stuDQButton4():
    #have logic here that changes the fourth student's qualification status to "Disqualifed"
    stuDQButton4.grid_forget()
    stuQButton4.grid(row=5, column=1)

def stuQButton5():
    #have logic here that changes the fifth student's qualification status to "Qualifed"
    stuQButton5.grid_forget()
    stuDQButton5.grid(row=6, column=2)

def stuDQButton5():
    #have logic here that changes the fifth student's qualification status to "Disqualifed"
    stuDQButton5.grid_forget()
    stuQButton5.grid(row=6, column=1)
    

#this is the function that will contain the logic for registering a Student, feel free to delete the print statement, I just put it there so the module would run during my testing
def regStu():
    print("placeholder")

#this is the function that will contain the logic for registering a teacher, feel free to delete the print statement, I just put it there so the module would run during my testing
def regTea():
    print("placeholder")
    

window = tkinter.Tk()
window.geometry("1000x500")
#the following buttons need logic assigned to them, stuLoginBtn, teaLoginBtn, adminLoginBtn regStuBtn, and regTeaBtn

stuLoginPgBtn = tkinter.Button(window, text="Student Login", bg="red", fg="white", command=stuLoginPg)
teaLoginPgBtn = tkinter.Button(window, text="Teacher Login", bg="green", fg="black", command=teaLoginPg)
adminLoginPgBtn = tkinter.Button(window, text="Admin Login", bg="blue", fg="white", command=adminLoginPg)
regAccPgBtn = tkinter.Button(window, text="Register an Account", bg="yellow", fg="black", command=regAccPg)

stuLoginBtn = tkinter.Button(window, text="Login", bg="red", fg="white", command=stuLogin)
teaLoginBtn = tkinter.Button(window, text="Login", bg="green", fg="black", command=teaLogin)
adminLoginBtn = tkinter.Button(window, text="Login", bg="blue", fg="white", command=adminLogin)

stuLogoutBtn = tkinter.Button(window, text="Logout",  bg="red", fg="white", command=stuLogout)
teaLogoutBtn = tkinter.Button(window, text="Logout", bg="green", fg="black", command=teaLogout)
adminLogoutBtn = tkinter.Button(window, text="Logout", bg="blue", fg="white", command=adminLogout)

stuCancelBtn = tkinter.Button(window, text="Cancel", bg="red", fg="white", command=stuCancel)
teaCancelBtn = tkinter.Button(window, text="Cancel", bg="green", fg="black", command=teaCancel)
adminCancelBtn = tkinter.Button(window, text="Cancel",  bg="blue", fg="white", command=adminCancel)
regAccCancelBtn = tkinter.Button(window, text="Cancel", bg="yellow", fg="black", command=regAccCancel)

regStuBtn = tkinter.Button(window, text="Register as Student", bg="red", fg="white", command=regStu) 
regTeaBtn = tkinter.Button(window, text="Register as Teacher", bg="green", fg="black", command=regTea)

studentNameLabel = tkinter.Label(window, text="Student Name")
stuQButton1 = tkinter.Button(window, text="Qualify", bg="blue", fg="white", command=stuQButton1)
stuDQButton1 = tkinter.Button(window, text="Disqualify", bg="red", fg="white", command=stuDQButton1)
stuQButton2 = tkinter.Button(window, text="Qualify", bg="blue", fg="white", command=stuQButton2)
stuDQButton2 = tkinter.Button(window, text="Disqualify", bg="red", fg="white", command=stuDQButton2)
stuQButton3 = tkinter.Button(window, text="Qualify", bg="blue", fg="white", command=stuQButton3)
stuDQButton3 = tkinter.Button(window, text="Disqualify", bg="red", fg="white", command=stuDQButton3)
stuQButton4 = tkinter.Button(window, text="Qualify", bg="blue", fg="white", command=stuQButton4)
stuDQButton4 = tkinter.Button(window, text="Disqualify", bg="red", fg="white", command=stuDQButton4)
stuQButton5 = tkinter.Button(window, text="Qualify", bg="blue", fg="white", command=stuQButton5)
stuDQButton5 = tkinter.Button(window, text="Disqualify", bg="red", fg="white", command=stuDQButton5)
#variables containing the verification status of the students
stuQ1 = False
stuQ2 = False
stuQ3 = False
stuQ4 = False
stuQ5 = False
studentName1Label = tkinter.Label(window, text="Placeholder 1")
studentName2Label = tkinter.Label(window, text="Placeholder 2")
studentName3Label = tkinter.Label(window, text="Placeholder 3")
studentName4Label = tkinter.Label(window, text="Placeholder 4")
studentName5Label = tkinter.Label(window, text="Placeholder 5")

email = Entry(window) #this is the variable containing the email field
emaillabel = tkinter.Label(window, text="Email:")
password = Entry(window, show="*") #this is the variable containing the password field
passwordlabel = tkinter.Label(window, text="Password:")
cPassword = Entry(window, show="*") #this is the variable containing the confirm password field on the registration page
cPasswordLabel = tkinter.Label(window, text="Confirm Password:")
fullname = Entry(window)
fullnameLabel = tkinter.Label(window, text= "Full Name:")

studentName = "placeholder" #this is the variable containing the name of the student logging in
stuPg = tkinter.Label(window, text="Welcome %s" % (studentName))
teacherName = "placeholder" #this is the variable containing the name of the teacher logging in
teaPg = tkinter.Label(window, text="Welcome %s" % (teacherName))
adminName = "placeholder" #this is the variable containing the name of the admin logging in
adminPg = tkinter.Label(window, text="Welcome %s" % (adminName))

logo= tkinter.PhotoImage(file ="books.png")
splash = tkinter.Label(window, image=logo)
studentLogo= tkinter.PhotoImage(file="studentlogin.png")
studentSplash = tkinter.Label(window, image=studentLogo)
teacherLogo= tkinter.PhotoImage(file="teacherlogin.png")
teacherSplash = tkinter.Label(window, image=teacherLogo)
adminLogo= tkinter.PhotoImage(file="adminlogin.png")
adminSplash = tkinter.Label(window, image=adminLogo)
registerLogo= tkinter.PhotoImage(file="registerpage.png")
registerSplash = tkinter.Label(window, image=registerLogo)

splash.pack()
stuLoginPgBtn.pack()
teaLoginPgBtn.pack()
adminLoginPgBtn.pack()
regAccPgBtn.pack()

