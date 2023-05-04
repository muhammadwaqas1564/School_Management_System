from tkinter import *
from PIL import Image ,ImageTk
from tkinter import messagebox as m_box
import pymysql

# -------------------  Import python File
import SMS
class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Registeration Window")
        self.root.geometry("1350x700+0+0")
        self.root.overrideredirect(True)
        self.root.overrideredirect(False)
        self.root.attributes('-fullscreen',True)

        # =========================================
        # ======== Creat database in SQL commands
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
        
       
        
        # ======================================================
        # ================================  Background picture
        self.bg = ImageTk.PhotoImage(file = "Images\\background5.JPG")
        bg = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        # ======================================================
        # ==================================== Frames
        self.frame2 = Frame(self.root,bg="white")
        self.frame2.place(x=364,y=150,width=700,height=500)
    

        # ======================================================
        # ===========================  get images for design
        self.left = ImageTk.PhotoImage(file = "Images\\imageleft.JPG")
        self.left_side_first = ImageTk.PhotoImage(file = "Images\\leftdesign.PNG")
        self.right_side = ImageTk.PhotoImage(file = "Images\\circle.JPG")
        self.left_side = ImageTk.PhotoImage(file = "Images\\leftdesign.PNG")
        self.btn_back_2 = ImageTk.PhotoImage(file = "Images\\quit_reg.png")
        self.btn_login = ImageTk.PhotoImage(file = "Images\\login.JPG")
        
        
        # ========================================== Design Labels
        left = Label(self.root,image=self.left).place(x=0,y=0,relheight=1)
        left_in_main = Label(self.frame2,image=self.left_side,bg="white").place(x=0,y=0)
        circle_corner = Label(self.frame2,image=self.right_side,bg="white").place(x=500,y=-100)


        # ======================================================
        # =========================================  variable
        self.sign_email = StringVar()
        self.sign_password = StringVar()
        # ======================================================
        # ======================================================
        title = Label(self.frame2,text="LOGIN INTO SYSTEM",font=("Times New Roman",20,'bold'),bg="white",fg="#0f3f65").place(x=150,y=40)


        # ======================================================
        # ========================   get data in Entry boxes
        Email = Label(self.frame2,text="Email",font=("Times New Roman",15,'bold'),bg="white").place(x=200,y=120)
        txt_Email = Entry(self.frame2,textvariable=self.sign_email,font=("Times New Roman",15,'bold'),bg="lightgray")
        txt_Email.place(x=200,y=150)
        txt_Email.focus()

        password = Label(self.frame2,text="Password",font=("Times New Roman",15,'bold'),bg="white").place(x=200,y=190)
        txt_password = Entry(self.frame2,textvariable=self.sign_password,show="*",font=("Times New Roman",15,'bold'),bg="lightgray").place(x=200,y=220)


              
        self.btn = Button(self.frame2,text="Forget Password?",bd=0,bg='white',fg="#d77337",cursor="hand2",command=self.Forget,font=("Times New Roman",11)).place(x=200,y=250)
        self.btn = Button(self.frame2,image=self.btn_login,bd=0,cursor="hand2",command=self.Login).place(x=250,y=455)
        self.btn = Button(self.frame2,image=self.btn_back_2,bd=0,cursor="hand2",command=self.back).place(x=540,y=455)
    
    # =======================================================================
    # ======================================================   Login
    def Login(self):
        if self.sign_email.get()=="" or self.sign_password.get()=="":
            m_box.showerror('Error','All Field are required')
        else:
            try:
                self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'REGISTRATION')")
                admission_table = list(self.courser.fetchall()[0])
                
                if admission_table[0] == 1:
                    self.courser.execute(f"select Email,Password from REGISTRATION where Email='{self.sign_email.get()}' and password='{self.sign_password.get()}'")
                    row = self.courser.fetchone()
                    if row==None:
                        m_box.showerror('Error',f'This Email: {self.sign_email.get()} and Password: {self.sign_password.get()}\n are incorrect')
                    else:
                        m_box.showinfo('welcome',f'Welcome to the School Management system')
                        self.root.destroy()
                        SMS.CMS()

                else:
                    self.courser.execute("CREATE TABLE REGISTRATION (Email varchar(25),password varchar(25))")

                    self.courser.execute("Insert into REGISTRATION (Email,password) values(%s,%s)",(self.sign_email.get(),self.sign_password.get()))
                    m_box.showinfo('welcome',f"Welcome You are the Admin of the system\nNow your Email is:{self.sign_email.get()} and Password is: {self.sign_password.get()}")

                    m_box.showinfo('welcome',f'Welcome to the School Management system')
                    self.main_call()
            except Exception as es:
                m_box.showerror('Error',f'Error Due to: {str(es)}')

    # =====================================================   forget password
    def Forget(self):
        self.sign_email.set("")
        self.sign_password.set("")

        frame3 = Frame(self.frame2,bg="white")
        frame3.place(x=0,y=0,width=700,height=500)

        # ======================================================
        # =========================================  variable
        forget_email = StringVar()
        forget_New_password = StringVar()
        forget_confirm_Passowrd = StringVar()

        # ======================================================
        # ===========================================  Design
        self.forget_right_side = ImageTk.PhotoImage(file = "Images\\circle.JPG")
        self.forget_left_side = ImageTk.PhotoImage(file = "Images\\leftdesign.PNG")
        self.forget_btn_back_2 = ImageTk.PhotoImage(file = "Images\\Back.JPG")
        self.forget_btn_login = ImageTk.PhotoImage(file = "Images\\save.png")

        lbl1 = Label(frame3,image=self.forget_left_side,bg="white").place(x=0,y=0)
        lbl2 = Label(frame3,image=self.forget_right_side,bg="white").place(x=500,y=-100)

        # ======================================================
        # ======================================================
        title = Label(frame3,text="FORGET PASSWORD",font=("Times New Roman",20,'bold'),bg="white",fg="#0f3f65").place(x=160,y=40)

        # ======================================================
        # ======================================================
        Email = Label(frame3,text="Email",font=("Times New Roman",15,'bold'),bg="white").place(x=200,y=120)
        txt_Email = Entry(frame3,textvariable=forget_email,font=("Times New Roman",15,'bold'),bg="lightgray")
        txt_Email.place(x=200,y=150)
        txt_Email.focus()
        
        password = Label(frame3,text="New Password",font=("Times New Roman",15,'bold'),bg="white").place(x=200,y=190)
        txt_password = Entry(frame3,textvariable=forget_New_password,font=("Times New Roman",15,'bold'),bg="lightgray").place(x=200,y=220)

        C_password = Label(frame3,text="Confirm Password",font=("Times New Roman",15,'bold'),bg="white").place(x=200,y=260)
        txt_C_password = Entry(frame3,textvariable=forget_confirm_Passowrd,font=("Times New Roman",15,'bold'),bg="lightgray").place(x=200,y=290)

        def save_forget_password():
            if forget_email.get()=="" or forget_New_password.get()=="" or forget_confirm_Passowrd.get()=="":
                m_box.showerror('Error','All Field are required',parent=self.root)
            elif forget_New_password.get() != forget_confirm_Passowrd.get():
                m_box.showerror('Error','password and Confirm Password should be same')
            else:
                try:
                    self.courser.execute(f"SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'CMS') AND (TABLE_NAME = 'REGISTRATION')")
                    current_table = list(self.courser.fetchall()[0])
                    if current_table[0] == 1:                      
                        self.courser.execute("select * from REGISTRATION where Email=%s",forget_email.get())
                        row = self.courser.fetchone()
                    else:
                        m_box.showerror('Error',f'This User name and Password are incorrect\nPlease Registered Your self')

                    if row==None:
                        m_box.showerror('Error',f'This Email: {forget_email.get()} is not Exists,Please Enter the correct Email',parent=self.root)

                    else:
                        self.courser.execute(f"""Update REGISTRATION SET Password='{forget_New_password.get()}' where Email='{forget_email.get()}'""")
                        m_box.showinfo('Success','Your Password is forget Now you can signin to the system',parent=self.root)
                        frame3.destroy()
                except Exception as es:
                    m_box.showerror('Error',f'Error Due to: {str(es)}',parent=self.root)



        btn = Button(frame3,image=self.forget_btn_login,bd=0,cursor="hand2",command=save_forget_password).place(x=250,y=455)
        btn = Button(frame3,image=self.forget_btn_back_2,bd=0,cursor="hand2",command=frame3.destroy).place(x=540,y=455)
#  =======================================================================
    # ======================================================  back
    def main_call(self):
        self.conn.commit()
        self.conn.close()
        self.root.destroy()
        SMS.CMS()
    # =======================================================================
    # ======================================================  back

    def back(self):
        self.conn.commit()
        self.conn.close()
        self.root.destroy()

root = Tk()
obj  =Register(root)
root.mainloop()