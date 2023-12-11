import data
from tkinter import *
from tkinter import messagebox





def scanSub():
    admin = user.get()
    username2 = user2.get()
    user.config(state=DISABLED)
    user2.config(state=DISABLED)
    print(admin)
    print(username2)
    #function for sending name to mariadb server below
    d1 = data.Data()
    d1.sendDetails(admin, username2)






window = Tk()
window.title("Login")
window.geometry("1920x1080")
window.configure(bg="#fff")



img = PhotoImage(file='images/1111.png')
Label(window, image=img, bg="white").place(x=200,y=200)

frame = Frame(window, width=500, height=500, bg="white")
frame1 = Frame(window, width=500, height=500, bg="white")
frame1.place(x=800,y=200)
heading = Label(frame1, text='Sign in', fg='red', bg='white', font=("Consolas", 25))
heading.pack()

lab4 = Label(frame1)
lab4.pack()

lab = Label(frame1, text='Admin no', fg='#57a1f8', bg='white', font=("Consolas", 15))
lab.pack()
user = Entry(frame1, font=("Arial",10, "bold"), bd=0, fg="black", width=35, bg="firebrick1")
user.pack()

lab4 = Label(frame1)
lab4.pack()

lab2 = Label(frame1, text='Name on Student Id', fg='#57a1f8', bg='white', font=("Consolas", 15))
lab2.pack()
user2 = Entry(frame1, font=("Arial",10, "bold"), bd=0, fg="black", width=35, bg="firebrick1")
user2.pack()

lab4 = Label(frame1)
lab4.pack()



lab4 = Label(frame1)
lab4.pack()

button = Button(frame1, text="Scan face to login",
                font=("Arial",10, "bold"),
                fg="black",
                width=30,
                command= scanSub
                )
button.pack()
window.mainloop()


