from tkinter import *
from tkinter import Tk
import string
from random import randint,choice
from time import sleep

passwordlogin = ""
usernamelogin = ""
password = ""

def login():
    login_infos = open("login.txt", "r")
    login_infos = login_infos.read()
    list_login_infos = login_infos.split(",")
    usernamelogin = username_entry.get()
    passwordlogin = password_entry.get()
    if usernamelogin == list_login_infos[0] and passwordlogin == list_login_infos[1]:
            print_generator_page()

def print_password():
    Generator_page.pack_forget()
    Password_page.pack(expand=YES)



def sign_in():
    user = sign_in_username_entry.get()
    password_verify = sign_in_password_entry.get()
    if len(user) and len(password_verify) > 0:
        with open("login.txt", "w") as login:
         login.write(sign_in_username_entry.get())
         login.write(",")
         login.write(sign_in_password_entry.get())
        login.close()
        print_generator_page()


    else:
        sleep(1)

def save_password():
    with open("password_list1.txt", "a+") as password_list:
        password_list.write("Name Password: ")
        password_list.write(name_password_entry.get())
        password_list.write(" | Password: ")
        password_list.write(password_entry1.get())
        password_list.write("\n")


def generate():
    password_min = 6
    password_max = 15
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))

    password_entry1.delete(0, END)  # supprime les éventuels caractères dans l'entrée.
    password_entry1.insert(0, password)  # injecte le password dans l'entrée.

def print_inscription_page():
    Accueil_page.pack_forget()
    Inscription_page.pack(expand=YES)

def print_generator_page():
    Connexion_page.pack_forget()
    Inscription_page.pack_forget()
    Password_page.pack_forget()
    Generator_page.pack(expand=YES)

def print_connexion_page():
    Accueil_page.pack_forget()
    Connexion_page.pack(expand=YES)

def print_accueil_page():
    Connexion_page.pack_forget()
    Inscription_page.pack_forget()
    Generator_page.pack_forget()
    Accueil_page.pack(expand=YES)


window = Tk()
window.title("Générateur de mot de passe")
window.iconbitmap("Password_Générator.ico")
window.geometry("720x480")
window.config(background="#E4E1CF")
Accueil_page = Frame(window, bg='#E4E1CF')
Connexion_page = Frame(window, bg='#E4E1CF')
Inscription_page = Frame(window, bg='#E4E1CF')
Generator_page = Frame(window, bg='#E4E1CF')
Password_page = Frame(window, bg='#E4E1CF')

#accueil

width = 300
height = 300
image = PhotoImage(file="Password_Generator.png").zoom(16).subsample(35)
canvas = Canvas(Accueil_page, width=width, height=height, bg='#E4E1CF', bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image)
canvas.grid(row=0, column=0, sticky=E)

left_frame = Frame(Accueil_page, bg='#E4E1CF')

sign_up_button = Button(left_frame, text="S'inscrire", font=("Arial", 20,), bg="white", command=print_inscription_page)
sign_up_button.pack()

login_button = Button(left_frame, text="Se connecter", font=("Arial", 20,), bg="white", command=print_connexion_page)
login_button.pack()

left_frame.grid(row=0, column=1, sticky=W)
Accueil_page.pack(expand=YES)

#connexion

width = 300
height = 300
image1 = PhotoImage(file="Password_Generator1.png").zoom(16).subsample(35)
canvas = Canvas(Connexion_page, width=width, height=height, bg='#E4E1CF', bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image1)
canvas.grid(row=0, column=0, sticky=E)

connexion_left_frame = Frame(Connexion_page, bg='#E4E1CF')

label_username = Label(connexion_left_frame, text="Username:", font=("Arial", 20,), bg="white")
label_username.pack()

username_entry = Entry(connexion_left_frame, font=("Arial", 20,), bg="white")
username_entry.pack()
label_password = Label(connexion_left_frame, text="Mot de passe:", font=("Arial", 20,), bg="white")
label_password.pack()

password_entry = Entry(connexion_left_frame, font=("Arial", 20,), bg="white")
password_entry.pack()

connexion_button = Button(connexion_left_frame, text="Connexion", font=("Arial", 20,), bg="white", command=login)
connexion_button.pack(fill=X)

home_return = Button(connexion_left_frame, text="Retour Accueil", font=("Arial", 20,), bg="white", command=print_accueil_page)
home_return.pack(fill=X)

connexion_left_frame.grid(row=0, column=1, sticky=W)

#inscription

width = 300
height = 300
image2 = PhotoImage(file="Password_Generator2.png").zoom(16).subsample(35)
canvas = Canvas(Inscription_page, width=width, height=height, bg='#E4E1CF', bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image)
canvas.grid(row=0, column=0, sticky=E)

inscription_left_frame = Frame(Inscription_page, bg='#E4E1CF')

label_username = Label(inscription_left_frame, text="Username:", font=("Arial", 20,), bg="white")
label_username.pack()

sign_in_username_entry = Entry(inscription_left_frame, font=("Arial", 20,), bg="white")
sign_in_username_entry.pack()

label_password = Label(inscription_left_frame, text="Mot de passe:", font=("Arial", 20,), bg="white")
label_password.pack()

sign_in_password_entry = Entry(inscription_left_frame, font=("Arial", 20,), bg="white")
sign_in_password_entry.pack()

sign_in_button = Button(inscription_left_frame, text="Connexion", font=("Arial", 20,), bg="white", command=sign_in)
sign_in_button.pack(fill=X)

home_return = Button(inscription_left_frame, text="Retour Accueil", font=("Arial", 20,), bg="white", command=print_accueil_page)
home_return.pack(fill=X)

inscription_left_frame.grid(row=0, column=1, sticky=W)

#Generateur

width = 300
height = 300
image3 = PhotoImage(file="Password_Generator3.png").zoom(16).subsample(35)
canvas = Canvas(Generator_page, width=width, height=height, bg='#E4E1CF', bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image)
canvas.grid(row=0, column=0, sticky=E)

left_frame = Frame(Generator_page, bg='#E4E1CF')

label_name_password = Label(left_frame, text="Nom du Mot de passe:", font=("Arial", 20,), bg="white")
label_name_password.pack()

name_password_entry = Entry(left_frame, font=("Arial", 20,), bg="white")
name_password_entry.pack()

label_password = Label(left_frame, text="Mot de passe:", font=("Arial", 20,), bg="white")
label_password.pack()

password_entry1 = Entry(left_frame, font=("Arial", 20,), bg="white")
password_entry1.pack()

password_button = Button(left_frame, text="Générer", font=("Arial", 20,), bg="white", command=generate)
password_button.pack(fill=X)

save_button = Button(left_frame, text="Save", font=("Arial", 20,), bg="white", command=save_password)
save_button.pack(fill=X)

print_password_button = Button(left_frame, text="Afficher les mots de passes", font=("Arial", 20,), bg="white", command=print_password)
print_password_button.pack(fill=X)

home_return = Button(left_frame, text="Retour Accueil", font=("Arial", 20,), bg="white", command=print_accueil_page)
home_return.pack(fill=X)

left_frame.grid(row=0, column=1, sticky=W)

#password page

width = 300
height = 300
image4 = PhotoImage(file="Password_Generator4.png").zoom(16).subsample(35)
canvas = Canvas(Password_page, width=width, height=height, bg='#E4E1CF', bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image)
canvas.grid(row=0, column=0, sticky=E)

password_left_frame = Frame(Password_page, bg='#E4E1CF')
print_password_list = open("password_list1.txt","r")
print_password_list = print_password_list.read()

generator_return = Button(password_left_frame, text="Retour", font=("Arial", 20,), bg="white", command=print_generator_page)
generator_return.pack()

label_password_list = Label(password_left_frame, text=print_password_list, font=("Arial", 20,), bg="white")
label_password_list.pack(fill=X)

password_left_frame.grid(row=0, column=1, sticky=W)



window.mainloop()
