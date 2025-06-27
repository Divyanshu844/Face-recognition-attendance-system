from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x730+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("Britannic Bold", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1366, height=35)

        # Left image
        img_top = Image.open(r"C:\Users\divya\OneDrive\Desktop\Face recognition\image\img16.jpg")
        img_top = img_top.resize((650, 680), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=35, width=650, height=680)

        # Right image
        img_bottom = Image.open(r"C:\Users\divya\OneDrive\Desktop\Face recognition\image\img17.jpg")
        img_bottom = img_bottom.resize((750, 680), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=38, width=750, height=680)

        # Button
        b1_1 = Button(f_lbl, text="Face Recognition", command=self.face_recog, cursor="hand2",
                      font=("times new roman", 18, "bold"), bg="Darkgreen", fg="white")
        b1_1.place(x=272, y=600, width=200, height=40)

        #attendance 
    def mark_attendance(self,i,r,n,d):
        with open("divyanshu.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split(",")
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and(i not in name_list) and(d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")
                


    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                conn = mysql.connector.connect(host="localhost", user="root", password="divyanshu@123", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE Student_id=%s", (str(id),))
                result_name = my_cursor.fetchone()
                n = "+".join(result_name) if result_name else "Unknown"

                my_cursor.execute("SELECT Roll FROM student WHERE Student_id=%s", (str(id),))
                result_roll = my_cursor.fetchone()
                r = "+".join(result_roll) if result_roll else "Unknown"

                my_cursor.execute("SELECT Dep FROM student WHERE Student_id=%s", (str(id),))
                result_dep = my_cursor.fetchone()
                d = "+".join(result_dep) if result_dep else "Unknown"

                my_cursor.execute("SELECT Student_id FROM student WHERE Student_id=%s", (str(id),))
                result_id = my_cursor.fetchone()
                i = "+".join(result_id) if result_id else "Unknown"


                conn.close()

                if confidence > 77:
                    cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

        def recognize(img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 255), "Face", clf)
            return img

        # Load Haar cascade
        cascade_path = os.path.join(os.getcwd(), "haarcascade_frontalface_default.xml")
        if not os.path.exists(cascade_path):
            messagebox.showerror("Error", f"Haarcascade file not found:\n{cascade_path}", parent=self.root)
            return

        faceCascade = cv2.CascadeClassifier(cascade_path)

        # Load trained model
        clf = cv2.face.LBPHFaceRecognizer_create()
        model_path = os.path.join(os.getcwd(), "classifier.xml")
        if not os.path.exists(model_path):
            messagebox.showerror("Error", f"Classifier file not found:\n{model_path}", parent=self.root)
            return
        clf.read(model_path)

        # Open webcam
        video_cap = cv2.VideoCapture(0)
        if not video_cap.isOpened():
            messagebox.showerror("Error", "Camera not accessible.", parent=self.root)
            return

        while True:
            ret, img = video_cap.read()
            if not ret:
                messagebox.showerror("Error", "Failed to read from camera.", parent=self.root)
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
