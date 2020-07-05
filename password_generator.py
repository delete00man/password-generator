import string
from random import randint,choice
from tkinter import *
from tkinter import Tk

password = ""

def generate():
    password_min = 6
    password_max = 15
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min,password_max)))

    password_entry.delete(0, END)
    password_entry.insert(0, password)








list_password = {}
def save_password_window():

    window.destroy()







def save_password():
    global name_password
    window1.destroy()
    name_password = name_password_entry.get()
    password_entry1.get()
    list_password[name_password] = password_entry1.get()




window = Tk()
window.title("Générateur de mot de passe")
window.iconbitmap("login.ico")
window.geometry("720x480")
window.config(background="#E4E1CF")
frame = Frame(window,bg='#E4E1CF')

width = 300
height = 300
image = PhotoImage(file="login.png").zoom(10).subsample(35)
canvas = Canvas(frame, width=width, height=height, bg='#E4E1CF',bd=0,highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0 ,column=0,sticky=W)

right_frame = Frame(frame, bg='#E4E1CF')


label_titre = Label(right_frame, text="Mot de passe", font=("Arial", 20,),bg="white")
label_titre.pack()

password_entry = Entry(right_frame, font=("Arial", 20,),bg="white")
password_entry.pack()

password_button = Button(right_frame, text="Générer", font=("Arial", 20,),bg="white",command=generate)
password_button.pack(side=LEFT)

password_save = Button(right_frame, text="Sauvegarder", font=("Arial", 20,),bg="white",command=save_password_window)
password_save.pack(side=RIGHT)

right_frame.grid(row=0,column=1, sticky=W)
frame.pack(expand=YES)

window.mainloop()

window1 = Tk()
window1.title("Générateur de mot de passe - Sauvegarder")
window1.iconbitmap("login.ico")
window1.geometry("720x480")
window1.config(background="#E4E1CF")
frame1 = Frame(window1,bg='#E4E1CF')

width = 300
height = 300
image = PhotoImage(file="Sans titre.png").zoom(16).subsample(35)
canvas = Canvas(frame1, width=width, height=height, bg='#E4E1CF',bd=0,highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0 ,column=0,sticky=E)

left_frame = Frame(frame1, bg='#E4E1CF')

label_name_password = Label(left_frame, text="Nom du Mot de passe:", font=("Arial", 20,),bg="white")
label_name_password.pack()

name_password_entry = Entry(left_frame, font=("Arial", 20,),bg="white")
name_password_entry.pack()

label_password = Label(left_frame, text="Mot de passe:", font=("Arial", 20,),bg="white")
label_password.pack()


password_entry1 = Entry(left_frame, font=("Arial", 20,), bg="white")
password_entry1.pack()


save_button = Button(left_frame, text="Save", font=("Arial", 20,),bg="white", command=save_password)
save_button.pack()

left_frame.grid(row=0,column=1, sticky=W)
frame1.pack(expand=YES)


window1.mainloop()

window2 = Tk()
window2.title("Générateur de mot de passe - Liste de Mot de Passe")
window2.iconbitmap("login.ico")
window2.geometry("720x480")
window2.config(background="#E4E1CF")
frame2 = Frame(window1,bg='#E4E1CF')

label_password_list = Label(frame2, text=print(list_password), font=("Arial", 20,),bg="white")

window2.mainloop()


