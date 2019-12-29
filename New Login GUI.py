import tkinter as tk

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
        givenUsername = enterusername.get()     ###problem here###
        givenPassword = enterpassword.get()
        #checking username and password against a txt file
        txtRead = open("logins.txt", "r")
        for line in txtRead:
            username, password = line.split(',')
            if username == givenUsername and password == givenPassword:
                completed()
                loginwin.destroy()
                
    tk.Label(loginwin, text="Username**").pack()
    enterusername = tk.Entry(loginwin).pack()
    tk.Label(loginwin).pack()
    tk.Label(loginwin, text="Password**").pack()
    enterpassword = tk.Entry(loginwin).pack()
    tk.Label(loginwin).pack()
    tk.Button(loginwin, text="Login", command = clickedlogin).pack()

###this is for the register button to open a new window###
def register():
    regwin = tk.Tk()
    regwin.title("Register")
    regwin.geometry("200x200")

    tk.Label(loginwin, text="Please enter a new Username").pack()
    newusername = tk.Entry(loginwin).pack()
    
    tk.Label(loginwin, text="Please enter a new Password").pack()
    newpassword = tk.Entry(loginwin).pack()


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
