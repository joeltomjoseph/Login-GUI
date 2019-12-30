import tkinter as tk
from tkinter import *

'''Functions'''
###this is for the completed login window###
def completed():
    comp = tk.Tk()
    comp.title("Logged in!")
    comp.geometry("400x400")

    tk.Label(comp, text="You have been logged in!!").pack()

    comp.mainloop()

###This is for the login button to open a new window###
def login():
    loginwin = tk.Tk()
    loginwin.title("Login")
    loginwin.geometry("200x200")

    def clickedlogin():
        givenUsername = str(enterusername.get())
        givenPassword = str(enterpassword.get())
        #checking username and password against a txt file
        for line in open("logins.txt","r").readlines():
            login_info = line.split()
            if login_info[0] == givenUsername and login_info[1] == givenPassword:
                loginwin.destroy()
                txtRead.close()
                completed()
            else:
                tk.Label(loginwin).pack()
                tk.Label(loginwin, text="Incorrect Credentials!! Try Again!!", font = 20).pack()
    
    tk.Label(loginwin, text="Username**").pack()
    global enterusername
    enterusername = tk.Entry(loginwin)
    enterusername.pack()
    tk.Label(loginwin).pack()
    tk.Label(loginwin, text="Password**").pack()
    global enterpassword
    enterpassword = tk.Entry(loginwin)
    enterpassword.pack()
    tk.Label(loginwin).pack()
    tk.Button(loginwin, text="Login", command = clickedlogin).pack()

###this is for the register button to open a new window###
def register():
    regwin = tk.Tk()
    regwin.title("Register")
    regwin.geometry("200x200")

    tk.Label(regwin, text="Please enter a new Username").pack()
    newusername = tk.Entry(regwin).pack()
    
    tk.Label(regwin, text="Please enter a new Password").pack()
    newpassword = tk.Entry(regwin).pack()


'''Main Program'''
r = tk.Tk()
r.title("My new GUI")
r.geometry("400x400")

tk.Label(r, text="Welcome to my program!").pack()
tk.Label(r).pack()
tk.Button(r, text="Login", command = login).pack()
tk.Label(r).pack()
tk.Button(r, text="Register", command = register).pack()
r.mainloop()
