from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

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
    if len(website_data) ==0 or len(website_data) ==0 or len(website_data) ==0:
        messagebox.showinfo(title="Error", message="Can't leave fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website_data, message=f"Username: {username_data}\n"
                                                               f"Password: {password_data}")
        if is_ok:
            with open("password.txt", "a") as pass_file:
                pass_file.write(f"{website_data} | {username_data} | {password_data}\n")
                website_entry.delete(0,END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)


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

website_entry = Entry(width=42)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)



username = Label(text="Email/Username: ")
username.grid(column=0,row=2)

username_entry = Entry(width=42)
username_entry.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:")
password.grid(column=0,row=3)

password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)

gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(column=2, row=3)

add_button = Button(text="Add",width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)






window.mainloop()