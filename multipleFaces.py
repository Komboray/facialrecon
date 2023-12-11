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

window.mainloop()