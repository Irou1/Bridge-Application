from tkinter import *
import mysql.connector as mysql
from MySQLdb import dbConnect
import datetime

class MainMenu(Frame):

    def __init__(self, parent):  #The very first screen of the web app
        Frame.__init__(self, parent)
        # w, h = parent.winfo_screenwidth(), parent.winfo_screenheight()
        # parent.overrideredirect(1)
        #parent.geometry("%dx%d+0+0" % (w, h))

        # canvas = Canvas(self, width = w, height = h)
        # canvas.pack()
        # bkgrd = PhotoImage(file="C:\\Users\\kanip\\PycharmProjects\\Desktop\\ABCL Project\\ACBL_background.png")
        # canvas.create_image(0,0, anchor=NW, image=bkgrd)
        titleLabel = Label(self, text="LET'S PLAY BRIDGE",fg ="white" ,font ='Arial 36').pack(side="top", padx=20)
        loginButton = Button(self, text="Log in",fg ="blue",font ="Arial 14",command= self.LoginScreen).pack(padx=20)
        signupButton = Button(self, text="Sign up", fg ="blue",font ="Arial 14",command= self.SignupScreen).pack(padx=20)
        quitButton = Button(self, text="Quit",font ="Arial 14",command= quit).pack(side="bottom", padx=20)

    def LoginScreen(self):
        global entry_user
        global entry_pass
        top = Toplevel(self)
        top.title("Log In - ABCL")
        # w, h = top.winfo_screenwidth(), top.winfo_screenheight()
        # top.overrideredirect(1)
        # top.geometry("%dx%d+0+0" % (w, h))
        quitButton = Button(top, text="Cancel", font="Arial 14", command= top.destroy).pack(side="bottom", padx=20)

        #entry_user = StringVar()
        #entry_pass = StringVar()

        # Frames to divide the window into three parts.. makes it easier to organize the widgets
        topFrame = Frame(top)
        topFrame.pack()
        middleFrame = Frame(top)
        middleFrame.pack()
        bottomFrame = Frame(top)
        bottomFrame.pack(side=BOTTOM)

        # Widgets and which frame they are in
        label = Label(topFrame, text="LET'S PLAY BRIDGE")
        userLabel = Label(middleFrame, text='Username:')
        passLabel = Label(middleFrame, text='Password:')
        entry_user = Entry((middleFrame) ) # For DB
        entry_pass = Entry(middleFrame, show ='*') # For DB
        b = Button(bottomFrame, text="Log in",command=lambda: get_Login_input())

        #Location of the Widgets in their frames
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        userLabel.grid(row=2, column=0, sticky=W, padx=20)
        entry_user.grid(row=2, column=1, padx=20)
        passLabel.grid(row=3, column=0, sticky=W, padx=20)
        entry_pass.grid(row=3, column=1, padx=20)
        b.grid(row=4, columnspan=2,padx=20, pady = 20)

###############################################DATABASE Check Login!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        def get_Login_input():
            var = dbConnect()
            dbconn = mysql.connect(host=var.host, user=var.user, password=var.password, db=var.db)
            cur = dbconn.cursor()  # Cursor object - required to execute all queries

            cur.execute("SELECT username FROM playerinfo WHERE username = '%s' AND password = '%s'" % (entry_user.get(), entry_pass.get()))

            rows = cur.fetchall()

            if rows:
                r = Tk()
                r.title(':D')
                r.geometry('150x150')
                rlbl = Label(r, text='\n[+] Logged In')
                rlbl.pack()
                r.mainloop()
            else:
                r = Tk()
                r.title(':D')
                r.geometry('150x150')
                rlbl = Label(r, text='\n[!] Invalid Login')
                rlbl.pack()
                r.mainloop()

    ########################################## SIGN UP PART ##########################################################
    def SignupScreen(self):
        global entry_fname
        global entry_lname
        global entry_user
        global entry_pass
        global entry_repass
        global entry_email
        global entry_ACBL
        global entry_disID
        top = Toplevel(self)
        top.title("Sign Up - ABCL")
        # w, h = top.winfo_screenwidth(), top.winfo_screenheight()
        # top.overrideredirect(1)
        # top.geometry("%dx%d+0+0" % (w, h))
        quitButton = Button(top, text="Cancel", font="Arial 14", command= top.destroy).pack(side="bottom", padx=20)
        topFrame = Frame(top)
        topFrame.pack()
        middleFrame = Frame(top)
        middleFrame.pack()
        bottomFrame = Frame(top)
        bottomFrame.pack(side=BOTTOM)

        # Widgets and which frame they are in
        label = Label(topFrame, text="LET'S PLAY BRIDGE")

        fnameLabel = Label(middleFrame,text = 'First Name:')
        lnameLabel = Label(middleFrame, text='Last Name:')
        userLabel = Label(middleFrame, text='Username:')
        passLabel = Label(middleFrame, text='Password:')
        repassLabel = Label(middleFrame, text='Re-Enter Password:')
        emailLabel = Label(middleFrame, text='Email(optional):')
        ACBLnumLabel = Label(middleFrame, text='ACBLnum(optional):')
        disIDLabel = Label(middleFrame, text='DistrictID(optional):')
        entry_fname = Entry(middleFrame)  #For DB
        entry_lname = Entry(middleFrame) #For DB
        entry_user = Entry(middleFrame)#For DB
        entry_pass = Entry(middleFrame, show = '*')#For DB
        entry_repass = Entry(middleFrame, show = '*')#For DB
        entry_email = Entry(middleFrame)#For DB
        entry_ACBL = Entry(middleFrame)#For DB
        entry_disID = Entry(middleFrame)#For DB
        b = Button(bottomFrame, text="Sign up", font="Arial 14", command=lambda : combined_Functions(self))

        # Location of the Widgets in their frames
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        fnameLabel.grid(row=1, column=0, sticky=W, padx=20)
        entry_fname.grid(row=1, column=1, padx=20)
        lnameLabel.grid(row=2, column=0, sticky=W, padx=20)
        entry_lname.grid(row=2, column=1, padx=20)
        userLabel.grid(row=3, column=0, sticky=W, padx=20)
        entry_user.grid(row=3, column=1, padx=20)
        passLabel.grid(row=4, column=0, sticky=W, padx=20)
        entry_pass.grid(row=4, column=1, padx=20)
        repassLabel.grid(row=5, column=0, sticky=W, padx=20)
        entry_repass.grid(row=5, column=1, padx=20)
        emailLabel.grid(row=6, column=0, sticky=W, padx=20)
        entry_email.grid(row=6, column=1, padx=20)
        ACBLnumLabel.grid(row=7, column=0, sticky=W, padx=20)
        entry_ACBL.grid(row=7, column=1, padx=20)
        disIDLabel.grid(row=8, column=0, sticky=W, padx=20)
        entry_disID.grid(row=8, column=1, padx=20)
        b.grid(row=8, columnspan=2, padx=20, pady=20)


        def get_Signup_input():
            fname = 'aditi'
            lname = 'pai'
            user = 'akp69'
            passwd = '123'
            #email = 'akp69@njit.edu'
            #ACBLnum = '456'
            #disID = '789'

            if entry_fname.get() == fname  and entry_lname.get() == lname and entry_user.get() == user \
                    and (entry_pass.get() and entry_repass.get()) == passwd:
                r = Tk()
                r.title(':D')
                r.geometry('150x150')
                rlbl = Label(r, text='\n[+] Signed Up!')
                rlbl.pack()
                r.mainloop()
            else:
                r = Tk()
                r.title(':D')
                r.geometry('150x150')
                rlbl = Label(r, text='\n[!] Invalid Sign Up')
                rlbl.pack()
                r.mainloop()

        def go_to_Tutorial():
            window = Toplevel()
            window.geometry("600x500")
            quitButton = Button(window, text="Cancel", font="Arial 14", command= window.destroy).pack(side="bottom", padx=20)

            top_Frame = Frame(window)
            top_Frame.pack()
            tLabel = Label(top_Frame, text="TUTORIAL", font="Arial 36").pack(side="top", fill="both", expand=True, padx=20, pady=20)

        def combined_Functions(self):  # for the Sign Up button - store data, exits Sign Up screen, goes to Tutorial screen
            get_Signup_input()
            # top.destroy()
            go_to_Tutorial()



root = Tk()
MainMenu(root).pack(fill="both", expand=True)
root.mainloop()