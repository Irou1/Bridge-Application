from tkinter import *
import mysql.connector as mysql
from MySQLdb import dbConnect
import datetime


class MainMenu(Frame):
    def __init__(self, parent):  #The very first screen of the web app
        Frame.__init__(self, parent)
        frame = Frame(parent)
        frame.pack()

        w, h = parent.winfo_screenwidth(), parent.winfo_screenheight()
        parent.overrideredirect(1)
        parent.geometry("%dx%d+0+0" % (w, h))

        #bkgrd = PhotoImage(file="C:\\Users\\kanip\\PycharmProjects\\Desktop\\Bridge_played_cards_after_game.png")
        #bkgrd_label = Label(frame, image=bkgrd)
        #bkgrd_label.image = bkgrd
        #bkgrd_label.place(x=0, y=0, relwidth=1, relheight= 1)


        titleLabel = Label(frame, text="LET'S PLAY BRIDGE",fg ="black" ,font ='Arial 36')
        titleLabel.pack(side="top",pady = 150)
        loginButton = Button(frame, text="Log in",fg ="blue",font ="Arial 14",command= self.LoginScreen)
        loginButton.pack(side = 'right')
        signupButton = Button(frame, text="Sign up", fg ="blue",font ="Arial 14",command= self.SignupScreen)
        signupButton.pack(side ="right")
        quitButton = Button(frame, text="Quit",font ="Arial 14",command= quit)
        quitButton.pack(side="bottom")
        myProfileButton = Button(frame, text="My Profile", fg="blue", font="Arial 14", command=self.myProfileScreen)
        myProfileButton.pack(side="right")

    def LoginScreen(self):
        global entry_user
        global entry_pass
        top = Toplevel(self)
        top.title("Log In - ABCL")
        w, h = top.winfo_screenwidth(), top.winfo_screenheight()
        top.overrideredirect(1)
        top.geometry("550x400+%d+%d" % (w/2-275, h/2-125)) #250
        top.configure(background = 'white')
        quitButton = Button(top, text="Cancel", font="Arial 14", command= top.destroy).pack(side="bottom", padx=20)

        #entry_user = StringVar()
        #entry_pass = StringVar()

        # Frames to divide the window into three parts.. makes it easier to organize the widgets
        topFrame = Frame(top)
        topFrame.pack()
        middleFrame = Frame(top)
        middleFrame.pack(pady=50)
        bottomFrame = Frame(top)
        bottomFrame.pack(side=BOTTOM)

        # Widgets and which frame they are in
        #label = Label(topFrame, text="LET'S PLAY BRIDGE")
        userLabel = Label(middleFrame, text='Username:', font="Arial 14")
        passLabel = Label(middleFrame, text='Password:', font="Arial 14")
        entry_user = Entry((middleFrame) ) # For DB
        entry_pass = Entry(middleFrame, show ='*') # For DB
        b = Button(bottomFrame, text="Log in",font = 'Arial 14',command=lambda: get_Login_input())

        #Location of the Widgets in their frames
        #label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        userLabel.grid(row=10, column=0, sticky=W, padx=20)
        entry_user.grid(row=10, column=1, padx=20)
        passLabel.grid(row=11, column=0, sticky=W, padx=20)
        entry_pass.grid(row=11, column=1, padx=20)
        b.grid(row=12, columnspan=2)

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
                r.geometry('250x200')
                #get first name and last name of current player
                cur.execute("SELECT firstname, lastname FROM playerinfo WHERE username = '%s' AND password = '%s'" % (entry_user.get(), entry_pass.get()))
                for namerow in cur.fetchall():  # print all the first cell
                    fn = namerow[0] #store firstname
                    ln = namerow[1] #store lastname

                rlb1 = Label(r, text='\nWelcome %s %s\n' % (fn, ln))
                rlb1.pack()
                rlb2 = Label(r, text='\nUserName: %s' % entry_user.get())
                rlb2.pack()
                r.mainloop()
            else:
                r = Tk()
                r.title(':D')
                r.geometry('150x150')
                rlbl = Label(r, text='\n[!] Invalid Login')
                rlbl.pack()
                r.mainloop()

            dbconn.close()
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
        w, h = top.winfo_screenwidth(), top.winfo_screenheight()
        top.overrideredirect(1)
        top.geometry("550x450+%d+%d" % (w / 2 - 275, h / 2 - 140))  # 250
        top.configure(background='white')
        quitButton = Button(top, text="Cancel", font="Arial 14", command= top.destroy).pack(side="bottom", padx=20)
        #topFrame = Frame(top)
        #topFrame.pack()
        middleFrame = Frame(top)
        middleFrame.pack(pady=50)
        bottomFrame = Frame(top)
        bottomFrame.pack(side=BOTTOM)

        # Widgets and which frame they are in
        #label = Label(topFrame, text="LET'S PLAY BRIDGE")

        fnameLabel = Label(middleFrame,text = 'First Name:',font="Arial 14")
        lnameLabel = Label(middleFrame, text='Last Name:',font="Arial 14")
        userLabel = Label(middleFrame, text='Username:',font="Arial 14")
        passLabel = Label(middleFrame, text='Password:',font="Arial 14")
        repassLabel = Label(middleFrame, text='Re-Enter Password:',font="Arial 14")
        emailLabel = Label(middleFrame, text='Email(optional):',font="Arial 14")
        ACBLnumLabel = Label(middleFrame, text='ACBLnum(optional):',font="Arial 14")
        disIDLabel = Label(middleFrame, text='DistrictID(optional):',font="Arial 14")
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
        #label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        fnameLabel.grid(row=1, column=0, sticky=W)
        entry_fname.grid(row=1, column=1)
        lnameLabel.grid(row=2, column=0, sticky=W)
        entry_lname.grid(row=2, column=1)
        userLabel.grid(row=3, column=0, sticky=W)
        entry_user.grid(row=3, column=1)
        passLabel.grid(row=4, column=0, sticky=W)
        entry_pass.grid(row=4, column=1)
        repassLabel.grid(row=5, column=0, sticky=W)
        entry_repass.grid(row=5, column=1)
        emailLabel.grid(row=6, column=0, sticky=W)
        entry_email.grid(row=6, column=1, padx=20, sticky= W)
        ACBLnumLabel.grid(row=7, column=0, sticky=W)
        entry_ACBL.grid(row=7, column=1, padx=20)
        disIDLabel.grid(row=8, column=0, sticky=W)
        entry_disID.grid(row=8, column=1)
        b.grid(row=10, columnspan=2)

##############DATABASE Check if Username is available, check if passwords Match -> if so SIGN UP!!!!!!!!!!!!!!!
        def get_Signup_input():
            var = dbConnect()
            dbconn = mysql.connect(host=var.host, user=var.user, password=var.password, db=var.db)
            cur = dbconn.cursor()  # Cursor object - required to execute all queries

            cur.execute("SELECT username FROM playerinfo WHERE username = '%s'" % entry_user.get())
            rows = cur.fetchall()
            if not rows:
                # print(userInput + " is available")
                if (entry_pass.get() == entry_repass.get()) and (entry_pass.get()!= "") and (entry_repass.get()!= ""):
                    # print("passwords match, good job brotha")
                    # INSERT
                    todaysdate = datetime.datetime.today().strftime('%Y-%m-%d')  # current date
                    cur.execute("INSERT INTO playerinfo(username, password, signUpDate, firstname, lastname, email, ACLnum, districtID) VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                    entry_user.get(), entry_pass.get(), todaysdate, entry_fname.get(), entry_lname.get(), entry_email.get(),entry_ACBL.get(), entry_disID.get()))


                    dbconn.commit()

                    r = Tk()
                    r.title(':D')
                    r.geometry('150x150')
                    rlbl = Label(r, text='\n[+] Signed Up!')
                    rlbl.pack()
                    r.mainloop()

                else:
                    # print("passwords don't match bruh or are NULL")
                    r = Tk()
                    r.title(':D')
                    r.geometry('150x150')
                    rlbl = Label(r, text='\n[!] Retype your passwords')
                    rlbl.pack()
                    r.mainloop()
            else:
                r = Tk()
                r.title(':D')
                r.geometry('150x150')
                rlbl = Label(r, text='\n[!] Username Not Available ')
                rlbl.pack()
                r.mainloop()

            dbconn.close()

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

    def myProfileScreen(self):
        top = Toplevel(self)
        w, h = top.winfo_screenwidth(), top.winfo_screenheight()
        top.overrideredirect(1)
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        top.overrideredirect(1)
        top.geometry("%dx%d+0+0" % (w, h))
        topFrame = Frame(top)
        topFrame.pack()
        bottomFrame = Frame(top)
        bottomFrame.pack(side=BOTTOM)
        rightFrame = Frame(top)
        rightFrame.pack(side= RIGHT)
        leftFrame = Frame(top)
        leftFrame.pack(side=LEFT)


        label = Label(topFrame, text="LET'S PLAY BRIDGE",font =('Coralva', 42)).pack(side="top", fill="both", expand=True)
        mpLabel = Label(rightFrame, text='My Profile', font = ('Comic Sans MS',24)).grid(ipadx = 200, columnspan = 2)
        nameLabel = Label(rightFrame, text='Name:', font = ('Comic Sans MS',14)).grid(row=1, column=0, sticky = W)
        userLabel = Label(rightFrame, text='Username:', font = ('Comic Sans MS',14)).grid(row=2, column=0, sticky = W)
        emailLabel = Label (rightFrame, text='Email:', font = ('Comic Sans MS',14)).grid(row=3, column=0, sticky = W)
        sLabel = Label(rightFrame, text='Signup Date:', font = ('Comic Sans MS',14)).grid(row=4, column=0, sticky = W)
        disIDLabel = Label(rightFrame, text='DistrictID:', font = ('Comic Sans MS',14)).grid(row=5, column=0, sticky = W)
        ACBLnumLabel = Label(rightFrame, text='ACBL #:', font = ('Comic Sans MS',14)).grid(row=6, column=0, sticky = W)
        nothing = Label(rightFrame).grid(row=7, column=0)
        msLabel= Label(rightFrame, text='My Stats', font = ('Comic Sans MS',14, 'bold')).grid(row=8, column=0, sticky = W)
        dpLabel = Label(rightFrame, text='Deals Played: ', font = ('Comic Sans MS',14)).grid(row=9, column=0, sticky = W)
        levelLabel = Label(rightFrame, text='Level: ', font = ('Comic Sans MS',14)).grid(row=10, column=0, sticky = W)
        expLabel = Label(rightFrame, text='Experience: ', font = ('Comic Sans MS',14)).grid(row=11, column=0, sticky = W)
        coinsLabel = Label(rightFrame, text='Coins: ', font = ('Comic Sans MS',14)).grid(row=12, column=0, sticky = W)
        tourLabel = Label(rightFrame, text='Tournaments: ', font = ('Comic Sans MS',14)).grid(row=13, column=0, sticky = W)

        b = Button(bottomFrame, text="HOME",font = 'Arial 12').pack(side=LEFT)   #FIND A IMAGE OF A HOUSE
        quitButton = Button(bottomFrame, text="CANCEL", command=top.destroy, font = 'Arial 12').pack(side = RIGHT)




root = Tk()
MainMenu(root).pack(fill="both", expand=True)
root.mainloop()