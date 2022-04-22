from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = Tk()
root.geometry("300x150")
root.resizable(False, False)
root.title("Sign In")

# Store email address and password
email = StringVar()
pwd = StringVar()

def login_clicked():
    '''Callback when the login button clicked'''

    msg = f"You entered email: {email.get()} & pwd: {pwd.get()}"
    showinfo(
        title = "Information",
        message=msg
    )

# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

# Email 
email_label = ttk.Label(signin, text = "Email Address: ")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# Password
password_label = ttk.Label(signin, text = "Password: ")
password_label.pack(fill = 'x', expand=True)

password_entry = ttk.Entry(signin, textvariable= pwd, show='*')
password_entry.pack(fill = 'x', expand=True)

# Login Button
login_button = ttk.Button(signin, text = "Login", command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)

root.mainloop()
