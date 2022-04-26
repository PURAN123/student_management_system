from tkinter import *
from tkinter.ttk import Combobox,Treeview
from tkinter import messagebox
import mysql.connector
class Student:
    def __init__(self,root):
        self.root= root
        self.root.title("Billing Project")
        self.root.geometry("1280x750+0+0")
        self.root.resizable(1,1)
        #self.root.iconbitmap("ball.ico")
        header_label=Label(self.root,text="Student Management System",font=('San-serif',30,'bold'),bg='#7e3a02',fg="#fff")
        header_label.pack(side=TOP,fill=X)

        ########################################## Variables ##########################################
        self.roll_no =IntVar()
        self.name = StringVar()
        self.father = StringVar()
        self.email = StringVar()
        self.contact_no = StringVar()
        self.dob_var = StringVar()
        self.gender_var = StringVar()
        self.search_by = StringVar()
        self.search_var = StringVar()
        self.ROLL_NUMBERS= []

        # Detail Frame
        manage_frame = Frame(self.root,width=400,height=700,bg="#193583")
        manage_frame.place(x=0,y=52)

        header_label = Label(manage_frame,text="Manage Students Details",font=("Arial",20,'bold'),bg="#193583",fg="#fff")
        header_label.place(x=5,y=10)
        roll_number=Label(manage_frame,text="Roll Number:  ",font=("Courier",13,'bold'),bg="#193583",fg="#fff")
        roll_number.place(x=3,y=80)
        self.roll_number_entry = Spinbox(manage_frame,textvariable=self.roll_no,width=19,from_=1,to=100,font=("Courier",13,'bold'),bg="lightGray",bd=2,relief=GROOVE)
        self.roll_number_entry.place(x=180,y=80)

        self.name_label=Label(manage_frame,text="Student Name:",font=("Courier",13,'bold'),bg="#193583",fg="#fff")
        self.name_label.place(x=3,y=130)
        self.name_label_entry = Entry(manage_frame,textvariable=self.name,width=20,font=("Courier",13,'bold'),bg="lightGray",bd=2,relief=GROOVE)
        self.name_label_entry.focus()
        self.name_label_entry.place(x=180,y=130)
        
        self.father_label=Label(manage_frame,text="Father Name:",font=("Courier",13,'bold'),bg="#193583",fg="#fff")
        self.father_label.place(x=3,y=180)
        self.father_label_entry = Entry(manage_frame,textvariable=self.father,width=20,font=("Courier",13,'bold'),bg="lightGray",bd=2,relief=GROOVE)
        self.father_label_entry.place(x=180,y=180)

        self.email_label=Label(manage_frame,text="Enter Email:",font=("Courier",13,'bold'),bg="#193583",fg="#fff")
        self.email_label.place(x=3,y=230)
        self.email_label_entry = Entry(manage_frame,width=20,textvariable=self.email,font=("Courier",13,'bold'),bg="lightGray",bd=2,relief=GROOVE)
        self.email_label_entry.place(x=180,y=230)

        self.contact=Label(manage_frame,text="Enter Phone:",font=("Courier",13,'bold'),bg="#193583",fg="#fff")
        self.contact.place(x=3,y=280)
        self.contact_entry = Entry(manage_frame,width=20,textvariable=self.contact_no,font=("Courier",13,'bold'),bg="lightGray",bd=2,relief=GROOVE)
        self.contact_entry.place(x=180,y=280)

        self.dob=Label(manage_frame,text="Date Of birth:",font=("Courier",13,'bold'),bg="#193583",fg="#fff")
        self.dob.place(x=3,y=330)
        self.dob_entry = Entry(manage_frame,width=20,textvariable=self.dob_var,font=("Courier",13,'bold'),bg="lightGray",bd=2,relief=GROOVE)
        self.dob_entry.place(x=180,y=330)
        
        gender=Label(manage_frame,text="Select Gender:",font=("Courier",13,'bold'),bg="#193583",fg="#fff")
        gender.place(x=3,y=380)
        gender_list=Combobox(manage_frame,width=18,state="readonly",textvariable=self.gender_var,font=("Courier",13,'bold'),background="lightGray")
        gender_list['values']=("Male","Female","Others")
        gender_list.place(x=180,y=380)

        address=Label(manage_frame,text="Enter Address:",font=("consolas",13,'bold'),bg="#193583",fg="#fff")
        address.place(x=3,y=430)
        self.text = Text(manage_frame,width=20,height=5,font=("consolas",14,'bold'),bg="lightgray")
        self.text.place(x=180,y=430)

        btn_label = Label(manage_frame,width= 60,height=4,bd=10,bg="#193583")
        btn_label.place(x=0,y=580)
        b1=Button(btn_label,cursor="hand2",text="Add",command=self.add_data,activebackground="#50022f",relief=GROOVE,activeforeground="#fff",font=("consolas",14,'bold'),background="#2ac51c",fg="#fff")
        b1.place(x=0,y=0,height=40,width=70)
        b2=Button(btn_label,cursor="hand2",text="Update",command=self.update_data,activebackground="#50022f",relief=GROOVE,activeforeground="#fff",font=("consolas",14,'bold'),background="#2ac51c",fg="#fff")
        b2.place(x=85,y=0,height=40,width=90)
        b3=Button(btn_label,cursor="hand2",text="Delete",command=self.delete_data,activebackground="#50022f",relief=GROOVE,activeforeground="#fff",font=("consolas",14,'bold'),background="#2ac51c",fg="#fff")
        b3.place(x=185,y=0,height=40,width=90)
        b4=Button(btn_label,cursor="hand2",text="Clear",command=self.clear_data,activebackground="#50022f",relief=GROOVE,activeforeground="#fff",font=("consolas",14,'bold'),background="#2ac51c",fg="#fff")
        b4.place(x=290,y=0,height=40,width=80)

        # List Frame
        list_frame = Frame(self.root,width=840,height=700,bg="#193583")
        list_frame.place(x=420,y=52)

        search_label = Label(list_frame,text="Search By",font=("serif",18,'bold'),bg="#193583",fg="#fff")
        search_label.place(x=20,y=20)

        search_combo = Combobox(list_frame,width=10,font=("Courier",15),textvariable=self.search_by,state="readonly")
        search_combo['values']=("Roll_No","Name",'Gender','Address','Phone')
        search_combo.place(x=200,y=20)

        search_entry = Entry(list_frame,width=12,font=("Courier",14,'bold'),bg="lightGray",textvariable=self.search_var,bd=2,relief=GROOVE)
        search_entry.place(x=380,y=20)

        search_btn=Button(list_frame,text="Search",command=self.searchItem,cursor="hand2",activebackground="#178999",font=("consolas",14,'bold'),background="lightgray",fg="#000")
        search_btn.place(x=560,y=20,height=28)

        search_btn2=Button(list_frame,text="Show All",command=self.fetch_data,cursor="hand2",activebackground="#178999",font=("consolas",14,'bold'),background="lightgray",fg="#000")
        search_btn2.place(x=670,y=20,height=28)
        
        # Table Frame
        table_frame = Frame(list_frame,width=900,height=700)
        table_frame.place(x=20,y=80,width=800,height=600)

        scroll_x = Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.student_table= Treeview(table_frame,columns=('Roll_No',"Name","Father","Email","Phone","DOB","Gender",'Address'))
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.configure(command=self.student_table.xview)
        scroll_y.configure(command=self.student_table.yview)
        self.student_table.config(xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        self.student_table.heading('Roll_No',text='Roll No.')
        self.student_table.heading('Name',text="Student Name")
        self.student_table.heading('Father',text="Father's Name")
        self.student_table.heading('Email',text="Email")
        self.student_table.heading('Phone',text="Phone No.")
        self.student_table.heading('DOB',text="D.O.B.")
        self.student_table.heading('Gender',text="Gender")
        self.student_table.heading('Address',text="Address")
        self.student_table['show']='headings'
        self.student_table.column('Roll_No',width=50)
        self.student_table.column('Name',width=100)
        self.student_table.column('Father',width=100)
        self.student_table.column('Email',width=150)
        self.student_table.column('Phone',width=100)
        self.student_table.column('DOB',width=100)
        self.student_table.column('Gender',width=100)
        self.student_table.column('Address',width=100)
        self.student_table.pack(fill=BOTH,expand=True)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()
    
    def add_data(self):
        if not int(self.roll_no.get()):
            messagebox.showerror("Invalid data","Roll Number must be an integer")
        elif self.roll_no.get() in self.ROLL_NUMBERS:
            messagebox.showerror("Repeat Data","Roll Number Already Exist")
        else:
            conn = mysql.connector.connect(
                host= 'localhost',
                user= 'root',
                port=3306,
                database= 'student',
                password= 'puran',
            )
            cur = conn.cursor()
            self.ROLL_NUMBERS.append(self.roll_no.get())
            if self.name.get()=="" or self.father.get()=="" or self.email.get()=="" or self.gender_var.get()=="":
                messagebox.showerror('Not Valid',"All Fields are required")
            else:
                cur.execute("INSERT INTO studentdata VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.roll_no.get(),
                    self.name.get(),
                    self.father.get(),
                    self.email.get(),
                    self.contact_no.get(),
                    self.dob_var.get(),
                    self.gender_var.get(),
                    self.text.get('1.0',END)
                ))
                conn.commit()
                self.fetch_data()
                x = int(self.roll_no.get())
                self.clear_data()
                self.roll_no.set(x+1)
                conn.close()

    def update_data(self):
        conn = mysql.connector.connect(
            host= 'localhost',
            user= 'root',
            port=3306,
            database= 'student',
            password= 'puran',
        )
        cur = conn.cursor()
        cur.execute("UPDATE studentdata SET Roll_no=%s,Name=%s,Father=%s,Email=%s,Phone=%s,DOB=%s,Gender=%s,Address=%s WHERE Roll_No=%s",(
                self.roll_no.get(),
                self.name.get(),
                self.father.get(),
                self.email.get(),
                self.contact_no.get(),
                self.dob_var.get(),
                self.gender_var.get(),
                self.text.get('1.0',END),
                self.roll_no.get(),
        ))
        conn.commit()
        self.fetch_data()
        self.clear_data()
        conn.close()

    def delete_data(self):
        conn=mysql.connector.connect(
            host="localhost",
            user="root",
            port=3306,
            database="student",
            password="puran",
        )
        cur=conn.cursor()
        cur.execute("DELETE FROM studentdata WHERE roll_no = '"+str(self.roll_no.get())+"'")
        conn.commit()
        conn.close()
        self.fetch_data()
        self.clear_data()

    def clear_data(self):
        self.roll_no.set('1')
        self.name.set('')
        self.email.set('')
        self.father.set('')
        self.contact_no.set('')
        self.dob_var.set('')
        self.gender_var.set('')
        self.text.delete(1.0,END)
    
    def searchItem(self):
        conn = mysql.connector.connect(
            host= 'localhost',
            user= 'root',
            port=3306,
            database= 'student',
            password= 'puran',
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM studentdata WHERE "+str(self.search_by.get())+" like '%"+str(self.search_var.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            conn.commit()
        self.search_var.set('')
        conn.close()
    
    def fetch_data(self):
        conn = mysql.connector.connect(
            host= "localhost",
            port=3306,
            user="root",
            database="student",
            password="puran"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM studentdata")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event=None):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        row = content['values']
        self.roll_no.set(row[0])
        self.name.set(row[1])
        self.father.set(row[2])
        self.email.set(row[3])
        self.contact_no.set(row[4])
        self.dob_var.set(row[5])
        self.gender_var.set(row[6])
        self.text.delete('1.0',END)
        self.text.insert(END,row[7])

root = Tk()
obj=Student(root)
root.mainloop()
