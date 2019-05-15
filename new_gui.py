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
    #We must now also set the doesStuQual variable, along with if they're taking course1~5, and or have checked out book for those courses
    studentSplash.pack_forget()
    emaillabel.pack_forget()
    email.pack_forget()
    passwordlabel.pack_forget()
    password.pack_forget()
    stuLoginBtn.pack_forget()
    stuCancelBtn.pack_forget()
    stuPg.grid(row=0, column=0)
    stuLogoutBtn.grid(row=0, column=3)
    coursesNameLabel.grid(row=1, column=0)
    bookNameLabel.grid(row=1, column=1)
    qualStatusLabel.grid(row=1, column=2)
    courseName1Label.grid(row=2,column=0)
    courseName2Label.grid(row=3,column=0)
    courseName3Label.grid(row=4,column=0)
    courseName4Label.grid(row=5,column=0)
    courseName5Label.grid(row=6,column=0)
    bookName1Label.grid(row=2,column=1)
    bookName2Label.grid(row=3,column=1)
    bookName3Label.grid(row=4,column=1)
    bookName4Label.grid(row=5,column=1)
    bookName5Label.grid(row=6,column=1)
    if courseQ1 == True:
        courseQualifies1.grid(row=2, column=2)
        if doesStuQual == True:
            if isTakingC1 == True:
                if book1CheckedOut == True:
                    book1CIn.grid(row=2, column=4)
                else:
                    book1COut.grid(row=2, column=3)
    elif courseQ1 == False:
        courseNotQualifies1.grid(row=2, column=2)

    if courseQ2 == True:
        courseQualifies2.grid(row=3, column=2)
        if doesStuQual == True:
            if isTakingC2 == True:
                if book2CheckedOut == True:
                    book2CIn.grid(row=3, column=4)
                else:
                    book2COut.grid(row=3, column=3)
    elif courseQ2 == False:
        courseNotQualifies2.grid(row=3, column=2)

    if courseQ3 == True:
        courseQualifies3.grid(row=4, column=2)
        if doesStuQual == True:
            if isTakingC3 == True:
                if book3CheckedOut == True:
                    book3CIn.grid(row=4, column=4)
                else:
                    book3COut.grid(row=4, column=3)
    elif courseQ3 == False:
        courseNotQualifies3.grid(row=4, column=2)

    if courseQ4 == True:
        courseQualifies4.grid(row=5, column=2)
        if doesStuQual == True:
            if isTakingC4 == True:
                if book4CheckedOut == True:
                    book4CIn.grid(row=5, column=4)
                else:
                    book4Cout.grid(row=5, column=3)
    elif courseQ4 == False:
        courseNotQualifies4.grid(row=5, column=2)

    if courseQ5 == True:
        courseQualifies5.grid(row=6, column=2)
        if doesStuQual == True:
            if isTakingC5 == True:
                if book5CheckedOut == True:
                    book5CIn.grid(row=6, column=4)
                else:
                    book5COut.grid(row=6, column=3)
    elif courseQ5 == False:
        courseNotQualifies5.grid(row=6, column=2)

def teaLogin():
    #ideally we have some login verification programmed here
    #if the email and password fields are correct we continue to execute the code
    #if not we DO NOT execute the following code
    #There are now variables later in the code that need to be set depending on the teacher loggin in, these variables are for if they're teaching course 1/2/3/4/5?
    teacherSplash.pack_forget()
    emaillabel.pack_forget()
    email.pack_forget()
    passwordlabel.pack_forget()
    password.pack_forget()
    teaLoginBtn.pack_forget()
    teaCancelBtn.pack_forget()
    teaPg.grid(row=0, column=0)
    teaLogoutBtn.grid(row=0, column=3)
    coursesNameLabel.grid(row=1, column=0)
    courseName1Label.grid(row=2,column=0)
    courseName2Label.grid(row=3,column=0)
    courseName3Label.grid(row=4,column=0)
    courseName4Label.grid(row=5,column=0)
    courseName5Label.grid(row=6,column=0)
    if isTeachingC1 == True:
        if courseQ1 == True:
            courseDQButton1.grid(row=2, column=2)
        else:
            courseQButton1.grid(row=2, column=1)
    if isTeachingC2 == True:
        if courseQ2 == True:
            courseDQButton2.grid(row=3, column=2)
        else:
            courseQButton2.grid(row=3, column=1)
    if isTeachingC3 == True:
        if courseQ3 == True:
            courseDQButton3.grid(row=4, column=2)
        else:
            courseQButton3.grid(row=4, column=1)
    if isTeachingC4 == True:
        if courseQ4 == True:
            courseDQButton4.grid(row=5, column=2)
        else:
            courseQButton4.grid(row=5, column=1)
    if isTeachingC5 == True:
        if courseQ5 == True:
            courseDQButton5.grid(row=6, column=2)
        else:
            courseQButton5.grid(row=6, column=1)

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
    stuPg.grid_forget()
    stuLogoutBtn.grid_forget()
    coursesNameLabel.grid_forget()
    bookNameLabel.grid_forget()
    qualStatusLabel.grid_forget()
    courseName1Label.grid_forget()
    courseName2Label.grid_forget()
    courseName3Label.grid_forget()
    courseName4Label.grid_forget()
    courseName5Label.grid_forget()
    bookName1Label.grid_forget()
    bookName2Label.grid_forget()
    bookName3Label.grid_forget()
    bookName4Label.grid_forget()
    bookName5Label.grid_forget()
    courseQualifies1.grid_forget()
    courseNotQualifies1.grid_forget()
    courseQualifies2.grid_forget()
    courseNotQualifies2.grid_forget()
    courseQualifies3.grid_forget()
    courseNotQualifies3.grid_forget()
    courseQualifies4.grid_forget()
    courseNotQualifies4.grid_forget()
    courseQualifies5.grid_forget()
    courseNotQualifies5.grid_forget()
    book1COut.grid_forget()
    book1CIn.grid_forget()
    book2COut.grid_forget()
    book2CIn.grid_forget()
    book3COut.grid_forget()
    book3CIn.grid_forget()
    book4COut.grid_forget()
    book4CIn.grid_forget()
    book5COut.grid_forget()
    book5CIn.grid_forget()
    doesStuQual = False
    isTakingC1 = False
    isTakingC2 = False
    isTakingC3 = False
    isTakingC4 = False
    isTakingC5 = False
    book1CheckedOut = False
    book2CheckedOut = False
    book3CheckedOut = False
    book4CheckedOut = False
    book5CheckedOut = False
    studentSplash.pack()
    emaillabel.pack()
    email.pack()
    passwordlabel.pack()
    password.pack()
    stuLoginBtn.pack()
    stuCancelBtn.pack()

def teaLogout():
    teaPg.grid_forget()
    teaLogoutBtn.grid_forget()
    coursesNameLabel.grid_forget()
    courseName1Label.grid_forget()
    courseName2Label.grid_forget()
    courseName3Label.grid_forget()
    courseName4Label.grid_forget()
    courseName5Label.grid_forget()
    courseQButton1.grid_forget()
    courseDQButton1.grid_forget()
    courseQButton2.grid_forget()
    courseDQButton2.grid_forget()
    courseQButton3.grid_forget()
    courseDQButton3.grid_forget()
    courseQButton4.grid_forget()
    courseDQButton4.grid_forget()
    courseQButton5.grid_forget()
    courseDQButton5.grid_forget()
    isTeachingC1 = False
    isTeachingC2 = False
    isTeachingC3 = False
    isTeachingC4 = False
    isTeachingC5 = False
    teacherSplash.pack()
    emaillabel.pack()
    email.pack()
    passwordlabel.pack()
    password.pack()
    teaLoginBtn.pack()
    teaCancelBtn.pack()

def adminLogout():
    adminPg.grid_forget()
    adminLogoutBtn.grid_forget()
    studentNameLabel.grid_forget()
    studentName1Label.grid_forget()
    studentName2Label.grid_forget()
    studentName3Label.grid_forget()
    studentName4Label.grid_forget()
    studentName5Label.grid_forget()
    stuQButton1.grid_forget()
    stuDQButton1.grid_forget()
    stuQButton2.grid_forget()
    stuDQButton2.grid_forget()
    stuQButton3.grid_forget()
    stuDQButton3.grid_forget()
    stuQButton4.grid_forget()
    stuDQButton4.grid_forget()
    stuQButton5.grid_forget()
    stuDQButton5.grid_forget()
    adminSplash.pack()
    emaillabel.pack()
    email.pack()
    passwordlabel.pack()
    password.pack()
    adminLoginBtn.pack()
    adminCancelBtn.pack()

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

def courseQButton1():
    #needs an SQL statement the qualifies the first course from the program
    courseQButton1.grid_forget()
    courseDQButton1.grid(row=2, column=2)

def courseDQButton1():
    #needs an SQL statement the disqualifies the first course from the program
    courseDQButton1.grid_forget()
    courseQButton1.grid(row=2, column=1)

def courseQButton2():
    #needs an SQL statement the qualifies the second course from the program
    courseQButton2.grid_forget()
    courseDQButton2.grid(row=3, column=2)

def courseDQButton2():
    #needs an SQL statement the disqualifies the second course from the program
    courseDQButton2.grid_forget()
    courseQButton2.grid(row=3, column=1)

def courseQButton3():
    #needs an SQL statement the qualifies the third course from the program
    courseQButton3.grid_forget()
    courseDQButton3.grid(row=4, column=2)

def courseDQButton3():
    #needs an SQL statement the disqualifies the third course from the program
    courseDQButton3.grid_forget()
    courseQButton3.grid(row=4, column=1)

def courseQButton4():
    #needs an SQL statement the qualifies the fourth course from the program
    courseQButton4.grid_forget()
    courseDQButton4.grid(row=5, column=2)

def courseDQButton4():
    #needs an SQL statement the disqualifies the fourth course from the program
    courseDQButton4.grid_forget()
    courseQButton4.grid(row=5, column=1)

def courseQButton5():
    #needs an SQL statement the qualifies the fifth course from the program
    courseQButton5.grid_forget()
    courseDQButton5.grid(row=6, column=2)

def courseDQButton5():
    #needs an SQL statement the disqualifies the fifth course from the program
    courseDQButton5.grid_forget()
    courseQButton5.grid(row=6, column=1)

def book1CIn():
    #needs an SQL statement that checks in book 1 for the student logged in
    book1CIn.grid_forget()
    book1COut.grid(row=2, column=3)

def book1COut():
    #needs an SQL statement that checks out book 1 for the student logged in
    book1COut.grid_forget()
    book1CIn.grid(row=2, column=4)

def book2CIn():
    #needs an SQL statement that checks in book 2 for the student logged in
    book2CIn.grid_forget()
    book2COut.grid(row=3, column=3)

def book2COut():
    #needs an SQL statement that checks out book 2 for the student logged in
    book2COut.grid_forget()
    book2CIn.grid(row=3, column=4)

def book3CIn():
    #needs an SQL statement that checks in book 3 for the student logged in
    book3CIn.grid_forget()
    book3COut.grid(row=4, column=3)

def book3COut():
    #needs an SQL statement that checks out book 3 for the student logged in
    book3COut.grid_forget()
    book3CIn.grid(row=4, column=4)

def book4CIn():
    #needs an SQL statement that checks in book 4 for the student logged in
    book4CIn.grid_forget()
    book4COut.grid(row=5, column=3)

def book4COut():
    #needs an SQL statement that checks out book 4 for the student logged in
    book4COut.grid_forget()
    book4CIn.grid(row=5, column=4)

def book5CIn():
    #needs an SQL statement that checks in book 5 for the student logged in
    book5CIn.grid_forget()
    book5COut.grid(row=6, column=3)

def book5COut():
    #needs an SQL statement that checks out book 5 for the student logged in
    book5COut.grid_forget()
    book5CIn.grid(row=6, column=4)

#this is the function that will contain the logic for registering a Student, feel free to delete the print statement, I just put it there so the module would run during my testing
def regStu():
    print("placeholder")

#this is the function that will contain the logic for registering a teacher, feel free to delete the print statement, I just put it there so the module would run during my testing
def regTea():
    print("placeholder")
    

window = tkinter.Tk()
window.geometry("1000x500")
#the following buttons need logic assigned to them, stuLoginBtn, teaLoginBtn, adminLoginBtn regStuBtn, regTeaBtn,
#all the stuD/QBtn(s), all the courseD/QBtn(s), and all the bookCIn/OutBtn(s) 

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
#variables containing the verification status and names of the students USED ONLY FOR THE ADMIN PAGE
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

coursesNameLabel = tkinter.Label(window, text="Course Name")
courseQButton1 = tkinter.Button(window, text="Qualify", bg="blue", fg="white", command=courseQButton1)
courseDQButton1 = tkinter.Button(window, text="Disqualify", bg="red", fg="white", command=courseDQButton1)
courseQButton2 = tkinter.Button(window, text="Qualify", bg="blue", fg="white", command=courseQButton2)
courseDQButton2 = tkinter.Button(window, text="Disqualify", bg="red", fg="white", command=courseDQButton2)
courseQButton3 = tkinter.Button(window, text="Qualify", bg="blue", fg="white", command=courseQButton3)
courseDQButton3 = tkinter.Button(window, text="Disqualify", bg="red", fg="white", command=courseDQButton3)
courseQButton4 = tkinter.Button(window, text="Qualify", bg="blue", fg="white", command=courseQButton4)
courseDQButton4 = tkinter.Button(window, text="Disqualify", bg="red", fg="white", command=courseDQButton4)
courseQButton5 = tkinter.Button(window, text="Qualify", bg="blue", fg="white", command=courseQButton5)
courseDQButton5 = tkinter.Button(window, text="Disqualify", bg="red", fg="white", command=courseDQButton5)
#variables containing the teaching status, qualification status, and names of the courses
isTeachingC1 = False
isTeachingC2 = False
isTeachingC3 = False
isTeachingC4 = False
isTeachingC5 = False
courseQ1 = False
courseQ2 = False
courseQ3 = False
courseQ4 = False
courseQ5 = False
courseName1Label = tkinter.Label(window, text="Course 1")
courseName2Label = tkinter.Label(window, text="Course 2")
courseName3Label = tkinter.Label(window, text="Course 3")
courseName4Label = tkinter.Label(window, text="Course 4")
courseName5Label = tkinter.Label(window, text="Course 5")

bookNameLabel = tkinter.Label(window, text="Book Name")
qualStatusLabel = tkinter.Label(window, text="Course Qualification")
courseQualifies1 = tkinter.Label(window, text="Qualifies!", bg="blue", fg="white")
courseNotQualifies1 = tkinter.Label(window, text="Doesn't Qualify!", bg="red", fg="white")
courseQualifies2 = tkinter.Label(window, text="Qualifies!", bg="blue", fg="white")
courseNotQualifies2 = tkinter.Label(window, text="Doesn't Qualify!", bg="red", fg="white")
courseQualifies3 = tkinter.Label(window, text="Qualifies!", bg="blue", fg="white")
courseNotQualifies3 = tkinter.Label(window, text="Doesn't Qualify!", bg="red", fg="white")
courseQualifies4 = tkinter.Label(window, text="Qualifies!", bg="blue", fg="white")
courseNotQualifies4 = tkinter.Label(window, text="Doesn't Qualify!", bg="red", fg="white")
courseQualifies5 = tkinter.Label(window, text="Qualifies!", bg="blue", fg="white")
courseNotQualifies5 = tkinter.Label(window, text="Doesn't Qualify!", bg="red", fg="white")
book1COut = tkinter.Button(window, text="Check Out", bg="blue", fg="white", command=book1COut)
book1CIn = tkinter.Button(window, text="Check In", bg="red", fg="white", command=book1CIn)
book2COut = tkinter.Button(window, text="Check Out", bg="blue", fg="white", command=book2COut)
book2CIn = tkinter.Button(window, text="Check In", bg="red", fg="white", command=book2CIn)
book3COut = tkinter.Button(window, text="Check Out", bg="blue", fg="white", command=book3COut)
book3CIn = tkinter.Button(window, text="Check In", bg="red", fg="white", command=book3CIn)
book4COut = tkinter.Button(window, text="Check Out", bg="blue", fg="white", command=book4COut)
book4CIn = tkinter.Button(window, text="Check In", bg="red", fg="white", command=book4CIn)
book5COut = tkinter.Button(window, text="Check Out", bg="blue", fg="white", command=book5COut)
book5CIn = tkinter.Button(window, text="Check In", bg="red", fg="white", command=book5CIn)
#variables containing the student's qualification status, if they're taking course 1~5, and if they've checked out the book from course 1~5
doesStuQual = False
isTakingC1 = False
isTakingC2 = False
isTakingC3 = False
isTakingC4 = False
isTakingC5 = False
book1CheckedOut = False
book2CheckedOut = False
book3CheckedOut = False
book4CheckedOut = False
book5CheckedOut = False
bookName1Label = tkinter.Label(window, text="Book 1")
bookName2Label = tkinter.Label(window, text="Book 2")
bookName3Label = tkinter.Label(window, text="Book 3")
bookName4Label = tkinter.Label(window, text="Book 4")
bookName5Label = tkinter.Label(window, text="Book 5")

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

