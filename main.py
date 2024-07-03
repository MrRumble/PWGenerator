from tkinter import *
from tkinter import messagebox
import isValid
import generator
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePasswordClick():
    generated_password = generator.password_generator()
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def addButtonClick():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data= {
        website: {
            "email" : email,
            "password" : password
        }
    }
    
    if len(website) ==0:
        messagebox.showwarning(message="Website field cannot be empty!")

    elif not isValid.is_valid_email(email):
        messagebox.showwarning(message="Invalid email!")

    elif not isValid.is_valid_password(password):
        messagebox.showwarning(title="Password invalid!", message="Password invalid!\nLength: Should be between 8 and 20 characters.\nCharacter types: Should include at least one uppercase letter (A-Z), one lowercase letter (a-z), one digit (0-9), and one special character (e.g., !@#$%^&*()).")
    else:
        try:
            with open("data.json", 'r') as file:
                data = json.load(file) # read old data
        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data) #add new data
            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4) #save updated data
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_button_click():
    data_to_search = website_entry.get()
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
            messagebox.showwarning(message="Data file not found.")
    else:
        searched_data = data.get(data_to_search)
        if searched_data:
            messagebox.showinfo(message=f'Email: {searched_data.get('email')}\nPassword: {searched_data.get("password")}')
        else:
            messagebox.showwarning(message=f'No detaiils for: {data_to_search}')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)

image_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_logo)
canvas.grid(row=0, column = 1)

website_label = Label(window, text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(window, width=21)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()

email_label = Label(window, text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(window, width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "jamesrumble@live.com")

password_label = Label(window, text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(window, width=21)
password_entry.grid(row=3, column=1)

generate_button = Button(window, width=12, text="Generate Password", command=generatePasswordClick)
generate_button.grid(row=3, column=2)

add_button=Button(window, width=34, text="Add Password", command=addButtonClick)
add_button.grid(row=4, column=1, columnspan=2)

search_button=Button(window, width=15, text="Search", command=search_button_click)
search_button.grid(row=1,column=2)

window.mainloop()
