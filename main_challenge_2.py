import json
import pyperclip
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle


# ---------------------------- PASSWORD FINDER ------------------------------- #
def find_password():
    check_website = website_entry.get()

    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if check_website == data[check_website]:
            messagebox.showinfo(title=check_website, message=f"Email: {data[check_website]['email']}\n"
                                                             f"Password: {data[check_website]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {check_website} exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, string=f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    w_info = website_entry.get()
    e_u_info = email_username_entry.get()
    p_info = password_entry.get()
    new_data = {
        w_info: {
            "email": e_u_info,
            "password": p_info,
        },
    }

    if len(w_info) == 0 or len(p_info) == 0:
        messagebox.showwarning(title="Oops!", message="Please make sure you haven't left any fields empty!")
    else:
        # messagebox.askokcancel(title=w_info, message=f"These are the details entered: \nEmail: {e_u_info} "
        #                                              f"\nPassword: {p_info} \nIs it ok to save?")
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data.
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data.
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # Saving updated data.
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="../Day 29 - Building a Password Manager/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=22)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "prototype@gmail.com")

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

search_button = Button(text="Search", width=9, command=find_password)
search_button.grid(column=2, row=1)

generate_password_button = Button(text="Generate", width=9, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=32, command=save)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
