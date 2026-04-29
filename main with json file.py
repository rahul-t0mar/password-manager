from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    random_letters = [choice(letters) for _ in range(randint(8,10))]
    random_numbers = [choice(numbers) for _ in range(randint(2,4))]
    random_symbols = [choice(symbols) for _ in range(randint(2,4))]
    gen_password_list = random_letters + random_numbers + random_symbols
    shuffle(gen_password_list)
    gen_password = "".join(gen_password_list)
    pyperclip.copy(gen_password)
    password_entry.insert(0,gen_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_data = website_entry.get()
    username_data = username_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
            "email": username_data,
            "password": password_data
        }
    }
    if len(website_data) ==0 or len(website_data) ==0 or len(website_data) ==0:
        messagebox.showinfo(title="Error", message="Can't leave fields empty")
    else:
        try:
            # Reading the data from the json file.
            with open("password.json", "r") as pass_file:
                data_1 = json.load(pass_file)

        except:
            with open("password.json", "w") as pass_file:
                json.dump(new_data, pass_file, indent=4)
        else:
            data_1.update(new_data)
            # Writing the data to the json file.
            with open("password.json", "w") as pass_file:
                json.dump(data_1, pass_file, indent=4)
        finally:
            website_entry.delete(0,END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)

def search():
    website_data = website_entry.get()
    if website_data == "":
        messagebox.showinfo(title="Error", message="Website field can't be empty")
    else:
        try:
            with open("password.json","r") as data_file:
                data =  json.load(data_file)
        except:
            messagebox.showinfo(title="Error", message="No entries for the entered website")
        else:
            if website_data in data:
                email= data[website_data]["email"]
                password= data[website_data]["password"]
                messagebox.showinfo(title="Password", message=f"Username: {email}\n"
                                                          f"Password : {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No password available for {website_data }")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website = Label(text="Website: ")
website.grid(column=0,row=1)
website.config(pady=2)

website_entry = Entry(width=31)
website_entry.focus()
website_entry.grid(column=1, row=1)




username = Label(text="Email/Username: ")
username.grid(column=0,row=2)
username.config(pady=2)

username_entry = Entry(width=49)
username_entry.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:")
password.grid(column=0,row=3)
password.config(pady=2)

password_entry = Entry(width=31)
password_entry.grid(column=1, row=3)

gen_pass = Button(text="Generate Password",width=14, command=generate_password)
gen_pass.grid(column=2, row=3)

add_button = Button(text="Add",width=42, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=13, command=search)
search_button.grid(column=2, row=1)






window.mainloop()