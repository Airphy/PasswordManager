from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import PM_Functionality as pm

password_manager_functionality = pm.PasswordManager()
password_manager_functionality.load_key("aidan.key")
password_manager_functionality.load_password_file("aidan.pass")


# Window Settings
window = ctk.CTk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

app_width = 1200
app_height = 600

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

window.title("Password Manager")
window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

window.resizable(False, False)
# window.minsize(200, 100)
# window.maxsize(200, 100)
window.bind("<Escape>", lambda event: window.quit())


# window.overrideredirect(True)
# grip = ttk.Sizegrip(window)
# grip.place(relx=1.0, rely=1.0, anchor="se")


# End of Window
def load_passwords_treeview():
    password_tree.insert(parent="", index="end", iid=0, values=("reddit", "123"))


def multifunction(site, password):
    password_manager_functionality.add_password(site, password)
    password_tree.insert(parent="", index="end", iid=1, values=(site, password))


def create_add_password_screen():
    # TopLevel
    add_password_screen = ctk.CTkToplevel(window)
    add_password_screen.title("Add a Password")
    screen_width = add_password_screen.winfo_screenwidth()
    screen_height = add_password_screen.winfo_screenheight()

    top_width = 600
    top_height = 200

    x = (screen_width / 2) - (top_width / 2)
    y = (screen_height / 2) - (top_height / 2)

    add_password_screen.attributes("-topmost", "true")
    add_password_screen.geometry(f"{top_width}x{top_height}+{int(x)}+{int(y)}")

    # Widget Fields
    site_input_label = ctk.CTkLabel(add_password_screen, text="Site:")
    site_input = ctk.CTkEntry(add_password_screen)

    pass_input_label = ctk.CTkLabel(add_password_screen, text="Password:")
    pass_input = ctk.CTkEntry(add_password_screen)

    add_button = ctk.CTkButton(
        add_password_screen,
        text="Add",
        command=lambda: multifunction(site_input.get(), pass_input.get()),
    )
    # password_manager_functionality.add_password( site_input.get(), pass_input.get() )
    # password_tree.insert(  parent="", index="end", iid=1, values=(site_input.get(), pass_input.get()))

    site_input_label.pack()
    site_input.pack()
    pass_input_label.pack()
    pass_input.pack()
    add_button.pack(side=BOTTOM, pady=15)


def multifunction_call(*args):
    for function in args:
        function()


def test1():
    print("1")


def test2():
    print("2")


# Widgets

# define grid
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=100000)
# window.rowconfigure(0, weight=1)

# Main Interaction

menu_frame = ctk.CTkFrame(master=window, fg_color="red")
menu_frame.place(x=0, y=0, relwidth=0.15, relheight=1)
main_frame = ctk.CTkFrame(master=window, fg_color="blue")
main_frame.place(relx=0.15, y=0, relwidth=0.85, relheight=1)

username_label = ctk.CTkLabel(
    menu_frame, text="Username", bg_color="black", padx=5, pady=5
)

decrypt_all = ctk.CTkButton(menu_frame, text="Decrpyt All")

add_password = ctk.CTkButton(
    menu_frame,
    text="Add Password",
    command=create_add_password_screen,
)
# password_manager_functionality.add_password("youtube2", "helpme")
remove_password = ctk.CTkButton(menu_frame, text="Remove Password")

username_label.pack(side=TOP, fill=X, pady=10, padx=10)

decrypt_all.pack(side=TOP, fill=X, pady=10, padx=10)
remove_password.pack(side=BOTTOM, fill=X, pady=10, padx=10)
add_password.pack(side=BOTTOM, fill=X, pady=10, padx=10)


password_tree_scroll = Scrollbar(main_frame)
password_tree_scroll.pack(side=RIGHT, fill=Y)

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background="black",
    foreground="red",
    fieldbackground="silver",
    rowheight=35,
    font=("Calibri", 15),
)
style.map("Treeview", background=[("selected", "green")])

style.configure(
    "Treeview.Heading",
    fieldbackground="silver",
    rowheight=45,
    font=("Calibri", 20),
)

password_tree = ttk.Treeview(
    main_frame,
    yscrollcommand=password_tree_scroll.set,
    selectmode="extended",
    show=["headings"],
)
# Defining Tree Columns
password_tree["columns"] = ("Website", "Password")
# Format Columns
password_tree.column("Website", anchor=W)
password_tree.column("Password", anchor=W)

# Create Heading (Visual Top Bar)
# password_tree.heading("#0", text="#", anchor=CENTER)
password_tree.heading("Website", text="Website", anchor=W)
password_tree.heading("Password", text="Password", anchor=W)
password_tree.pack(expand=TRUE, fill=BOTH, padx=10, pady=10)

# Add data

# password_tree.insert(parent="", index="end", iid=0, values=("reddit", "123"))

password_tree_scroll.configure(command=password_tree.yview)


# Loops GUI
window.mainloop()
