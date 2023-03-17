from tkinter import *

# ---------------------------- PASSWORD GENERATOR ---------------------------- #


# ---------------------------- SAVE PASSWORD ---------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")

    website_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- UI SETUP ---------------------------- #
window = Tk()
window.title("P4$5w0Rd M4n4g3r")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Inputs
website_input = Entry(width=52)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
email_input = Entry(width=52)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "dave@dryweb.com")
password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky=EW)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
