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
    loginwin.geometry("250x200")

    def clickedlogin():
        givenUsername = str(enterusername.get())
        givenPassword = str(enterpassword.get())
        
        #checking username and password against a txt file
        txtRead = open("logins.txt","r")
        for line in txtRead.readlines():
            login_info = line.split()
            if login_info[0] == givenUsername and login_info[1] == givenPassword:
                loginwin.destroy()
                txtRead.close()
                completed()
            else:
                tk.Label(loginwin).pack()
                tk.Label(loginwin, text="Incorrect Credentials!! Try Again!!", font = 20).pack()
    
    tk.Label(loginwin, text="Username**", font = 20).pack()
    global enterusername
    enterusername = tk.Entry(loginwin)
    enterusername.pack()
    tk.Label(loginwin).pack()
    tk.Label(loginwin, text="Password**", font = 20).pack()
    global enterpassword
    enterpassword = tk.Entry(loginwin, show = "*")
    enterpassword.pack()
    tk.Label(loginwin).pack()
    tk.Button(loginwin, text="Login", command = clickedlogin, font = 30).pack()

###this is for the register button to open a new window###
def register():
    regwin = tk.Tk()
    regwin.title("Register")
    regwin.geometry("250x200")

    def clickedregister():
        newusername = str(newusernameentry.get())
        newpassword = str(newpasswordentry.get())

        #Adding new username and password to text file
        open_File = open("logins.txt","a")
        open_File.write(newusername + "" + newpassword)
    
    tk.Label(regwin, text="Please enter a new Username", font = 20).pack()
    global newusernameentry
    newusernameentry = tk.Entry(regwin).pack()
    
    tk.Label(regwin, text="Please enter a new Password", font = 20).pack()
    global newpasswordentry
    newpasswordentry = tk.Entry(regwin).pack()
    
    tk.Label(regwin).pack()
    tk.Button(regwin, text="Register", font = 30, command = clickedregister).pack()
    #Adding new username and password to text file
        

'''Main Program'''
r = tk.Tk()
r.title("My new GUI")
r.geometry("400x200")

tk.Label(r).pack()
tk.Label(r, text="Welcome to my program!", font = 30).pack()
tk.Label(r).pack()
tk.Button(r, text="Login", command = login, font = 30).pack()
tk.Label(r).pack()
tk.Button(r, text="Register", command = register, font = 30).pack()
r.mainloop()
