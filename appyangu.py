##################should detect multiple faces main app###############

from tkinter import *
from tkinter import ttk
import cv2


running = False
def launchCam():
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()

        cv2.imshow("Camera feed", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def stop(self):
    running = False


window = Tk()
window.geometry("1920x1080")
window.title("VAKO tech Facial recognition system")
window.configure(bg="#fff")
img = PhotoImage(file='images/1111.png')
notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Scan face to Sign Up")
notebook.add(tab2, text="Scan face for attendance")
notebook.pack(expand=True,fill="both")


Button(tab1, command=launchCam, text="Press to scan your face",font=("Consolas", 25), width=35).pack(side=LEFT)

frame = Frame(tab2,bg="pink", bd=5)
frame.place(x=100, y=100)
Label(tab2, text="Goodbye, this is tab 2")
#the added part
Label(tab2, image=img, bg="white").place(x=200,y=200)

# frame = Frame(tab2, width=500, height=500, bg="white")
frame1 = Frame(tab2, width=500, height=500, bg="white")
frame1.place(x=800,y=200)
heading = Label(tab2, text='Sign in', fg='red', bg='white', font=("Consolas", 25))
heading.pack()

lab4 = Label(tab2)
lab4.pack()

lab = Label(tab2, text='Admin no', fg='#57a1f8', bg='white', font=("Consolas", 15))
lab.pack()
user = Entry(tab2, font=("Arial",10, "bold"), bd=0, fg="black", width=35, bg="firebrick1")
user.pack()

lab4 = Label(tab2)
lab4.pack()

lab2 = Label(tab2, text='Name on Student Id', fg='#57a1f8', bg='white', font=("Consolas", 15))
lab2.pack()
user2 = Entry(tab2, font=("Arial",10, "bold"), bd=0, fg="black", width=35, bg="firebrick1")
user2.pack()

lab4 = Label(tab2)
lab4.pack()



lab4 = Label(tab2)
lab4.pack()

button = Button(tab2, text="Scan face to login",
                font=("Arial",10, "bold"),
                fg="black",
                width=30,

                )
button.pack()

#the added part

window.mainloop()