#crime record management system project
#program starts
from tkinter import *     #importing tkinter
import sqlite3            #importing sqlite3 for database work
from tkinter import messagebox    #importing messagebox from tkinter
f2 = Tk()
f2.config(bg="#333333")   #SETTING PAGE COLOUR TO CHARCOAL GRAY FOR LOGIN PAGE
f2.title("Login Page")    #giving page title as Login Page
f2.geometry("1500x600")   #setting geometry size for login page
def login(event):         #defining function Login
    if tx1.get()==""or tx2.get()=="":
        #giving if condition such that if user does not enters anything
        #then it will show an error to enter all fields
        messagebox.showerror("Error"," All fields are required!!!")
    elif tx1.get()=="CHANDRA SHEKHAR SINGH" and tx2.get()=="POLICE@220":
        #giving elif condition such that if user name and password
        #is entered correctly then on account will get open
        messagebox.showinfo("Successfull","You have successfully logged in")
        f1 = Toplevel(f2)
        f1.config(bg="#333333")   #giving page colour charcoal gray
        f2.withdraw()
        f1.title("USER ACCOUNT")  #giving page title as user account which displays after successfully logging in

        def add_fir(event):
            #creating function add_fir() for ADD FIR PAGE
            #add_fir() function starts
            f3 = Toplevel(f2)
            f3.config(bg="#333333") #setting page colour to Charcoal gray
            f1.destroy()
            f3.title("ADD FIR")    #giving page title as ADD FIR

            def submit(event):
                #submit function for Submit button to insert all Data entered by
                #user into adding_fir_1 table in add_fir_1 database
                #submit() function starts
                name = var.get()
                cnic = victim_cnic.get()
                con = victim_contact.get()
                address = v1.get()
                date = incident_date.get()
                place = v2.get()
                officer = v3.get()
                entry = v4.get()
                import sqlite3                               #importing sqlite3
                conn = sqlite3.connect('add_fir_1.db')       #creating database connection
                c = conn.cursor()                            #defining cursor
                #executing query (to conclude if table does not exist then create new table)
                c.execute(
                    "CREATE TABLE IF NOT EXISTS adding_fir_1(VICTIM_NAME text,VICTIM_CNIC text,VICTIM_CONTACT text,VICTIM_ADDRESS text,INCIDENT_DATE text,INCIDENT_PLACE text,INVESTIGATION_OFFICER text,ENTRY_BY text)")
                #executing query for insert operation
                c.execute(
                    "INSERT INTO adding_fir_1 VALUES(:VICTIM_NAME,:VICTIM_CNIC,:VICTIM_CONTACT,:VICTIM_ADDRESS,:INCIDENT_DATE,:INCIDENT_PLACE,:INVESTIGATION_OFFICER,:ENTRY_BY)",
                    {
                        'VICTIM_NAME': name.upper(),
                        'VICTIM_CNIC': victim_cnic.get(),
                        'VICTIM_CONTACT': victim_contact.get(),
                        'VICTIM_ADDRESS': address.upper(),
                        'INCIDENT_DATE': incident_date.get(),
                        'INCIDENT_PLACE': place.upper(),
                        'INVESTIGATION_OFFICER': officer.upper(),
                        'ENTRY_BY': entry.upper()

                    })
                conn.commit()
                conn.close()                 #closing db connection
                if victim_name.get()==""or victim_cnic.get()=="" or victim_contact.get()==""or victim_address==""or incident_date.get()==""or incident_place.get()==""or investigation_officer.get()=="":
                    #giving if condition such that if any data in any field is not entered
                    #by the user then it will show error to enter all fields
                    messagebox.showerror("Error!","All fields are required!!!")
                else:
                    #giving else condition to make sure data is inserted successfully or not
                    messagebox.showinfo('Successfull !!', "You are successfully in...")
                f3.destroy()
                f2.deiconify()
                #end of submit() function

            def reset_add_fir(event):
                #reset function for Reset button to clear all
                # data entered previously
                victim_name.delete(0, END)
                victim_cnic.delete(0, END)
                victim_contact.delete(0, END)
                victim_address.delete(0, END)
                incident_place.delete(0, END)
                incident_date.delete(0, END)
                investigation_officer.delete(0, END)
                entry_by.delete(0, END)
            #creating all GUI controls required for ADD FIR page
            lb1 = Label(f3, text="ADD FIR", height=2, width=10, font="Elephant", fg='white',bg="#333333")
            lb1.grid(row=1, column=8, padx=10, pady=10)
            lb2 = Label(f3, text="PERSONAL INFORMATION",fg="white",bg="#333333", font={"Cooper Black"})
            lb2.grid(row=2, column=8, padx=10, pady=10)
            lb3 = Label(f3, text="VICTIM NAME", font={"Cooper Black"},fg="white",bg="#333333")
            lb3.grid(row=3, column=4, padx=10, pady=10)
            var = StringVar()
            victim_name = Entry(f3, width=100,bd='5', textvariable=var)
            victim_name.grid(row=3, column=8, padx=10, pady=10)
            lb4 = Label(f3, text="VICTIM CNIC", font={"Cooper Black"},fg="white",bg="#333333")
            lb4.grid(row=4, column=4, padx=10, pady=10)
            victim_cnic = Entry(f3, width=100,bd='5')
            victim_cnic.grid(row=4, column=8, padx=10, pady=10)
            lb5 = Label(f3, text="VICTIM CONTACT", font={"Cooper Black"},fg="white",bg="#333333")
            lb5.grid(row=5, column=4, padx=10, pady=10)
            victim_contact = Entry(f3, width=100,bd='5')
            victim_contact.grid(row=5, column=8, padx=10, pady=10)
            lb6 = Label(f3, text="VICTIM ADDRESS",bd='5', font={"Cooper Black"},fg="white",bg="#333333")
            lb6.grid(row=6, column=4, padx=10, pady=10)
            v1 = StringVar()
            victim_address = Entry(f3,bd='5', width=100, textvariable=v1)
            victim_address.grid(row=6, column=8, padx=10, pady=10)
            lb7 = Label(f3, text="CRIME INFORMATIOIN",fg="white",bg="#333333", font={"Cooper Black"})
            lb7.grid(row=7, column=8, padx=10, pady=10)
            lb8 = Label(f3, text="INCIDENT DATE", font={"Cooper Black"},fg="white",bg="#333333")
            lb8.grid(row=8, column=4, padx=10, pady=10)
            incident_date = Entry(f3,bd='5', width=100)
            incident_date.grid(row=8, column=8, padx=10, pady=10)
            lb9 = Label(f3, text="INCIDENT PLACE",fg="white",bg="#333333", font={"Cooper Black"})
            lb9.grid(row=9, column=4, padx=10, pady=10)
            v2 = StringVar()
            incident_place = Entry(f3, width=100, textvariable=v2)
            incident_place.grid(row=9, column=8, padx=10, pady=10)
            lb10 = Label(f3, text="INVESTIGATION OFFICER", font={"Cooper Black"},fg="white",bg="#333333")
            lb10.grid(row=10, column=4, padx=10, pady=10)
            v3 = StringVar()
            investigation_officer = Entry(f3,bd='5', width=100, textvariable=v3)
            investigation_officer.grid(row=10, column=8, padx=10, pady=10)
            lb11 = Label(f3, text="ENTRY BY", font={"Cooper Black"},fg="white",bg="#333333")
            lb11.grid(row=11, column=4, padx=10, pady=10)
            v4 = StringVar()
            entry_by = Entry(f3, width=100,bd='5', textvariable=v4)
            entry_by.grid(row=11, column=8, padx=10, pady=10)
            bt1 = Button(f3, text="ADD", font={"Cooper Black"}, width=10, bg='darkgray')
            bt1.bind('<Button>', submit)
            bt1.grid(row=15, column=8, padx=10, pady=10)
            bt2 = Button(f3, text="RESET", font={"Cooper Black"}, width=10, bg='darkgray')
            bt2.bind('<Button>', reset_add_fir)
            bt2.grid(row=15, column=9, padx=10, pady=10)
            #end of add_fir() function

        def add_criminal(event):
            #creating add_criminal function for ADD CRIMINAL page
            #add_criminal() function starts
            f4 = Toplevel(f2)
            f4.config(bg="#333333")   #setting page colour to charcoal gray
            f1.destroy()
            f4.geometry("1500x400")   #setting page geometry
            f4.title("ADD CRIMINAL")  #defining page title as ADD CRIMINAL
            def submit1(event):
                #creating function submit1 for submit button
                #submit1() function starts
                cname = c1.get()
                cstatus = c2.get()
                import sqlite3                           #importing sqlite3
                conn = sqlite3.connect('add_fir_1.db')   #creating database connection
                c = conn.cursor()                        #defining cursor
                #execting query to make sure if the table exists already
                #if does not exist then create new table to perform insert query
                c.execute(
                    "CREATE TABLE IF NOT EXISTS add_criminal_1(CRIMINAL_NAME text,CRIMINAL_CNIC text,CRIMINAL_STATUS text)")
                #query for insert operation
                c.execute("INSERT INTO add_criminal_1 VALUES(:CRIMINAL_NAME,:CRIMINAL_CNIC,:CRIMINAL_STATUS)",
                          {
                              'CRIMINAL_NAME': cname.upper(),
                              'CRIMINAL_CNIC': criminal_cnic.get(),
                              'CRIMINAL_STATUS': cstatus.upper()
                          })
                conn.commit()
                conn.close()
                if criminal_name.get()=="" or criminal_status=="" or criminal_cnic=="":
                    #giving if condition to make sure that data in every field is entered
                    messagebox.showerror("Error!","All fields are required!!!")
                else:
                    #giving else condition to make sure all the data entered is inserted
                    #successfully in the table add_criminal_1 in database add_fir_1
                    messagebox.showinfo('Successfull !!', "You are successfully in ...")
                f4.destroy()
                f2.deiconify()
                #end of submit1() function
            #creating submit button
            but1 = Button(f4, text="ADD", font={"Cooper Black"}, bg='darkgray')
            but1.bind('<Button>', submit1)
            but1.grid(row=12, column=2)

            def reset_2(event):
                #defing reset function for reset button to
                # clear all the data previously
                # entered in the entry boxes by the user
                criminal_name.delete(0, END)
                criminal_cnic.delete(0, END)
                criminal_status.delete(0, END)
            #creating different GUI controls required for ADD CRIMINAL page
            labl1 = Label(f4, text="ADD CRIMINAL", font="Elephant",height=4,fg="white",bg="#333333")
            labl1.grid(row=2, column=2)
            labl2 = Label(f4, text="CRIMINAL NAME",fg="white",bg="#333333", font={"Cooper Black"})
            labl2.grid(row=4, column=1, padx=250, pady=10)
            c1 = StringVar()
            criminal_name = Entry(f4, width=80,bd='5', textvariable=c1)
            criminal_name.grid(row=4, column=2, padx=10, pady=10)
            labl3 = Label(f4, text="CRIMINAL CNIC", font={"Cooper Black"},fg="white",bg="#333333")
            labl3.grid(row=3, column=1, padx=20, pady=10)
            criminal_cnic = Entry(f4, width=80,bd='5')
            criminal_cnic.grid(row=3, column=2, padx=10, pady=10)
            labl4 = Label(f4, text="CRIMINAL STATUS",fg="white",bg="#333333", font={"Cooper Black"})
            labl4.grid(row=4, column=1, padx=20, pady=10)
            c2 = StringVar()
            criminal_status = Entry(f4,bd='5', width=80, textvariable=c2)
            criminal_status.grid(row=4, column=2, padx=20, pady=10)
            but2 = Button(f4, text="RESET", font={"Cooper Black"}, bg='darkgray')
            but2.bind('<Button>', reset_2)
            but2.grid(row=12, column=3, padx=20, pady=10)
            #end of add_criminal() function
        def view_fir(event):
            #creating view_fir function for VIEW FIR page
            #view_fir() function starts
            f5 = Toplevel(f2)
            f5.config(bg="#333333")      #setting page background colour to charcoal gray
            f1.destroy()
            f5.geometry("1400x400")      #adjusting page geometry
            f5.title("VIEW FIR")         #giving page title as VIEW FIR
            #creating GUI controls required for view fir page
            lab1 = Label(f5, text="SEARCH   view FIR details", font="Elephant",fg="white",bg="#333333", height="4",bd="2")
            lab1.grid(row=1, column=6,padx=120,pady=10)
            lab3 = Label(f5, text="CRIMINAL NAME(VICTIM NAME)",fg="white",bg="#333333", font={"Cooper Black"})
            lab3.grid(row=4, column=5,padx=120,pady=10)
            varc = StringVar()
            entr1 = Entry(f5,bd='5', textvariable=varc,width='80')
            entr1.grid(row=4, column=6,padx=120,pady=10)
            def res():
                entr1.delete(0,END)
            def search1(event):
                #creating search1 function for search button on view fir page
                #search1 function starts
                import sqlite3           #importing sqlite3
                val1 = varc.get()
                val2 = val1.upper()
                conn = sqlite3.connect('add_fir_1.db') #creating db connection
                c = conn.cursor()                      #defining cursor
                c.execute("select * from adding_fir_1") #executing select query
                s = c.fetchall()
                i = list(sum(s, ()))
                if val2 in i:
                    c.execute("SELECT *FROM adding_fir_1 WHERE VICTIM_NAME=?", (val2,))
                    g = c.fetchone()
                    conn.commit()
                    conn.close()
                    messagebox.showinfo('Successfull!',
                                        "VICTIM_NAME={}\n VICTIM_CNIC={}\n VICTIM_CONTACT={}\n VICTIM_ADDRESS={}\n INCIDENT_DATE={}\n INCIDENT_PLACE={}\n INVESTIGATION_OFFICER={}\n ENTRY_BY={}".format(
                                            g[0], g[1], g[2], g[3], g[4], g[5], g[6], g[7]))
                    f5.destroy()
                    f2.deiconify()
                else:
                    messagebox.showwarning('Failed !!', "No such fir....")
                    entr1.delete(0, END)

            butt1 = Button(f5, text="SEARCH", font={"Cooper Black"})
            butt1.bind('<Button>', search1)
            butt1.grid(row=8, column=6)
            butt2 = Button(f5, text="RESET", font={"Cooper Black"},command=res)
            butt2.grid(row=8, column=7)
            #end od view_fir() function
        def view_criminal(event):
            #creating view_criminal function for VIEW CRIMINAL page
            #view_criminal function starts
            f6 = Toplevel(f2)
            f6.config(bg="#333333")   #setting page colour to Charcoal gray
            f1.destroy()
            f6.geometry("1200x400")   #adjusting geometry
            f6.title("VIEW CRIMINAL")      #giving page title as VIEW CRIMINAL
            valv = StringVar()
            et1 = Entry(f6,bd='5',width=80, textvariable=valv)
            et1.grid(row=4, column=5)
            val2 = str(et1.get())

            def reset_1(event):
                #creating reset function for reset button to clear all presviously
                # entered data in entryboxes by the user
                et1.delete(0, END)
                #end of reset() function
            def Search2(event):
                #creating Search2 function for performing select query
                #Search2() function starts
                val3 = valv.get()
                val4 = val3.upper()
                import sqlite3                          #importing sqlite3
                conn = sqlite3.connect('add_fir_1.db')  #creating db connection
                c = conn.cursor()                       #defining cursor
                c.execute("select * from add_criminal_1")#executing selecting query
                m = c.fetchall()
                j = list(sum(m, ()))
                if val4 in j:
                    c.execute("SELECT *FROM add_criminal_1 where CRIMINAL_NAME=?", (val4,))
                    rec = c.fetchone()
                    conn.commit()
                    conn.close()
                    messagebox.showinfo('Successfull !!',
                                        "CRIMINAL_NAME = {} \n CRIMINAL_CINI = {} \n CRIMINAL_STATUS = {} \n".format(
                                            rec[0],
                                            rec[1],
                                            rec[2]))
                    f6.destroy()
                    f2.deiconify()
                else:
                    #giving else condition to make sure if the criminal name does not exist
                    messagebox.showwarning('Failed !!', " No such Criminal...")
                    et1.delete(0, END)

            # creating all GUI controls required for VIEW CRIMINAL page
            la1 = Label(f6, text="SEARCH    view criminal details",fg="white",bg="#333333",height='4', font={"Elephant"})
            la1.grid(row=1, column=5,padx=120,pady=10)
            la3 = Label(f6, text="CRIMINAL CNIC",fg="white",bg="#333333", font={"Cooper Black"})
            la3.grid(row=4, column=4,padx=120,pady=10)
            b1 = Button(f6, text="SEARCH", font={"Cooper Black"})
            b1.bind('<Button>', Search2)
            b1.grid(row=6, column=5,padx=120,pady=10)
            b2 = Button(f6, text="RESET", font={"Cooper Black"})
            b2.bind('<Button>', reset_1)
            b2.grid(row=6, column=6,padx=120,pady=10)
            #end of view_criminal function
        def update(event):
            #update function starts
            f7 = Toplevel(f2)
            f7.config(bg="#333333")     #setting page colour to Charcoal gray
            f7.title("UPDATE")          #giving page title as UPDATE
            f7.geometry("1200x500")     #setting geometry

            def update_cnic(event):
                #update_cnic function starts
                f10 = Toplevel(f2)
                f10.config(bg="#333333")
                f10.title("page 4.1")
                f10.geometry("1500x400")
                def update_1(event):
                    #upadte1() function starts
                    valoi = varo.get()
                    valti = vart.get()
                    import sqlite3
                    conn = sqlite3.connect('add_fir_1.db')
                    c = conn.cursor()
                    c.execute("update add_criminal_1 SET CRIMINAL_CNIC=? where CRIMINAL_NAME=? ", (valti, valoi))
                    conn.commit()
                    conn.close()
                    if et1.get()==""or et.get()=="":
                        messagebox.showerror("Error!","All fields are required!!!")
                    else:
                        messagebox.showinfo("Successfull","Successfully updated")
                    #end of update1() function
                #creating different GUI controls required for UPADTE CNIC page
                lb1 = Label(f10, text="UPADTE CRIMINAL CNIC",fg="white",bg="#333333",height=4, font="Elephant")
                lb1.grid(row=0, column=4,padx=120,pady=10)
                lb2 = Label(f10, text="CRIMINAL NAME",fg="white",bg="#333333", font={"Cooper Black"})
                lb2.grid(row=3, column=3,padx=120,pady=10)
                varo = StringVar()
                et = Entry(f10, width=80,bd='5', textvariable=varo)
                et.grid(row=3, column=4,padx=120,pady=10)
                lb3 = Label(f10, text="UPDATED CRIMINAL CNIC",fg="white",bg="#333333", font={"Cooper Black"})
                lb3.grid(row=4, column=3,padx=120,pady=10)
                vart = StringVar()
                et1 = Entry(f10,bd='5', width=80, textvariable=vart)
                et1.grid(row=4, column=4)
                bt = Button(f10, text="UPDATE", font={"Cooper Black"})
                bt.bind('<Button>', update_1)
                bt.grid(row=6, column=4,padx=120,pady=10)

                def reset_cnic(event):
                    #creating reset_cnic() function for reset button on
                    #update cnic page
                    et.delete(0, END)
                    et1.delete(0, END)

                bt1 = Button(f10, text="RESET", font={"Cooper Black"})
                bt1.bind('<Button>', reset_cnic)
                bt1.grid(row=6, column=5,padx=120,pady=10)
                #end of update_cnic() function
            def update_status(event):
                #creating upadte_status() function for UPADTE STATUS page
                f30 = Toplevel(f2)
                f30.config(bg="#333333")      #setting page colour to charcoal gray
                f30.title("UPDATE STATUS")    #giving page title as UPDATE STATUS
                f30.geometry("1200x400")      #adjusting page geometry

                def reset123(event):
                    #creating reset123() function for reset button
                    en1.delete(0, END)
                    en2.delete(0, END)

                lb = Label(f30, text="UPDATE CRIMINAL STATUS",height=4,fg="white",bg="#333333", font="Elephant")
                lb.grid(row=0, column=3, padx=10, pady=10)
                lb1 = Label(f30, text="CRIMINAL NAME",fg="white",bg="#333333", font={"Cooper Black"})
                lb1.grid(row=2, column=2, padx=10, pady=10)
                vaco = StringVar()
                en1 = Entry(f30,bd='5', width=80, textvariable=vaco)
                en1.grid(row=2, column=3, padx=10, pady=10)
                lb2 = Label(f30, text="UPDATED CRIMINAL STATUS",fg="white",bg="#333333", font={"Cooper Black"})
                lb2.grid(row=3, column=2, padx=10, pady=10)
                vaci = StringVar()
                en2 = Entry(f30, width=80,bd='5', textvariable=vaci)
                en2.grid(row=3, column=3, padx=10, pady=10)
                #end od update_status() function

                def upadte2(event):
                    #update2() function starts
                    valoi = vaco.get()
                    valti = vaci.get()
                    import sqlite3                            #importing sqlite3
                    conn = sqlite3.connect('add_fir_1.db')    #creating db connection
                    c = conn.cursor()
                    #executing update query
                    c.execute("update add_criminal_1 SET CRIMINAL_STATUS=? where CRIMINAL_NAME=? ", (valti, valoi))
                    conn.commit()
                    conn.close()
                    if en1.get()==""or en2.get()=="":
                         #giving else condition to make sure the all fields are entered
                         messagebox.showerror("Error!","All fields are required!!!")
                    else:
                        #testing else condition to make sure the data is updated successfully or not
                         messagebox.showinfo("Successfull","Successfully updated")
                    #end of update2() function
                bt = Button(f30, text="UPDATE", font={"Cooper Black"})
                bt.bind('<Button>', upadte2)
                bt.grid(row=4, column=3, padx=10, pady=10)
                bt1 = Button(f30, text="RESET", font={"Cooper Black"})
                bt1.bind('<Button>', reset123)
                bt1.grid(row=4, column=4, padx=10, pady=10)
                #end of update() function
            #creating different GUI controls for UPDATE page
            lb = Label(f7, text="UPADTE CRIMINAL DETAILS",height=4,fg="white",bg="#333333", font="Elephant")
            lb.grid(row=0, column=2,padx=120,pady=20)
            bt = Button(f7, text="UPDATE CRIMINAL CNIC", font={"Cooper Black"})
            bt.bind('<Button>', update_cnic)
            bt.grid(row=2, column=2,padx=120,pady=20)
            bt1 = Button(f7, text="UPDATE CRIMINAL STATUS", font={"Cooper Black"})
            bt1.bind('<Button>', update_status)
            bt1.grid(row=3, column=2,padx=120,pady=20)
        #creating different controls required for USER ACCOUNT page
        btn100 = Button(f1, text="ADD FIR", font={"Cooper Black"}, bg='light gray', width=20)
        btn100.bind('<Button>', add_fir)
        btn100.grid(row=10, column=100, padx=600, pady=30)
        btn101 = Button(f1, text="ADD CRIMINAL", font={"Cooper Black"}, bg='light gray', width=20)
        btn101.bind('<Button>', add_criminal)
        btn101.grid(row=20, column=100, padx=200, pady=30)
        btn102 = Button(f1, text="VIEW FIR", font={"Cooper Black"}, bg='lightgray', width=20)
        btn102.bind('<Button>', view_fir)
        btn102.grid(row=30, column=100, padx=200, pady=30)
        btn103 = Button(f1, text="VIEW CRIMINAL", font={"Cooper Black"}, bg='light gray', width=20)
        btn103.bind('<Button>', view_criminal)
        btn103.grid(row=40, column=100, padx=200, pady=30)
        btn104 = Button(f1, text="UPDATE", font={"Cooper Black"}, bg='light gray', width=20)
        btn104.bind('<Button>', update)
        btn104.grid(row=50, column=100, padx=200, pady=30)
    else:
        #giving else condition to make sure the username
        #as well as password entered by the user is correct or incorrect
        messagebox.showerror("Error!"," incorrect username and password!!!")
    #end of login() function
def reset(event):
    #creating reset function to clear all previously entered data
    #in different entryboxes on login page
    #reset() function starts
    tx1.delete(0, END)
    tx2.delete(0, END)
    #end of reset() function

def about_us():
    #creating about_us function to display information about maharashtra police
    #about_us() function starts
    f0=Toplevel(f2)
    f0.config(bg="#333333")
    f0.geometry("1600x1500")
    f0.title("About us")
    lb=Label(f0,text="MAHRASHTRA POLICE",font="Elephant",bg="white")
    lb.grid(row=0,column=0)
    lb1=Label(f0,text="Maharashtra, the third largest State in Republic of India, has one of the largest police forces in the country.Besides 250 Indian Police Service",bg="#333333",font={"Cooper black"},fg="white")
    lb1.grid(row=2,column=0)
    lb30=Label(f0,text="officers borne on the State Cadre, it consists of 277 Superintendents of Police,652 Deputy Superintendents of Police, 3530 Inspectors,4530 Assistant",bg="#333333",font={"Cooper black"},fg="white")
    lb30.grid(row=3, column=0)
    lb40=Label(f0,text=" Police Inspectors,7601 Sub Inspectors and 1,84,745 men (members of constabulary).Maharashtra, a highly industrialized State with large urban ",bg="#333333",font={"Cooper black"},fg="white")
    lb40.grid(row=4, column=0)
    lb2=Label(f0,text="conglomerates,has adopted Commissionerates system for policing its large cities. The State has 11 Commissionerates and 36 district police units.",bg="#333333",font={"Cooper black"},fg="white")
    lb2.grid(row=5,column=0)
    lb50=Label(f0,text="Details about these units as well as special units of Maharashtra Police Department are available under sub-head Districts & Commissionerates and ",bg="#333333",font={"Cooper black"},fg="white")
    lb50.grid(row=6, column=0)
    lb70=Label(f0,text="Special Units of MPD on the menu bar of the home page.The motto of Maharashtra Police is .It means that Maharashtra Police is committed to PROTECTING",bg="#333333",font={"Cooper black"},fg="white")
    lb70.grid(row=7, column=0)
    lb60=Label(f0,text=" THE RIGHTOUS AND CONTROLLING & ANNIHILATING THE EVIL. Maharashtra Police is headed by Director General of Police. ",bg="#333333",font={"Cooper black"},fg="white")
    lb60.grid(row=8, column=0)
    lb200=Label(f0,text="Maharashtra Police Head Quarter",font="Elephant",bg="white")
    lb200.grid(row=10,column=0)
    lb201=Label(f0,text="The Maharashtra Police Headquarters was shifted to the present heritage building in Year 1982.At that time, the state police force with a strength of",bg="#333333",font={"Calibri"},fg="white")
    lb201.grid(row=11, column=0)
    lb202=Label(f0,text="87000 was headed by an officer of the rank of Inspector General of Police. Today, the force has increased beyond 2,00,000 and is headed by the ",bg="#333333",font={"Cooper black"},fg="white")
    lb202.grid(row=12, column=0)
    lb205=Label(f0,text="Director General of Police.The present heritage building has a long history. The construction of this building, as the Royal Alfred Sailors Home, ",bg="#333333",font={"Cooper black"},fg="white")
    lb205.grid(row=13, column=0)
    lb207=Label(f0,text="commenced in Feb.1872 and was completed in 1876 at a cost of Rs.3,66,629 (Rs.2000 less than the estimated cost !). His Highness Maharaja Khanderao ",bg="#333333",font={"Cooper black"},fg="white")
    lb207.grid(row=14, column=0)
    lb209=Label(f0,text="Gaekwad of Baroda had donated Rs.200,000 for this prestigious building.This building was conceived to commemorate the visit of the Duke of Edinburgh ",bg="#333333",font={"Cooper black"},fg="white")
    lb209.grid(row=15, column=0)
    lb301=Label(f0,text="in 1870. The duke laid the Foundation, during his visit, at the lower end of Hornby Row.This site,however, was changed and the foundation stone was",bg="#333333",font={"Cooper black"},fg="white")
    lb301.grid(row=16, column=0)
    lb304=Label(f0,text="re laid on a new site when construction commenced on February 18th, 1872.Architect Stevens designed this 270 feet long and 58 feet wide building  ",bg="#333333",font={"Cooper black"},fg="white")
    lb304.grid(row=17, column=0)
    lb306=Label(f0,text="ingeniously using blue basalt in the facing with different colored natural stones in the detailing, to impart an incredible polychromatic effect,  ",bg="#333333",font={"Cooper black"},fg="white")
    lb306.grid(row=18, column=0)
    lb308=Label(f0,text="which were used in many of the building he later designed.The building is divided into two wings, the north one being 110 feet by 58 feet and the  ",bg="#333333",font={"Cooper black"},fg="white")
    lb308.grid(row=19, column=0)
    lb400=Label(f0,text="south wing was originally allocated as quarters for the superintendent.Dining rooms for officers and sailors were located to the north end of the ",bg="#333333",font={"Cooper black"},fg="white")
    lb400.grid(row=20, column=0)
    lb401=Label(f0,text="ground floor with a grand entrance hall with a paneled teak ceiling at the centre. Iron railings placed on neatly designed ground arches protect ",bg="#333333",font={"Cooper black"},fg="white")
    lb401.grid(row=21, column=0)
    lb403=Label(f0,text="the blue basalt stone stairs. The southern half of the ground floor accommodated a large library,the superintendent's office and storerooms.  ",bg="#333333",font={"Cooper black"},fg="white")
    lb403.grid(row=22, column=0)
    lb405=Label(f0,text="The entire north wing of the first floor was set apart for the officer's dormitory. The remainder portion of this section and the second floor,",bg="#333333",font={"Cooper black"},fg="white")
    lb405.grid(row=23, column=0)
    lb407=Label(f0,text=" with the exception of a small portion at the extreme south of the building was used by seamen. In the yard were servant' quarters and a fine ",bg="#333333",font={"Cooper black"},fg="white")
    lb407.grid(row=24, column=0)
    lb409=Label(f0,text="bowling and a skittle alley.The Home was built to accommodate 20 officers and 100 seamen,with provision for additional accommodation when needed.",bg="#333333",font={"Cooper black"},fg="white")
    lb409.grid(row=25, column=0)
    lb501=Label(f0,text=" A sculpture of Neptune in has-relief adorns the pediment at the top, with red Mangalore tiles on the pitched roof.The sculptures were crafted ",bg="#333333",font={"Cooper black"},fg="white")
    lb501.grid(row=26, column=0)
    lb503=Label(f0,text="by students of the J J School of Art under the supervision of John Lockwood Kipling (father of renowned writer, Rudyard Kipling),who had been ",bg="#333333",font={"Cooper black"},fg="white")
    lb503.grid(row=27, column=0)
    lb505=Label(f0,text="appointed Professor of Architectural Sculpture at the School in 1865.The State police Head Quarter is located at Mumbai.",bg="#333333",font={"Cooper black"},fg="white")
    lb505.grid(row=28, column=0)
    #end of about_us() function
def help():
    #creating help() function for HELP? page
    #help() function starts
    f73=Toplevel(f2)
    f73.title("Help?")
    f73.config(bg="#333333")
    f73.geometry("1100x500")
    #creating different functions to display different mesages in different messageboxes
    def h_fir():
        messagebox.showinfo("ADD FIR","Login > ADDFIR > Enter all criminal details > ADD ")
    def h_crim():
        messagebox.showinfo("ADD CRIMINAL","login > ADD CRIMINAL > Enter all criminal details > ADD ")
    def h_s_fir():
        messagebox.showinfo("SEARCH FIR","Login > VIEW FIR > Enter CRIMINAL NAME > SEARCH")
    def h_s_crim():
        messagebox.showinfo("SEARCH CRIMINAL","Login > VIEW CRIMINAL > Enter CRIMINAL NAME > SEARCH ")
    def h_u_cnic():
        messagebox.showinfo("UPDATE CRIMINAL CNIC","Login > UPDATE > PDATE CNIC > Enter CRIMINAL NAME and UPDATED CNIC > UPDATE")
    def h_u_status():
        messagebox.showinfo("UPDATE CRIMINAL STATUS","Login > UPDATE > UPDATE STATUS > Enter CRIMINAL NAME and UPDATED STATUS > UPDATE")
    #creating different GUI controls for HELP page
    lb=Label(f73,text="HELP",font='Elephant',fg="white",bg="#333333")
    lb.grid(row=0,column=2,padx=200,pady=30)
    btn1=Button(f73,text="HOW TO ADD NEW FIR?",font={"Times new roman"},fg="white",bg="#333333",command=h_fir)
    btn1.grid(row=1,column=2,padx=200,pady=10)
    btn2=Button(f73,text="HOW TO ADD NEW CRIMINAL?",font={"Times new roman"},fg="white",bg="#333333",command=h_crim)
    btn2.grid(row=2,column=2,padx=200,pady=10)
    btn3=Button(f73,text="HOW TO SEARCH FOR FIR DETAILS OF PARTICULAR CRIMINAL?",font={"Times new roman"},fg="white",bg="#333333",command=h_s_fir)
    btn3.grid(row=3,column=2,padx=200,pady=10)
    btn4=Button(f73,text="HOW TO SEARCH FOR CRIMINAL DETAILS OF PARTICULAR CRIMINAL",font={"Times new roman"},fg="white",bg="#333333",command=h_s_crim)
    btn4.grid(row=4, column=2,padx=200,pady=10)
    btn5=Button(f73,text="HOW TO UPDATE CRIMINAL STATUS?",font={"Times new roman"},fg="white",bg="#333333",command=h_u_status)
    btn5.grid(row=5, column=2,padx=200,pady=10)
    btn6=Button(f73,text="HOW TO UPDATE CRIMINAL CNIC?",font={"Times new roman"},fg="white",bg="#333333",command=h_u_cnic)
    btn6.grid(row= 6,column= 2,padx=200,pady=10)
    #end of help() function
def complain():
    #creating complain() function for COMPLAIN page
    #complain() function starts
    cm=Toplevel(f2)
    cm.title("COMPLAIN")            #giving page title as COMPLAIN
    cm.geometry("1200x400")         #adjusting geometry
    cm.config(bg="#333333")
    def c_reset():
        #defining c_reset() function for reset button complain page
        et.delete(0,END)
    def sub():
        #defining function sub()
        #for insert query to insert all complains by user
        #sub() function starts
        import sqlite3                        #importing sqlite3
        conn = sqlite3.connect('add_fir_1.db')#creating db connection
        c = conn.cursor()
        #executing query to create table if it does not exist
        c.execute(
            "CREATE TABLE IF NOT EXISTS complain1(COMPLAIN text)")
        c.execute(
            "INSERT INTO complain1 VALUES(:COMPLAIN)",
            {
                'COMPLAIN':et.get()

            })
        if et.get()=="":
            #giving if condition to make sure whether the complain is entered
            messagebox.showwarning("Error!","Please! Enter Your complain")
        conn.commit()
        conn.close()
        #end of sub() function
    def show():
        #defining function show() for peerforming select query to
        #display all complains
        #show() function starts
        conn = sqlite3.connect('add_fir_1.db')
        command="select *from complain1"
        res=conn.execute(command)
        for row in res:
            COMPLAIN=row
            print(COMPLAIN)
        conn.close()
        cm.destroy()
        f2.deiconify()
        #end of show() function
    #creating different controls required for COMPLAIN page
    lb=Label(cm,text="COMPLAIN",height=6,fg="white", width=12,bg="#333333",font="Elephant")
    lb.grid(row=1,column=2)
    lb1=Label(cm,text="Enter your complain here:",height=4,bg='#333333',fg="white",font={"Times new roman"})
    lb1.grid(row=2,column=1)
    et=Entry(cm,bd='5',width='80')
    et.grid(row=2,column=2)
    btn1=Button(cm,text="SUBMIT",font={"Times new roman"},command=sub)
    btn1.grid(row=3,column=2)
    btn2=Button(cm,text="RESET",font={"Times new roman"},command=c_reset)
    btn2.grid(row=3,column=3)
    btn3=Button(cm,text="COMPLAIN BOX",font={"Cooper black"},bg="white",fg="red",command=show)
    btn3.grid(row=0,column=4)
    #end of complain() function
#creating different GUI controls for LOGIN page
lb10 =Label(text="LOGIN", height=4,fg="white", width=12,bg="#333333",font="Elephant")
lb10.grid(row=1, column=1)
lab=Button(text="ABOUT US",font={"Times new roman"},command=about_us,fg="White",bg="#333333")
lab.grid(row=0,column=2)
lb = Label(f2, text="User Name",height=3,font={"Times new roman"},fg="white",bg="#333333")
lb.grid(row=2, column=0, padx=150, pady=10)
tx1 = Entry(f2,bd='5', width=80,font={"Times new roman"})
tx1.grid(row=2, column=1)
lb1 = Label(f2, text="Password",fg="white",height=3,font={"Times new roman"},bg='#333333')
lb1.grid(row=3, column=0,padx=150,pady=10)
tx2 = Entry(f2,bd='5', show="*", width=80,font={"Times new roman"})
tx2.grid(row=3, column=1)
btn1 = Button(f2, text="LOGIN",font={"Times new roman"})
btn1.bind('<Button>',login)
btn1.grid(row=5, column=1, padx=200, pady=10)
btn2 = Button(f2, text="RESET",font={"Times new roman"})
btn2.grid(row=5, column=2)
btn2.bind('<Button>', reset)
btn200 = Button(f2,text="HELP?",bg='#333333',fg="white",font={"Times new roman"},command=help)
btn200.grid(row=0, column=0)
btnw=Button(text="COMPLAIN",bg='#333333',fg="white",font={"Times new roman"},command=complain)
btnw.grid(row=0,column=1)
#end of GUI controls for login page
f2.mainloop()
#end of the program
