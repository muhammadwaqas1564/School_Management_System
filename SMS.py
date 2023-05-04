from tkinter import*
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from time import strftime
import pymysql
from tkinter.ttk import Treeview
import os
from tkinter import messagebox as m_box
from tkinter import filedialog
from tkcalendar import DateEntry;
import datetime

from docx.api import Document

import fee_and_result_and_certificate_generate as F_R

class CMS:
    def __init__(self):
        # self.win = win
        self.win=Tk()
        self.win.title('CMS')
        self.win.configure(background= '#0b9798')
        self.win.overrideredirect(True)
        self.win.overrideredirect(False)
        self.win.attributes('-fullscreen',True)



        # ================================================================
        # ===============================  create database and connection
        database_name="CMS"
        self.conn = pymysql.connect(host="localhost",
                                user="root",
                                password=""
                )
        self.courser = self.conn.cursor()
        self.courser.execute(f"CREATE DATABASE IF NOT EXISTS {database_name} ")
        
        self.conn = pymysql.connect(host="localhost",
                                user="root",
                                password="",
                                database=database_name
        )
        self.courser = self.conn.cursor()


        # # ==========================================================================
        # # ===========================================================   LOGO 
        top_frame = Frame(self.win,bg="#0d8888",height=30,relief=RIDGE,bd=2)
        top_frame.pack(side=TOP,fill=X)
        
        def tick():
            date_string = strftime("%d/%m/%Y")
            date_label.configure(text = "Date : "+date_string)

        date_frame = Frame(top_frame,bg="#0d8888")
        date_frame.pack(side=LEFT)
        date_label =  Label(date_frame,background="#0d8888",fg='white',font=("Bookman Old Style",20))
        date_label.pack()
        tick()

        def time():
            string = strftime('%H:%M:%S  %p')
            time_label.config(text="Time : "+string)
            time_label.after(1000,time)

        time_frame = Frame(top_frame,bg="#0d8888")
        time_frame.pack(side=RIGHT)
        time_label = Label(time_frame,background="#0d8888",fg='white',font=("Bookman Old Style",20))
        time_label.pack()
        time()

        
        # ==========================================================================
        # ============================================ School Name in first page 
        heding_frame = Frame(top_frame,bg="#0d8888")
        heding_frame.pack()

        SN1_label = Label(heding_frame,text="New Informatics model school",font=("ALGERIAN",23),background="#0d8888",foreground="white")
        SN1_label.pack()

        SN2_label = Label(heding_frame,text="NIMS & college  (dherai swat)",font=("ALGERIAN",18),
            background="#0d8888",foreground="white")
        SN2_label.pack()
        contect_no_label = Label(heding_frame,text="Contect No : 0123456789 ",fg="white",bg="#0d8888",font=("Times New Roman",13))
        contect_no_label.pack()
        Email_label = Label(heding_frame,text="Email: abc@gmail.com ",fg="white",bg="#0d8888",font=("Times New Roman",12))
        Email_label.pack()

       
        # ==========================================================================
        # ============================================  left side buttons frame
        left_side_buttons_frame = Frame(self.win,bg="#0b9798",width=30,relief=RIDGE,bd=1)
        left_side_buttons_frame.pack(fill=Y,side=LEFT)

        # ===========================================================================
        self.main_frame = Frame(self.win,height=600,width=845,bg="#0b9798")
        self.main_frame.pack()
        
        self.logo_frame = Frame(self.main_frame,height=600,width=850,bg="#0b9798")
        self.logo_frame.place(x=0,y=0)

        # ===========================================================================
        # ====================================================   show Logo 
        img= Image.open("Images\\NIMS LOGO.PNG")
        img=img.resize((405,405),Image.ANTIALIAS)
        img=ImageTk.PhotoImage(img)

        welcome_lbl=Label(self.logo_frame,text="WELCOME TO THE SYSTEM",font=("Times New Roman",40,'bold'),fg='white',bg="#0b9798")
        welcome_lbl.place(x=50,y=10)
        logolab=Label(self.logo_frame,image=img , height=405,width=405)
        logolab.place(x=200,y=100)
        logolab.configure(image=img)
        logolab.image=img


        # ==========================================================================
        # =======================================================  Design buttons
        self.dashboard_btn = ImageTk.PhotoImage(file = "Images\\Dashboard.png")
        self.Admission_btn = ImageTk.PhotoImage(file = "Images\\Admission.png")
        self.Search_btn = ImageTk.PhotoImage(file = "Images\\Search.png")
        self.Withdrawl_btn = ImageTk.PhotoImage(file = "Images\\Withdrawl.png")
        self.Fee_btn = ImageTk.PhotoImage(file = "Images\\Fee.png")
        self.Result_btn = ImageTk.PhotoImage(file = "Images\\Result.png")
        self.Certificate_btn = ImageTk.PhotoImage(file = "Images\\Certificate.png")
        self.course_btn = ImageTk.PhotoImage(file = "Images\\course.png")
        self.promote_btn = ImageTk.PhotoImage(file = "Images\\promote.png")
        self.Logout_btn = ImageTk.PhotoImage(file = "Images\\logout.png")
        self.Quit_btn = ImageTk.PhotoImage(file = "Images\\Quit.png")

        # ------------------>         dashboard first button         <-----------------|
        dashboard_butten = tk.Button(left_side_buttons_frame,image=self.dashboard_btn,bd=0,cursor="hand2",command=self.main_page,
           bg="#0b9798",activebackground="#0b9798").pack(padx=7,pady=2)

        # ------------------>        Add butten first button         <-----------------|
        Add_butten = tk.Button(left_side_buttons_frame,image=self.Admission_btn,bd=0,cursor="hand2",command=self.New_Admission,
           bg="#0b9798",activebackground="#0b9798").pack(pady=2)

        # ------------------>       search butten second button      <-----------------|
        Search_butten = tk.Button(left_side_buttons_frame,image=self.Search_btn,bd=0,cursor="hand2",command=self.search_Student,
            bg="#0b9798",activebackground="#0b9798").pack(pady=2)

        # ------------------>     withdrawl butten   third button    <-----------------|
        Withdrawl_butten = tk.Button(left_side_buttons_frame,image=self.Withdrawl_btn,bd=0,cursor="hand2",command=self.with_drawl_student,
            bg="#0b9798",activebackground="#0b9798").pack(pady=2)

        # ------------------>  Fee Structure butten   fourth button  <-----------------|
        Fee_structure_butten = tk.Button(left_side_buttons_frame,image=self.Fee_btn,bd=0,cursor="hand2",command=self.Fee_Structure,
            bg="#0b9798",activebackground="#0b9798").pack(pady=2)

        # ------------------>      result butten   FIFTH button      <-----------------|
        Result_butten = tk.Button(left_side_buttons_frame,image=self.Result_btn,bd=0,cursor="hand2",command=self.Result_data,
            bg="#0b9798",activebackground="#0b9798").pack(pady=2)

        # ------------------>    certificate butten   sixth button   <-----------------|
        Certificate_butten = tk.Button(left_side_buttons_frame,image=self.Certificate_btn,bd=0,cursor="hand2",command=self.Certificate,
           bg="#0b9798",activebackground="#0b9798").pack(pady=2)

        # ------------------>       course Butten seven Button       <-----------------|
        Course_butten = tk.Button(left_side_buttons_frame,image=self.course_btn,bd=0,cursor="hand2",command=self.Courses,
            bg="#0b9798",activebackground="#0b9798").pack(pady=2)
        # ------------------>           promote  button              <-----------------|
        promote_butten = tk.Button(left_side_buttons_frame,image=self.promote_btn,bd=0,cursor="hand2",command=self.promote_student,
           bg="#0b9798",activebackground="#0b9798").pack(pady=2)
        # ------------------>             logout button              <-----------------|
        logout_butten = tk.Button(left_side_buttons_frame,image=self.Logout_btn,bd=0,cursor="hand2",command=self.Logout,
           bg="#0b9798",activebackground="#0b9798").pack(pady=2)
        # ------------------>                quit button             <-----------------|
        quit_butten = tk.Button(left_side_buttons_frame,image=self.Quit_btn,bd=0,cursor="hand2",command=self.Quit,
           bg="#0b9798",activebackground="#0b9798").pack(pady=2)

        self.win.mainloop()











#                                          Start the function which show the main page
# ===============================================================================================================================
# ===============================================================================================================================
# ==================================    Dashboard
# ===============================================================================================================================
# ===============================================================================================================================  
    
    
    def main_page(self):
        main_page_logo_frame = Frame(self.main_frame,height=600,width=850,bg="#0b9798")
        main_page_logo_frame.place(x=0,y=0)
        img= Image.open("Images\\NIMS LOGO.PNG")
        img=img.resize((405,405),Image.ANTIALIAS)
        img=ImageTk.PhotoImage(img)

        welcome_lbl=Label(main_page_logo_frame,text="WELCOME TO THE SYSTEM",font=("Times New Roman",40,'bold'),fg='white',bg="#0b9798")
        welcome_lbl.place(x=50,y=10)

        logolab=Label(main_page_logo_frame,image=img , height=405,width=405)
        logolab.place(x=200,y=100)
        logolab.configure(image=img)
        logolab.image=img














#                                        Start the functio which save the data of new student
# ================================================================================================================================
# ================================================================================================================================
# ==================================    NEW Admission
# ================================================================================================================================
# ================================================================================================================================

    def New_Admission(self):
        self.main_2_frame = Frame(self.main_frame,height=600,width=850,bg="#0b9798")
        self.main_2_frame.place(x=0,y=0)

        # =============================================================
        # ========================================pick up  next reg No
        self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'new_Admission')")
        admission_table = list(self.courser.fetchall()[0])
        if admission_table[0] == 1:
            self.courser.execute('select Std_Registeration_NO from new_Admission')
            record = self.courser.fetchall()
            w = [i[0] for i in record]
            next_Registeration_No = w[-1]+1
        else:
            next_Registeration_No = 0
        self.reg_no_var =StringVar()
        self.reg_no_var.set(next_Registeration_No )
        self.first_name_var =StringVar()
        self.last_name_var =StringVar()
        self.gender_var =StringVar()
        self.DOB_var =StringVar()
        self.contect_var =StringVar()
        self.BG_var =StringVar()
        self.Email_var =StringVar()
        self.Addmission_var =StringVar()
        self.religion_var =StringVar()
        self.Grade_var =StringVar()
        self.class_no_var =StringVar()
        self.Monthly_Fee_var =StringVar()
        self.Birth_place_var =StringVar()
        self.Address_var =StringVar()
        # -----------------------  Student BIO DATA
        self.Father_name_var = StringVar()
        self.F_Contect_no_var = StringVar()
        self.F_CNIC_var = StringVar()
        # ----------------------- LAst School Attended
        self.Last_School_name_var = StringVar()
        self.Last_School_name_var.set("")
        self.Date_of_Discharge_var = StringVar()
        self.Date_of_Discharge_var.set("")
        self.Prev_Class_var = StringVar()
        self.Prev_Class_var.set("")
        # ------------------------
        self.Admission_fee_var = StringVar()
        self.Admission_fee_var.set(0)
        self.Transport_fee_var = StringVar()
        self.Transport_fee_var.set(0)
        self.Medical_fee_var = StringVar()
        self.Medical_fee_var.set(0)

        # =====================================================
        # =============================  Labels And Entry Boxes
        Std_Record_label = Label(self.main_2_frame,text="Student Record",padx=313,bg='#0b9798',font=("Times New Roman",20),relief=RAISED,bd=1 )
        Std_Record_label.place(x=0,y=2)

        reg_no_label = Label(self.main_2_frame,text="Registeration NO:",background='#0b9798',font=("Times New Roman",13))
        reg_no_label.place(x=20,y=45)
        reg_no_entery_box = Entry(self.main_2_frame , width=11 ,state=DISABLED, textvariable = self.reg_no_var,relief=RIDGE,bd=2,font=("Times New Roman",11))
        reg_no_entery_box.place(x=160,y=45)

        # =====================================================
        first_name_label = Label(self.main_2_frame,text="First name:",background='#0b9798',font=("Times New Roman",13) )
        first_name_label.place(x=20,y=72)
        first_name_entery_box = Entry(self.main_2_frame , width=17, textvariable = self.first_name_var,bd=2,font=("Times New Roman",11))
        first_name_entery_box.place(x=120,y=72)
        first_name_entery_box.focus()  # for curser

        last_name_label = Label(self.main_2_frame,text="Last name:" ,background='#0b9798',font=("Times New Roman",13))
        last_name_label.place(x=320,y=72)
        last_name_entery_box = Entry(self.main_2_frame , width=20 , textvariable = self.last_name_var,bd=2,font=("Times New Roman",11))
        last_name_entery_box.place(x=450,y=72)

        # =====================================================
        gender_label = Label(self.main_2_frame,text="Gender:",background='#0b9798',font=("Times New Roman",13))
        gender_label.place(x=20,y=99)
        gender_combobox = ttk.Combobox(self.main_2_frame,width=17,textvariable = self.gender_var,state="readonly", font=("Times New Roman",10))
        gender_combobox["values"] = ("Male","Female","Other")
        gender_combobox.place(x=120,y=99)

        Todays = datetime.date.today()
        DOB_label = Label(self.main_2_frame,text="Date of Birth:",background='#0b9798',font=("Times New Roman",13))
        DOB_label.place(x=320,y=99)
        DOB_entery_box = DateEntry(self.main_2_frame, width=18,textvariable = self.DOB_var, year=Todays.year, month=Todays.month, day=Todays.day, 
                    background='#0b9798', borderwidth=2,font=("Times New Roman",11))   
        DOB_entery_box.place(x=448,y=99)
        # =========================================
        contect_no_label = Label(self.main_2_frame,text="Contact No:",background='#0b9798',font=("Times New Roman",13))
        contect_no_label.place(x=20,y=126)
        contect_entery_box = Entry(self.main_2_frame,width=17,textvariable=self.contect_var, bd=2,font=("Times New Roman",11))
        contect_entery_box.place(x=120,y=126)

        BG_label = Label(self.main_2_frame,text="Blood Group:",background='#0b9798',font=("Times New Roman",13))
        BG_label.place(x=320,y=126)
        BG_entery_entery_box = ttk.Combobox(self.main_2_frame,width=18,textvariable = self.BG_var,state="readonly", font=("Times New Roman",11))
        BG_entery_entery_box["values"] = ("A+","B+","AB+","A-","B-","AB-","O+","O-")
        BG_entery_entery_box.place(x=448,y=126)


        # =====================================================
        Email_label = Label(self.main_2_frame,text="Email:",background='#0b9798',font=("Times New Roman",13))
        Email_label.place(x=20,y=153)
        Email_entery_box = Entry(self.main_2_frame , width=17 , textvariable = self.Email_var, bd=2,font=("Times New Roman",11))
        Email_entery_box.place(x=120,y=153)

        Addmission_label = Label(self.main_2_frame,text="Admission Date:",background='#0b9798',font=("Times New Roman",13))
        Addmission_label.place(x=320,y=153)
        Addmission_entery_box = DateEntry(self.main_2_frame, width=18,textvariable = self.Addmission_var, year=Todays.year, month=Todays.month, day=Todays.day, 
                    background='#0b9798', borderwidth=2,font=("Times New Roman",11))   
        Addmission_entery_box.place(x=448,y=153)

        # =====================================================
        religion_label = Label(self.main_2_frame,text="Religion:",background='#0b9798',font=("Times New Roman",13))
        religion_label.place(x=20,y=180)
        religion_entery_box = ttk.Combobox(self.main_2_frame , width=17 , textvariable = self.religion_var,state="readonly",font=("Times New Roman",10))
        religion_entery_box["values"]=("Muslim","Non Muslim")
        religion_entery_box.place(x=120,y=180)

        class_label = Label(self.main_2_frame,text="Grade:",background='#0b9798',font=("Times New Roman",13))
        class_label.place(x=320,y=180)
        Grade_entery_box = ttk.Combobox(self.main_2_frame,width=18,textvariable = self.Grade_var,state="readonly", font=("Times New Roman",11))
        Grade_entery_box["values"] = ("Ist","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th")
        Grade_entery_box.place(x=448,y=180)

        # =====================================================
        class_no_label = Label(self.main_2_frame,text="Class No:",background='#0b9798',font=("Times New Roman",13))
        class_no_label.place(x=20,y=207)
        class_no_entery_box = Entry(self.main_2_frame , width=17 , textvariable = self.class_no_var,bd=2,font=("Times New Roman",11))
        class_no_entery_box.place(x=120,y=207)

        Monthly_Fee_label = Label(self.main_2_frame,text="Monthly Fee:",background='#0b9798',font=("Times New Roman",13))
        Monthly_Fee_label.place(x=320,y=207)
        Monthly_Fee_entery_box = Entry(self.main_2_frame , width=20 , textvariable = self.Monthly_Fee_var,bd=2,font=("Times New Roman",11))
        Monthly_Fee_entery_box.place(x=450,y=207)

        # =====================================================
        Birth_place_label = Label(self.main_2_frame,text="Birth Place:",background='#0b9798',font=("Times New Roman",13))
        Birth_place_label.place(x=20,y=234)
        Birth_place_entery_box = Entry(self.main_2_frame , width=67 , textvariable = self.Birth_place_var,bd=2,font=("Times New Roman",11))
        Birth_place_entery_box.place(x=120,y=234)

        Address_label = Label(self.main_2_frame,text="Permanent Address:",background='#0b9798',font=("Times New Roman",13))
        Address_label.place(x=20,y=261)
        Address_entery_box = Entry(self.main_2_frame , width=59 , textvariable = self.Address_var,bd=2,font=("Times New Roman",11))
        Address_entery_box.place(x=177,y=261)

        # ======================================================== 
        # ======================================== Student Bio Data

        Std_Record_label = Label(self.main_2_frame,text="Student Bio Data",padx=304,bg='#0b9798',font=("Times New Roman",20),relief=RAISED,bd=1 )
        Std_Record_label.place(x=0,y=293)

        Father_name_label = Label(self.main_2_frame,text="Father Name:",background='#0b9798',font=("Times New Roman",13) )
        Father_name_label.place(x=20,y=333)
        Father_name_entery_box = Entry(self.main_2_frame , width=19, textvariable = self.Father_name_var,bd=2,font=("Times New Roman",11))
        Father_name_entery_box.place(x=130,y=333)

        F_Contect_no_label = Label(self.main_2_frame,text="Contact No:" ,background='#0b9798',font=("Times New Roman",13))
        F_Contect_no_label.place(x=315,y=333)
        F_Contect_no_entery_box = Entry(self.main_2_frame , width=16 , textvariable = self.F_Contect_no_var, bd=2,font=("Times New Roman",11))
        F_Contect_no_entery_box.place(x=415,y=333)

        F_CNIC_label = Label(self.main_2_frame,text="CNIC:" ,background='#0b9798',font=("Times New Roman",13))
        F_CNIC_label.place(x=580,y=333)
        F_CNIC_entery_box = Entry(self.main_2_frame , width=18 , textvariable = self.F_CNIC_var, bd=2,font=("Times New Roman",11))
        F_CNIC_entery_box.place(x=640,y=333)

        # ========================================================
        # =================================== Last School Attended
        
        Std_Record_label = Label(self.main_2_frame,width=53,text="  *\t\t         Last School Attended ",bg='#0b9798',font=("Times New Roman",20),relief=RAISED,bd=1 ,anchor=W)
        Std_Record_label.place(x=0,y=367)

        Last_School_name_label = Label(self.main_2_frame,text="* School Name:",background='#0b9798',font=("Times New Roman",13) )
        Last_School_name_label.place(x=15,y=404)
        Last_School_name_entery_box = Entry(self.main_2_frame , width=19, textvariable = self.Last_School_name_var ,bd=2,font=("Times New Roman",11))
        Last_School_name_entery_box.place(x=130,y=404)
        Last_School_name_entery_box.focus()  # for curser

        Date_of_Discharge_label = Label(self.main_2_frame,text="* Date of Discharge:" ,background='#0b9798',font=("Times New Roman",13))
        Date_of_Discharge_label.place(x=320,y=404)
        Date_of_Dischargeentery_box = Entry(self.main_2_frame, width=12,textvariable = self.Date_of_Discharge_var, bd=2,font=("Times New Roman",11))   
        Date_of_Dischargeentery_box.place(x=475,y=404)

        Prev_Class_label = Label(self.main_2_frame,text="* Class:" ,background='#0b9798',font=("Times New Roman",13))
        Prev_Class_label.place(x=625,y=404)
        Prev_Class_entery_box = ttk.Combobox(self.main_2_frame,width=8,textvariable = self.Prev_Class_var,state="readonly", font=("Times New Roman",11))
        Prev_Class_entery_box["values"] = ("NULL","Ist","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th")
        Prev_Class_entery_box.place(x=690,y=404)
        
        # ======================================================================
        # ===========================================  Extra data from Student

        Std_Record_label = Label(self.main_2_frame,text="  *",width=53,bg='#0b9798',font=("Times New Roman",20),relief=RAISED,bd=1,anchor=W)
        Std_Record_label.place(x=0,y=439)

        Admission_fee_label = Label(self.main_2_frame,text="Admission Fee:",background='#0b9798',font=("Times New Roman",13) )
        Admission_fee_label.place(x=20,y=482)
        Admission_fee_entery_box = Entry(self.main_2_frame , width=14,textvariable = self.Admission_fee_var, bd=2,font=("Times New Roman",11))
        Admission_fee_entery_box.place(x=142,y=482)

        Transport_fee_label = Label(self.main_2_frame,text="* Transport Fee:" ,background='#0b9798',font=("Times New Roman",13))
        Transport_fee_label.place(x=280,y=482)
        Transport_fee_entery_box = Entry(self.main_2_frame , width=14 , textvariable = self.Transport_fee_var,bd=2,font=("Times New Roman",11))
        Transport_fee_entery_box.place(x=405,y=482)

        Medical_fee_label = Label(self.main_2_frame,text="* Medical Fee:" ,background='#0b9798',font=("Times New Roman",13))
        Medical_fee_label.place(x=550,y=482)
        Medical_fee_entery_box = Entry(self.main_2_frame , width=14 , textvariable = self.Medical_fee_var,bd=2,font=("Times New Roman",11))
        Medical_fee_entery_box.place(x=663,y=483)
        
        # =====================================================
        # ====================================== Upload Picture 
        self.picture = None
        def showimage():
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("All Files","*.*")))
            if len(fln) == 0:
                return None
            else:
                # print(fln)
                img=Image.open(fln)
                img=img.resize((110,125),Image.ANTIALIAS)
                img=ImageTk.PhotoImage(img)
                self.lbl.configure(image=img)
                self.lbl.image=img
                self.picture = fln


        self.pic_frame = Frame(self.main_2_frame,height=133,width=120,relief=GROOVE,bd=2)
        self.pic_frame.place(x=660,y=80)

        self.lbl = Label(self.pic_frame,width=110,height=125)
        self.lbl.place(x=0,y=0)

        btn = Button(self.main_2_frame,text="Upload Picture",padx=10,command=showimage,background="#0d8888",foreground="white",cursor="hand2",
            activebackground="#076d6d",activeforeground = "white")
        btn.place(x=665,y=225)

        def save_data_function():
            name = self.first_name_var.get() +"_"+ self.last_name_var.get()
            if self.first_name_var.get()=="" or self.last_name_var.get()=="" or self.gender_var.get()=="" or self.DOB_var.get()=="" or self.contect_var.get()=="" or self.BG_var.get()=="" or self.Email_var.get()=="" or self.Addmission_var.get()=="" or self.religion_var.get()=="" or self.Grade_var.get()=="" or self.class_no_var.get()=="" or self.Monthly_Fee_var.get()=="" or self.Birth_place_var.get()=="" or self.Address_var.get()=="" or self.Father_name_var.get()=="" or self.F_Contect_no_var.get()=="" or self.F_CNIC_var.get()=="":
                m_box.showerror('Error','Please fill all the compulsary data\nTry again.... ')
            else:
                try:
                    int(self.contect_var.get())
                    int(self.class_no_var.get())
                    int(self.Monthly_Fee_var.get())
                    int(self.F_Contect_no_var.get())
                    int(self.F_CNIC_var.get())
                    int(self.Admission_fee_var.get())
                    int(self.Transport_fee_var.get())
                    int(self.Medical_fee_var.get())
                    
                except ValueError:
                    m_box.showerror('title','Only digite are allowed in the \nContect No, Class No and Monthly fee field\nPlease try again....')
                else:
                    path = os.path.exists("picture")
                    if self.picture==None:
                        pass
                    else:
                        image = Image.open(self.picture)
                        if path==True:
                            image.save(f"picture//{name}_{self.reg_no_var.get()}.jpg")
                        else:
                            os.mkdir("picture")
                            image.save(f"picture//{name}_{self.reg_no_var.get()}.jpg")
                    if len(self.F_CNIC_var.get()) == 13:
                        self.courser.execute("CREATE TABLE IF NOT EXISTS NEW_ADMISSION(Std_Registeration_NO BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT, Std_First_Name VARCHAR(25),Std_Last_Name VARCHAR(25),Std_Father_Name VARCHAR(25),Gander VARCHAR(10),Date_Of_Birth VARCHAR(100),Contect_No BIGINT ,Blood_Group VARCHAR(5),Email VARCHAR(25),Admission_Date VARCHAR(100),Religion VARCHAR(10),Grade VARCHAR(10),Class_no INT, Monthly_Fee BIGINT, Birth_Place VARCHAR(50) , Per_Address VARCHAR(50) ,Father_Contect_No BIGINT ,Father_CNIC varchar(13), Pree_School_Name VARCHAR(25),Date_Of_Discharge VARCHAR(100), Class VARCHAR(10), Admission_Fee BIGINT, Transport_Fee BIGINT,Medical_Fee BIGINT)")
                        self.courser.execute( "Insert Into new_admission (Std_Registeration_NO,Std_First_Name,Std_Last_Name,Std_Father_Name,Gander,Date_Of_Birth,Contect_No,Blood_Group,Email,Admission_Date,Religion,Grade,Class_no,Monthly_Fee,Birth_Place,Per_Address,Father_Contect_No,Father_CNIC,Pree_School_Name,Date_Of_Discharge,Class,Admission_Fee, Transport_Fee,Medical_Fee ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                                            (self.reg_no_var.get(),self.first_name_var.get(),self.last_name_var.get(),self.Father_name_var.get(),self.gender_var.get(),self.DOB_var.get(),self.contect_var.get(),self.BG_var.get(),self.Email_var.get(),
                                            self.Addmission_var.get(),self.religion_var.get(),self.Grade_var.get(),self.class_no_var.get(),self.Monthly_Fee_var.get(),self.Birth_place_var.get(),self.Address_var.get(), self.F_Contect_no_var.get(),
                                            self.F_CNIC_var.get(),self.Last_School_name_var.get(),self.Date_of_Discharge_var.get(),self.Prev_Class_var.get(),self.Admission_fee_var.get(),self.Transport_fee_var.get(),self.Medical_fee_var.get()))
                        
                        m_box.showinfo('Saved',"Your Data is Save Successfuly.....")
                        self.reg_no_var.set("")
                        self.first_name_var.set("")
                        self.last_name_var.set("")
                        self.gender_var.set("")
                        self.DOB_var.set("")
                        self.contect_var.set("")
                        self.BG_var.set("")
                        self.Email_var.set("")
                        self.Addmission_var.set("")
                        self.religion_var.set("")
                        self.Grade_var.set("")
                        self.class_no_var.set("")
                        self.Monthly_Fee_var.set("")
                        self.Birth_place_var.set("")
                        self.Address_var.set("")
                        # -----------------------  Student BIO DATA
                        self.Father_name_var.set("")
                        self.F_Contect_no_var.set("")
                        self.F_CNIC_var.set("")
                        # ----------------------- LAst School Attended
                        self.Last_School_name_var.set("")
                        self.Date_of_Discharge_var.set("")
                        self.Prev_Class_var.set("")
                        # -------------------------
                        self.Admission_fee_var.set("")
                        self.Transport_fee_var.set("")
                        self.Medical_fee_var.set("")
                        self.lbl=Label(self.pic_frame,width=110,height=125)
                        self.lbl.place(x=0,y=0)
                        self.main_page()
                    else:
                        m_box.showerror('length Problem',"Please Correct the CNIC No \nit must be 13 values")
        # =====================================================
        # ============================================  Button
        btn = Button(self.main_2_frame,width= 10,text="Submitte",bg="#0d8888",fg="white",font=("Bookman Old Style",12),cursor="hand2",command=save_data_function,
                        activebackground="#076d6d",activeforeground = "white")
        btn.place(x=345,y=560)














#                                 start the function which search to show, upadte and delete the student data
# ================================================================================================================================
# ================================================================================================================================
# ==================================    search Student
# ================================================================================================================================
# /===============================================================================================================================

    def search_Student(self):
        # ===========================================================
        # ================================  Search Student Frame
        self.main_2_frame = Frame(self.main_frame,height=600,width=850,bg="#0b9798")
        self.main_2_frame.place(x=0,y=0)
        
        # =========================================================
        # =========================== all variable For Search 
        self.reg_var = StringVar()
        self.name_var = StringVar()

        # ----------------------------- Student Information
        self.reg_no_var_s =StringVar()
        self.first_name_var_s =StringVar()
        self.last_name_var_s =StringVar()
        self.gander_var_s =StringVar()
        self.DOB_var_s =StringVar()
        self.contect_var_s =StringVar()
        self.BG_var_s =StringVar()
        self.Email_var_s =StringVar()
        self.Addmission_var_s =StringVar()
        self.religion_var_s =StringVar()
        self.Grade_var_s =StringVar()
        self.class_no_var_s =StringVar()
        self.Monthly_Fee_var_s =StringVar()
        self.Birth_place_var_s =StringVar()
        self.Address_var_s =StringVar()
        # -----------------------  Student BIO DATA
        self.Father_name_var_s = StringVar()
        self.F_Contect_no_var_s = StringVar()
        self.F_CNIC_var_s = StringVar()
        # ----------------------- LAst School Attended
        self.Last_School_name_var_s = StringVar()
        self.Date_of_Discharge_var_s = StringVar()
        self.Prev_Class_var_s = StringVar()
        # ------------------------
        self.Admission_fee_var_s = StringVar()
        self.Transport_fee_var_s = StringVar()
        self.Medical_fee_var_s = StringVar() 
        # ------------------------
        self.image_var = StringVar()
        self.image_var.set("")
        
        # =======================================================================
        # ====================================== Picture function in Search Std
        self.picture = None
        def showimage():
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("All Files","*.*")))
            if len(fln) == 0:
                return None
            else:
                # print(fln)
                img=Image.open(fln)
                img=img.resize((110,125),Image.ANTIALIAS)
                img=ImageTk.PhotoImage(img)
                self.lbl.configure(image=img)
                self.lbl.image=img
                self.picture = fln

        self.pic_frame = Frame(self.main_2_frame,height=133,width=120,relief=GROOVE,bd=2)
        self.pic_frame.place(x=710,y=80)

        self.lbl = Label(self.pic_frame,width=110,height=125)
        self.lbl.place(x=0,y=0)

        btn = Button(self.main_2_frame,text="Upload Picture",padx=10,command=showimage,background="#0d8888",foreground="white",cursor="hand2",
            activebackground="#076d6d",activeforeground = "white")
        btn.place(x=715,y=225)


        # =================================================================
        # ==========================================  All Labels
        self.Frame_left = Frame(self.main_2_frame,width=235,height=600,bg="#0d8888",relief=RIDGE,bd=1)
        self.Frame_left.place(x=0,y=0)
        last_in_left = Frame(self.Frame_left,bg="powder blue")#-------->  frmae are created for scrool
        last_in_left.place(y=251,x=1,height=346,width=230)


        lab = Label(self.Frame_left,text='Search By Registeration No',padx=11,font=("Times New Roman",14),
                    bg="#0d8888",fg="white",relief=RAISED,bd=1)
        lab.place(x=1,y=30)
        entry_box1 = Entry(self.Frame_left, width=21,textvariable=self.reg_var ,font=("Times New Roman",12),relief=RIDGE,bd=2)
        entry_box1.place(x=30,y=60)
        entry_box1.focus()

        lab = Label(self.Frame_left,text='Search By Name',padx=52,font=("Times New Roman",14),bg="#0d8888",fg="white",relief=RAISED,bd=1)
        lab.place(x=1,y=150)
        entry_box1 = Entry(self.Frame_left, width=21,textvariable=self.name_var ,font=("Times New Roman",12),relief=RIDGE,bd=2)
        entry_box1.place(x=30,y=180)
       
        
        # =====================================================
        # =============================  Labels And Entry Boxes
        Std_Record_label = Label(self.main_2_frame,text="Student Record",padx=213,bg='#0b9798',font=("Times New Roman",20),relief=RAISED,bd=1 )
        Std_Record_label.place(x=240,y=2)

        reg_no_label = Label(self.main_2_frame,text="Registeration NO:",background='#0b9798',font=("Times New Roman",13))
        reg_no_label.place(x=240,y=45)
        reg_no_entery_box = Entry(self.main_2_frame , width=11 ,state=DISABLED, textvariable = self.reg_no_var_s,relief=RIDGE,bd=2,font=("Times New Roman",11))
        reg_no_entery_box.place(x=380,y=45)

        # =====================================================
        first_name_label = Label(self.main_2_frame,text="First name:",background='#0b9798',font=("Times New Roman",13))
        first_name_label.place(x=240,y=72)
        first_name_entery_box = Entry(self.main_2_frame , width=12, textvariable = self.first_name_var_s,bd=2,font=("Times New Roman",11),state=DISABLED)
        first_name_entery_box.place(x=330,y=72)

        last_name_label = Label(self.main_2_frame,text="Last name:" ,background='#0b9798',font=("Times New Roman",13))
        last_name_label.place(x=460,y=72)
        last_name_entery_box = Entry(self.main_2_frame , width=12 , textvariable = self.last_name_var_s,bd=2,font=("Times New Roman",11),state=DISABLED)
        last_name_entery_box.place(x=580,y=72)
        
        # =====================================================
        gender_label = Label(self.main_2_frame,text="Gender:",background='#0b9798',font=("Times New Roman",13))
        gender_label.place(x=240,y=99)
        gender_combobox = ttk.Combobox(self.main_2_frame,width=11,textvariable = self.gander_var_s, font=("Times New Roman",10),state=DISABLED)
        gender_combobox["values"] = ("Male","Female","Other")
        gender_combobox.place(x=330,y=99)

        Todays = datetime.date.today()
        DOB_label = Label(self.main_2_frame,text="Date of Birth:",background='#0b9798',font=("Times New Roman",13))
        DOB_label.place(x=460,y=99)
        DOB_entery_box = DateEntry(self.main_2_frame, width=10,textvariable = self.DOB_var_s, year=Todays.year, month=Todays.month, day=Todays.day, 
                    background='#0b9798', borderwidth=2,font=("Times New Roman",11),state=DISABLED)   
        DOB_entery_box.place(x=580,y=99)
        # =========================================
        contect_no_label = Label(self.main_2_frame,text="Contact No:",background='#0b9798',font=("Times New Roman",13))
        contect_no_label.place(x=240,y=126)
        contect_entery_box = Entry(self.main_2_frame,width=12,textvariable=self.contect_var_s, bd=2,font=("Times New Roman",11),state=DISABLED)
        contect_entery_box.place(x=330,y=126)

        BG_label = Label(self.main_2_frame,text="Blood Group:",background='#0b9798',font=("Times New Roman",13))
        BG_label.place(x=460,y=126)
        BG_entery_entery_box = ttk.Combobox(self.main_2_frame,width=10,textvariable = self.BG_var_s, font=("Times New Roman",11),state=DISABLED)
        BG_entery_entery_box["values"] = ("A+","B+","AB+","A-","B-","AB-","O+","O-")
        BG_entery_entery_box.place(x=580,y=126)

  
        # =====================================================
        Email_label = Label(self.main_2_frame,text="Email:",background='#0b9798',font=("Times New Roman",13))
        Email_label.place(x=240,y=153)
        Email_entery_box = Entry(self.main_2_frame , width=12 , textvariable = self.Email_var_s, bd=2,font=("Times New Roman",11),state=DISABLED)
        Email_entery_box.place(x=330,y=153)

        Addmission_label = Label(self.main_2_frame,text="Admission Date:",background='#0b9798',font=("Times New Roman",13))
        Addmission_label.place(x=460,y=153)
        Addmission_entery_box = DateEntry(self.main_2_frame, width=10,textvariable = self.Addmission_var_s, year=Todays.year, month=Todays.month, day=Todays.day, 
                    background='#0b9798', borderwidth=2,font=("Times New Roman",11),state=DISABLED)   
        Addmission_entery_box.place(x=580,y=153)

        # =====================================================
        religion_label = Label(self.main_2_frame,text="Religion:",background='#0b9798',font=("Times New Roman",13))
        religion_label.place(x=240,y=180)
        religion_entery_box = ttk.Combobox(self.main_2_frame , width=11 , textvariable = self.religion_var_s,font=("Times New Roman",10),state=DISABLED)
        religion_entery_box["values"]=("Muslim","Non Muslim")
        religion_entery_box.place(x=330,y=180)

        class_label = Label(self.main_2_frame,text="Grade:",background='#0b9798',font=("Times New Roman",13))
        class_label.place(x=460,y=180)
        Grade_entery_box = ttk.Combobox(self.main_2_frame,width=10,textvariable = self.Grade_var_s, font=("Times New Roman",11),state=DISABLED)
        Grade_entery_box["values"] = ("Ist","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th")
        Grade_entery_box.place(x=580,y=180)

        # =====================================================
        class_no_label = Label(self.main_2_frame,text="Class No:",background='#0b9798',font=("Times New Roman",13))
        class_no_label.place(x=240,y=207)
        class_no_entery_box = Entry(self.main_2_frame , width=12 , textvariable = self.class_no_var_s,bd=2,font=("Times New Roman",11),state=DISABLED)
        class_no_entery_box.place(x=330,y=207)

        Monthly_Fee_label = Label(self.main_2_frame,text="Monthly Fee:",background='#0b9798',font=("Times New Roman",13))
        Monthly_Fee_label.place(x=460,y=207)
        Monthly_Fee_entery_box = Entry(self.main_2_frame , width=12 , textvariable = self.Monthly_Fee_var_s,bd=2,font=("Times New Roman",11),state=DISABLED)
        Monthly_Fee_entery_box.place(x=580,y=207)

        # =====================================================
        Birth_place_label = Label(self.main_2_frame,text="Birth Place:",background='#0b9798',font=("Times New Roman",13))
        Birth_place_label.place(x=240,y=234)
        Birth_place_entery_box = Entry(self.main_2_frame , width=48 , textvariable = self.Birth_place_var_s,bd=2,font=("Times New Roman",11),state=DISABLED)
        Birth_place_entery_box.place(x=330,y=234)

        Address_label = Label(self.main_2_frame,text="Permanent Address:",background='#0b9798',font=("Times New Roman",13))
        Address_label.place(x=240,y=261)
        Address_entery_box = Entry(self.main_2_frame , width=41 , textvariable = self.Address_var_s,bd=2,font=("Times New Roman",11),state=DISABLED)
        Address_entery_box.place(x=380,y=261)

        # ======================================================== 
        # ======================================== Student Bio Data

        Std_Record_label = Label(self.main_2_frame,text="Student Bio Data",padx=204,bg='#0b9798',font=("Times New Roman",20),relief=RAISED,bd=1 )
        Std_Record_label.place(x=240,y=293)

        Father_name_label = Label(self.main_2_frame,text="Father Name:",background='#0b9798',font=("Times New Roman",13))
        Father_name_label.place(x=240,y=333)
        Father_name_entery_box = Entry(self.main_2_frame , width=15, textvariable = self.Father_name_var_s,bd=2,font=("Times New Roman",11),state=DISABLED)
        Father_name_entery_box.place(x=340,y=333)

        F_Contect_no_label = Label(self.main_2_frame,text="Contact No:" ,background='#0b9798',font=("Times New Roman",13))
        F_Contect_no_label.place(x=465,y=333)
        F_Contect_no_entery_box = Entry(self.main_2_frame , width=12 , textvariable = self.F_Contect_no_var_s, bd=2,font=("Times New Roman",11),state=DISABLED)
        F_Contect_no_entery_box.place(x=555,y=333)

        F_CNIC_label = Label(self.main_2_frame,text="CNIC:" ,background='#0b9798',font=("Times New Roman",13))
        F_CNIC_label.place(x=670,y=333)
        F_CNIC_entery_box = Entry(self.main_2_frame , width=15 , textvariable = self.F_CNIC_var_s, bd=2,font=("Times New Roman",11),state=DISABLED)
        F_CNIC_entery_box.place(x=720,y=333)
     
        # ========================================================
        # =================================== Last School Attended
        
        Std_Record_label = Label(self.main_2_frame,width=39,padx=6,text="  *\t        Last School Attended ",bg='#0b9798',font=("Times New Roman",20),relief=RAISED,bd=1 ,anchor=W)
        Std_Record_label.place(x=240,y=367)

        Last_School_name_label = Label(self.main_2_frame,text="* School Name:",background='#0b9798',font=("Times New Roman",13) )
        Last_School_name_label.place(x=240,y=404)
        Last_School_name_entery_box = Entry(self.main_2_frame , width=13, textvariable = self.Last_School_name_var_s ,bd=2,font=("Times New Roman",11),state=DISABLED)
        Last_School_name_entery_box.place(x=355,y=404)

        Date_of_Discharge_label = Label(self.main_2_frame,text="* Date of Discharge:" ,background='#0b9798',font=("Times New Roman",13))
        Date_of_Discharge_label.place(x=455,y=404)
        Date_of_Dischargeentery_box = Entry(self.main_2_frame, width=10,textvariable = self.Date_of_Discharge_var_s, bd=2,font=("Times New Roman",11),state=DISABLED)   
        Date_of_Dischargeentery_box.place(x=605,y=404)

        Prev_Class_label = Label(self.main_2_frame,text="* Class:" ,background='#0b9798',font=("Times New Roman",13))
        Prev_Class_label.place(x=690,y=404)
        Prev_Class_entery_box = ttk.Combobox(self.main_2_frame,width=7,textvariable = self.Prev_Class_var_s,font=("Times New Roman",11),state=DISABLED)
        Prev_Class_entery_box["values"] = ("NULL","Ist","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th")
        Prev_Class_entery_box.place(x=760,y=404)
        
        # ======================================================================
        # ===========================================  Extra data from Student

        Std_Record_label = Label(self.main_2_frame,text="  *",width=42,padx=5,bg='#0b9798',font=("Times New Roman",19),relief=RAISED,bd=1,anchor=W)
        Std_Record_label.place(x=240,y=439)

        Admission_fee_label = Label(self.main_2_frame,text="Admission Fee:",background='#0b9798',font=("Times New Roman",13) )
        Admission_fee_label.place(x=240,y=482)
        Admission_fee_entery_box = Entry(self.main_2_frame , width=10,textvariable = self.Admission_fee_var_s, bd=2,font=("Times New Roman",11),state=DISABLED)
        Admission_fee_entery_box.place(x=355,y=482)

        Transport_fee_label = Label(self.main_2_frame,text="* Transport Fee:" ,background='#0b9798',font=("Times New Roman",13))
        Transport_fee_label.place(x=440,y=482)
        Transport_fee_entery_box = Entry(self.main_2_frame , width=10 , textvariable = self.Transport_fee_var_s,bd=2,font=("Times New Roman",11),state=DISABLED)
        Transport_fee_entery_box.place(x=560,y=482)

        Medical_fee_label = Label(self.main_2_frame,text="* Medical Fee:" ,background='#0b9798',font=("Times New Roman",13))
        Medical_fee_label.place(x=645,y=482)
        Medical_fee_entery_box = Entry(self.main_2_frame , width=10 , textvariable = self.Medical_fee_var_s,bd=2,font=("Times New Roman",11),state=DISABLED)
        Medical_fee_entery_box.place(x=755,y=483)

  

        def search_student_by_ID():
            if self.reg_var.get()=="":
                m_box.showerror('Blank Field Error','Please Enter The Registeration No\n\nTry again.....')
            else:
                try:
                    id=int(self.reg_var.get())
                except ValueError:
                    m_box.showerror('Value Type Error','Only digite are allowed in the\nRegisteration No field\n\nTry again.....')
                else:
                    self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'New_Admission')")
                    search_admission_table = list(self.courser.fetchall()[0])

                    if search_admission_table[0]==1:
                        self.courser.execute(f"Select * from new_Admission where Std_registeration_NO = '{self.reg_var.get()}'")
                        record = self.courser.fetchall()
                        data = [i for i in record]
                        
                        if len(data) == 0:
                            m_box.showerror('Incorrect Registeration No','Sorry.....!\nYour Registeration No is Incorrect\nThere is no Student Whose Registered in this \nRegisteration No\n\nPlease try again.....')
                        else:
                            self.reg_no_var_s.set(data[0][0])
                            self.first_name_var_s.set(data[0][1])
                            self.last_name_var_s.set(data[0][2])
                            self.gander_var_s.set(data[0][4])
                            self.DOB_var_s.set(data[0][5])
                            self.contect_var_s.set(data[0][6])
                            self.BG_var_s.set(data[0][7])
                            self.Email_var_s.set(data[0][8])
                            self.Addmission_var_s.set(data[0][9])
                            self.religion_var_s.set(data[0][10])
                            self.Grade_var_s.set(data[0][11])
                            self.class_no_var_s.set(data[0][12])
                            self.Monthly_Fee_var_s.set(data[0][13])
                            self.Birth_place_var_s.set(data[0][14])
                            self.Address_var_s.set(data[0][15])
                            # -----------------------  Student BIO DATA
                            self.Father_name_var_s.set(data[0][3])
                            self.F_Contect_no_var_s.set(data[0][16])
                            self.F_CNIC_var_s.set(data[0][17])
                            # ----------------------- LAst School Attended
                            self.Last_School_name_var_s.set(data[0][18])
                            self.Date_of_Discharge_var_s.set(data[0][19])
                            self.Prev_Class_var_s.set(data[0][20])
                            # ------------------------
                            self.Admission_fee_var_s.set(data[0][21])
                            self.Transport_fee_var_s.set(data[0][22])
                            self.Medical_fee_var_s.set(data[0][23])
                            
                            # -------------------------------   student picture
                            self.pic = "picture//"+data[0][1]+"_"+data[0][2]+"_"+str(data[0][0])+".jpg"
                            if os.path.exists(self.pic):
                                self.pic=Image.open(self.pic)
                                self.pic=self.pic.resize((110,125),Image.ANTIALIAS)
                                self.pic=ImageTk.PhotoImage(self.pic)
                                self.lbl.configure(image=self.pic)
                                self.lbl.image=self.pic
                            else:
                                self.lbl = Label(self.pic_frame,width=110,height=125)
                                self.lbl.place(x=0,y=0)
                    else:
                        m_box.showerror('Error','Sorry.....!\nThere is no Table on Admission \nplease Registered the Student .....')
        
        # ================================================================================
        # ====================================  Search the Student Record By Student Name            
        def search_student_by_name():
            std_Name = self.name_var.get()
            first = std_Name.split(" ")
            name = "%"+first[0]+"%"

            if self.name_var.get()=="":
                m_box.showerror('Error','Enter Student Name\nplease try again.... ')
            else:
                self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'New_Admission')")
                search_admission_table = list(self.courser.fetchall()[0])

                if search_admission_table[0]==1:
                    right_first1 = Frame(self.Frame_left,bg="powder blue")#-------->  frmae are created for scrool
                    right_first1.place(y=251,x=1,height=346,width=230)    

                    style = ttk.Style()
                    style.configure('Treeview.Heading',font=("Times New Roman",10,'bold'))
                    style.configure('Treeview',font=("Times New Roman",10),background="cyan",foreground='black')
                    scroll_x = Scrollbar(right_first1,orient=HORIZONTAL)
                    scroll_y = Scrollbar(right_first1,orient=VERTICAL)

                    self.studenttabel = Treeview(right_first1 , columns=('Reg no','First Name','Last Name','Father name','Grade','Class no'),
                                                                    yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

                    scroll_x.pack(side=BOTTOM,fill=X)
                    scroll_y.pack(side=RIGHT,fill=Y)
                    scroll_x.config(command=self.studenttabel.xview)
                    scroll_y.config(command=self.studenttabel.yview)

                    self.studenttabel.heading('Reg no', text="Reg no")
                    self.studenttabel.heading('First Name', text="First Name")
                    self.studenttabel.heading('Last Name', text="Last Name")
                    self.studenttabel.heading('Father name', text="Father name")
                    self.studenttabel.heading('Grade', text="Grade")
                    self.studenttabel.heading('Class no', text="Class no")

                    self.studenttabel['show']='headings'

                    self.studenttabel.column('Reg no',width=60)
                    self.studenttabel.column('First Name',width=100)
                    self.studenttabel.column('Last Name',width=100)
                    self.studenttabel.column('Father name',width=100)
                    self.studenttabel.column('Grade',width=70)
                    self.studenttabel.column('Class no',width=70)
                    
                    self.studenttabel.pack(fill=BOTH,expand=1)
                    self.courser.execute(f"""select Std_Registeration_NO,Std_First_Name,Std_Last_Name,
                                        Std_Father_Name,Grade,Class_No from new_Admission 
                                where Std_First_Name LIKE '{name}' OR Std_Last_Name LIKE '{name}' """)
                    data_1 = self.courser.fetchall()
                    if len(data_1) == 0:
                        m_box.showerror('Incorrect Name',f'Sorry.....!\nYour Name is Incorrect\nThere is no Student Whose Name is {std_Name}\n\nPlease try again.....')
                    else:
                        for i in data_1:
                            # print(i)
                            list_1= [i[0],i[1],i[2],i[3],i[4],i[5]]
                            self.studenttabel.insert('',END,values=list_1)
                    self.studenttabel.bind("<ButtonRelease-1>",get_data)
                else:
                    m_box.showerror('Error','Sorry.....!\nThere is no Table on Admission \nplease Registered the Student .....')
                    
        # ===================================================================================
        # ============================================  get Data from search By Name Function
        def get_data(event):
            curItem = self.studenttabel.item(self.studenttabel.focus())
            reg_no = curItem['values'][0]

            self.courser.execute(f"select * from new_Admission where Std_Registeration_NO={reg_no}")
            record = self.courser.fetchall()
            data = [i for i in record]
            # print(data)

            self.reg_no_var_s.set(data[0][0])
            self.first_name_var_s.set(data[0][1])
            self.last_name_var_s.set(data[0][2])
            self.gander_var_s.set(data[0][4])
            self.DOB_var_s.set(data[0][5])
            self.contect_var_s.set(data[0][6])
            self.BG_var_s.set(data[0][7])
            self.Email_var_s.set(data[0][8])
            self.Addmission_var_s.set(data[0][9])
            self.religion_var_s.set(data[0][10])
            self.Grade_var_s.set(data[0][11])
            self.class_no_var_s.set(data[0][12])
            self.Monthly_Fee_var_s.set(data[0][13])
            self.Birth_place_var_s.set(data[0][14])
            self.Address_var_s.set(data[0][15])
            # -----------------------  Student BIO DATA
            self.Father_name_var_s.set(data[0][3])
            self.F_Contect_no_var_s.set(data[0][16])
            self.F_CNIC_var_s.set(data[0][17])
            # ----------------------- LAst School Attended
            self.Last_School_name_var_s.set(data[0][18])
            self.Date_of_Discharge_var_s.set(data[0][19])
            self.Prev_Class_var_s.set(data[0][20])
            # ------------------------
            self.Admission_fee_var_s.set(data[0][21])
            self.Transport_fee_var_s.set(data[0][22])
            self.Medical_fee_var_s.set(data[0][23])

            # -------------------------------   student picture
            self.pic = "picture//"+data[0][1]+"_"+data[0][2]+"_"+str(data[0][0])+".jpg"
            if os.path.exists(self.pic):
                self.pic=Image.open(self.pic)
                self.pic=self.pic.resize((110,125),Image.ANTIALIAS)
                self.pic=ImageTk.PhotoImage(self.pic)
                self.lbl.configure(image=self.pic)
                self.lbl.image=self.pic
            else:
                self.lbl = Label(self.pic_frame,width=110,height=125)
                self.lbl.place(x=0,y=0)


        # =======================================================================
        # =========================================  Update The Student Record
        def update_std_record():
            if  self.reg_no_var_s.get() == "" or self.first_name_var_s.get() == "" or self.last_name_var_s.get() == "" or self.gander_var_s.get() == "" or self.DOB_var_s.get() == "" or self.contect_var_s.get() == "" or self.BG_var_s.get() == "" or self.Email_var_s.get() == "" or self.Addmission_var_s.get() == "" or self.religion_var_s.get() == "" or self.Grade_var_s.get() == "" or self.class_no_var_s.get() == "" or self.Monthly_Fee_var_s.get() == "" or self.Birth_place_var_s.get() == "" or self.Address_var_s.get() == "" or self.Father_name_var_s.get() == "" or self.F_Contect_no_var_s.get() == "" or self.F_CNIC_var_s.get() == "" or self.Last_School_name_var_s.get() == "" or self.Date_of_Discharge_var_s.get() == "" or self.Prev_Class_var_s.get() == "" or self.Admission_fee_var_s.get() == "" or self.Transport_fee_var_s.get() == "" or self.Medical_fee_var_s.get() == "":
                m_box.showerror("Error","Please search the Student")
            else:
                first_name_entery_box.configure(state=NORMAL)
                last_name_entery_box.configure(state=NORMAL)
                gender_combobox.configure(state=NORMAL)
                DOB_entery_box.configure(state=NORMAL)
                contect_entery_box.configure(state=NORMAL)
                BG_entery_entery_box.configure(state=NORMAL)
                Email_entery_box.configure(state=NORMAL)
                Addmission_entery_box.configure(state=NORMAL)
                religion_entery_box.configure(state=NORMAL)
                Grade_entery_box.configure(state=NORMAL)
                class_no_entery_box.configure(state=NORMAL)
                Monthly_Fee_entery_box.configure(state=NORMAL)
                Birth_place_entery_box.configure(state=NORMAL)
                Address_entery_box.configure(state=NORMAL)
                Father_name_entery_box.configure(state=NORMAL)
                F_Contect_no_entery_box.configure(state=NORMAL)
                F_CNIC_entery_box.configure(state=NORMAL)
                Last_School_name_entery_box.configure(state=NORMAL)
                Date_of_Dischargeentery_box.configure(state=NORMAL)
                Prev_Class_entery_box.configure(state=NORMAL)
                Admission_fee_entery_box.configure(state=NORMAL)
                Transport_fee_entery_box.configure(state=NORMAL)
                Medical_fee_entery_box.configure(state=NORMAL)
                
                def save_update():
                    name = self.first_name_var_s.get() +"_"+ self.last_name_var_s.get()
                    if self.reg_no_var_s.get()=="":
                        m_box.showerror('Error','There is no Data which you are Update\nplease try again.... ')
                    else:
                        # ---------------------------------------   ask question for update
                        updat = m_box.askyesno('Updating.....',"Do you want to Update the Data?")               
                        if(updat==True):
                            # -----------------------------  student picture
                            if self.picture == None:
                                pass
                            else: 
                                path = os.path.exists("picture")
                                image = Image.open(self.picture)
                                if path==True:
                                    image.save(f"picture//"+name+"_"+self.reg_no_var_s.get()+".jpg")
                                else:
                                    os.mkdir("picture")
                                    image.save(f"picture//{name}_{self.reg_no_var_s.get()}.jpg")
                            # -------------------  SQL  Query to update the student record 
                            self.courser.execute(f"""update CMS.new_Admission set Std_Registeration_NO='{self.reg_no_var_s.get()}',Std_First_Name ='{self.first_name_var_s.get()}',
                                                Std_Last_Name='{self.last_name_var_s.get()}',Std_Father_Name ='{self.Father_name_var_s.get()}',Gander='{self.gander_var_s.get()}',
                                                Date_Of_Birth ='{self.DOB_var_s.get()}',Contect_No='{self.contect_var_s.get()}',Blood_Group='{self.BG_var_s.get()}',
                                                Email='{self.Email_var_s.get()}',Admission_Date ='{self.Addmission_var_s.get()}',Religion='{self.religion_var_s.get()}',
                                                Grade='{self.Grade_var_s.get()}',Class_no='{self.class_no_var_s.get()}',Monthly_Fee ='{self.Monthly_Fee_var_s.get()}',
                                                Birth_Place ='{self.Birth_place_var_s.get()}',Per_Address='{self.Address_var_s.get()}',Father_Contect_No='{self.F_Contect_no_var_s.get()}',
                                                Father_CNIC='{self.F_CNIC_var_s.get()}',Pree_School_Name ='{self.Last_School_name_var_s.get()}',
                                                Date_Of_Discharge='{self.Date_of_Discharge_var_s.get()}',Class='{self.Prev_Class_var_s.get()}',
                                                Admission_Fee='{self.Admission_fee_var_s.get()}', Transport_Fee='{self.Transport_fee_var_s.get()}',Medical_Fee='{self.Medical_fee_var_s.get()}'
                                        where Std_Registeration_NO='{self.reg_no_var_s.get()}' """)
                            
                            m_box.showinfo('Updated',"Your Data is Update Successfuly.....")
                            self.main_page()

                
                update_butten = tk.Button(self.main_2_frame,width=10,text="Save",bd=2,pady=5,cursor="hand2",command=save_update,
                                    foreground='white',background="#0d8888",activebackground="#076d6d",
                                    activeforeground = "white",font=("Times New Roman",10))
                update_butten.place(x=391,y=565)

        # =======================================================================
        # =============================================== delete Data function
        def delete_std_record():
            if self.reg_no_var_s.get()=="":
                m_box.showerror('Error','There is no Data which you are delete \nplease try again.... ')
            else:
                delet = m_box.askyesno('Deleting.....',"Do you want to delete the Data?")
                if(delet==True):
                    self.courser.execute(f"select * from CMS.new_Admission where Std_Registeration_NO='{self.reg_no_var_s.get()}'")
                    Std_record4 = self.courser.fetchall()
                    Std_data = [i for i in Std_record4]
                    # print(Std_data)
                    # ==================  the deleted data is saved in teh withdrawl table in the database
                    self.courser.execute("CREATE TABLE IF NOT EXISTS WITHDRAWL_STUDENT(Std_Registeration_NO BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT, Std_First_Name VARCHAR(25),Std_Last_Name VARCHAR(25),Std_Father_Name VARCHAR(25),Gander VARCHAR(10),Date_Of_Birth VARCHAR(100),Contect_No BIGINT ,Blood_Group VARCHAR(5),Email VARCHAR(25),Admission_Date VARCHAR(100),Religion VARCHAR(10),Grade VARCHAR(10),Class_no INT, Monthly_Fee BIGINT, Birth_Place VARCHAR(50) , Per_Address VARCHAR(50) ,Father_Contect_No BIGINT ,Father_CNIC VARCHAR(15), Pree_School_Name VARCHAR(25),Date_Of_Discharge VARCHAR(100), Class VARCHAR(10), Admission_Fee BIGINT, Transport_Fee BIGINT,Medical_Fee BIGINT)")
                    for i in Std_data:
                        self.courser.execute( "Insert IGNORE Into WITHDRAWL_STUDENT (Std_Registeration_NO,Std_First_Name,Std_Last_Name,Std_Father_Name,Gander,Date_Of_Birth,Contect_No,Blood_Group,Email,Admission_Date,Religion,Grade,Class_no,Monthly_Fee,Birth_Place,Per_Address,Father_Contect_No,Father_CNIC,Pree_School_Name,Date_Of_Discharge,Class,Admission_Fee, Transport_Fee,Medical_Fee) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                                            (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[16],i[17],i[18],i[19],i[20],i[21],i[22],i[23]))
                    
                    # ==================  Delete the data
                    self.courser.execute(f"delete from CMS.new_Admission where Std_Registeration_NO='{self.reg_no_var_s.get()}'")
                    
                    directory = 'picture'
                    os.chdir(directory)
                    path = self.first_name_var_s.get()+"_"+self.last_name_var_s.get()+"_"+self.reg_no_var_s.get()+".jpg"
                    # print(path)
                    if os.path.exists(path):
                        os.unlink(path)
                    else:
                        None
                    m_box.showinfo('Delete',"Your Data is Deleted Successfuly.....")
                    self.main_2_frame.destroy()


        def all_clear():
            self.reg_var.set("")
            self.name_var.set("")
            self.reg_no_var_s.set("")
            self.first_name_var_s.set("")
            self.last_name_var_s.set("")
            self.gander_var_s.set("")
            self.DOB_var_s.set("")
            self.contect_var_s.set("")
            self.BG_var_s.set("")
            self.Email_var_s.set("")
            self.Addmission_var_s.set("")
            self.religion_var_s.set("")
            self.Grade_var_s.set("")
            self.class_no_var_s.set("")
            self.Monthly_Fee_var_s.set("")
            self.Birth_place_var_s.set("")
            self.Address_var_s.set("")
            # -----------------------  Student BIO DATA
            self.Father_name_var_s.set("")
            self.F_Contect_no_var_s.set("")
            self.F_CNIC_var_s.set("")
            # ----------------------- LAst School Attended
            self.Last_School_name_var_s.set("")
            self.Date_of_Discharge_var_s.set("")
            self.Prev_Class_var_s.set("")
            # ------------------------
            self.Admission_fee_var_s.set("")
            self.Transport_fee_var_s.set("")
            self.Medical_fee_var_s.set("")
            self.lbl=Label(self.pic_frame,width=110,height=125)
            self.lbl.place(x=0,y=0)

        # ===================================================================================
        # ====================================================  Buttons search Student
        search_by_Reg_No_butten = Button(self.Frame_left,text="Search",width=9,cursor="hand2",command=search_student_by_ID,
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        search_by_Reg_No_butten.place(x=80,y=90)

        search_by_Name_butten = Button(self.Frame_left,width=9,text="Search",cursor="hand2",command=search_student_by_name,
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        search_by_Name_butten.place(x=80,y=210)
        
        # ===================================================================================
        # ==============================================  Buttons Update,Delete and Clear
        update_butten = tk.Button(self.main_2_frame,width=10,text="Update",bd=2,pady=5,cursor="hand2",command=update_std_record,
                                foreground='white',background="#0d8888",activebackground="#076d6d",
                                activeforeground = "white",font=("Times New Roman",10))
        update_butten.place(x=391,y=565)
        
        delete_butten = tk.Button(self.main_2_frame,width=10,text="Delete", bd=2,pady=5,cursor="hand2",command=delete_std_record,
                                foreground='white',background="#0d8888",activebackground="#076d6d",
                                activeforeground = "white",font=("Times New Roman",10))
        delete_butten.place(x=478,y=565)

        clear_butten = tk.Button(self.main_2_frame,width=10,text="Clear",bd=2,pady=5, cursor="hand2",command=all_clear,
                                foreground='white',background="#0d8888",activebackground="#076d6d",
                                activeforeground = "white",font=("Times New Roman",10))
        clear_butten.place(x=565,y=565)
    














#                                start the function which show the student in numbers
# ======================================================================================================================================
# ======================================================================================================================================
# ==================================  check Student
# ======================================================================================================================================
# ======================================================================================================================================
    def with_drawl_student(self):
        # ===============================================================
        # =============================================  All Variable
        self.tot_student = StringVar()
        self.class_for_std = StringVar()
        self.class_tot_student = StringVar()
        self.all_withdrawl_student = StringVar()

        # ================================================================
        # =================================  ALL Frames
        self.frame1 = Frame(self.main_frame,bg="#0b9798",width=850,height=600)
        self.frame1.place(x=0,y=0)
        
        self.frame2 = Frame(self.frame1,bg="#0b9798",width=300,height=190,relief= RIDGE,bd=2)
        self.frame2.place(x=15,y=6)
        
        self.frame3 = Frame(self.frame1,bg="#0b9798",width=487,height=190,relief= RIDGE,bd=2)
        self.frame3.place(x=319,y=6)

        self.frame4 = Frame(self.frame1,bg="#0b9798",width=300,height=190,relief=RIDGE,bd=2)
        self.frame4.place(x=15,y=200)
        
        self.frame5 = Frame(self.frame1,bg="#0b9798",width=487,height=190,relief= RIDGE,bd=2)
        self.frame5.place(x=319,y=200)

        self.frame6 = Frame(self.frame1,bg="#0b9798",width=300,height=190,relief=RIDGE,bd=2)
        self.frame6.place(x=15,y=394)
        
        self.frame7 = Frame(self.frame1,bg="#0b9798",width=487,height=190,relief= RIDGE,bd=2)
        self.frame7.place(x=319,y=394)
        

        
        # ================================================================
        # =====================================  Labels and Entry boxes

        # ========================================================================================================
        # ========================================================================================================
        lab_1 = Label(self.frame2,text='Click The Button To Show\nAll Student in the School',padx=10,font=("Times New Roman",14),bg="#0b9798",fg="white")
        lab_1.pack(ipadx=34,ipady=21)

        lab_2 = Label(self.frame3,text='Total Student',padx=10,font=("Times New Roman",14),bg="#0b9798",fg="white")
        lab_2.place(x=5,y=60)
        class_entery_box = Entry(self.frame3,width=12,textvariable=self.tot_student,state="readonly", font=("Arial",11))
        class_entery_box.place(x=18,y=82)


       

        # ========================================================================================================
        # ========================================================================================================
        lab_1 = Label(self.frame4,text='Enter Grade to show\nStudent in the Class',padx=10,font=("Times New Roman",14),bg="#0b9798",fg="white")
        lab_1.pack(ipadx=58,ipady=21)
        lab_1 = Label(self.frame4,text='Class ',padx=10,font=("Times New Roman",14),bg="#0b9798",fg="white")
        lab_1.place(x=60,y=80)
        class_entery_box = ttk.Combobox(self.frame4,width=11,textvariable=self.class_for_std,state="readonly", font=("Arial",10))
        class_entery_box["values"] = ("Ist","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th")
        class_entery_box.place(x=120,y=80)
        
        # =================================
        lab_2 = Label(self.frame5,text='Total Student',padx=10,font=("Times New Roman",14),bg="#0b9798",fg="white")
        lab_2.place(x=5,y=60)
        class_entery_box = Entry(self.frame5,width=12,textvariable=self.class_tot_student,state="readonly", font=("Arial",11))
        class_entery_box.place(x=18,y=82)
        

        # ========================================================================================================
        # ========================================================================================================
        lab_1 = Label(self.frame6,text='Click The Button To Show\nWithdrawl Student from the school',padx=10,font=("Times New Roman",14),bg="#0b9798",fg="white")
        lab_1.pack(ipadx=5,ipady=21)
        # =================================
        lab_2 = Label(self.frame7,text='Total Student',padx=10,font=("Times New Roman",14),bg="#0b9798",fg="white")
        lab_2.place(x=5,y=60)
        class_entery_box = Entry(self.frame7,width=12,textvariable=self.all_withdrawl_student,state="readonly", font=("Arial",11))
        class_entery_box.place(x=18,y=82)


        # ==========================================================================================================
        # ==========================================================================================================

        def all_student():
            self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'New_Admission')")
            search_admission_table = list(self.courser.fetchall()[0])

            if search_admission_table[0]==1:
                self.courser.execute(f"""select count(*) from new_Admission;""")
                Std_record1 = list(self.courser.fetchall()[0])
                self.tot_student.set(Std_record1[0])

                self.courser.execute(f"""select * from new_Admission;""")
                all_school_record = self.courser.fetchall()
                all_school_data = [i for i in all_school_record]

                self.frame3_1 = Frame(self.frame3,bg="#0b9798",relief= RIDGE,bd=2)
                self.frame3_1.place(x=125,y=0,width=358,height=186)

                style = ttk.Style()
                style.configure('Treeview.Heading',font=("Times New Roman",10,'bold'))
                style.configure('Treeview',font=("Times New Roman",10),background="cyan",foreground='black')

                scroll_x = Scrollbar(self.frame3_1,orient=HORIZONTAL)
                scroll_y = Scrollbar(self.frame3_1,orient=VERTICAL)

                self.studenttabel_all = Treeview(self.frame3_1 , columns=('Registeration No','Name','Father Name','Gender','Grade','Class No'),
                                                                    yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.config(command=self.studenttabel_all.yview)
                scroll_x.config(command=self.studenttabel_all.xview)

                self.studenttabel_all.heading('Registeration No', text="Registeration No")
                self.studenttabel_all.heading('Name', text="Name")
                self.studenttabel_all.heading('Father Name', text="Father Name")
                self.studenttabel_all.heading('Gender', text="Gender")
                self.studenttabel_all.heading('Grade', text="Grade")
                self.studenttabel_all.heading('Class No', text="Class No")

                self.studenttabel_all['show']='headings'

                self.studenttabel_all.column('Registeration No',width=100)
                self.studenttabel_all.column('Name',width=150)
                self.studenttabel_all.column('Father Name',width=150)
                self.studenttabel_all.column('Gender',width=100)
                self.studenttabel_all.column('Grade',width=100)
                self.studenttabel_all.column('Class No',width=100)
                self.studenttabel_all.pack(fill=BOTH,expand=1)


                
                for i in all_school_data:
                    # print(i)
                    list_1= [i[0],i[1]+" "+i[2],i[3],i[4],i[11],i[12]]
                    self.studenttabel_all.insert('',END,values=list_1)
            else:
                m_box.showerror('Error','Sorry.....!\nThere is no Table on Admission \nplease Registered the Student .....')
                    
        # ==========================================================================================================
        # ==========================================================================================================

        def class_student():
            if self.class_for_std.get()=="":
                m_box.showerror('Error','Please Enter Class\nTry again.... ')
            else:
                self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'New_Admission')")
                search_admission_table = list(self.courser.fetchall()[0])

                if search_admission_table[0]==1:
                    self.courser.execute(f"""select count(*) from new_Admission where Grade='{self.class_for_std.get()}';""")
                    class_record = list(self.courser.fetchall()[0])
                    self.class_tot_student.set(class_record[0])

                    self.courser.execute(f"""select * from new_Admission where Grade='{self.class_for_std.get()}';""")
                    Std_class_record = self.courser.fetchall()
                    all_std_class = [i for i in Std_class_record]

                    self.frame5_1 = Frame(self.frame5,bg="#0b9798",relief= RIDGE,bd=2)
                    self.frame5_1.place(x=125,y=0,width=358,height=186)

                    style = ttk.Style()
                    style.configure('Treeview.Heading',font=("Times New Roman",10,'bold'))
                    style.configure('Treeview',font=("Times New Roman",10),background="cyan",foreground='black')

                    scroll_x = Scrollbar(self.frame5_1,orient=HORIZONTAL)
                    scroll_y = Scrollbar(self.frame5_1,orient=VERTICAL)

                    self.studenttabel_class = Treeview(self.frame5_1 , columns=('Registeration No','Name','Father Name','Gender','Grade','Class No'),
                                                                        yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
                    scroll_y.pack(side=RIGHT,fill=Y)
                    scroll_x.pack(side=BOTTOM,fill=X)
                    scroll_y.config(command=self.studenttabel_class.yview)
                    scroll_x.config(command=self.studenttabel_class.xview)

                    self.studenttabel_class.heading('Registeration No', text="Registeration No")
                    self.studenttabel_class.heading('Name', text="Name")
                    self.studenttabel_class.heading('Father Name', text="Father Name")
                    self.studenttabel_class.heading('Gender', text="Gender")
                    self.studenttabel_class.heading('Grade', text="Grade")
                    self.studenttabel_class.heading('Class No', text="Class No")

                    self.studenttabel_class['show']='headings'

                    self.studenttabel_class.column('Registeration No',width=100)
                    self.studenttabel_class.column('Name',width=150)
                    self.studenttabel_class.column('Father Name',width=150)
                    self.studenttabel_class.column('Gender',width=100)
                    self.studenttabel_class.column('Grade',width=100)
                    self.studenttabel_class.column('Class No',width=100)
                    self.studenttabel_class.pack(fill=BOTH,expand=1)
                    
                    for i in all_std_class:
                        # print(i)
                        list_2= [i[0],i[1]+" "+i[2],i[3],i[4],i[11],i[12]]
                        self.studenttabel_class.insert('',END,values=list_2)
                else:
                    m_box.showerror('Error','Sorry.....!\nThere is no Table on Admission \nplease Registered the Student .....')
                    
        # ==========================================================================================================
        # ==========================================================================================================

        def withdrawl_student():
            self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'WITHDRAWL_STUDENT')")
            check_submitte_class = list(self.courser.fetchall()[0])
            # print(check_submitte_class[0])
            if check_submitte_class[0] == 0:
                m_box.showinfo('Information','there is no withdraw student from your School')
            else:
                self.courser.execute(f"""select count(*) from WITHDRAWL_STUDENT;""")
                Std_record1 = list(self.courser.fetchall()[0])
                # print(Std_record[0])
                self.all_withdrawl_student.set(Std_record1[0])

                self.courser.execute(f"""select * from WITHDRAWL_STUDENT;""")
                withdrawl_student = self.courser.fetchall()
                Std_data = [i for i in withdrawl_student]

                self.frame7_1 = Frame(self.frame7,bg="#0b9798",relief= RIDGE,bd=2)
                self.frame7_1.place(x=125,y=0,width=358,height=186)

                style = ttk.Style()
                style.configure('Treeview.Heading',font=("Times New Roman",10,'bold'))
                style.configure('Treeview',font=("Times New Roman",10),background="cyan",foreground='black')

                scroll_x = Scrollbar(self.frame7_1,orient=HORIZONTAL)
                scroll_y = Scrollbar(self.frame7_1,orient=VERTICAL)

                self.studenttabel_all = Treeview(self.frame7_1 , columns=('Registeration No','Name','Father Name','Gender','Grade','Class No'),
                                                                    yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.config(command=self.studenttabel_all.yview)
                scroll_x.config(command=self.studenttabel_all.xview)

                self.studenttabel_all.heading('Registeration No', text="Registeration No")
                self.studenttabel_all.heading('Name', text="Name")
                self.studenttabel_all.heading('Father Name', text="Father Name")
                self.studenttabel_all.heading('Gender', text="Gender")
                self.studenttabel_all.heading('Grade', text="Grade")
                self.studenttabel_all.heading('Class No', text="Class No")

                self.studenttabel_all['show']='headings'

                self.studenttabel_all.column('Registeration No',width=100)
                self.studenttabel_all.column('Name',width=150)
                self.studenttabel_all.column('Father Name',width=150)
                self.studenttabel_all.column('Gender',width=100)
                self.studenttabel_all.column('Grade',width=100)
                self.studenttabel_all.column('Class No',width=100)
                self.studenttabel_all.pack(fill=BOTH,expand=1)

                for i in withdrawl_student:
                    # print(i)
                    list_1= [i[0],i[1]+" "+i[2],i[3],i[4],i[11],i[12]]
                    self.studenttabel_all.insert('',END,values=list_1)
                    
          
        # ===================   Buttons
        display_all_student = Button(self.frame2,text="Display Student",command=all_student,cursor="hand2",
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        display_all_student.pack(pady=35)

        # ===================   Buttons
        display_class_student = Button(self.frame4,text="Display Student",command=class_student,cursor="hand2",
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        display_class_student.pack(pady=35)   

        # ===================   Buttons
        withdrawl_student = Button(self.frame6,text="withdrawl Student",command=withdrawl_student,cursor="hand2",
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        withdrawl_student.pack(pady=35)


















#                               Start the function which maintain the Fee record of all student
# ==================================================================================================================================
# ==================================================================================================================================
# ==================================  Fee Structure 
# ==================================================================================================================================
# ==================================================================================================================================
    def Fee_Structure(self):
        # ============================================
        # ===========================   Current Date
        get_date = strftime("%d/%m/%Y")
        CURRENT_DATE =get_date.split("/")[0]
        MONTH =get_date.split("/")[1]
        CURRENT_YEAR =get_date.split("/")[2]

        dict_date = {"01":'January',"02":'February',"03":'MArch',"04":'April',"05":'May',"06":'June',
                    "07":'July',"08":'August',"09":'September',"10":'October',"11":'November',"12":'December',
                    }
        
        for i in  dict_date:
            if i==MONTH:
                CURRENT_MONTH = dict_date[i]
        # ============================================================
        # =============================================  Variables
        # ========================== generate all class fee slip
        self.Class_var= StringVar()
        self.Month_var = StringVar()
        self.Month_var.set(CURRENT_MONTH)
        self.year_var = StringVar()
        self.year_var.set(CURRENT_YEAR)
        self.Examination_var = StringVar()
        self.Examination_var.set(0)
        self.Promotion_var = StringVar()
        self.Promotion_var.set(0)
        self.SecondTime_var = StringVar()
        self.SecondTime_var.set(0)

        # =============================================
        # ====================== generate one or more then one student fee slip
        self.Class_student_var= StringVar()
        self.Month_student_var = StringVar()
        self.Month_student_var.set(CURRENT_MONTH)
        self.year_student_var = StringVar()
        self.year_student_var.set(CURRENT_YEAR)
        self.Class_No_student_var = StringVar()
        self.Examination_student_var = StringVar()
        self.Examination_student_var.set(0)
        self.Promotion_student_var = StringVar()
        self.Promotion_student_var.set(0)
        self.SecondTime_student_var = StringVar()
        self.SecondTime_student_var.set(0)

        # =============================================
        # ========================== Submitte fee slip
        self.Class_submitte_fee_var= StringVar()
        self.Month_submitte_fee_var = StringVar()
        self.Month_submitte_fee_var.set(CURRENT_MONTH)
        self.year_submitte_fee_var = StringVar()
        self.year_submitte_fee_var.set(CURRENT_YEAR)
        self.Class_No_submitte_fee_var = StringVar()
        self.Discount_submitte_fee_var = StringVar()
        self.Discount_submitte_fee_var.set(0)
        self.Paid_submitte_fee_var = StringVar()

        # ===============================================
        # ============================= Submitte fee slip
        self.Month_submitte_fee_std_var = StringVar()
        self.Month_submitte_fee_std_var.set(CURRENT_MONTH)
        self.year_submitte_fee_std_var = StringVar()
        self.year_submitte_fee_std_var.set(CURRENT_YEAR)
        self.Reg_No_submitte_fee_std_var = StringVar()
        self.Paid_submitte_fee_std_var = StringVar()
        self.Adjust_submitte_fee_std_var = StringVar()
        self.Adjust_submitte_fee_std_var.set(0)

        # ================================================
        # =============================  check fee detail
        self.Class_check_fee_var= StringVar()
        self.Month_check_fee_var = StringVar()
        self.Month_check_fee_var.set(CURRENT_MONTH)
        self.year_check_fee_var = StringVar()
        self.year_check_fee_var.set(CURRENT_YEAR)

        self.All_std_detail_var = StringVar()
        self.submitte_fee_std_detail_var = StringVar()
        self.remaining_fee_std_detail_var = StringVar()

        # ===============================================================
        # ==================================================== Frames  
      
        self.frame1 = Frame(self.main_frame,bg="#0b9798",width=850,height=600)
        self.frame1.place(x=0,y=0)
        
        self.frame2 = Frame(self.frame1,bg="#0b9798",width=260,height=330,relief=RIDGE,bd=2)
        self.frame2.place(x=6,y=6)
        
        self.frame3 = Frame(self.frame1,bg="#0b9798",width=260,height=330,relief=RIDGE,bd=2)
        self.frame3.place(x=270,y=6)
        
        self.frame4 = Frame(self.frame1,bg="#0b9798",width=260,height=330,relief=RIDGE,bd=2)
        self.frame4.place(x=536,y=6)

        self.frame5 = Frame(self.frame1,bg="#0b9798",width=260,height=245,relief=RIDGE,bd=2)
        self.frame5.place(x=6,y=340)
        
        self.frame6 = Frame(self.frame1,bg="#0b9798",width=527,height=245,relief= RIDGE,bd=2)
        self.frame6.place(x=270,y=340)
        self.frame6_1 = Frame(self.frame6,bg="#0b9798",width=250,height=170,relief=RAISED,bd=2)
        self.frame6_1.place(x=245,y=20)

        # ================================================================
        # =====================================   Labels and Entry Boxes


        # ==================================================================================================
        # ===========================================================   Generate Fee Slip of all student
        year =[]
        for i in range(2000,2100):
            year.append(i)

        lab = Label(self.frame2,text='Generate Fee Slip of All Class',padx=10,font=("Times New Roman",14),bg="#0b9798",fg="white")
        lab.place(x=2,y=10)

        all_class_lbl = Label(self.frame2,text='Class',font=("Times New Roman",14),bg="#0b9798",fg="white")
        all_class_lbl.place(x=35,y=70)
        all_class_entery_box = ttk.Combobox(self.frame2,textvariable=self.Class_var,width=11,state="readonly", font=("Arial",10))
        all_class_entery_box["values"] = ("Ist","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th")
        all_class_entery_box.place(x=95,y=72)
        
        date_lbl = Label(self.frame2,text='Month',font=("Times New Roman",14),bg="#0b9798",fg="white")
        date_lbl.place(x=35,y=100)
        all_class_entery_box = ttk.Combobox(self.frame2,textvariable=self.Month_var,width=11,state="readonly", font=("Arial",10))
        all_class_entery_box["values"] = ("January","February","March","April","May","June","July","August","September","October","November","December")
        all_class_entery_box.place(x=95,y=102)

        date_lbl = Label(self.frame2,text='Year',font=("Times New Roman",14),bg="#0b9798",fg="white")
        date_lbl.place(x=35,y=130)
        all_class_entery_box = ttk.Combobox(self.frame2,textvariable=self.year_var,width=11,font=("Arial",10))
        all_class_entery_box["values"] = (year)
        all_class_entery_box.place(x=95,y=132)

        date_lbl = Label(self.frame2,text='Examination Fee:',font=("Times New Roman",14),bg="#0b9798",fg="white")
        date_lbl.place(x=15,y=180)
        all_class_entery_box =Entry(self.frame2,textvariable=self.Examination_var,width=9,font=("Arial",10))
        all_class_entery_box.place(x=160,y=182)

        date_lbl = Label(self.frame2,text='Promotion Fee:',font=("Times New Roman",14),bg="#0b9798",fg="white")
        date_lbl.place(x=15,y=210)
        all_class_entery_box =Entry(self.frame2,textvariable=self.Promotion_var,width=9,font=("Arial",10))
        all_class_entery_box.place(x=160,y=212)

        date_lbl = Label(self.frame2,text='Second Time Fee:',font=("Times New Roman",14),bg="#0b9798",fg="white")
        date_lbl.place(x=15,y=240)
        all_class_entery_box =Entry(self.frame2,textvariable=self.SecondTime_var,width=9,font=("Arial",10))
        all_class_entery_box.place(x=160,y=242)


        # ====================================================================================================
        # ===========================================================  Generate fee slip of spicific student
        lab = Label(self.frame3,text='Generate Fee Slip of Student',padx=10,font=("Times New Roman",14),bg="#0b9798",fg="white")
        lab.place(x=2,y=10)

        all_class_lbl = Label(self.frame3,text='Class',font=("Times New Roman",14),bg="#0b9798",fg="white")
        all_class_lbl.place(x=35,y=70)
        all_class_entery_box = ttk.Combobox(self.frame3,textvariable=self.Class_student_var,width=11,state="readonly", font=("Arial",10))
        all_class_entery_box["values"] = ("Ist","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th")
        all_class_entery_box.place(x=110,y=72)
        
        date_lbl = Label(self.frame3,text='Month',font=("Times New Roman",14),bg="#0b9798",fg="white")
        date_lbl.place(x=35,y=95)
        all_class_entery_box = ttk.Combobox(self.frame3,textvariable=self.Month_student_var,width=11,state="readonly", font=("Arial",10))
        all_class_entery_box["values"] = ("January","February","March","April","May","June","July","August","September","October","November","December")
        all_class_entery_box.place(x=110,y=97)

        date_lbl = Label(self.frame3,text='Year',font=("Times New Roman",14),bg="#0b9798",fg="white")
        date_lbl.place(x=35,y=120)
        all_class_entery_box = ttk.Combobox(self.frame3,textvariable=self.year_student_var,width=11,font=("Arial",10))
        all_class_entery_box["values"] = (year)
        all_class_entery_box.place(x=110,y=122)

        date_lbl = Label(self.frame3,text='Class No',font=("Times New Roman",14),bg="#0b9798",fg="white")
        date_lbl.place(x=35,y=145)
        all_class_entery_box = Entry(self.frame3,textvariable=self.Class_No_student_var,width=11,font=("Arial",12))
        all_class_entery_box.place(x=110,y=147)

        date_lbl = Label(self.frame3,text='Examination Fee:',font=("Times New Roman",14),bg="#0b9798",fg="white")
        date_lbl.place(x=15,y=180)
        all_class_entery_box =Entry(self.frame3,textvariable=self.Examination_student_var,width=9,font=("Arial",10))
        all_class_entery_box.place(x=160,y=182)

        date_lbl = Label(self.frame3,text='Promotion Fee:',font=("Times New Roman",14),bg="#0b9798",fg="white")
        date_lbl.place(x=15,y=210)
        all_class_entery_box =Entry(self.frame3,textvariable=self.Promotion_student_var,width=9,font=("Arial",10))
        all_class_entery_box.place(x=160,y=212)

        date_lbl = Label(self.frame3,text='Second Time Fee:',font=("Times New Roman",14),bg="#0b9798",fg="white")
        date_lbl.place(x=15,y=240)
        all_class_entery_box =Entry(self.frame3,textvariable=self.SecondTime_student_var,width=9,font=("Arial",10))
        all_class_entery_box.place(x=160,y=242)


        # ===================================================================================
        # ===========================================================  Submitte Fee
        lab = Label(self.frame4,text='Submitte Monthly Fee',padx=10,font=("Times New Roman",14),bg="#0b9798",fg="white")
        lab.place(x=25,y=10)

        Submt_class_lbl = Label(self.frame4,text='Class',font=("Times New Roman",14),bg="#0b9798",fg="white")
        Submt_class_lbl.place(x=35,y=70)
        Submt_class_entery_box = ttk.Combobox(self.frame4,textvariable=self.Class_submitte_fee_var,width=9,state="readonly", font=("Arial",10))
        Submt_class_entery_box["values"] = ("Ist","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th")
        Submt_class_entery_box.place(x=120,y=72)
        
        submt_month_lbl = Label(self.frame4,text='Month',font=("Times New Roman",14),bg="#0b9798",fg="white")
        submt_month_lbl.place(x=35,y=100)
        submt_month_entery_box = ttk.Combobox(self.frame4,textvariable=self.Month_submitte_fee_var,width=9,state="readonly", font=("Arial",10))
        submt_month_entery_box["values"] = ("January","February","March","April","May","June","July","August","September","October","November","December")
        submt_month_entery_box.place(x=120,y=102)

        submt_year_lbl = Label(self.frame4,text='Year',font=("Times New Roman",14),bg="#0b9798",fg="white")
        submt_year_lbl.place(x=35,y=130)
        submt_year_entery_box = ttk.Combobox(self.frame4,textvariable=self.year_submitte_fee_var,width=9,font=("Arial",10))
        submt_year_entery_box["values"] = (year)
        submt_year_entery_box.place(x=120,y=132)

        submt_class_no_lbl = Label(self.frame4,text='Class No',font=("Times New Roman",14),bg="#0b9798",fg="white")
        submt_class_no_lbl.place(x=35,y=160)
        submt_class_no_entery_box = Entry(self.frame4,textvariable=self.Class_No_submitte_fee_var,width=10,font=("Arial",11))
        submt_class_no_entery_box.place(x=120,y=162)

        discount_lbl = Label(self.frame4,text='Adjust',font=("Times New Roman",14),bg="#0b9798",fg="white")
        discount_lbl.place(x=35,y=190)
        discount_entery_box =Entry(self.frame4,textvariable=self.Discount_submitte_fee_var,width=10,font=("Arial",11))
        discount_entery_box.place(x=120,y=192)

        submt_paid_lbl = Label(self.frame4,text='Paid',font=("Times New Roman",14),bg="#0b9798",fg="white")
        submt_paid_lbl.place(x=35,y=220)
        submt_paid_entery_box =Entry(self.frame4,textvariable=self.Paid_submitte_fee_var,width=10,font=("Arial",11))
        submt_paid_entery_box.place(x=120,y=222)


        # ===================================================================================
        # ===========================================================  Submitte Fee
        lab = Label(self.frame5,text='Submitte Monthly Fee',padx=10,font=("Times New Roman",14),bg="#0b9798",fg="white")
        lab.place(x=25,y=10)
            
       
        submt_month_lbl = Label(self.frame5,text='Month',font=("Times New Roman",14),bg="#0b9798",fg="white")
        submt_month_lbl.place(x=35,y=50)
        submt_month_entery_box = ttk.Combobox(self.frame5,textvariable=self.Month_submitte_fee_std_var,width=9,state="readonly", font=("Arial",10))
        submt_month_entery_box["values"] = ("January","February","March","April","May","June","July","August","September","October","November","December")
        submt_month_entery_box.place(x=120,y=52)

        submt_year_lbl = Label(self.frame5,text='Year',font=("Times New Roman",14),bg="#0b9798",fg="white")
        submt_year_lbl.place(x=35,y=75)
        submt_year_entery_box = ttk.Combobox(self.frame5,textvariable=self.year_submitte_fee_std_var,width=9,font=("Arial",10))
        submt_year_entery_box["values"] = (year)
        submt_year_entery_box.place(x=120,y=77)

        submt_class_no_lbl = Label(self.frame5,text='Reg No',font=("Times New Roman",14),bg="#0b9798",fg="white")
        submt_class_no_lbl.place(x=35,y=100)
        submt_class_no_entery_box = Entry(self.frame5,textvariable=self.Reg_No_submitte_fee_std_var,width=10,font=("Arial",11))
        submt_class_no_entery_box.place(x=120,y=102)

        submt_Adjust_lbl = Label(self.frame5,text='Adjust',font=("Times New Roman",14),bg="#0b9798",fg="white")
        submt_Adjust_lbl.place(x=35,y=125)
        submt_Adjust_entery_box =Entry(self.frame5,textvariable=self.Adjust_submitte_fee_std_var,width=10,font=("Arial",11))
        submt_Adjust_entery_box.place(x=120,y=127)

        submt_paid_lbl = Label(self.frame5,text='Paid',font=("Times New Roman",14),bg="#0b9798",fg="white")
        submt_paid_lbl.place(x=35,y=150)
        submt_paid_entery_box =Entry(self.frame5,textvariable=self.Paid_submitte_fee_std_var,width=10,font=("Arial",11))
        submt_paid_entery_box.place(x=120,y=152)


        # =======================================================================
        # ==================================================  check fee recird
        lab = Label(self.frame6,text='Check Fee Record ',padx=10,font=("Times New Roman",14),bg="#0b9798",fg="white")
        lab.place(x=15,y=10)
            
       
        check_class_lbl = Label(self.frame6,text='Class',font=("Times New Roman",14),bg="#0b9798",fg="white")
        check_class_lbl.place(x=25,y=70)
        check_class_entery_box = ttk.Combobox(self.frame6,textvariable=self.Class_check_fee_var,width=9,state="readonly", font=("Arial",10))
        check_class_entery_box["values"] = ("All","Ist","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th")
        check_class_entery_box.place(x=90,y=72)
        
        check_month_lbl = Label(self.frame6,text='Month',font=("Times New Roman",14),bg="#0b9798",fg="white")
        check_month_lbl.place(x=25,y=100)
        check_month_entery_box = ttk.Combobox(self.frame6,textvariable=self.Month_check_fee_var,width=9,state="readonly", font=("Arial",10))
        check_month_entery_box["values"] = ("January","February","March","April","May","June","July","August","September","October","November","December")
        check_month_entery_box.place(x=90,y=102)

        check_year_lbl = Label(self.frame6,text='Year',font=("Times New Roman",14),bg="#0b9798",fg="white")
        check_year_lbl.place(x=25,y=130)
        check_year_entery_box = ttk.Combobox(self.frame6,textvariable=self.year_check_fee_var,width=9,font=("Arial",10))
        check_year_entery_box["values"] = (year)
        check_year_entery_box.place(x=90,y=132)


        # ====================================================================
        # ==============================================  Student Fee Detail
        lab = Label(self.frame6_1,text='Student Fee Detail',padx=10,font=("Times New Roman",14),bg="#0b9798",fg="white")
        lab.place(x=30,y=10)

        submt_paid_lbl = Label(self.frame6_1,text='All Student',font=("Times New Roman",14),bg="#0b9798",fg="white")
        submt_paid_lbl.place(x=5,y=55)
        submt_paid_entery_box =Entry(self.frame6_1,textvariable=self.All_std_detail_var,width=8,font=("Arial",11),relief=GROOVE,bd=2)
        submt_paid_entery_box.place(x=155,y=55)

        submt_paid_lbl = Label(self.frame6_1,text='Submitted Fee',font=("Times New Roman",14),bg="#0b9798",fg="white")
        submt_paid_lbl.place(x=5,y=85)
        submt_paid_entery_box =Entry(self.frame6_1,textvariable=self.submitte_fee_std_detail_var,width=8,font=("Arial",11),relief=GROOVE,bd=2)
        submt_paid_entery_box.place(x=155,y=85)

        submt_paid_lbl = Label(self.frame6_1,text='Remaining Student',font=("Times New Roman",14),bg="#0b9798",fg="white")
        submt_paid_lbl.place(x=5,y=115)
        submt_paid_entery_box =Entry(self.frame6_1,textvariable=self.remaining_fee_std_detail_var,width=8,font=("Arial",11),relief=GROOVE,bd=2)
        submt_paid_entery_box.place(x=155,y=115)


    
        # =======================================================================================
        # ====================================================  Generate Fee Slip of All Student
        def clear():
            self.Class_var.set("")
            self.Examination_var.set(0)
            self.Promotion_var.set(0)
            self.SecondTime_var.set(0)
            # =============================
            # =============================
            self.Class_student_var.set("")
            self.Examination_student_var.set(0)
            self.Promotion_student_var.set(0)
            self.SecondTime_student_var.set(0)
            self.Class_No_student_var.set(0)
            # =============================
            # =============================
            self.Class_submitte_fee_var.set("")
            self.Class_No_submitte_fee_var.set("")
            self.Discount_submitte_fee_var.set(0)
            self.Paid_submitte_fee_var.set("")
            # =============================
            # =============================
            self.Reg_No_submitte_fee_std_var.set("")
            self.Adjust_submitte_fee_std_var.set(0)
            self.Paid_submitte_fee_std_var.set("")
            # =============================
            # =============================
            self.Class_check_fee_var.set("")
            self.All_std_detail_var.set("")
            self.submitte_fee_std_detail_var.set("")
            self.remaining_fee_std_detail_var.set("")

        # =============================================================================
        # =============================================================================

        def Fee_Slip_all():
            date_string = strftime("%d/%m/%Y")

            Exam_Fee = self.Examination_var.get()
            promo_Fee = self.Promotion_var.get()
            Sec_Time_Fee  = self.SecondTime_var.get()

            # ====================================================
            # ====================================================
            if self.Class_var.get()=="" or self.Month_var.get()=="" or self.year_var.get()=="":
                m_box.showerror('Error','Please fill all the boxes\nTry again.... ')
            else:
                Table_Name = self.Month_var.get()+"_"+self.year_var.get()+"FEE"
                self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'New_Admission')")
                search_admission_table = list(self.courser.fetchall()[0])

                if search_admission_table[0]==0:
                    m_box.showerror('Error','Sorry.....!\nThere is no Table on Admission \nplease Registered the Student .....')
                else:   
                    self.courser.execute(f"""CREATE TABLE IF NOT EXISTS {Table_Name}(Curr_Date VARCHAR(25),Std_Registeration_NO BIGINT NOT NULL PRIMARY KEY,
                                            Std_First_Name VARCHAR(25),Std_Last_Name VARCHAR(25),Std_Father_Name VARCHAR(25),Grade VARCHAR(15),
                                        Std_Class_No BIGINT, Dues BIGINT,Monthly_Fee BIGINT,Medical_Fee BIGINT,Transport_Fee BIGINT,
                                            Promotion_Fee BIGINT,Admission_Fee BIGINT,Second_Time_Fee BIGINT,Examination_Fee BIGINT,Total_Fee BIGINT);""")
                    
                    # =========================================================================================
                    # ============================================   Creat trigger on the table before updation
                    self.courser.execute(f"""CREATE TRIGGER IF NOT EXISTS {Table_Name} BEFORE UPDATE ON {Table_Name} FOR EACH ROW 
                                            SET NEW.Total_Fee = NEW.Dues + NEW.Monthly_Fee + NEW.Medical_Fee + NEW.Transport_Fee + NEW.Promotion_Fee + NEW.Admission_Fee + NEW.Second_Time_Fee + NEW.Examination_Fee;""")
                    
                    # ==================================================================================================
                    # =============================================   select data from new_Admission table for fee slip
                    try:
                        self.courser.execute(f"""select Std_Registeration_NO,Std_First_Name,Std_Last_Name,Std_Father_Name,Grade,Class_No,Monthly_Fee,
                                                Medical_Fee,Transport_Fee,Admission_Fee from New_Admission where Grade='{self.Class_var.get()}';""")
                        Std_record = self.courser.fetchall()
                        Std_data = [i for i in Std_record]
                    
                        # ================================================================================================
                        # =========================================  check the previous dues if submitte Fee in previous month
                        curr_month=self.Month_var.get()

                        dict_month = {"01":'January',"02":'February',"03":'March',"04":'April',"05":'May',"06":'June',
                                        "07":'July',"08":'August',"09":'September',"10":'October',"11":'November',"12":'December'}
                        for i in dict_month:
                            if dict_month[i] == curr_month:
                                month= str(int(i) - 1)
                        if len(month)==1:
                            month = "0"+month
                        previous_month = dict_month.get(month)
                        
                        # ========================================================================================
                        # ==================================== check previous month submitte fee if exists or not
                        previous_month_submitte = previous_month+"_"+self.year_submitte_fee_var.get()+"submitte_FEE"
                        
                        self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = '{previous_month_submitte}')")
                        previous_month_submitte_Table = list(self.courser.fetchall()[0])
                        # print(previous_month_submitte_Table)

                        # ==============================================================================================
                        # ====================================== previous month not submitte fee if exists or not 
                        previous_month_not_submitte = previous_month+"_"+self.year_submitte_fee_var.get()+"FEE"
                        
                        self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = '{previous_month_not_submitte}')")
                        previous_month_Table = list(self.courser.fetchall()[0])
                        # print(previous_month_Table)

                        # ==================================================================================================
                        # ==================================================================================================
                        if previous_month_submitte_Table[0] == 1:

                            # ===============================================================================================================
                            # ================== Get the previous balance of student if the student submitte fee but the balance is remaining
                            self.courser.execute(f"""select Std_Registeration_NO,Balance from {previous_month_submitte} where Grade='{self.Class_var.get()}'""")
                            record_dues= self.courser.fetchall()
                            # print(record_dues)
                            for i in Std_data:
                                dues = 0
                                self.courser.execute(f"""Insert IGNORE Into {Table_Name}(Curr_Date,Std_Registeration_NO,Std_First_Name,Std_Last_Name,Std_Father_Name,
                                                            Grade,Std_Class_No,Dues,Monthly_Fee,Medical_Fee,Transport_Fee,Promotion_Fee,Admission_Fee,
                                                            Second_Time_Fee,Examination_Fee,Total_Fee) 
                                                            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", 
                                                    (date_string,i[0],i[1],i[2],i[3],i[4],i[5],dues,i[6],i[7],i[8],promo_Fee,i[9],Sec_Time_Fee,Exam_Fee,0))
                                self.courser.execute(f"update new_Admission SET Admission_Fee='0' WHERE Std_Registeration_NO = {i[0]}")
                            # ======================================================================
                            # ==================================================  Update the table
                            for j in record_dues:
                                self.courser.execute(f"update {Table_Name} SET Dues={j[1]} WHERE Std_Registeration_NO = {j[0]}")

                        else:
                            dues=0
                            for i in Std_data:
                                self.courser.execute(f"""Insert IGNORE Into {Table_Name}(Curr_Date,Std_Registeration_NO,Std_First_Name,Std_Last_Name,Std_Father_Name,
                                                            Grade,Std_Class_No,Dues,Monthly_Fee,Medical_Fee,Transport_Fee,Promotion_Fee,Admission_Fee,
                                                            Second_Time_Fee,Examination_Fee,Total_Fee) 
                                                            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", 
                                                    (date_string,i[0],i[1],i[2],i[3],i[4],i[5],dues,i[6],i[7],i[8],promo_Fee,i[9],Sec_Time_Fee,Exam_Fee,0))
                                self.courser.execute(f"update {Table_Name} SET Dues=0 WHERE Std_Registeration_NO = {i[0]}")
                                self.courser.execute(f"update new_Admission SET Admission_Fee='0' WHERE Std_Registeration_NO = {i[0]}")
                        
                        # ============================================================================================
                        # ============================================================================================
                        if previous_month_Table[0] == 1:

                            self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = '{previous_month_submitte}')")
                            previous_month_submitte_Table = list(self.courser.fetchall()[0])

                            if previous_month_submitte_Table[0] == 1:
                                self.courser.execute(f"""select {previous_month_submitte}.Std_Registeration_NO from {previous_month_submitte}""")
                                record2 = self.courser.fetchall()
                                data2 = tuple([i[0] for i in record2])
                                # print(data2)
                    
                                self.courser.execute(f"""select {previous_month_not_submitte}.Std_Registeration_NO,{previous_month_not_submitte}.Total_Fee from {previous_month_not_submitte} where Grade='{self.Class_var.get()}' and Std_Registeration_No NOT IN {data2}""")
                                record3 = self.courser.fetchall()
                                data_of_not_submitte_fee_student = [i for i in record3]
                                # print(data_of_not_submitte_fee_student)
                                for k in data_of_not_submitte_fee_student:
                                    self.courser.execute(f"update {Table_Name} SET Dues={k[1]} WHERE Std_Registeration_NO = {k[0]}")
                            else:
                                self.courser.execute(f"""select {previous_month_not_submitte}.Std_Registeration_NO,{previous_month_not_submitte}.Total_Fee from {previous_month_not_submitte} where Grade='{self.Class_var.get()}'""")
                                record3 = self.courser.fetchall()
                                data_of_all_class_not_submitte = [i for i in record3]
                                # print(data_of_all_class_not_submitte)

                                for k in data_of_all_class_not_submitte:
                                    self.courser.execute(f"update {Table_Name} SET Dues={k[1]} WHERE Std_Registeration_NO = {k[0]}")
                        
                        self.courser.execute(f"""select * from {Table_Name}""")
                        for_print = self.courser.fetchall()
                        data_which_is_print = [i for i in for_print]
                        # print(data_which_is_print)
                        question = m_box.askyesno('Question','Do you want to generate the record?')
                        if question == 1:
                            prt = F_R.generatre_feeslip(data_which_is_print)
                            quest_for_print = m_box.askyesno('Question','Do you want to print Fee Slips?')
                            if quest_for_print == 1:
                                os.startfile(prt)
                            self.Class_var.set("")
                            self.Examination_var.set(0)
                            self.Promotion_var.set(0)
                            self.SecondTime_var.set(0)
                        else:
                            return

                    except Exception as es:
                        m_box.showerror('Error',f'Error Due to: {str(es)}')

        # ===========================================================================
        # ===========================================================================
        def Fee_Slip_Separate():
            date_string = strftime("%d/%m/%Y")
            Exam_Fee = self.Examination_student_var.get()
            promo_Fee = self.Promotion_student_var.get()
            Sec_Time_Fee  = self.SecondTime_student_var.get()
            class_no = self.Class_No_student_var.get().split(",")
            
            if self.Class_student_var.get()=="" or self.Month_student_var.get()=="" or self.year_student_var.get()=="" or self.Class_No_student_var.get()=="":
                m_box.showerror('Error','Please fill all the boxes\nTry again.... ')
            else:
                Table_Name = self.Month_student_var.get()+"_"+self.year_student_var.get()+"FEE"

                self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'New_Admission')")
                search_admission_table = list(self.courser.fetchall()[0])

                if search_admission_table[0]==0:
                    m_box.showerror('Error','Sorry.....!\nThere is no Table on Admission \nplease Registered the Student .....')
                else:    
                    self.courser.execute(f"""CREATE TABLE IF NOT EXISTS {Table_Name}(Curr_Date VARCHAR(25),Std_Registeration_NO BIGINT NOT NULL PRIMARY KEY,
                                            Std_First_Name VARCHAR(25),Std_Last_Name VARCHAR(25),Std_Father_Name VARCHAR(25),Grade VARCHAR(15),
                                        Std_Class_No BIGINT, Dues BIGINT,Monthly_Fee BIGINT,Medical_Fee BIGINT,Transport_Fee BIGINT,
                                            Promotion_Fee BIGINT,Admission_Fee BIGINT,Second_Time_Fee BIGINT,Examination_Fee BIGINT,Total_Fee BIGINT);""")
                    
                    self.courser.execute(f"""CREATE TRIGGER IF NOT EXISTS {Table_Name} BEFORE UPDATE ON {Table_Name} FOR EACH ROW 
                                            SET NEW.Total_Fee = NEW.Dues + NEW.Monthly_Fee + NEW.Medical_Fee + NEW.Transport_Fee + NEW.Promotion_Fee + NEW.Admission_Fee + NEW.Second_Time_Fee + NEW.Examination_Fee;""")
                    
                    # ======================================================================================================
                    # =========================================  check the previous dues if submitte Fee in previous month
                    curr_month=self.Month_student_var.get()

                    dict_month = {"01":'January',"02":'February',"03":'March',"04":'April',"05":'May',"06":'June',
                                    "07":'July',"08":'August',"09":'September',"10":'October',"11":'November',"12":'December'}
                    for i in dict_month:
                        if dict_month[i] == curr_month:
                            month= str(int(i) - 1)
                    if len(month)==1:
                        month = "0"+month
                    previous_month = dict_month.get(month)
                    
                    # =======================================================  previous month submitte fee Table
                    previous_month_submitte = previous_month+"_"+self.year_student_var.get()+"submitte_FEE"
                    
                    self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = '{previous_month_submitte}')")
                    previous_month_submitte_Table = list(self.courser.fetchall()[0])
                    # print(previous_month_submitte_Table)

                    # ==============================================================================
                    # =======================================================  previous month Table
                    previous_month_not_submitte = previous_month+"_"+self.year_student_var.get()+"FEE"
                    
                    self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = '{previous_month_not_submitte}')")
                    previous_month_Table = list(self.courser.fetchall()[0])
                    # print(previous_month_Table)
            
                    # ==================================================================================================
                    # ==================================================================================================
                    if len(class_no) == 1:
                        self.courser.execute(f"""select Std_Registeration_NO,Std_First_Name,Std_Last_Name,Std_Father_Name,Grade,Class_No,Monthly_Fee,
                                            Medical_Fee,Transport_Fee,Admission_Fee from New_Admission where Grade='{self.Class_student_var.get()}' and Class_no={self.Class_No_student_var.get()};""")
                        record = self.courser.fetchall()
                        if len(record)==0:
                            m_box.showerror('Error',f'The Grade: {self.Class_student_var.get()} and Class No: {self.Class_No_student_var.get()}\n are incorrect')
                        else:
                            data = [i for i in record]
                            dues = 0
                            for i in data:
                                self.courser.execute(f"""Insert IGNORE Into {Table_Name}(Curr_Date,Std_Registeration_NO,Std_First_Name,Std_Last_Name,Std_Father_Name,
                                                            Grade,Std_Class_No,Dues,Monthly_Fee,Medical_Fee,Transport_Fee,Promotion_Fee,Admission_Fee,
                                                            Second_Time_Fee,Examination_Fee,Total_Fee ) 
                                                            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", 
                                                    (date_string,i[0],i[1],i[2],i[3],i[4],i[5],dues,i[6],i[7],i[8],promo_Fee,i[9],Sec_Time_Fee,Exam_Fee,0))
                                self.courser.execute(f"update new_Admission SET Admission_Fee='0' WHERE Std_Registeration_NO = {i[0]}")
                            
                            
                            # ==================================================================================================
                            # ==================================================================================================
                            if previous_month_submitte_Table[0] == 1:
                                # ===============================================================================================================
                                # ================== Get the previous balance of student if the student submitte fee but the balance is remaining
                                self.courser.execute(f"""select Std_Registeration_NO,Balance from {previous_month_submitte} where Grade='{self.Class_student_var.get()}' and Std_Class_No={self.Class_No_student_var.get()}""")
                                record_dues_submitte= self.courser.fetchall()
                                # print(record_dues_submitte)

                                if len(record_dues_submitte) == 0:
                                    self.courser.execute(f"""select Std_Registeration_NO,Total_Fee from {previous_month_not_submitte} where Grade='{self.Class_student_var.get()}' and Std_Class_No={self.Class_No_student_var.get()}""")
                                    record_dues_in_previous_table= self.courser.fetchall()
                                    # print(record_dues_in_previous_table)

                                    for i in record_dues_in_previous_table:
                                        self.courser.execute(f"update {Table_Name} SET Dues={i[1]} WHERE Std_Registeration_NO = {i[0]}")
                                else:
                                    for j in record_dues_submitte:
                                        self.courser.execute(f"update {Table_Name} SET Dues={j[1]} WHERE Std_Registeration_NO = {j[0]}")
                            # ============================================================================================
                            # ============================================================================================
                            if previous_month_Table[0] == 1:
                                self.courser.execute(f"""select {previous_month_not_submitte}.Std_Registeration_NO,{previous_month_not_submitte}.Total_Fee from {previous_month_not_submitte} where Grade='{self.Class_student_var.get()}' and Std_Class_No={self.Class_No_student_var.get()}""")
                                record3 = self.courser.fetchall()
                                data_of_not_submitte_fee_student = [i for i in record3]
                                # print(data_of_not_submitte_fee_student)

                                for k in data_of_not_submitte_fee_student:
                                    self.courser.execute(f"update {Table_Name} SET Dues={k[1]} WHERE Std_Registeration_NO = {k[0]}")  
                            # ============================================================================
                            # ====================================show the data in pdf file for printing
                            self.courser.execute(f"""select * from {Table_Name} where Std_Class_No = {self.Class_No_student_var.get()}""")
                            for_print = self.courser.fetchall()
                            data_which_is_print = [i for i in for_print]
                            # ====================================================  this data is for print out fee slip
                            # print(data_which_is_print)

                            question = m_box.askyesno('Question','Do you want to generate the record?')
                            if question==1:
                                prt = F_R.generatre_feeslip(data_which_is_print)
                                quest_for_print = m_box.askyesno('Question','Do you want to print Fee Slip?')
                                if quest_for_print == 1:
                                    os.startfile(prt)
                                self.Class_student_var.set("")
                                self.Class_No_student_var.set("")
                                self.Examination_student_var.set(0)
                                self.Promotion_student_var.set(0)
                                self.SecondTime_student_var.set(0)
                            else:
                                return
                    else:
                        C_NO = tuple(class_no)
                        self.courser.execute(f"""select Std_Registeration_NO,Std_First_Name,Std_Last_Name,Std_Father_Name,Grade,Class_No,Monthly_Fee,
                                                Medical_Fee,Transport_Fee,Admission_Fee from New_Admission where Grade='{self.Class_student_var.get()}' and Class_no IN {C_NO};""")
                        record = self.courser.fetchall()
                        # print(record)

                        if len(record)==0:
                            m_box.showerror('Error',f'The Grade: {self.Class_student_var.get()} and Class No: {C_NO}\n are incorrect')
                        else:
                            data = [i for i in record]
                            dues = 0
                        
                            for i in data:
                                self.courser.execute(f"""Insert IGNORE Into {Table_Name}(Curr_Date,Std_Registeration_NO,Std_First_Name,Std_Last_Name,Std_Father_Name,
                                                            Grade,Std_Class_No,Dues,Monthly_Fee,Medical_Fee,Transport_Fee,Promotion_Fee,Admission_Fee,
                                                            Second_Time_Fee,Examination_Fee,Total_Fee) 
                                                            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", 
                                                    (date_string,i[0],i[1],i[2],i[3],i[4],i[5],dues,i[6],i[7],i[8],promo_Fee,i[9],Sec_Time_Fee,Exam_Fee,0))
                                self.courser.execute(f"update new_Admission SET Admission_Fee='0' WHERE Std_Registeration_NO = {i[0]}")
                            
                            
                            # ==================================================================================================
                            # ==================================================================================================
                            if previous_month_submitte_Table[0] == 1:
                                # ===============================================================================================================
                                # ================== Get the previous balance of student if the student submitte fee but the balance is remaining
                                self.courser.execute(f"""select Std_Registeration_NO,Balance from {previous_month_submitte} where Grade='{self.Class_student_var.get()}' and Std_Class_No IN {C_NO}""")
                                record_dues_submitte_stds= self.courser.fetchall()
                                # print(record_dues_submitte_stds)

                                if len(record_dues_submitte_stds) == 0:
                                    self.courser.execute(f"""select Std_Registeration_NO,Total_Fee from {previous_month_not_submitte} where Grade='{self.Class_student_var.get()}' and Std_Class_No IN {C_NO}""")
                                    record_dues_in_previous_table= self.courser.fetchall()
                                    # print(record_dues_in_previous_table)

                                    for i in record_dues_in_previous_table:
                                        self.courser.execute(f"update {Table_Name} SET Dues={i[1]} WHERE Std_Registeration_NO = {i[0]}")
                                else:
                                    for j in record_dues_submitte_stds:
                                        self.courser.execute(f"update {Table_Name} SET Dues={j[1]} WHERE Std_Registeration_NO = {j[0]}")
                            # # ============================================================================================
                            # # ============================================================================================
                            if previous_month_Table[0] == 1:
                                self.courser.execute(f"""select {previous_month_not_submitte}.Std_Registeration_NO,{previous_month_not_submitte}.Total_Fee from {previous_month_not_submitte} where Grade='{self.Class_student_var.get()}' and Std_Class_No IN {C_NO}""")
                                record3 = self.courser.fetchall()
                                data_of_not_submitte_fee_student = [i for i in record3]
                                # print(data_of_not_submitte_fee_student)
                                
                                for k in data_of_not_submitte_fee_student:
                                    self.courser.execute(f"update {Table_Name} SET Dues={k[1]} WHERE Std_Registeration_NO = {k[0]}")
                            
                            # ============================================================================
                            # ====================================show the data in pdf file for printing
                        
                            self.courser.execute(f"""select * from {Table_Name} where Std_Class_No IN {C_NO}""")
                            for_print = self.courser.fetchall()
                            data_which_is_print = [i for i in for_print]
                            # ==============================   this data is for print out fee slip
                            question = m_box.askyesno('Question','Do you want to generate the record?')
                            if question==1:
                                prt = F_R.generatre_feeslip(data_which_is_print)
                                quest_for_print = m_box.askyesno('Question','Do you want to print the fee Slips?')
                                if quest_for_print == 1:
                                    os.startfile(prt)
                                self.Class_student_var.set("")
                                self.Class_No_student_var.set("")
                                self.Examination_student_var.set(0)
                                self.Promotion_student_var.set(0)
                                self.SecondTime_student_var.set(0)
                            else:
                                return
                    

        # =============================================================================
        # =============================================================================
        def submitte_fee():
            date_string = strftime("%d/%m/%Y")
            grade = self.Class_submitte_fee_var.get()
            month = self.Month_submitte_fee_var.get()
            year = self.year_submitte_fee_var.get()
            class_no = self.Class_No_submitte_fee_var.get()
            discount = self.Discount_submitte_fee_var.get()
            paid = self.Paid_submitte_fee_var.get()
            

            if self.Class_submitte_fee_var.get()=="" or self.Month_submitte_fee_var.get()=="" or self.year_submitte_fee_var.get()=="" or self.Class_No_submitte_fee_var.get()=="" or self.Discount_submitte_fee_var.get()=="" or self.Paid_submitte_fee_var.get()=="":
                m_box.showerror('Error','Please fill all the boxes\nTry again.... ')
            else:
                submitte_fee_table = self.Month_submitte_fee_var.get()+"_"+self.year_submitte_fee_var.get()+"submitte_FEE"

                Table_Name = self.Month_submitte_fee_var.get()+"_"+self.year_submitte_fee_var.get()+"FEE"

                self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = '{Table_Name}')")
                check_unsubmitte_class = list(self.courser.fetchall()[0])
                # print(check_submitte_class[0])

                if check_unsubmitte_class[0] == 0:
                    m_box.showerror('Error',f'Sorry......!\nthere is no Table on {Table_Name}')
                else:   
                    self.courser.execute(f"""select Std_Registeration_NO,Std_First_Name,Std_Last_Name,Std_Father_Name,Total_Fee from {Table_Name} 
                                            where Grade='{self.Class_submitte_fee_var.get()}' and std_Class_No = '{self.Class_No_submitte_fee_var.get()}';""")
                    record = self.courser.fetchall()
                    data = [i for i in record]
                    # print(data)

                    if len(data) == 0:
                        m_box.showerror('Error','Sorry!\none of your Entry is incorrect\nClass OR Class No\nTry again.... ')
                    else:
                        self.courser.execute(f"""CREATE TABLE IF NOT EXISTS {submitte_fee_table}(Curr_Date VARCHAR(25),Std_Registeration_NO BIGINT NOT NULL PRIMARY KEY,
                                                Std_First_Name VARCHAR(25),Std_Last_Name VARCHAR(25),Std_Father_Name VARCHAR(25),Grade VARCHAR(15),
                                                Month VARCHAR(25),Year VARCHAR(25),Std_Class_No BIGINT,Total_Fee BIGINT,Discount BIGINT,Paid BIGINT,Balance BIGINT);""")
                        

                        self.courser.execute(f"""CREATE TRIGGER IF NOT EXISTS {submitte_fee_table} BEFORE INSERT ON {submitte_fee_table} FOR EACH ROW 
                                                SET NEW.Balance = NEW.Total_Fee - (NEW.Discount+NEW.Paid);""")

                    
                        self.courser.execute(f"""Insert IGNORE Into {submitte_fee_table} (Curr_Date,Std_Registeration_NO,Std_First_Name,Std_Last_Name,Std_Father_Name,
                                                        Grade,Month,Year,Std_Class_No,Total_Fee ,Discount,Paid,Balance) 
                                                        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", 
                                                (date_string,data[0][0],data[0][1],data[0][2],data[0][3],grade,month,year,class_no,data[0][4],discount,paid,0))
                        m_box.showinfo('Information',f'Your Fee is submitted Successfuly.......\nThank you')
                        # =================================
                        self.Class_submitte_fee_var.set("")
                        self.Class_No_submitte_fee_var.set("")
                        self.Discount_submitte_fee_var.set(0)
                        self.Paid_submitte_fee_var.set("")


        # =============================================================================
        # =============================================================================
        def submitte_spicific_fee():
            date_string = strftime("%d/%m/%Y")
            month = self.Month_submitte_fee_std_var.get()
            year = self.year_submitte_fee_std_var.get()
            Reg_no = self.Reg_No_submitte_fee_std_var.get()
            adjust = self.Adjust_submitte_fee_std_var.get()
            paid = self.Paid_submitte_fee_std_var.get()
            

            if  self.Month_submitte_fee_std_var.get()=="" or self.year_submitte_fee_std_var.get()=="" or self.Reg_No_submitte_fee_std_var.get()=="" or self.Adjust_submitte_fee_std_var.get()=="" or self.Paid_submitte_fee_std_var.get()=="":
                m_box.showerror('Error','Please fill all the boxes\nTry again.... ')
            else:
                submitte_fee_table = self.Month_submitte_fee_std_var.get()+"_"+self.year_submitte_fee_std_var.get()+"submitte_FEE"

                Table_Name = self.Month_submitte_fee_std_var.get()+"_"+self.year_submitte_fee_std_var.get()+"FEE"
                
                self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = '{Table_Name}')")
                check_unsubmitte_class = list(self.courser.fetchall()[0])
                # print(check_submitte_class[0])
                
                if check_unsubmitte_class[0] == 0:
                    m_box.showinfo('Information',f'Sorry......!\nthere is no Table on {Table_Name}')
                else: 
                    self.courser.execute(f"""select Std_First_Name,Std_Last_Name,Std_Father_Name,Grade,Std_Class_No,Total_Fee from {Table_Name} 
                                            where Std_registeration_NO='{Reg_no}';""")
                    record = self.courser.fetchall()
                    data = [i for i in record]
                    
                    if len(data) == 0:
                        m_box.showerror('Error','Sorry!\nYour Registeration No is incorrect\nTry again.... ')
                    else:
                        self.courser.execute(f"""CREATE TABLE IF NOT EXISTS {submitte_fee_table}(Curr_Date VARCHAR(25),Std_Registeration_NO BIGINT NOT NULL PRIMARY KEY,
                                                Std_First_Name VARCHAR(25),Std_Last_Name VARCHAR(25),Std_Father_Name VARCHAR(25),Grade VARCHAR(15),
                                                Month VARCHAR(25),Year VARCHAR(25),Std_Class_No BIGINT,Total_Fee BIGINT,Discount BIGINT,Paid BIGINT,Balance BIGINT);""")
                        

                        self.courser.execute(f"""CREATE TRIGGER IF NOT EXISTS {submitte_fee_table} BEFORE INSERT ON {submitte_fee_table} FOR EACH ROW 
                                            SET NEW.Balance = NEW.Total_Fee - (NEW.Discount+NEW.Paid);""")

                
                    
                        self.courser.execute(f"""Insert IGNORE Into {submitte_fee_table} (Curr_Date,Std_Registeration_NO,Std_First_Name,Std_Last_Name,Std_Father_Name,
                                                        Grade,Month,Year,Std_Class_No,Total_Fee ,Discount,Paid,Balance) 
                                                        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", 
                                                (date_string,Reg_no,data[0][0],data[0][1],data[0][2],data[0][3],month,year,data[0][4],data[0][5],adjust,paid,0))
                    
                        m_box.showinfo('Information',f'Your Fee is submitted Successfuly.......\nThank you')
                    #  =======================  
                        self.Reg_No_submitte_fee_std_var.set("")
                        self.Paid_submitte_fee_std_var.set("")
                        self.Adjust_submitte_fee_std_var.set(0)
            
        # ==============================================================================================================
        # ==============================================================================================================
        def fee_detail():
            check_submitte_fee = self.Month_check_fee_var.get()+"_"+self.year_check_fee_var.get()+"submitte_FEE"
            check_all_fee = self.Month_check_fee_var.get()+"_"+self.year_check_fee_var.get()+"FEE"

            self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = '{check_submitte_fee}')")
            check_submitte_class = list(self.courser.fetchall()[0])
            # print(check_submitte_class)

            self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = '{check_all_fee}')")
            check_all = list(self.courser.fetchall()[0])
            # print(type(check_all))

            if  self.Month_check_fee_var.get()=="" or self.year_check_fee_var.get()=="" or self.Class_check_fee_var.get()=="":
                m_box.showerror('Error','Please fill all the boxes\nTry again.... ')
            else:
                if self.Class_check_fee_var.get()=="All":
                    if check_all[0] == 0:
                        m_box.showerror('Error',f'There is No Data on this Month ({self.Month_check_fee_var.get()})\nPlease Generate the fee slip record\nTry again.... ')
                    else:
                        self.courser.execute(f"""select {check_all_fee}.Std_Registeration_NO from {check_all_fee}""")
                        record1 = self.courser.fetchall()
                        data1 = [i[0] for i in record1]
                        all_student = len(data1)
                        if check_submitte_class[0]==0:
                            submitte_fee_student = 0
                            self.remaining_fee_std_detail_var.set(all_student)
                        else:    
                            self.courser.execute(f"""select {check_submitte_fee}.Std_Registeration_NO from {check_submitte_fee} """)
                            record2 = self.courser.fetchall()
                            data2 = tuple([i[0] for i in record2])
                            submitte_fee_student = len(data2)
                        
                            if len(data2) == 0:
                                m_box.showerror('Not Submitted',f'No one in {self.Class_check_fee_var.get()} School paid the fee \nTry again....')
                                self.remaining_fee_std_detail_var.set(all_student)
                            elif len(data2) == 1:
                                data_1 = data2[0]
                                self.courser.execute(f"""select {check_all_fee}.Std_Registeration_NO from {check_all_fee} where Std_Registeration_No != {data_1}""")
                                record3 = self.courser.fetchall()
                                data3 = [i[0] for i in record3]
                                not_submitte_fee_student = len(data3)
                                self.remaining_fee_std_detail_var.set(not_submitte_fee_student)

                            else:
                                self.courser.execute(f"""select {check_all_fee}.Std_Registeration_NO from {check_all_fee} where Std_Registeration_No NOT IN {data2}""")
                                record3 = self.courser.fetchall()
                                data3 = [i[0] for i in record3]
                                not_submitte_fee_student = len(data3)
                                self.remaining_fee_std_detail_var.set(not_submitte_fee_student)

                        self.All_std_detail_var.set(all_student)
                        self.submitte_fee_std_detail_var.set(submitte_fee_student)
                # =========================================================================   Spicific class 
                else:
                    if check_all[0]==0:
                        m_box.showerror('Error',f'There is No Data on this Class: {self.Class_check_fee_var.get()} and Month: {self.Month_check_fee_var.get()}\nPlease generate the fee slips record\nTry again.... ')
                    else:
                        self.courser.execute(f"""select {check_all_fee}.Std_Registeration_NO from {check_all_fee} where Grade='{self.Class_check_fee_var.get()}'""")
                        record4 = self.courser.fetchall()
                        data4 = [i for i in record4]
                        class_all_student = len(data4)
                        if check_submitte_class[0]==0:
                            submitte_fee_student = 0
                            class_submitte_fee_student=0
                            self.remaining_fee_std_detail_var.set(class_all_student)
                        else:    
                            self.courser.execute(f"""select {check_submitte_fee}.Std_Registeration_NO from {check_submitte_fee}  where Grade='{self.Class_check_fee_var.get()}'""")
                            record5 = self.courser.fetchall()
                            data5 =tuple([i[0] for i in record5])
                            class_submitte_fee_student = len(data5)
                        
                            if len(data5) == 0:
                                m_box.showinfo('Not Submitted',f'No one in Class {self.Class_check_fee_var.get()} paid the fee \nTry again....')
                                submitte_fee_student = 0
                                self.remaining_fee_std_detail_var.set(class_all_student)
                            elif len(data5) == 1:
                                data_2 = data5[0]
                                self.courser.execute(f"""select {check_all_fee}.Std_Registeration_NO from {check_all_fee} where Grade='{self.Class_check_fee_var.get()}' and Std_Registeration_No != {data_2}""")
                                record6 = self.courser.fetchall()
                                data6 = [i[0] for i in record6]
                                class_not_submitte_fee_student = len(data6)
                                self.remaining_fee_std_detail_var.set(class_not_submitte_fee_student)
                                
                            else:
                                self.courser.execute(f"""select {check_all_fee}.Std_Registeration_NO from {check_all_fee} where Grade='{self.Class_check_fee_var.get()}' and Std_Registeration_No NOT IN {data5}""")
                                record6 = self.courser.fetchall()
                                data6 = [i[0] for i in record6]
                                class_not_submitte_fee_student = len(data6)
                                self.remaining_fee_std_detail_var.set(class_not_submitte_fee_student)

                        self.All_std_detail_var.set(class_all_student)
                        self.submitte_fee_std_detail_var.set(class_submitte_fee_student)



        
        # ===============================================================
        # ====================================================  Buttons 
        generate_all_fee = Button(self.frame2,text="Generate Fee Slip",command=Fee_Slip_all,cursor="hand2",
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        generate_all_fee.place(x=80,y=290)

        generate_spicific_fee = Button(self.frame3,text="Generate Fee Slip",command=Fee_Slip_Separate,cursor="hand2",
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        generate_spicific_fee.place(x=80,y=290)

        submitte_fee = Button(self.frame4,text="Submitte Fee",command=submitte_fee,cursor="hand2",
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        submitte_fee.place(x=80,y=290)

        submitte_spicific_fee = Button(self.frame5,text="Submitte Fee",command=submitte_spicific_fee,cursor="hand2",
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        submitte_spicific_fee.place(x=80,y=200)

        check_fee = Button(self.frame6,text="Check Detail",command=fee_detail,cursor="hand2",
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        check_fee.place(x=70,y=200)

        clear_fee = Button(self.frame6,text="Clear",width=8,command=clear,cursor="hand2",
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        clear_fee.place(x=429,y=200)   










    






#                          Start the function which maintain the result of all student with all functionality
# ==============================================================================================================================
# ==============================================================================================================================
# ==================================  Result data
# ==============================================================================================================================
# ==============================================================================================================================
    def Result_data(self):
         # ===============================================================
        # =============================================  All Variable
        self.Class = StringVar()
        self.Exam = StringVar()
        self.Year = StringVar()
        self.Subject = StringVar()
       
        # ===============================
        # ===============================
        self.Disp_result_Class = StringVar()
        self.Disp_result_Exam = StringVar()
        self.Disp_result_Year = StringVar()
        self.Disp_result_Class_No = StringVar()
        
        # ===============================
        # ===============================
        self.gen_result_Class = StringVar()
        self.gen_result_Exam = StringVar()
        self.gen_result_Year = StringVar()

        # ===============================================================
        # ==================================================== Frames  s
  

        self.frame1 = Frame(self.main_frame,bg="#0b9798",width=850,height=600)
        self.frame1.place(x=0,y=5)
        
        # --------------------------------  Upload award List
        self.frame2 = Frame(self.frame1,bg="#0b9798",width=435,height=270,relief=RIDGE,bd=2)
        self.frame2.place(x=6,y=6)
        
        # --------------------------------  Display student result
        self.frame3 = Frame(self.frame1,bg="#0b9798",width=260,height=305,relief=RIDGE,bd=2)
        self.frame3.place(x=6,y=280)
        
        # ------------------------  generate result
        self.frame5 = Frame(self.frame1,bg="#0b9798",width=350,height=270,relief=RIDGE,bd=2)
        self.frame5.place(x=446,y=6)
        
        # -----------------------    Scrollbar
        self.frame6 = Frame(self.frame1,bg="#b3ffff",width=527,height=305,relief= RIDGE,bd=2)
        self.frame6.place(x=270,y=280)
        

        
        # ================================================================
        # =====================================   Labels and Entry Boxes
        year =[]
        for i in range(2000,2100):
            year.append(i)
      
        # ==================================================================
        # ========================  SQL Query to show ths all subjects

        self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'course_registeration')")
        check_course_table = list(self.courser.fetchall()[0])

        if check_course_table[0]==0:
            show_course_in_combobox=("No_Subject")
        else:
            self.courser.execute(f"SELECT Course_Name FROM CMS.course_registeration")
            show_course = self.courser.fetchall()
            if len(show_course)>0:
                show_course_in_combobox = show_course
            else:
                show_course_in_combobox=("No_Subject")
        # ========================================================================================================
        # ========================================================================================================
        lab_1 = Label(self.frame2,text='Upload Award List to Submitte Result',padx=10,font=("Times New Roman",14),bg="#0b9798",fg="white")
        lab_1.place(x=55,y=10)

        class_lbl = Label(self.frame2,text='Class',font=("Times New Roman",14),bg="#0b9798",fg="white")
        class_lbl.place(x=120,y=70)
        class_entery_box = ttk.Combobox(self.frame2,width=11,textvariable=self.Class,state="readonly", font=("Arial",10))
        class_entery_box["values"] = ("Ist","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th")
        class_entery_box.place(x=200,y=72)
        
        Exam_lbl = Label(self.frame2,text='Exam',font=("Times New Roman",14),bg="#0b9798",fg="white")
        Exam_lbl.place(x=120,y=100)
        Exam_entery_box = ttk.Combobox(self.frame2,width=11,textvariable=self.Exam,state="readonly", font=("Arial",10))
        Exam_entery_box["values"] = ("First","Second","Final")
        Exam_entery_box.place(x=200,y=102)

        Year_lbl = Label(self.frame2,text='Year',font=("Times New Roman",14),bg="#0b9798",fg="white")
        Year_lbl.place(x=120,y=130)
        Year_entery_box = ttk.Combobox(self.frame2,width=11,textvariable=self.Year,font=("Arial",10))
        Year_entery_box["values"] = (year)
        Year_entery_box.place(x=200,y=132)

        subject_lbl = Label(self.frame2,text='Subject',font=("Times New Roman",14),bg="#0b9798",fg="white")
        subject_lbl.place(x=120,y=160)
        subject_entery_box = ttk.Combobox(self.frame2,width=11,textvariable=self.Subject,font=("Arial",10))
        subject_entery_box["values"] = (show_course_in_combobox)
        subject_entery_box.place(x=200,y=162)
        # "Biology","Chemistry","Computer","English","English Grammer","Islamyat","Maths","Pak Study","Physics","Science","Urdu","Urdu Grammer"
        # ========================================================================================================
        # ========================================================================================================
        lab_4 = Label(self.frame5,text='Generate Result',padx=10,font=("Times New Roman",14),bg="#0b9798",fg="white")
        lab_4.place(x=90,y=10)

        class_display_lbl = Label(self.frame5,text='Class',font=("Times New Roman",14),bg="#0b9798",fg="white")
        class_display_lbl.place(x=80,y=70)
        class_display_entery_box = ttk.Combobox(self.frame5,width=11,textvariable=self.gen_result_Class,state="readonly", font=("Arial",10))
        class_display_entery_box["values"] = ("Ist","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th")
        class_display_entery_box.place(x=150,y=72)
        
        Exam_display_lbl = Label(self.frame5,text='Exam',font=("Times New Roman",14),bg="#0b9798",fg="white")
        Exam_display_lbl.place(x=80,y=100)
        Exam_display_entery_box = ttk.Combobox(self.frame5,width=11,textvariable=self.gen_result_Exam,state="readonly", font=("Arial",10))
        Exam_display_entery_box["values"] = ("First","Second","Final")
        Exam_display_entery_box.place(x=150,y=102)

        Year_display_lbl = Label(self.frame5,text='Year',font=("Times New Roman",14),bg="#0b9798",fg="white")
        Year_display_lbl.place(x=80,y=130)
        Year_display_entery_box = ttk.Combobox(self.frame5,width=11,textvariable=self.gen_result_Year,font=("Arial",10))
        Year_display_entery_box["values"] = (year)
        Year_display_entery_box.place(x=150,y=132)        

         
        # ========================================================================================================
        # ========================================================================================================
        lab_2 = Label(self.frame3,text='Display Student Result',padx=10,font=("Times New Roman",14),bg="#0b9798",fg="white")
        lab_2.place(x=30,y=10)

        class_display_lbl = Label(self.frame3,text='Class',font=("Times New Roman",14),bg="#0b9798",fg="white")
        class_display_lbl.place(x=35,y=70)
        class_display_entery_box = ttk.Combobox(self.frame3,width=11,textvariable=self.Disp_result_Class,state="readonly", font=("Arial",10))
        class_display_entery_box["values"] = ("Ist","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th")
        class_display_entery_box.place(x=127,y=72)
        
        Exam_display_lbl = Label(self.frame3,text='Exam',font=("Times New Roman",14),bg="#0b9798",fg="white")
        Exam_display_lbl.place(x=35,y=100)
        Exam_display_entery_box = ttk.Combobox(self.frame3,width=11,textvariable=self.Disp_result_Exam,state="readonly", font=("Arial",10))
        Exam_display_entery_box["values"] = ("First","Second","Final")
        Exam_display_entery_box.place(x=127,y=102)

        Year_display_lbl = Label(self.frame3,text='Year',font=("Times New Roman",14),bg="#0b9798",fg="white")
        Year_display_lbl.place(x=35,y=130)
        Year_display_entery_box = ttk.Combobox(self.frame3,width=11,textvariable=self.Disp_result_Year,font=("Arial",10))
        Year_display_entery_box["values"] = (year)
        Year_display_entery_box.place(x=127,y=132)

        class_no_lbl = Label(self.frame3,text='Class NO',font=("Times New Roman",14),bg="#0b9798",fg="white")
        class_no_lbl.place(x=35,y=160)
        class_no_entery_box = Entry(self.frame3,width=12,textvariable=self.Disp_result_Class_No,font=("Arial",11))
        class_no_entery_box.place(x=127,y=162)


        # ==========================================================================================================
        # ==========================================================================================================
        def creat_award_list():
            
            if self.Class.get()=="" or self.Exam.get()=="" or self.Year.get()=="" or self.Subject.get()=="":
                m_box.showerror('Error','Please fill all the boxes\nTry again.... ')
            else:
                file=filedialog.askopenfilename()
                file = Document(file)
                first_data = []
                for table in file.tables:
                    for row in table.rows:
                        for cell in row.cells:
                                first_data.append(cell.text)
                final_data = []
                start = 0
                end = 4
                for i in range(len(first_data)//4):
                        final_data.append(first_data[start:end])
                        start = end
                        end = end+4
                final_data = final_data[1:]
                # print(final_data)
                # ========================================================
                # ===================== create new window for award list
                self.award_win = Toplevel()
                self.award_win.title("Create Award ist")
                self.award_win.grab_set()
                self.award_win.resizable(False,False)
                self.award_win.geometry("500x400+350+50")
            
                # ========================================================
                # ===================   create frames in award_win window
                self.Frame2 = Frame(self.award_win)
                self.Frame2.pack()
                self.Frame = Frame(self.award_win,width=500,height=500,relief=RIDGE,bd=4)
                self.Frame.place(x=7,y=100)

                # ========================================================
                # ==================   Labels scroll bar to show ward list
                lbl1 = Label(self.Frame2,text=f'New Informatics Model School\nNIMS & College\nAward List of Class {self.Class.get()} {self.Subject.get()}\n{self.Exam.get()} term Exam',font=("Times New Roman",14))
                lbl1.grid(row=0,column=0,columnspan=20) 
                
                style = ttk.Style()
                style.configure('Treeview.Heading',font=("Times New Roman",10,'bold'))
                style.configure('Treeview',font=("Times New Roman",10),background="cyan",foreground='black')

                scroll_y = Scrollbar(self.Frame,orient=VERTICAL)

                self.studenttabel = Treeview(self.Frame , columns=('Class No','Name','Total Marks','Obtained Marks'),yscrollcommand=scroll_y.set,)

                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_y.config(command=self.studenttabel.yview)

                self.studenttabel.heading('Class No', text="Class No")
                self.studenttabel.heading('Name', text="Name")
                self.studenttabel.heading('Total Marks', text="Total Marks")
                self.studenttabel.heading('Obtained Marks', text="Obtained Marks")

                self.studenttabel['show']='headings'

                self.studenttabel.column('Class No',width=70)
                self.studenttabel.column('Name',width=150)
                self.studenttabel.column('Total Marks',width=120)
                self.studenttabel.column('Obtained Marks',width=120)
                self.studenttabel.pack(fill=BOTH,expand=1)

                for i in final_data:
                    list_1= [i[0],i[1],i[2],i[3]]
                    self.studenttabel.insert('',END,values=list_1)
                
                # ========================================================
                # ========================================================
            
                def Submitte_award_list():
                    Exam_Table = self.Exam.get()+"_Term_Exam_"+self.Year.get()

                    self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'New_Admission')")
                    search_admission_table = list(self.courser.fetchall()[0])

                    if search_admission_table[0]==0:
                        m_box.showerror('Error','Sorry.....!\nThere is no Table on Admission \nplease Registered the Student .....')
                    else:
                        self.courser.execute(f"""select Std_Registeration_NO,Std_First_Name,Std_Last_Name,Std_Father_Name,Class_no from New_Admission
                                                where Grade='{self.Class.get()}';""")
                        record = self.courser.fetchall()
                        data = [i for i in record]
                        # print(record)
                        # print(data)

                        self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'ASSIGN_COURSES')")
                        search_assign_course_table = list(self.courser.fetchall()[0])
                        # print(search_assign_course_table_table)
                        if search_assign_course_table[0]==0:
                            m_box.showerror('Error','Sorry.....!\nThere is no course assign to the class \nplease Registered the course and then assign to class .....')
                        else:
                            self.courser.execute(f"SELECT Course_Id FROM CMS.course_Registeration where Course_Name='{self.Subject.get()}'")
                            check_assign_course = self.courser.fetchall()
                            course = [i[0] for i in check_assign_course]
                            course_id = course[0]
                            # print(type(course_id))

                            self.courser.execute(f"SELECT * FROM CMS.ASSIGN_COURSES where Course_Id={course_id} and Grade='{self.Class.get()}'")
                            check_assign_course = self.courser.fetchall()
                            # print(check_assign_course)
                            if len(check_assign_course) ==0:
                                m_box.showerror('Error','Sorry.....!\nThis course is not Assign to the this class\nplease first assign the course and then upload award list')
                            else:
                                self.courser.execute(f"""CREATE TABLE IF NOT EXISTS CMS.{Exam_Table}(Std_Registeration_NO BIGINT,Std_First_Name VARCHAR(25),
                                                        Std_Last_Name VARCHAR(25),Std_Father_Name VARCHAR(25),Grade VARCHAR(10),Class_no INT,Exam VARCHAR(25),
                                                        Subject_Name VARCHAR(25),Subject_Marks INT,Obtain_Marks INT,Status VARCHAR(25) , PRIMARY KEY(Grade,Class_No,Subject_Name));""")
                                
                                
                                self.courser.execute(f"""CREATE TRIGGER IF NOT EXISTS {Exam_Table} BEFORE UPDATE ON CMS.{Exam_Table} FOR EACH ROW
                                                        SET NEW.Status = IF((NEW.Obtain_Marks/NEW.Subject_Marks)*100 <50,"Fail","Pass");""")
                                
                                # print(data)
                                # print(self.Exam.get(),self.Class.get(),self.Subject.get())
                                for i in data:
                                    self.courser.execute(f"""Insert IGNORE Into {Exam_Table} (Std_Registeration_NO,Std_First_Name,Std_Last_Name,Std_Father_Name,
                                                            Class_no,Grade,Exam,Subject_Name,Subject_Marks,Obtain_Marks,Status) 
                                                            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                                                            (i[0],i[1],i[2],i[3],i[4],self.Class.get(),self.Exam.get(),self.Subject.get(),0,0,0))
                                
                                for i in final_data:
                                    self.courser.execute(f"""update {Exam_Table} SET Subject_Marks= {i[2]}, Obtain_Marks = {i[3]} WHERE Grade='{self.Class.get()}' and Subject_Name = '{self.Subject.get()}' and Class_No = {i[0]}""")
                                
                                m_box.showinfo('Submitte Award List','Your Award List is Submitte Successfuly\nThank You ')
                                self.award_win.destroy()

                Submitte_award_list_butten = Button(self.award_win,width=16,text="Submitte Award List",command=Submitte_award_list,bd=2,pady=4,cursor="hand2",
                    fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white",font=("Times New Roman",10,"bold"))
                Submitte_award_list_butten.pack(side=BOTTOM,pady=10)




        
        # =================================================================================
        # ============================================  desplay the result of one student

        def display_result():

            Exam_Table = self.Disp_result_Exam.get()+"_Term_Exam_"+self.Disp_result_Year.get()
                
            self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = '{Exam_Table}')")
            Exam_table = list(self.courser.fetchall()[0])
            # print(Exam_table)
            if Exam_table[0] == 0:
                m_box.showerror('Error',f'this Table is not present in the database\nExam : {self.Disp_result_Exam.get()} Tearm\nYear   : {self.Disp_result_Year.get()}\nTry again.... ')
            else:
                self.courser.execute(f"SELECT * from {Exam_Table} where Grade = '{self.Disp_result_Class.get()}' and Class_no = '{self.Disp_result_Class_No.get()}'")
                result_record = self.courser.fetchall()
                result_data = [i for i in result_record]
                # print(result_data)

                self.frame6_1 = Frame(self.frame6,bg="#0b9798",relief= RIDGE,bd=2)
                self.frame6_1.place(x=0,y=0,width=523,height=270)

                style = ttk.Style()
                style.configure('Treeview.Heading',font=("Times New Roman",10,'bold'))
                style.configure('Treeview',font=("Times New Roman",10),background="cyan",foreground='black')

                scroll_x = Scrollbar(self.frame6_1,orient=HORIZONTAL)
                scroll_y = Scrollbar(self.frame6_1,orient=VERTICAL)

                self.studenttabel = Treeview(self.frame6_1 , columns=('Subject','Total Marks','Obtained Marks','Status'),
                                                                    yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.config(command=self.studenttabel.yview)
                scroll_x.config(command=self.studenttabel.xview)

                self.studenttabel.heading('Subject', text="Subject")
                self.studenttabel.heading('Total Marks', text="Total Marks")
                self.studenttabel.heading('Obtained Marks', text="Obtained Marks")
                self.studenttabel.heading('Status', text="Status")

                self.studenttabel['show']='headings'

                self.studenttabel.column('Subject',width=100)
                self.studenttabel.column('Total Marks',width=85)
                self.studenttabel.column('Obtained Marks',width=100)
                self.studenttabel.column('Status',width=50)
                self.studenttabel.pack(fill=BOTH,expand=1)

                for i in result_data:
                    # print(i)
                    list_1= [i[7],i[8],i[9],i[10]]
                    self.studenttabel.insert('',END,values=list_1)
                # print(result_data)
                def show_transcript():
                    prt = F_R.generatre_result_one(result_data)
                    quest_for_print = m_box.askyesno('Question','Do you want to Show Transcript?')
                    if quest_for_print == 1:
                        os.startfile(prt[0])
                print_btn = Button(self.frame6,text="Show Transcript",padx=13,cursor="hand2",command=show_transcript,
                    fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
                print_btn.place(x=400,y=273)



        # ==========================================================================================
        # ======================================================   Generate the result of Student
        def generate_result():
            Exam_Table = self.gen_result_Exam.get()+"_Term_Exam_"+self.gen_result_Year.get()
                
            self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = '{Exam_Table}')")
            Exam_table = list(self.courser.fetchall()[0])
            # print(Exam_table)

            if Exam_table[0] == 0:
                m_box.showerror('Error',f'this Table is not present in the database\nExam : {self.gen_result_Exam.get()} Tearm\nYear   : {self.gen_result_Year.get()}\nTry again.... ')
            else:
                # ========================  select result data of all class student 
                self.courser.execute(f"SELECT * from {Exam_Table} where Grade = '{self.gen_result_Class.get()}' ")
                result_record = self.courser.fetchall()
                result_data = [i for i in result_record]
                course_for_check = [i[7] for i in result_record]
                # print(result_data)
                
                subj=[]
                for i in course_for_check:
                    if i not in subj:
                        subj.append(i)
                # print(subj)
                # =========================   select the assign courses for scroolbar

                self.courser.execute(f"SELECT Course_Id from ASSIGN_COURSES where Grade = '{self.gen_result_Class.get()}' ")
                courses_rec = self.courser.fetchall()
                courses = [i[0] for i in courses_rec]
                my_course = tuple(courses)

                
                self.courser.execute(f"SELECT Course_Name from course_registeration where course_Id in {(my_course)} ")
                courses_record = self.courser.fetchall()
                courses_data = [i[0] for i in courses_record]


                subj_not_upload_award_list=[]
                for i in courses_data:
                    if i not in subj:
                        subj_not_upload_award_list.append(i)
                # print(courses_data)


                if len(subj_not_upload_award_list)>0:
                    m_box.showerror('Error',f'Award list of sub: {subj_not_upload_award_list} is not Uploaded\nPlease Upload the Award list\nTry again.... ')
                else:
                    # print(result_data)
                    final = []
                    start = 0
                    end = len(courses_data)
                    for i in range(len(result_data)):
                        final.append(result_data[start:end])
                        start=end
                        end = end+len(courses_data)
                    courses_final_names = final[0:]
                    result_data_for_print = []
                    for i in courses_final_names:
                        if len(i)>0:
                            result_data_for_print.append(i)
                    # print(courses_name_which_show)
                    prt = F_R.generatre_result(result_data_for_print)
                    std_result_data = prt[1]
  
                    # ----------------------------------  create the table of student status in exam
                    if self.gen_result_Exam.get()=="Final":
                        d,m,Year = strftime("%d/%m/%Y").split("/")
                        
                        self.courser.execute(f"CREATE TABLE IF NOT EXISTS CMS.promote_Student_of_Year_{Year}_{self.gen_result_Exam.get()}_exam(Student_Id INT PRIMARY KEY,Student_Status varchar(10))")
                        for i in std_result_data:
                            self.courser.execute(f"INSERT IGNORE INTO promote_Student_of_Year_{Year}_{self.gen_result_Exam.get()}_exam(Student_Id,Student_Status) values(%s,%s)",
                                                    (i[0],i[1]))
            
                    quest_for_print = m_box.askyesno('Question','Do you want to print the result?')
                    if quest_for_print == 1:
                        os.startfile(prt[0])

    
        # =================================================================================
        # ====================================================================   Buttons
        submitte_awardlist = Button(self.frame2,text="Upload Award List",command=creat_award_list,cursor="hand2",
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        submitte_awardlist.place(x=160,y=220)

        display_result_fee = Button(self.frame3,text="Display Result",command=display_result,cursor="hand2",
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        display_result_fee.place(x=80,y=250)

        display_result_fee = Button(self.frame5,text="Generate Result",command=generate_result,cursor="hand2",
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        display_result_fee.place(x=130,y=220)


    














#                         Start the function which to provide the certificate of the Student
# ======================================================================================================================
# ======================================================================================================================
# ============================================   Certificate
# ======================================================================================================================
# ======================================================================================================================
    def Certificate(self):
        certificate_frame = Frame(self.main_frame,height=600,width=850,bg="#0b9798")
        certificate_frame.place(x=0,y=0)

        # =======================================================
        # ==============================  Frames
        first_frame = Frame(certificate_frame,bg="#0d8888",relief= RIDGE,bd=2)
        first_frame.place(x=150,y=100,width=415,height=320)
        frame_reg_1 = Frame(first_frame,bg="#0b9798",relief= RIDGE,bd=2)
        frame_reg_1.place(x=5,y=5,width=400,height=150)
        frame_reg_2 = Frame(first_frame,bg="#0b9798",relief= RIDGE,bd=2)
        frame_reg_2.place(x=5,y=160,width=400,height=150)
        # ========================================================
        # ======================================  Variables
        reg_var = StringVar()
        grade_var = StringVar()

        # ========================================================
        # ==================================  SQL Query
        self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'New_Admission')")
        admission_table = list(self.courser.fetchall()[0])
        if admission_table[0] == 0:
            self.main_page()
            m_box.showerror('Error',f'Sorry.....!\nthere is no Admission Table in the database')
            
        else:
            self.courser.execute(f"""select Std_Registeration_NO from CMS.New_Admission""")
            std_reg_no = self.courser.fetchall()
            reg_no = [i[0] for i in std_reg_no]
            Reg_No = tuple(reg_no)
                  
            # ========================================================
            # ==============================  Labels and Entry Boxes
            lbl = Label(frame_reg_1,text="Enter Registeration No",font=("Times New Roman",14),fg='white',bg="#0b9798").pack(pady=10)
            Entry_1 = ttk.Combobox(frame_reg_1,width=10,textvariable=reg_var,font=("Times New Roman",14))
            Entry_1['values'] = (Reg_No)
            Entry_1.pack()
            def std_certificate():
                if reg_var.get()=="":
                    m_box.showerror('Error','Please fill all the boxes\nTry again.... ')
                else:
                    try:
                        int(reg_var.get())
                    except ValueError:
                        m_box.showerror('title','Only digite are allowed in the \nRegisteration No field\nPlease try again....')
                    else:
                        self.courser.execute(f"""select Std_First_Name,Std_Last_Name,Std_Father_Name,Date_Of_Birth,Grade from CMS.New_Admission where Std_Registeration_NO ={reg_var.get()}""")
                        std_reg_no = self.courser.fetchall()
                        if len(std_reg_no)==0:
                            m_box.showinfo('Informatin',"Registeration No is Incorrect\nPlease Try again.....")
                        else:
                            std_data = [i for i in std_reg_no]
                            # -------------------  the print function is call
                            prt = F_R.generatre_certificate(std_data)
                            quest_for_print = m_box.askyesno('Question','Do you want to Show the Certificate?')
                            if quest_for_print == 1:
                                os.startfile(prt[0])

                            ask_question = m_box.askyesno("Deleting",f"Do you want to Delete data of the Student Registeration No: {reg_var.get()}")
                            if ask_question == 1:
                                ask_question = m_box.askyesno("Confirmation",f"Are you Sure\nTo Delete the data of all Class\nIf you Click 'Yes', it will be the Student Delete whose Registeration No: {reg_var.get()}.")
                                if ask_question == 1:
                                    self.courser.execute(f"select * from CMS.new_Admission where Std_Registeration_NO='{reg_var.get()}'")
                                    Std_record4 = self.courser.fetchall()
                                    Std_data = [i for i in Std_record4]
                                    # print(Std_data)
                                    # ==================  the deleted data is saved in the withdrawl table in the database
                                    self.courser.execute("CREATE TABLE IF NOT EXISTS WITHDRAWL_STUDENT(Std_Registeration_NO BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT, Std_First_Name VARCHAR(25),Std_Last_Name VARCHAR(25),Std_Father_Name VARCHAR(25),Gander VARCHAR(10),Date_Of_Birth VARCHAR(100),Contect_No BIGINT ,Blood_Group VARCHAR(5),Email VARCHAR(25),Admission_Date VARCHAR(100),Religion VARCHAR(10),Grade VARCHAR(10),Class_no INT, Monthly_Fee BIGINT, Birth_Place VARCHAR(50) , Per_Address VARCHAR(50) ,Father_Contect_No BIGINT ,Father_CNIC VARCHAR(15), Pree_School_Name VARCHAR(25),Date_Of_Discharge VARCHAR(100), Class VARCHAR(10), Admission_Fee BIGINT, Transport_Fee BIGINT,Medical_Fee BIGINT)")
                                    for i in Std_data:
                                        self.courser.execute( "Insert IGNORE Into WITHDRAWL_STUDENT (Std_Registeration_NO,Std_First_Name,Std_Last_Name,Std_Father_Name,Gander,Date_Of_Birth,Contect_No,Blood_Group,Email,Admission_Date,Religion,Grade,Class_no,Monthly_Fee,Birth_Place,Per_Address,Father_Contect_No,Father_CNIC,Pree_School_Name,Date_Of_Discharge,Class,Admission_Fee, Transport_Fee,Medical_Fee) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                                                            (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[16],i[17],i[18],i[19],i[20],i[21],i[22],i[23]))

                                        # ==================  Delete the data
                                        self.courser.execute(f"delete from CMS.new_Admission where Std_Registeration_NO='{reg_var.get()}'")
            
                                        path = "picture//"+str(i[1])+"_"+str(i[2])+"_"+str(i[0])+".jpg"

                                        if os.path.exists(path):
                                            os.unlink(path)
                                        else:
                                            None
                                m_box.showinfo('Delete',"Your Data is Deleted Successfuly.....")
                                reg_var.set('')
                                grade_var.set('')
                                self.main_page()

            certificate_butten = Button(frame_reg_1,text="Get Certificate",bd=2,pady=1,padx=4,cursor="hand2",command=std_certificate,
                    fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white",font=("Times New Roman",12)).pack(side=BOTTOM,pady=10)



        # ===============================================================================================
        # ===============================================================================================
        
        lbl = Label(frame_reg_2,text="Select Grade\nTo Generate Certificate",font=("Times New Roman",14),fg='white',bg="#0b9798").pack(pady=10)
        Entry_1 = ttk.Combobox(frame_reg_2,width=10,textvariable=grade_var,state="readonly",font=("Times New Roman",14))
        Entry_1['values'] = ("Ist","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th")
        Entry_1.pack()
        def generate_class_certificate():
            if grade_var.get()=="":
                m_box.showerror('Error','Please Select the Grade\nTry again.... ')
            else:
                try:
                    self.courser.execute(f"""select Std_First_Name,Std_Last_Name,Std_Father_Name,Date_Of_Birth,Grade from CMS.New_Admission where Grade ='{grade_var.get()}'""")
                    std_data_manage_certificate = self.courser.fetchall()
                    if len(std_data_manage_certificate) == 0:
                        m_box.showinfo('Informatin',"Your Entry is Incorrect\nPlease Try again.....")
                    else:
                        std_data = [i for i in std_data_manage_certificate]
                        # print(std_data_manage_certificate)
                        # -------------------  the print function is call
                        for_print = F_R.generatre_certificate_of_class(std_data)
                        quest_for_print = m_box.askyesno('Question','Do you want to Show the Certificates?')
                        if quest_for_print == 1:
                            os.startfile(for_print)

                except Exception as es:
                    m_box.showerror('Error',f'Error Due to: {str(es)}')
            
            ask_question = m_box.askyesno("Deleting",f"Do you want to Delete the data of all Class : {grade_var.get()}")
            if ask_question == 1:
                ask_question = m_box.askyesno("Confirmation",f"Are you Sure\nTo Delete the data of all Class\nIf you Click 'Yes', it will be the Student Delete whose Gradse is {grade_var.get()}.")
                if ask_question == 1:
                    self.courser.execute(f"select * from CMS.new_Admission where Grade='{grade_var.get()}'")
                    Std_data_for_delete = self.courser.fetchall()
                    Std_data = [i for i in Std_data_for_delete]
                    # print(Std_data)
                    # ==================  the deleted data is saved in teh withdrawl table in the database
                    self.courser.execute("CREATE TABLE IF NOT EXISTS WITHDRAWL_STUDENT(Std_Registeration_NO BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT, Std_First_Name VARCHAR(25),Std_Last_Name VARCHAR(25),Std_Father_Name VARCHAR(25),Gander VARCHAR(10),Date_Of_Birth VARCHAR(100),Contect_No BIGINT ,Blood_Group VARCHAR(5),Email VARCHAR(25),Admission_Date VARCHAR(100),Religion VARCHAR(10),Grade VARCHAR(10),Class_no INT, Monthly_Fee BIGINT, Birth_Place VARCHAR(50) , Per_Address VARCHAR(50) ,Father_Contect_No BIGINT ,Father_CNIC VARCHAR(15), Pree_School_Name VARCHAR(25),Date_Of_Discharge VARCHAR(100), Class VARCHAR(10), Admission_Fee BIGINT, Transport_Fee BIGINT,Medical_Fee BIGINT)")
                    for i in Std_data:
                        self.courser.execute( "Insert IGNORE Into WITHDRAWL_STUDENT (Std_Registeration_NO,Std_First_Name,Std_Last_Name,Std_Father_Name,Gander,Date_Of_Birth,Contect_No,Blood_Group,Email,Admission_Date,Religion,Grade,Class_no,Monthly_Fee,Birth_Place,Per_Address,Father_Contect_No,Father_CNIC,Pree_School_Name,Date_Of_Discharge,Class,Admission_Fee, Transport_Fee,Medical_Fee) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                                            (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[16],i[17],i[18],i[19],i[20],i[21],i[22],i[23]))
                    
                    # ==================  Delete the data
                        # self.courser.execute(f"delete from CMS.new_Admission where Std_Registeration_NO='{i[0]}'")
                    
                        path = "picture//"+str(i[1])+"_"+str(i[2])+"_"+str(i[0])+".jpg"
                        # print(path)
                        if os.path.exists(path):
                            os.unlink(path)
                        else:
                            None
                    m_box.showinfo('Delete',"Your Data is Deleted Successfuly.....")
                    reg_var.set('')
                    grade_var.set('')
                    self.main_page()
        certificate_butten = Button(frame_reg_2,text="Get Certificate",bd=2,pady=1,padx=4,cursor="hand2",command=generate_class_certificate,
                fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white",font=("Times New Roman",12)).pack(side=BOTTOM,pady=10)

    














#                        Start the function which manage the courses of all school
# =============================================================================================================================
# =============================================================================================================================
# ==================================   MANAGEN   COURSES
# =============================================================================================================================
# =============================================================================================================================
    def Courses(self):
        first_frame = Frame(self.main_frame,bg="#0b9798",width=850,height=600)
        first_frame.place(x=0,y=0)

        # self.first_frame = Frame(self.frame1,bg="#0b9798",width=545,height=235,relief= RIDGE,bd=2)
        # self.first_frame.place(x=175,y=100)
        Frame_1 = Frame(first_frame,bg="#0b9798",width=530,height=320,relief= RIDGE,bd=2)
        Frame_1.place(x=180,y=100)
        
        

        # ==============================================================================================
        # =========================================================  Registered New Course
        def register_course():
            self.reg_win = Toplevel()
            self.reg_win.title("registered Subject")
            self.reg_win.grab_set()
            self.reg_win.resizable(False,False)
            self.reg_win.geometry("400x300+440+80")
            self.reg_win.configure(background = "#0b9798")

            # ========================================================
            # ======================================  Variables
            courses_var = StringVar()
            courses_Id_var = StringVar()

            # ========================================================
            # ===================   create frames in award_win window   
            self.frame_reg_1 = Frame(self.reg_win,bg="#0b9798",relief= RIDGE,bd=5)
            self.frame_reg_1.place(x=0,y=5,width=390,height=290)

            lbl = Label(self.frame_reg_1,text="Enter Courses Name of all section\nto separate its by Comma's ( , )",font=("Times New Roman",14),fg='white',bg="#0b9798").place(x=50,y=10)
            lbl_1 = Label(self.frame_reg_1,text="Enter Courses Names",font=("Times New Roman",14),fg='white',bg="#0b9798").place(x=90,y=70)
            Entry_1 = Entry(self.frame_reg_1,width=39,textvariable=courses_var,font=("Times New Roman",14),bg="#b3ffff").place(x=10,y=95)

            lbl_2 = Label(self.frame_reg_1,text="Enter a number that start the Id of a courses\nif there is no course registered before",font=("Times New Roman",14),fg='white',bg="#0b9798").place(x=20,y=140)
            Entry_2 = Entry(self.frame_reg_1,width=12,textvariable=courses_Id_var,font=("Times New Roman",14),bg="#b3ffff").place(x=133,y=190)
            # ================================  Save function that save the course
            def save_courses():
                courses = (courses_var.get()).split(',')
                if courses_var.get()=="":
                    m_box.showerror('Error','Please Enter the courses name')
                else:
                    self.courser.execute(f"""CREATE TABLE IF NOT EXISTS CMS.COURSE_REGISTERATION(Course_Id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
                                                                                        Course_Name VARCHAR(25))""")
                    self.courser.execute(f"""select count(*) from CMS.COURSE_REGISTERATION""")
                    count_courses = self.courser.fetchall()[0]
                    if count_courses[0] == 0:
                        if courses_var.get()=="" or courses_Id_var.get()=="":
                            m_box.showerror('error',"please fill both boxes. there is no registered course\nTry again......")
                        else:
                            count = 0
                            for i in courses:
                                if count==0:
                                    self.courser.execute(f"""Insert Into COURSE_REGISTERATION(Course_Id,Course_Name) Value (%s,%s)""",
                                                        (courses_Id_var.get(),i))
                                    count = count+1
                                else:
                                    self.courser.execute(f"""Insert Into COURSE_REGISTERATION(Course_Id,Course_Name) Value (%s,%s)""",
                                                        (0,i))
                            m_box.showinfo('registered Courses',"Your Courses is now registered\nThank you")
                            self.reg_win.destroy()
                    else:
                        self.courser.execute(f"""select Course_Name from CMS.COURSE_REGISTERATION""")
                        count_courses = self.courser.fetchall()
                        subj_Name = [i[0] for i in count_courses]

                        if courses_var.get()=="":
                            m_box.showerror('Error',"please Enter Course Name\nTry again......")
                        else:
                            subj = []
                            for i in courses:
                                if i in subj_Name:
                                    subj.append(i)
                            if len(subj)==0:    
                                for i in courses:
                                    self.courser.execute(f"""Insert Into COURSE_REGISTERATION(Course_Id,Course_Name) Value (%s,%s)""",
                                                    (0,i))
                                m_box.showinfo('registered Courses',"Your Courses is now registered\nThank you")
                                self.reg_win.destroy()
                            else:
                               m_box.showinfo('Exists',f"Your Course: {subj} is already registered in the database")
                          
                           
            register_course_butten = Button(self.frame_reg_1,width=16,text="Add Courses",bd=2,pady=4,command=save_courses,cursor="hand2",
                    fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white",font=("Times New Roman",10)).pack(side=BOTTOM,pady=20)

        
        
        # ==============================================================================================
        # ===============================================================   delete he course from class
        def deallocate_course():
            # =======================================================
            # =======================================================
            self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'ASSIGN_COURSES')")
            courses_names = list(self.courser.fetchall()[0])
            if courses_names[0]==0:
                m_box.showerror('Error','Sorry.....!\nThere is no course to assign Class \nplease first allocate the course to Class')
            else:
                self.delete_assign_win = Toplevel()
                self.delete_assign_win.title("registered Subject")
                self.delete_assign_win.grab_set()
                self.delete_assign_win.resizable(False,False)
                self.delete_assign_win.geometry("400x400+440+80")
                self.delete_assign_win.configure(background = "#0b9798")
                self.courser.execute(f"""select * from CMS.ASSIGN_COURSES""")
                courses_pick = self.courser.fetchall()
                subj_Id = [i[1] for i in courses_pick]
                course_name = [i for i in courses_pick]
                # print(course_name)
                # print(course_name)
                for_combo = []
                for i in subj_Id:
                    if i not in for_combo:
                        for_combo.append(i)
                # ========================================================
                # ======================================  Variables
                pick_grade = StringVar()
                pick_subjects = StringVar()
                # ========================================================
                # ===================   create frames in award_win window
                
                self.frame_reg_1 = Frame(self.delete_assign_win,bg="#0b9798",relief= RIDGE,bd=5)
                self.frame_reg_1.place(x=5,y=5,width=390,height=390)

                lbl_1 = Label(self.frame_reg_1,text="Deallocate the courses from the Class",font=("Times New Roman",14),fg='white',bg="#0b9798").place(x=50,y=5)
                lbl_2 = Label(self.frame_reg_1,text="Enter Grade :",font=("Times New Roman",14),fg='white',bg="#0b9798").place(x=75,y=35)
                entery_box = ttk.Combobox(self.frame_reg_1,width=9,textvariable=pick_grade,state="readonly", font=("Arial",10))
                entery_box["values"] = ("Ist","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th")
                entery_box.place(x=185,y=35)

                self.frame_reg_2 = Frame(self.frame_reg_1)
                self.frame_reg_2.place(x=2,y=70,width=376,height=200)

                style = ttk.Style()
                style.configure('Treeview.Heading',font=("Times New Roman",10,'bold'))
                style.configure('Treeview',font=("Times New Roman",10),background="cyan",foreground='black')

                scroll_y = Scrollbar(self.frame_reg_2,orient=VERTICAL)

                self.course_scrollbar = Treeview(self.frame_reg_2 , columns=('col_1','col_2'),
                                                                    yscrollcommand=scroll_y.set)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_y.config(command=self.course_scrollbar.yview)

                self.course_scrollbar['show']='headings'

                self.course_scrollbar.column('col_1',width=100)
                self.course_scrollbar.column('col_2',width=100)
                self.course_scrollbar.pack(fill=BOTH,expand=1)

                #=============  display the values in scrollbar
                for i in course_name:
                    list_1= [i[0],i[1]]
                    self.course_scrollbar.insert('',END,values=list_1)

                course = tuple(for_combo)
                lbl_1 = Label(self.frame_reg_1,text="Enter Courses Id   (separated by Comma's {,} )",font=("Times New Roman",13),fg='white',bg="#0b9798").place(x=10,y=280)
                Entry_1 = ttk.Combobox(self.frame_reg_1,width=13,textvariable=pick_subjects,font=("Times New Roman",14))
                Entry_1["values"] = (course)
                Entry_1.place(x=120,y=305)

                
                def delete_class_course():
                    self.courser.execute(f"""select count(*) from CMS.ASSIGN_COURSES where Course_Id = '{pick_subjects.get()}' and Grade='{pick_grade.get()}'""")
                    courses_count = self.courser.fetchone()[0]
                    print(courses_count)
                    
                    if pick_grade.get()=="" or pick_subjects.get()=="":
                        m_box.showerror("Error","Please Enter the Grade and Subjects\nTry again.....")
                    else:
                        try:
                            if courses_count==0:
                                m_box.showerror("Error",f"'{pick_subjects.get()}' is not assign to Class '{pick_grade.get()}'\nPlease Correct your entries.....")
                            else:
                                self.courser.execute(f"""delete from CMS.ASSIGN_COURSES where Course_Id = '{pick_subjects.get()}' and Grade='{pick_grade.get()}'""")   
                                m_box.showinfo('Information',f"Courses: '{pick_subjects.get()}' of Class: '{pick_grade.get()}'\nis de Alocated")
                                self.delete_assign_win.destroy()
                        except Exception as es:
                            m_box.showerror('Error',f'Error Due to: {str(es)}')
            
                register_course_butten = Button(self.frame_reg_1,width=16,text="De Allocate Course",bd=2,pady=4,command=delete_class_course,cursor="hand2",
                        fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white",font=("Times New Roman",10)).pack(side=BOTTOM,pady=10)


            
        # ==============================================================================================
        # =========================================================   delete the courses from Database
        def delete_course():
            # =======================================================
            # =======================================================
            self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'COURSE_REGISTERATION')")
            courses_register = list(self.courser.fetchall()[0])
            if courses_register[0]==0:
                m_box.showerror('Error','Sorry.....!\n There is no course Registered')
            else:
                self.delete_reg_win = Toplevel()
                self.delete_reg_win.title("registered Subject")
                self.delete_reg_win.grab_set()
                self.delete_reg_win.resizable(False,False)
                self.delete_reg_win.geometry("400x400+440+80")
                self.delete_reg_win.configure(background = "#0b9798")

                self.courser.execute(f"""select * from CMS.COURSE_REGISTERATION""")
                courses_record = self.courser.fetchall()
                course_name = [i for i in courses_record]
                # print(course_name)
                
                for i in range(3):
                    if len(course_name)%3!=0:
                        course_name.append("No Subject")
                # print(course_name)
                
                final = []
                start = 0
                end = 3
                for i in range(len(course_name)):
                    final.append(course_name[start:end])
                    start=end
                    end = end+3
                courses_final_names = final[0:]
                couses_name_which_show = []
                for i in courses_final_names:
                    if len(i)>0:
                        couses_name_which_show.append(i)
                # print(couses_name_which_show)

                # ========================================================
                # ======================================  Variables
                pick_grade = StringVar()
                pick_subjects = StringVar()
                # ========================================================
                # ===================   create frames in award_win window
                
                self.frame_reg_1 = Frame(self.delete_reg_win,bg="#0b9798",relief= RIDGE,bd=5)
                self.frame_reg_1.place(x=5,y=5,width=390,height=390)

                lbl_1 = Label(self.frame_reg_1,text="Delete the Courses from DataBase",font=("Times New Roman",16),fg='white',bg="#0b9798").place(x=45,y=5)

                self.frame_reg_2 = Frame(self.frame_reg_1)
                self.frame_reg_2.place(x=2,y=40,width=376,height=220)

                style = ttk.Style()
                style.configure('Treeview.Heading',font=("Times New Roman",10,'bold'))
                style.configure('Treeview',font=("Times New Roman",10),background="cyan",foreground='black')

                scroll_y = Scrollbar(self.frame_reg_2,orient=VERTICAL)

                self.course_scrollbar = Treeview(self.frame_reg_2 , columns=('col_1','col_2','col_3'),
                                                                    yscrollcommand=scroll_y.set)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_y.config(command=self.course_scrollbar.yview)

                self.course_scrollbar['show']='headings'

                self.course_scrollbar.column('col_1',width=100)
                self.course_scrollbar.column('col_2',width=100)
                self.course_scrollbar.column('col_3',width=100)
                self.course_scrollbar.pack(fill=BOTH,expand=1)

                for i in couses_name_which_show:
                    list_1= [i[0],i[1],i[2]]
                    self.course_scrollbar.insert('',END,values=list_1)

                lbl_1 = Label(self.frame_reg_1,text="Enter Courses ID    (separated by Comma's {,} )",font=("Times New Roman",13),fg='white',bg="#0b9798").place(x=10,y=280)
                Entry_1 = Entry(self.frame_reg_1,width=39,textvariable=pick_subjects,font=("Times New Roman",14),bg="#b3ffff").place(x=10,y=305)
                
                # ===============================================  assign courses to class and then save the courses
                def delete_reg_course():
                    subj_names = pick_subjects.get().split(",")
                    self.courser.execute(f"""select Course_Id from CMS.COURSE_REGISTERATION""")
                    courses_record = self.courser.fetchall()
                    course_Id = [str(i[0]) for i in courses_record]
                    # print(course_Id)
                    if pick_subjects.get()=="":
                        m_box.showerror("Error","Please Enter Subjects\nTry again.....")
                    else:
                        course_list = []
                        for i in subj_names:
                            if i in course_Id:
                                course_list.append(i)
                        try:
                            if len(course_list) > 1:
                                delete_courses = tuple(course_list)      
                                self.courser.execute(f"""DELETE FROM CMS.COURSE_REGISTERATION where Course_Id in {delete_courses}""")
                                m_box.showinfo('Courses deleted',"Your Courses is deleted from Database\nThank you")
                                self.delete_reg_win.destroy()
                            else:
                                num = self.courser.execute(f"""DELETE FROM CMS.COURSE_REGISTERATION where Course_Id = '{pick_subjects.get()}'""")
                                if num==1:
                                    m_box.showinfo('Course deleted',"Your Course is deleted from Database\nThank you")
                                    self.delete_reg_win.destroy()
                                else:
                                    m_box.showerror('Not registered',"Sorry.....!\nYour Course is not registered in the Database")
                                    

                        except Exception as es:
                            m_box.showerror('Error',f'Error Due to: {str(es)}')
            delete_register_course_butten = Button(self.frame_reg_1,width=16,text="Delete Courses",bd=2,pady=4,command=delete_reg_course,cursor="hand2",
                    fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white",font=("Times New Roman",10)).pack(side=BOTTOM,pady=10)


        
        # ===============================================================================================
        # ====================================================================   Assign course to class
        def register_class_course():
            # =======================================================
            # =======================================================
            self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'COURSE_REGISTERATION')")
            courses_register = list(self.courser.fetchall()[0])
            if courses_register[0]==0:
                m_box.showerror('Error','Sorry.....!\nThere is no course to Registered \nplease First registered the courses')
            else:
                self.assign_win = Toplevel()
                self.assign_win.title("registered Subject")
                self.assign_win.grab_set()
                self.assign_win.resizable(False,False)
                self.assign_win.geometry("400x400+440+80")
                self.assign_win.configure(background = "#0b9798")

                self.courser.execute(f"""select * from CMS.COURSE_REGISTERATION""")
                courses_record = self.courser.fetchall()
                course_name = [i for i in courses_record]
                # print(course_name)
                
                for i in range(3):
                    if len(course_name)%3!=0:
                        course_name.append("No Subject")
                # print(course_name)
                
                final = []
                start = 0
                end = 3
                for i in range(len(course_name)):
                    final.append(course_name[start:end])
                    start=end
                    end = end+3
                courses_final_names = final[0:]
                couses_name_which_show = []
                for i in courses_final_names:
                    if len(i)>0:
                        couses_name_which_show.append(i)
                # print(couses_name_which_show)

                # ========================================================
                # ======================================  Variables
                pick_grade = StringVar()
                pick_subjects_Id = StringVar()
                # ========================================================
                # ===================   create frames in award_win window
                
                self.frame_reg_1 = Frame(self.assign_win,bg="#0b9798",relief= RIDGE,bd=5)
                self.frame_reg_1.place(x=5,y=5,width=390,height=390)

                lbl_1 = Label(self.frame_reg_1,text="Select the Class & it's Courses",font=("Times New Roman",14),fg='white',bg="#0b9798").place(x=60,y=5)
                lbl_2 = Label(self.frame_reg_1,text="Enter Grade :",font=("Times New Roman",14),fg='white',bg="#0b9798").place(x=75,y=35)
                entery_box = ttk.Combobox(self.frame_reg_1,width=9,textvariable=pick_grade,state="readonly", font=("Arial",10))
                entery_box["values"] = ("Ist","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th")
                entery_box.place(x=185,y=35)


                self.frame_reg_2 = Frame(self.frame_reg_1)
                self.frame_reg_2.place(x=2,y=70,width=376,height=200)

                style = ttk.Style()
                style.configure('Treeview.Heading',font=("Times New Roman",10,'bold'))
                style.configure('Treeview',font=("Times New Roman",10),background="cyan",foreground='black')

                scroll_y = Scrollbar(self.frame_reg_2,orient=VERTICAL)

                self.course_scrollbar = Treeview(self.frame_reg_2 , columns=('col_1','col_2','col_3'),
                                                                    yscrollcommand=scroll_y.set)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_y.config(command=self.course_scrollbar.yview)

                self.course_scrollbar['show']='headings'

                self.course_scrollbar.column('col_1',width=100)
                self.course_scrollbar.column('col_2',width=100)
                self.course_scrollbar.column('col_3',width=100)
                self.course_scrollbar.pack(fill=BOTH,expand=1)

                for i in couses_name_which_show:
                    list_1= [i[0],i[1],i[2]]
                    self.course_scrollbar.insert('',END,values=list_1)

                lbl_1 = Label(self.frame_reg_1,text="Enter Courses ID    (separated by Comma's {,} )",font=("Times New Roman",13),fg='white',bg="#0b9798").place(x=10,y=280)
                Entry_1 = Entry(self.frame_reg_1,width=39,textvariable=pick_subjects_Id,font=("Times New Roman",14),bg="#b3ffff").place(x=10,y=305)
                
                # ===============================================  assign courses to class and then save the courses
                def class_course():
                    subj_names = pick_subjects_Id.get().split(",")
                    self.courser.execute(f"""select Course_Id from CMS.COURSE_REGISTERATION""")
                    courses_record = self.courser.fetchall()
                    course_Id = [str(i[0]) for i in courses_record]
                    # print(course_Id)
                    if pick_grade.get()=="" or pick_subjects_Id.get()=="":
                        m_box.showerror("Error","Please Enter the Grade and Subjects\nTry again.....")
                    else:
                        count = 0
                        for i in subj_names:
                            if i not in course_Id:
                                count = count+1
                                m_box.showerror("Error",f"this Subject '{i}' is Not registered in your database\n Please Correct the Subject Name.")
                                return
                        try:
                            if count==0:        
                                self.courser.execute(f"""CREATE TABLE IF NOT EXISTS CMS.ASSIGN_COURSES(Grade VARCHAR(25),Course_Id INT ,FOREIGN KEY (Course_Id) REFERENCES Course_registeration(Course_Id), PRIMARY Key(Grade,Course_Id))""")
                                
                                for i in subj_names:
                                    self.courser.execute(f"""Insert Into CMS.ASSIGN_COURSES(Grade,course_Id) Value (%s,%s)""",
                                                            (pick_grade.get(),i))
                                
                                m_box.showinfo('registered Courses in class',"Your Courses is now Assign to Classes\nThank you")
                                self.assign_win.destroy()
                            else:
                                return
                        except Exception as es:
                            m_box.showerror('Error',f'Error Due to: {str(es)}')
                class_course_butten = Button(self.frame_reg_1,width=16,text="Registered Courses",bd=2,pady=4,command=class_course,cursor="hand2",
                        fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white",font=("Times New Roman",10)).pack(side=BOTTOM,pady=10)


                
        # =====================================================================================
        # =========================================================     Buttons

        Add_course = Button(Frame_1,width=15,height=3,text="Add course",font=("Times New Roman",16),command=register_course,cursor="hand2",
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        Add_course.place(x=50,y=50)

        reg_course_class = Button(Frame_1,width=15,height=3,text="Course for Class",font=("Times New Roman",16),command=register_class_course,cursor="hand2",
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        reg_course_class.place(x=290,y=50)

        deallocate_course = Button(Frame_1,width=15,height=3,text="De Allocate Course",font=("Times New Roman",16),command=deallocate_course,cursor="hand2",
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        deallocate_course.place(x=50,y=180)

        delete_course = Button(Frame_1,width=15,height=3,text="Delete Course",font=("Times New Roman",16),command=delete_course,cursor="hand2",
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        delete_course.place(x=290,y=180)

   



















# =============================================================================================================================
# =============================================================================================================================
# ==================================     Student promotion after final term exam
# =============================================================================================================================
# =============================================================================================================================
    def promote_student(self):
        # ========================================================
        # ========================================n  Frames
        hide_frame = Frame(self.main_frame,height=600,width=850,bg="#0b9798")
        hide_frame.place(x=0,y=0)

        first_frame = Frame(hide_frame,height=400,width=400,bg="#0d8888",relief= RIDGE,bd=2)
        first_frame.place(x=200,y=100)

        upper_frame = Frame(first_frame,height=220,width=385,bg="#0b9798",relief= RIDGE,bd=2)
        upper_frame.place(x=5,y=5)
        lower_frame = Frame(first_frame,height=160,width=385,bg="#0b9798",relief= RIDGE,bd=2)
        lower_frame.place(x=5,y=230)

        # =========================================================
        # ====================================  Variables
        Grade = StringVar()
        monthly_fee = StringVar()

        # =========================================================
        # ===========================  Manage fees of the student
        bl_1 = Label(upper_frame,text="To Manage the Monthly Fee",font=("Times New Roman",15),fg='white',bg="#0b9798").place(x=80,y=5)
        bl_2 = Label(upper_frame,text="Select the Class",font=("Times New Roman",14),fg='white',bg="#0b9798").place(x=130,y=30)
        
        entery_box_1 = ttk.Combobox(upper_frame,width=13,textvariable=Grade,state="readonly", font=("Arial",10))
        entery_box_1["values"] = ("Ist","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th")
        entery_box_1.place(x=133,y=60)

        bl_3 = Label(upper_frame,text="Monthly Fee",font=("Times New Roman",14),fg='white',bg="#0b9798").place(x=140,y=120)   
        entery_box_2 = Entry(upper_frame,width=14,textvariable=monthly_fee, font=("Times New Roman",12))
        entery_box_2.place(x=133,y=145)

        # =========================================================
        # ===========================   Update Fee function
        def update_fee():
            if Grade.get()=="" or monthly_fee.get()=="":
                m_box.showerror("Error","Please Enter both Class and Fee")
            else:
                try:
                    int(monthly_fee.get())
                except ValueError:
                    m_box.showerror("Error","only Numbers are allowed in Fee Entry Box")
                else:
                    self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'New_Admission')")
                    admission_table = list(self.courser.fetchall()[0])
                    if admission_table[0] == 0:
                        m_box.showerror("Error","Sorry.....!\nThere is no Admission Table\nPlease Upload the Student Data")
                    else:
                        self.courser.execute(f"""select * from CMS.New_Admission where Grade='{Grade.get()}'""")
                        check_class = self.courser.fetchall()
                        class_data = [i for i in check_class]
                        if len(class_data)==0:
                            m_box.showerror("Error",f"Sorry.....!\n{Grade.get()} Class is not in your School")
                        else:
                            update = m_box.askyesno("Update...",f"Do you  want to update the fee of Class {Grade.get()}")
                            if update==1:
                                self.courser.execute(f"UPDATE CMS.New_Admission set Monthly_Fee={monthly_fee.get()} where Grade='{Grade.get()}'")
                                m_box.showinfo("Update...",f"Your Fee is Successfuly Updated\nThank you!")
                                Grade.set("")
                                monthly_fee.set("")

        # =========================================================
        # ===========================   promote student function
        bl_1 = Label(lower_frame,text="Click on the button to promote the students",font=("Times New Roman",15),fg='white',bg="#0b9798").place(x=20,y=5)
       
        def promotion_of_student():
            dict_classes = {"01":'Ist',"02":'2nd',"03":'3rd',"04":'4th',"05":'5th',"06":'6th',
                        "07":'7th',"08":'8th',"09":'9th',"10":'10th',"11":"11th","12":"12th"
                        }

            self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'New_Admission')")
            admission_table = list(self.courser.fetchall()[0])
            if admission_table[0] == 0:
                m_box.showerror('Error',f'Sorry.....!\nthere is no Admission Table in the database')
            else:
                d,m,Year = strftime("%d/%m/%Y").split("/")
                self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'promote_Student_of_Year_{Year}_Final_exam')")
                check_promote_table = list(self.courser.fetchall()[0])
                # print(check_promote_table[0])

                if check_promote_table[0] ==0:
                    m_box.showerror('Error','Sorry......!\nYou are promoted the student in this year.\nif you want to promote the student again then generate the result')
                else:
                    ask_question = m_box.askyesno("Promotion","Do you want to promote the student of the School")
                    if ask_question == 1:
                        ask_question = m_box.askyesno("Confirmation","Are you Sure\nTo promote the students of all classes\nIf you Click 'Yes', it will be the Student Promote whose result has been generated.")
                        if ask_question == 1:
                            self.courser.execute(f"SELECT * from promote_Student_of_Year_{Year}_Final_exam")
                            promote_data = self.courser.fetchall()
                            std_promote = [i for i in promote_data]
                            # print(std_promote)

                            self.courser.execute(f"SELECT Std_Registeration_NO, Grade from New_Admission")
                            Class = self.courser.fetchall()
                            std_Class = [i for i in Class]
                            
                            Completed_std =[] 

                            for i in std_promote:
                                if i[1] == "Pass":
                                    for j in std_Class:
                                        if i[0]==j[0]:
                                            for k in dict_classes:
                                                if dict_classes[k] == j[1]:
                                                    if int(k)>11:
                                                        Completed_std.append(i[0])
                                                    else:
                                                        pro = str(int(k)+1)
                                                        if len(pro) == 1:
                                                            pro =  "0"+pro
                                                            self.courser.execute(f"update New_Admission set Grade = '{dict_classes[pro]}' where Std_Registeration_NO = {i[0]}")
                                                        else:
                                                            self.courser.execute(f"update New_Admission set Grade = '{dict_classes[pro]}' where Std_Registeration_NO = {i[0]}")
                                    
                            self.courser.execute(f"Drop table promote_Student_of_Year_{Year}_Final_exam")

                            if len(Completed_std)>0:
                                m_box.showinfo('Certified Student',f'Registeration NO {Completed_std} \n the above student are Completed the F.Sc')
                            
                            m_box.showinfo('promotion Successfuly','Congratulation......!\nThe has been promoted')
        
        # ======================    Buttons
        update_fee_btn = Button(upper_frame,width=15,text="Update Fee",cursor="hand2",command=update_fee,
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        update_fee_btn.place(x=132,y=180)
        promote_btn = Button(lower_frame,width=15,height=2,text="Promote Student",font=("Times New Roman",16),cursor="hand2",command=promotion_of_student,
            fg='white',bg="#0d8888",activebackground="#076d6d",activeforeground = "white")
        promote_btn.place(x=90,y=55)








# =============================================================================================================================
# =============================================================================================================================
# ==================================  Quite
# =============================================================================================================================
# =============================================================================================================================
    def Logout(self):
        self.conn.commit()
        self.conn.close()
        self.win.destroy()
        import Login





# ============================================================================================================================
# ============================================================================================================================
# ==================================  Quite
# ============================================================================================================================
# ============================================================================================================================
    def Quit(self):
        self.conn.commit()
        self.conn.close()
        self.win.destroy()
   
# ===============================================================================
# =========================================  Create Object Of class  And Window 

# win=Tk()
# obj=CMS(win)

# win.mainloop()
