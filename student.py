from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self , root):
        self.root = root
        self.root.geometry("1366x730+0+0")
        self.root.title("Face Recognition System")

        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_sec=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        

        #first image
        img = Image.open(r"C:\Users\divya\OneDrive\Desktop\Face recognition\image\student1.jpg")
        img = img.resize((500, 100), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)  
        f_lbl.place(x=0, y=0, width=500, height=100)   

        #second image
        img1 = Image.open(r"C:\Users\divya\OneDrive\Desktop\Face recognition\image\student2.jpg")
        img1 = img1.resize((500, 100), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)  
        f_lbl.place(x=455, y=0, width=500, height=100)   

        #third image
        img2 = Image.open(r"C:\Users\divya\OneDrive\Desktop\Face recognition\image\student3.jpg")
        img2 = img2.resize((500, 100), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)  
        f_lbl.place(x=910, y=0, width=500, height=100)   



        #bg image
        img3 = Image.open(r"C:\Users\divya\OneDrive\Desktop\Face recognition\image\img11.jpg")
        img3 = img3.resize((1366,638), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)  
        bg_img.place(x=0, y=100, width=1366, height=630) 

        title_lbl=Label(bg_img,text="Student Management System",font=("Britannic Bold",25,"bold"),bg="white",fg="red") 
        title_lbl.place(x=0,y=0,width=1366,height=35) 

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=35,width=1366,height=630)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=5,y=0,width=670,height=550)

        img_left = Image.open(r"C:\Users\divya\OneDrive\Desktop\Face recognition\image\student4.jpg")
        img_left = img_left.resize((655, 120), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)  
        f_lbl.place(x=5, y=0, width=655, height=120)


        #current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=120,width=655,height=90)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",10,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechnical","Commerce","Other")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",10,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),state="readonly")
        course_combo["values"]=("Select Course","BCA","MCA","Btech","BBA","BCOM","Other")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",10,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2025-26","2026-27","2027-28","2027-28")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",10,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),state="readonly")
        semester_combo["values"]=("Current Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #class student information
        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_Student_frame.place(x=5, y=210, width=655, height=300)

        studentID_label = Label(class_Student_frame, text="StudentID:", font=("times new roman", 10, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        studentID_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id, width=20, font=("times new roman", 10, "bold"))
        studentID_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)


        #student name
        studentName_label = Label(class_Student_frame, text="Student Name:", font=("times new roman", 10, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        studentName_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name, width=20, font=("times new roman", 10, "bold"))
        studentName_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)


        #class section
        class_div_label = Label(class_Student_frame, text="Section:", font=("times new roman", 10, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        class_div_entry = ttk.Entry(class_Student_frame,textvariable=self.var_sec, width=20, font=("times new roman", 10, "bold"))
        class_div_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)


        #Roll No
        roll_no_label = Label(class_Student_frame, text="Roll No:", font=("times new roman", 10, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        roll_no_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll, width=20, font=("times new roman", 10, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        #Dob
        dob_label = Label(class_Student_frame, text="DOB:", font=("times new roman", 10, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob, width=20, font=("times new roman", 10, "bold"))
        dob_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)


        #Gender
        gender_label = Label(class_Student_frame, text="Gender:", font=("times new roman", 10, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        #gender_entry = ttk.Entry(class_Student_frame,textvariable=self.var_gender, width=20, font=("times new roman", 10, "bold"))
        #gender_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=18,font=("times new roman",10,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #email
        email_label = Label(class_Student_frame, text="Email:", font=("times new roman", 10, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email, width=20, font=("times new roman", 10, "bold"))
        email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        #Phone
        phone_label = Label(class_Student_frame, text="Phone No.:", font=("times new roman", 10, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        phone_entry = ttk.Entry(class_Student_frame,textvariable=self.var_phone, width=20, font=("times new roman", 10, "bold"))
        phone_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        #address
        address_label = Label(class_Student_frame, text="Address:", font=("times new roman", 10, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address, width=20, font=("times new roman", 10, "bold"))
        address_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        #Teacher Name
        teacher_label = Label(class_Student_frame, text="Teacher Name:", font=("times new roman", 10, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        teacher_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher, width=20, font=("times new roman", 10, "bold"))
        teacher_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)  

       # Radio button variable
        self.var_radio1= StringVar()

        # Radio buttons (mutually exclusive now)
        radionbtn1 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radionbtn1.grid(row=5, column=0, padx=5, pady=5, sticky=W)    
        
        radionbtn2 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radionbtn2.grid(row=5, column=1, padx=5, pady=5, sticky=W)



        # Buttons Frame (below radio buttons)
        btn_frame = Frame(class_Student_frame, bg="white", bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=185, width=650, height=90)

        # First row of buttons
        save_btn = Button(btn_frame, text="Save",command=self.add_data, width=10,height=1, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=5, pady=10)
        
        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=10,height=1, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1, padx=5, pady=10)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=10,height=1, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2, padx=5, pady=10)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=10,height=1, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, padx=5, pady=10)

        # Second row of buttons
        photo_btn = Button(btn_frame, text="Take Photo Sample",command=self.generate_dataset, width=31, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        photo_btn.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        update_photo_btn = Button(btn_frame, text="Update Photo Sample", width=31, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=1, column=2, columnspan=2, padx=5, pady=5)



        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=0,width=670,height=550)

        img_right = Image.open(r"C:\Users\divya\OneDrive\Desktop\Face recognition\image\student4.jpg")
        img_right = img_right.resize((655, 120), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)  
        f_lbl.place(x=5, y=0, width=655, height=120)

        #search frame
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=120, width=655, height=70)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 10, "bold"), bg="red",fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",10,"bold"),state="readonly")
        search_combo["values"]=("Select","Semester-1","Semester-2")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        search_entry = ttk.Entry(search_frame, width=20, font=("times new roman", 10, "bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=10,height=1, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=5, pady=10)
        
        showall_btn = Button(search_frame, text="Show All", width=10,height=1, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        showall_btn.grid(row=0, column=4, padx=5, pady=10)

        #table frame
        table_frame =Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=200, width=655, height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","Id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)    
        scroll_x.config(command=self.student_table.xview)   
        scroll_y.config(command=self.student_table.yview) 

        self.student_table.heading("dep",text="Department") 
        self.student_table.heading("course",text="Course") 
        self.student_table.heading("year",text="Year") 
        self.student_table.heading("sem",text="Semester") 
        self.student_table.heading("Id",text="StudentID") 
        self.student_table.heading("name",text="Name") 
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB") 
        self.student_table.heading("email",text="Email") 
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address") 
        self.student_table.heading("teacher",text="Teacher") 
        self.student_table.heading("photo",text="PhotoStatus") 
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100) 
        self.student_table.column("course",width=100) 
        self.student_table.column("year",width=100) 
        self.student_table.column("sem",width=100) 
        self.student_table.column("Id",width=100) 
        self.student_table.column("name",width=100) 
        self.student_table.column("div",width=100) 
        self.student_table.column("roll",width=100) 
        self.student_table.column("gender",width=100) 
        self.student_table.column("dob",width=100) 
        self.student_table.column("email",width=100) 
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100) 
        self.student_table.column("teacher",width=100) 
        self.student_table.column("photo",width=100) 


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #function declaration

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="divyanshu@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_sec.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()                                                                                                            
                                                                                            
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
 
    #data fetch
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="divyanshu@123",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_sec.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]), 
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                   conn=mysql.connector.connect(host="localhost",user="root",password="divyanshu@123",database="face_recognizer")
                   my_cursor=conn.cursor()
                   my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                  
                                                                                                                                                                             self.var_dep.get(),      
                                                                                                                                                                             self.var_course.get(),
                                                                                                                                                                             self.var_year.get(),
                                                                                                                                                                             self.var_semester.get(),
                                                                                                                                                                             self.var_std_name.get(),
                                                                                                                                                                             self.var_sec.get(),
                                                                                                                                                                             self.var_roll.get(),
                                                                                                                                                                             self.var_gender.get(),
                                                                                                                                                                             self.var_dob.get(),
                                                                                                                                                                             self.var_email.get(),
                                                                                                                                                                             self.var_phone.get(),
                                                                                                                                                                             self.var_address.get(),
                                                                                                                                                                             self.var_teacher.get(),
                                                                                                                                                                             self.var_radio1.get(),
                                                                                                                                                                             self.var_std_id.get()

                                                                                                                                                                         ))
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)   

    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="divyanshu@123",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details successfully deleted", parent=self.root)            
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)   

    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_sec.set("Select Section")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    #generate dataset
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="divyanshu@123", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = self.var_std_id.get()
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_sec.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Haar Cascade setup
                
                face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        return img[y:y+h, x:x+w]
                    return None

                # Open camera
                cap = cv2.VideoCapture(0)
                if not cap.isOpened():
                    messagebox.showerror("Error", "Webcam not accessible!", parent=self.root)
                    return

                img_id = 0
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    cropped_face = face_cropped(frame)
                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = f"data/user.{id}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or img_id == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    
















if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()