from tkinter import *
from tkinter import messagebox, ttk, filedialog
from PIL import Image, ImageTk
from datetime import datetime
import os
import csv

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x730+0+0")
        self.root.title("Face Recognition System")

        # Tkinter variables
        self.var_std_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()

        self.mydata = []  # to store imported data

        # First image
        img = Image.open(r"C:\Users\divya\OneDrive\Desktop\Face recognition\image\student1.jpg")
        img = img.resize((683, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        Label(self.root, image=self.photoimg).place(x=0, y=0, width=683, height=130)

        # Second image
        img1 = Image.open(r"C:\Users\divya\OneDrive\Desktop\Face recognition\image\student2.jpg")
        img1 = img1.resize((683, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1).place(x=683, y=0, width=683, height=130)

        # Background image
        img3 = Image.open(r"C:\Users\divya\OneDrive\Desktop\Face recognition\image\img11.jpg")
        img3 = img3.resize((1366, 600), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1366, height=600)

        title_lbl = Label(bg_img, text="Attendance Management System", font=("Britannic Bold", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1366, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=0, y=45, width=1366, height=650)

        # Left frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=5, y=0, width=670, height=550)

        img_left = Image.open(r"C:\Users\divya\OneDrive\Desktop\Face recognition\image\student4.jpg")
        img_left = img_left.resize((655, 120), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(Left_frame, image=self.photoimg_left).place(x=5, y=0, width=655, height=120)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=125, width=655, height=300)

        # Row 1
        Label(left_inside_frame, text="Student ID:", font=("times new roman", 11, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, textvariable=self.var_std_id, width=20, font=("times new roman", 11, "bold")).grid(row=0, column=1, padx=10, pady=5, sticky=W)

        Label(left_inside_frame, text="Roll No:", font=("times new roman", 11, "bold"), bg="white").grid(row=0, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, textvariable=self.var_roll, width=20, font=("times new roman", 11, "bold")).grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Row 2
        Label(left_inside_frame, text="Name:", font=("times new roman", 11, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, textvariable=self.var_name, width=20, font=("times new roman", 11, "bold")).grid(row=1, column=1, padx=10, pady=5, sticky=W)

        Label(left_inside_frame, text="Department:", font=("times new roman", 11, "bold"), bg="white").grid(row=1, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, textvariable=self.var_dep, width=20, font=("times new roman", 11, "bold")).grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Row 3
        Label(left_inside_frame, text="Time:", font=("times new roman", 11, "bold"), bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, textvariable=self.var_time, width=20, font=("times new roman", 11, "bold")).grid(row=2, column=1, padx=10, pady=5, sticky=W)

        Label(left_inside_frame, text="Date:", font=("times new roman", 11, "bold"), bg="white").grid(row=2, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, textvariable=self.var_date, width=20, font=("times new roman", 11, "bold")).grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Row 4
        Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 11, "bold"), bg="white").grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.atten_status = ttk.Combobox(left_inside_frame, textvariable=self.var_attendance, width=18, font=("times new roman", 11, "bold"), state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Buttons Frame
        btn_frame = Frame(left_inside_frame, bg="white", bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=185, width=650, height=90)

        Button(btn_frame, text="Import CSV", command=self.importCsv, width=15, font=("times new roman", 10, "bold"), bg="blue", fg="white").grid(row=0, column=0, padx=5, pady=10)
        Button(btn_frame, text="Export CSV", command=self.exportCsv, width=15, font=("times new roman", 10, "bold"), bg="blue", fg="white").grid(row=0, column=1, padx=5, pady=10)
        Button(btn_frame, text="Update", command=self.update_data, width=15, font=("times new roman", 10, "bold"), bg="blue", fg="white").grid(row=0, column=2, padx=5, pady=10)
        Button(btn_frame, text="Reset", command=self.reset_data, width=15, font=("times new roman", 10, "bold"), bg="blue", fg="white").grid(row=0, column=3, padx=5, pady=10)

        # Right frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=680, y=0, width=670, height=550)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=660, height=520)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("id", "roll", "name", "department", "time", "date", "attendance"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        for col in ("id", "roll", "name", "department", "time", "date", "attendance"):
            self.AttendanceReportTable.heading(col, text=col.capitalize())
            self.AttendanceReportTable.column(col, width=100)
        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCsv(self):
        self.mydata.clear()
        fln = filedialog.askopenfilename(title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        with open(fln) as file:
            csvread = csv.reader(file)
            for row in csvread:
                self.mydata.append(row)
            self.fetchData(self.mydata)

    def exportCsv(self):
        try:
            if not self.mydata:
                messagebox.showerror("Error", "No Data Found", parent=self.root)
                return
            fln = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(self.mydata)
            messagebox.showinfo("Data Exported", f"Data exported to {os.path.basename(fln)} successfully", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error exporting data: {e}", parent=self.root)

    def reset_data(self):
        for var in [self.var_std_id, self.var_roll, self.var_name, self.var_dep, self.var_time, self.var_date]:
            var.set("")
        self.atten_status.current(0)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        row = content["values"]
        if row:
            self.var_std_id.set(row[0])
            self.var_roll.set(row[1])
            self.var_name.set(row[2])
            self.var_dep.set(row[3])
            self.var_time.set(row[4])
            self.var_date.set(row[5])
            self.var_attendance.set(row[6])

    def update_data(self):
        selected = self.AttendanceReportTable.focus()
        if not selected:
            messagebox.showerror("Error", "No record selected", parent=self.root)
            return
        updated_row = (self.var_std_id.get(), self.var_roll.get(), self.var_name.get(), self.var_dep.get(),
                       self.var_time.get(), self.var_date.get(), self.var_attendance.get())
        self.AttendanceReportTable.item(selected, values=updated_row)
        messagebox.showinfo("Success", "Record updated successfully", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
