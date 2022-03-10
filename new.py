from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import pymysql
from tkinter import messagebox
import tkinter as tk



class HMS(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1200x700+200+70")
        self.resizable(False, False)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Login, MainMenu, BookApp, Covid):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title('HOSPITAL MANAGEMENT SYSTEM')
        self.controller.geometry("1200x700+200+70")
        self.controller.resizable(False, False)

        # adding image on root window
        self.image = ImageTk.PhotoImage(file="doctor picture.jpg")
        self.label = Label(self, image=self.image)
        self.label.pack()

        # creating heading for root window
        self.lbel = Label(self, text="HOSPITAL MANAGEMENT SYSTEM", font=("Times New Roman", 20, 'bold'), bg='grey')
        self.lbel.place(x=0, y=0, width=1200, height=80)

        # creating frame on root window
        self.frame = Frame(self)
        self.frame.place(x=485, y=130, width=500, height=400)

        self.userlabel = Label(self.frame, text="USERNAME", font=("Andalus", 15, 'bold'), bg='white', fg='black')
        self.userlabel.place(x=80, y=50)

        self.entry1 = Entry(self.frame, font=("Andalus", 15))
        self.entry1.place(x=80, y=100, width=300)

        self.passlabel = Label(self.frame, text="PASSWORD", font=("Andalus", 15, 'bold'), bg='white', fg='black')
        self.passlabel.place(x=80, y=150)

        self.entry2 = Entry(self.frame, show="*", font=("Andalus", 15))
        self.entry2.place(x=80, y=200, width=300)

        self.button = Button(self.frame, text='LOGIN', activebackground="#0000F0", activeforeground="white", fg='black',
                             bg='#F0F8FF', font=("Arial", 15, 'bold'), command=lambda: logindata(self))
        self.button.place(x=180, y=260, width=100)

        # creating 'create login' button on frame
        self.button1 = Button(self.frame, text="Create Login", activebackground='white',
                              command=lambda: self.fwindow()
                              , font=("Times New Roman", 13, 'bold'), fg='black', bd=0)
        self.button1.place(x=80, y=340)

        ####DATABASE ACCESS####
        def logindata(self):
            con = pymysql.connect(user="root", host="localhost", passwd="timtu123", database="project")
            cur = con.cursor()
            cur.execute("Select * from login where username=%s and password=%s", (self.entry1.get(), self.entry2.get()))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("WARNING ERROR", "USER NOT FOUND")
            else:
                messagebox.showinfo("SUCCESS", "Login successful")
                controller.show_frame('MainMenu')

    # creating button and labels for create login window
    def fwindow(self):
        createwindow = Toplevel()
        self.createwindow = createwindow
        self.createwindow.title("CREATE LOGIN")
        self.createwindow.geometry("600x500+450+250")
        self.createwindow.resizable(False, False)

        self.userID = Label(self.createwindow, text="USERNAME (Ph no.)", font=("Andalus", 15, 'bold'), bg='white',
                            fg='black')
        self.userID.place(x=100, y=90)

        self.entry3 = Entry(self.createwindow, font=("Andalus", 15))
        self.entry3.place(x=100, y=140, width=250)

        self.userID = Label(self.createwindow, text="PASSWORD", font=("Andalus", 15, 'bold'), bg='white',
                            fg='black')
        self.userID.place(x=100, y=190)

        self.entry4 = Entry(self.createwindow, show="*", font=("Andalus", 15))
        self.entry4.place(x=100, y=240, width=250)

        self.userID = Label(self.createwindow, text="CONFIRM PASSWORD", font=("Andalus", 15, 'bold'), bg='white',
                            fg='black')
        self.userID.place(x=100, y=290)

        self.entry5 = Entry(self.createwindow, show="*", font=("Andalus", 15))
        self.entry5.place(x=100, y=340, width=250)

        self.chbutton = Button(self.createwindow, text="CREATE LOGIN", activebackground="#0000F0",
                               activeforeground="white", fg='black', bg='#F0F8FF', font=("Andalus", 15, 'bold'),
                               bd=5, command=lambda: self.chpass())
        self.chbutton.place(x=200, y=390, width=250)

    # For create window database connection
    def chpass(self):
        if self.entry3.get() == '' and self.entry4.get() == '' and self.entry5.get() == '':
            messagebox.showerror("Warning", "All fields required")

        else:
            con = pymysql.connect(user="root", host="localhost", passwd="timtu123", database="project")
            cur = con.cursor()
            if len(self.entry3.get()) != 10:
                messagebox.showinfo("ERROR", 'Username can only be 10 digits')
            else:
                cur.execute("insert into login values (%s,%s); ", (self.entry3.get(), self.entry4.get()))
                con.commit()
                con.close()
                messagebox.showinfo("SUCCESS", "NEW LOGIN CREATED SUCCESSFULLY")


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("HOSPITAL MANAGEMENT SYSTEM")
        self.controller.geometry("1200x700+200+70")
        self.controller.resizable(False, False)

        # adding image on root window
        self.image1 = ImageTk.PhotoImage(file="docpicmainmenu.jpg")
        self.label1 = Label(self, image=self.image1)
        self.label1.pack()

        # creating heading for root window
        self.lbel1 = Label(self, text="MAIN MENU", font=("Times New Roman", 20, 'bold'), bg='light grey')
        self.lbel1.place(x=0, y=0, width=1200, height=80)

        # creating frame on root window
        self.frame1 = Frame(self)
        self.frame1.place(x=500, y=120, width=520, height=550)

        self.button2 = Button(self, text='BOOK APPOINTMENT', activebackground="#0000F0", activeforeground="white",
                              fg='black',
                              bg='#F0F8FF', font=("Andalus", 15, 'bold'),
                              command=lambda: controller.show_frame("BookApp"))
        self.button2.place(x=600, y=200, width=300)

        self.button3 = Button(self, text='COVID-19 VACCINE', activebackground="#0000F0", activeforeground="white",
                              fg='black', bg='#F0F8FF', font=("Andalus", 15, 'bold'),
                              command=lambda: controller.show_frame("Covid"))
        self.button3.place(x=600, y=380, width=300)

        self.button5 = Button(self, text='Logout', activebackground="#0000F0", activeforeground="white",
                              fg='black', bg='#F0F8FF', font=("Andalus", 15, 'bold'),
                              command=lambda: controller.show_frame("Login"))
        self.button5.place(x=600, y=560, width=300)

        self.lbel2 = Label(self, text="PLEASE CHOOSE AN OPTION FROM BELOW", font=("Times New Roman", 20, 'bold'),
                           bg='grey')
        self.lbel2.place(x=0, y=0, width=1200, height=80)


class BookApp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Adding image on bookapp window
        self.image = ImageTk.PhotoImage(file="docpicbookapp.jpg")
        self.label = Label(self, image=self.image)
        self.label.pack()

        # Creating heading for bookapp window
        self.lbel = Label(self, text="BOOK AN APPOINTMENT", font=("Times New Roman", 20, 'bold'), bg='grey')
        self.lbel.place(x=0, y=0, width=1200, height=80)
        self.controller.geometry("1200x700+200+70")
        self.controller.resizable(False, False)

        self.lbel1 = Label(self, text="NAME:", font=("Andalus", 18, 'bold'), activebackground="#0000F0",
                           activeforeground="white",
                           fg='black', bg='#F0F8FF')
        self.lbel1.place(x=150, y=110, height=40)

        self.entry1 = Entry(self, font=("Andalus", 15), fg="black", bg="lightgrey")
        self.entry1.place(x=150, y=170, width=300, height=40)

        self.lbel2 = Label(self, text="CONTACT NUMBER:", font=("Andalus", 18, 'bold'), activebackground="#0000F0",
                           activeforeground="white",
                           fg='black', bg='#F0F8FF')
        self.lbel2.place(x=150, y=240, height=40)

        self.entry2 = Entry(self, font=("Andalus", 15), fg="black", bg="lightgrey")
        self.entry2.place(x=150, y=300, width=300, height=40)

        # date and time of appointment
        self.lbel_date = Label(self, text="DATE OF APPOINTMENT:", font=("Andalus", 18, 'bold'),
                               activebackground="#0000F0",
                               activeforeground="white",
                               fg='black', bg='#F0F8FF')
        self.lbel_date.place(x=750, y=110, height=40)

        date_dropdown = ttk.Combobox(self, font=("Andalus", 15), state='readonly', justify=CENTER)
        date_dropdown['values'] = (
            '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th',
            '15th','16th','17th', '18th', '19th', '20th', '21th', '22th', '23th', '24th', '25th', '26th', '27th', '28th', '29th',
            '30th', '31st')
        date_dropdown.current(0)
        date_dropdown.place(x=750, y=170, width=300, height=40)

        self.lbel_time = Label(self, text="TIME SLOT:", font=("Andalus", 18, 'bold'),
                               activebackground="#0000F0",
                               activeforeground="white",
                               fg='black', bg='#F0F8FF')
        self.lbel_time.place(x=750, y=240, height=40)

        time_dropdown = ttk.Combobox(self, font=("Andalus", 15), state='readonly', justify=CENTER)
        time_dropdown['values'] = ("8am-10am", "10am-12pm", "1pm-3pm", "3pm-5pm", "5pm-7pm", "7pm-9pm")
        time_dropdown.current(0)
        time_dropdown.place(x=750, y=300, width=300, height=40)

        #Buttons to return to main menu and confirm appointment
        self.button5 = Button(self, text='Go back to Main Menu', activebackground="#0000F0", activeforeground="white",
                              fg='black', bg='#F0F8FF', font=("Andalus", 15, 'bold'),
                              command=lambda: controller.show_frame("MainMenu"))
        self.button5.place(x=200, y=600, width=300)

        self.chbutton = Button(self, text='Book Appointment', activebackground="#0000F0", activeforeground="white",
                               fg='black', bg='#F0F8FF', font=("Andalus", 15, 'bold'),
                               bd=5, command=lambda: chpass1())
        self.chbutton.place(x=700, y=600, width=300)

        # choosing specialities
        self.lbel3 = Label(self, text="CHOOSE THE REQUIRED SPECIALTY:", font=("Andalus", 18, 'bold'),
                           activebackground="#0000F0",
                           activeforeground="white",
                           fg='black', bg='#F0F8FF')
        self.lbel3.place(x=150, y=370, height=40)

        # Choosing doctor
        self.lbel3 = Label(self, text="CHOOSE DOCTOR:", font=("Andalus", 18, 'bold'),
                           activebackground="#0000F0",
                           activeforeground="white",
                           fg='black', bg='#F0F8FF')
        self.lbel3.place(x=750, y=370, height=40)

        # function for list of doctors
        def choose_doc(e):
            if speciality_dropdown.get() == "Pediatrics":
                con = pymysql.connect(user="root", host="localhost", passwd="timtu123", database="project")
                cur = con.cursor()
                query = ("select name from doctor where specialty = 'pediatrics'")
                cur.execute(query)
                data = cur.fetchall()
                l = []
                for i in data:
                    for x in i:
                        l.append(x)
                doc_dropdown.config(value=l)
                doc_dropdown.current(0)
                con.commit()
                con.close()
            elif speciality_dropdown.get() == "Cardiology":
                con = pymysql.connect(user="root", host="localhost", passwd="timtu123", database="project")
                cur = con.cursor()
                query = ("select name from doctor where specialty = 'cardiology'")
                cur.execute(query)
                data = cur.fetchall()
                l = []
                for i in data:
                    for x in i:
                        l.append(x)
                doc_dropdown.config(value=l)
                doc_dropdown.current(0)
                con.commit()
                con.close()
            elif speciality_dropdown.get() == "Neurology":
                con = pymysql.connect(user="root", host="localhost", passwd="timtu123", database="project")
                cur = con.cursor()
                query = ("select name from doctor where specialty = 'neurology'")
                cur.execute(query)
                data = cur.fetchall()
                l = []
                for i in data:
                    for x in i:
                        l.append(x)
                doc_dropdown.config(value=l)
                doc_dropdown.current(0)
                con.commit()
                con.close()
            elif speciality_dropdown.get() == "Gynecology":
                con = pymysql.connect(user="root", host="localhost", passwd="timtu123", database="project")
                cur = con.cursor()
                query = ("select name from doctor where specialty = 'gynecology'")
                cur.execute(query)
                data = cur.fetchall()
                l = []
                for i in data:
                    for x in i:
                        l.append(x)
                doc_dropdown.config(value=l)
                doc_dropdown.current(0)
                con.commit()
                con.close()
            elif speciality_dropdown.get() == "Orthopedics":
                con = pymysql.connect(user="root", host="localhost", passwd="timtu123", database="project")
                cur = con.cursor()
                query = ("select name from doctor where specialty = 'orthopedics'")
                cur.execute(query)
                data = cur.fetchall()
                l = []
                for i in data:
                    for x in i:
                        l.append(x)
                doc_dropdown.config(value=l)
                doc_dropdown.current(0)
                con.commit()
                con.close()

        # drop down for list of specialities
        speciality_dropdown = ttk.Combobox(self, font=("Andalus", 15), state='readonly', justify=CENTER)
        speciality_dropdown['values'] = ("Pediatrics", "Cardiology", "Gynecology", "Orthopedics", "Neurology")
        speciality_dropdown.current(0)
        speciality_dropdown.place(x=150, y=430, width=300, height=40)
        speciality_dropdown.bind("<<ComboboxSelected>>", choose_doc)

        doc_dropdown = ttk.Combobox(self, font=("Andalus", 15), state='readonly', justify=CENTER)
        doc_dropdown['values'] = (" ")
        doc_dropdown.place(x=750, y=430, width=300, height=40)

        # inserting values into sql table
        def chpass1():
            if self.entry1.get() == '' or self.entry2.get() == '' or speciality_dropdown.get() == '' or date_dropdown.get() == '' or time_dropdown.get() == '':
                messagebox.showerror("Warning", "All fields required")
            else:
                con = pymysql.connect(user="root", host="localhost", passwd="timtu123", database="project")
                cur = con.cursor()
                cur.execute("select * from appointment")
                data = cur.fetchall()
                if (self.entry1.get(), self.entry2.get(), speciality_dropdown.get(), doc_dropdown.get(),
                     date_dropdown.get(),
                     time_dropdown.get()) in data:
                    messagebox.showinfo("ERROR", 'Appointment already exists!')
                else:
                    cur.execute(
                        "insert into appointment(name,contact,specialty,doc_name,appt_date,appt_time) values (%s,%s,%s,%s,%s,%s); ",
                        (self.entry1.get(), self.entry2.get(), speciality_dropdown.get(), doc_dropdown.get(),
                         date_dropdown.get(),
                         time_dropdown.get()))
                    con.commit()
                    con.close()


                if speciality_dropdown.get() == 'Pediatrics':
                    messagebox.showinfo("SUCCESS", 'Appointment Confirmed!! Your Fee is: 600Rs ')
                if speciality_dropdown.get() == 'Cardiology':
                    messagebox.showinfo("APPOINTMENT CONFIRMED", 'Your Fee is: 1000Rs ')
                if speciality_dropdown.get() == 'Gynecology':
                    messagebox.showinfo("APPOINTMENT CONFIRMED", 'Your Fee is: 800Rs ')
                if speciality_dropdown.get() == 'Orthopedics':
                    messagebox.showinfo("APPOINTMENT CONFIRMED", 'Your Fee is: 700Rs ')
                if speciality_dropdown.get() == 'Neurology':
                    messagebox.showinfo("APPOINTMENT CONFIRMED", 'Your Fee is: 900Rs ')


class Covid(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.lbel = Label(self, text="COVID-19 VACCINATION", font=("Times New Roman", 20, 'bold'), bg='grey')
        self.lbel.place(x=0, y=0, width=1200, height=80)
        self.controller.geometry("1200x700+200+70")
        self.controller.resizable(False, False)

        # Adding image on covid window
        self.image = ImageTk.PhotoImage(file="bgimage2 copy.jpg")
        self.label = Label(self, image=self.image)
        self.label.pack()

        # Creating heading for covid window
        self.lbel = Label(self, text="BOOK A VACCINATION APPOINTMENT", font=("Times New Roman", 20, 'bold'), bg='grey')
        self.lbel.place(x=0, y=0, width=1200, height=80)
        self.controller.geometry("1200x700+200+70")
        self.controller.resizable(False, False)

        self.lbel1 = Label(self, text="NAME:", font=("Andalus", 18, 'bold'), activebackground="#0000F0",
                           activeforeground="white",
                           fg='black', bg='rosy brown')
        self.lbel1.place(x=150, y=120, height=40)

        self.entry1 = Entry(self, font=("Andalus", 15), fg="black", bg="white")
        self.entry1.place(x=150, y=180, width=300, height=40)

        self.lbel2 = Label(self, text="CONTACT NUMBER:", font=("Andalus", 18, 'bold'), activebackground="#0000F0",
                           activeforeground="white",
                           fg='black', bg='rosy brown')
        self.lbel2.place(x=150, y=270, height=40)

        self.entry2 = Entry(self, font=("Andalus", 15), fg="black", bg="white")
        self.entry2.place(x=150, y=330, width=300, height=40)

        # Choosing Vaccine
        self.lbel3 = Label(self, text="CHOOSE VACCINE:", font=("Andalus", 18, 'bold'),
                           activebackground="rosy brown",
                           activeforeground="white",
                           fg='black', bg='rosy brown')
        self.lbel3.place(x=150, y=420, height=40)

        vacc_dropdown = ttk.Combobox(self, font=("Andalus", 15), state='readonly', justify=CENTER)
        vacc_dropdown['values'] = ("Covishield", "Covaxin")
        vacc_dropdown.current(0)
        vacc_dropdown.place(x=150, y=480, width=300, height=40)

        # Choosing dose
        self.lbel4 = Label(self, text="CHOOSE DOSE:", font=("Andalus", 18, 'bold'),
                           activebackground="rosy brown",
                           activeforeground="white",
                           fg='black', bg='rosy brown')
        self.lbel4.place(x=750, y=420, height=40)

        dose_dropdown = ttk.Combobox(self, font=("Andalus", 15), state='readonly', justify=CENTER)
        dose_dropdown['values'] = ("1st Dose", "2nd Dose")
        dose_dropdown.current(0)
        dose_dropdown.place(x=750, y=480, width=300, height=40)

        # date and time of appointment
        self.lbel_date = Label(self, text="DATE OF APPOINTMENT:", font=("Andalus", 18, 'bold'),
                               activebackground="#0000F0",
                               activeforeground="white",
                               fg='black', bg='rosy brown')
        self.lbel_date.place(x=750, y=120, height=40)

        date_dropdown = ttk.Combobox(self, font=("Andalus", 15), state='readonly', justify=CENTER)
        date_dropdown['values'] = (
            '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th',
            '15th','16th','17th', '18th', '19th', '20th', '21th', '22th', '23th', '24th', '25th', '26th', '27th', '28th', '29th',
            '30th','31st')
        date_dropdown.current(0)
        date_dropdown.place(x=750, y=180, width=300, height=40)

        self.lbel_time = Label(self, text="TIME SLOT:", font=("Andalus", 18, 'bold'),
                               activebackground="#0000F0",
                               activeforeground="white",
                               fg='black', bg='rosy brown')
        self.lbel_time.place(x=750, y=270, height=40)

        time_dropdown = ttk.Combobox(self, font=("Andalus", 15), state='readonly', justify=CENTER)
        time_dropdown['values'] = ("8am-10am", "10am-12pm", "1pm-3pm", "3pm-5pm", "5pm-7pm", "7pm-9pm")
        time_dropdown.current(0)
        time_dropdown.place(x=750, y=330, width=300, height=40)

        # Buttons to return to main menu and confirm appointment
        self.button5 = Button(self, text='Go back to Main Menu', activebackground="#0000F0", activeforeground="white",
                              fg='black', bg='seashell3', font=("Andalus", 15, 'bold'),
                              command=lambda: controller.show_frame("MainMenu"))
        self.button5.place(x=250, y=600, width=300)

        self.chbutton = Button(self, text='Book Appointment', activebackground="#0000F0", activeforeground="white",
                               fg='black', bg='seashell3', font=("Andalus", 15, 'bold'),
                               bd=5, command=lambda: chpass1())
        self.chbutton.place(x=650, y=600, width=300)

        # inserting values into sql table
        def chpass1():
            if self.entry1.get() == "" or self.entry2.get() == "" or vacc_dropdown.get() == '' or date_dropdown.get() == '' and time_dropdown.get() == '':
                messagebox.showerror("Warning", "All fields required")

            else:
                con = pymysql.connect(user="root", host="localhost", passwd="timtu123", database="project")
                cur = con.cursor()
                cur.execute("select * from covid_appointment")
                data = cur.fetchall()
                if (self.entry1.get(), self.entry2.get(), vacc_dropdown.get(), dose_dropdown.get(),
                        date_dropdown.get(),
                        time_dropdown.get()) in data:
                    messagebox.showinfo("ERROR", 'Appointment already exists!')
                else:
                    cur.execute(
                        'insert into covid_appointment(name,contact,vaccine,dose,cov_date,cov_time) values (%s,%s,%s,%s,%s,%s); ',
                        (
                            self.entry1.get(), self.entry2.get(), vacc_dropdown.get(), dose_dropdown.get(),
                            date_dropdown.get(),
                            time_dropdown.get()))
                    con.commit()
                    con.close()


                if vacc_dropdown.get() == 'Covishield':
                    messagebox.showinfo("APPOINTMENT CONFIRMED", 'Your Fee is: 700Rs ')
                if vacc_dropdown.get() == 'Covaxin':
                    messagebox.showinfo("APPOINTMENT CONFIRMED", 'Your Fee is: 500Rs ')


if __name__ == "__main__":
    app = HMS()
    app.mainloop()