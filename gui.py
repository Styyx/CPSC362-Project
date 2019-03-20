from tkinter import Tk, Label, Entry, Button, E, W

class logscreen:
    def __init__(self, master):
        self.master = master
        master.title("Books Advantage Web App")

        self.title = Label(master, text="Welcome to Books Advantage! Please sign in below.")
        
        self.username = Entry(master)
        self.text1 = Label(master, text="username")

        self.password = Entry(master)
        self.text2 = Label(master, text="password")
        
        self.login_button = Button(master, text="Login")

        self.title.grid(row=0, column=0, sticky=W+E)
        self.text1.grid(row=1, column=0, sticky=W)
        self.username.grid(row=1, column=1, sticky=E)
        self.text2.grid(row=2, column=0, sticky=W)
        self.password.grid(row=2, column=1, sticky=E)
        self.login_button.grid(row=3, column=0, sticky=W+E)

    def login(self):
        print("~")

root = Tk()
my_gui = logscreen(root)
root.mainloop()
