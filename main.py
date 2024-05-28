from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox  # To show message dialogs
import random
import pyperclip
import json
# --------------------------PASSWORD GENERATOR -----------------------#


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters+password_symbols+password_numbers
    random.shuffle(password_list)
    # we can replace the after code by join method
    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# --------------------------SAVE PASSWORD ------------------------------#


def save():
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    len_wesite = len(website)
    len_email = len(email)
    len_pass = len(password)
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len_email == 0 or len_pass == 0 or len_wesite == 0:
        messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # json.dump() -> write , json.load() -> Read , json.update(0) -> Update
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving the updating data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
# ---------------------------Find Password -------------------------------#
def find_password():
    website = website_entry.get().lower()
    try:
        with open("data.json")as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exist.")
# ---------------------------UI SETUP ------------------------------------#
window = Tk()
window.title("Password Manager")
window.iconbitmap('./images/forgot-password-icon-18355-Windows.ico')
window_width = 500
window_height = 400
# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.resizable(False, False)
# Setup the frames
frame1 = Frame(width=500, height=250)
frame1.pack()
img = Image.open("./images/forgot-password-icon-18355.png")
new_image = ImageTk.PhotoImage(img)
img_label = Label(frame1, image=new_image, padx=50)
img_label.place(relx=0.5, rely=0.5, anchor="center")

# Create Labels
frame2 = Frame(window, width='500', height='250')
frame2.pack()
website_label = Label(frame2, text="Website:", pady=5)
website_label.grid(column=0, row=1)
email_label = Label(frame2, text="Email/Username:", pady=5)
email_label.grid(column=0, row=2)
password_label = Label(frame2, text="Password:", pady=5)
password_label.grid(column=0, row=3)
# Create the entries
website_entry = Entry(frame2, width=20)
website_entry.focus()
website_entry.grid(column=1, row=1)
email_entry = Entry(frame2, width=40)
# index -> where to insert the text (مكان المؤشر) , string -> the text
email_entry.insert(0, "anas.yusuf200112@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(frame2, width=20, justify='center')
password_entry.grid(column=1, row=3)
# Create Buttons
search_btn = Button(frame2, text="Search",
                    relief='groove', width=14,command=find_password)
# search_btn.grid(column=2, row=1)
search_btn.grid(column=2, row=1)
generate_btn = Button(frame2, text="Generate Password",
                      relief="groove", command=generate_password)
generate_btn.grid(column=2, row=3)
add_btn = Button(frame2, text="Add", relief="groove", width=33, command=save)
add_btn.grid(column=1, row=4, columnspan=2, pady=5)

window.mainloop()
