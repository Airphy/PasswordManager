from tkinter import *
from tkinter import ttk
import customtkinter as ctk

# Window
window = ctk.CTk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

app_width = 1200
app_height = 599

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


# Widgets

# define grid
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=100000)
# window.rowconfigure(0, weight=1)

menu_frame = ctk.CTkFrame(master=window, fg_color="red")
menu_frame.place(x=0, y=0, relwidth=0.15, relheight=1)
main_frame = ctk.CTkFrame(master=window, fg_color="blue")
main_frame.place(relx=0.15, y=0, relwidth=0.85, relheight=1)

username_label = ctk.CTkLabel(
    menu_frame, text="Username", bg_color="black", padx=5, pady=5
)

decrypt_all = ctk.CTkButton(menu_frame, text="Decrpyt All")

username_label.pack(side=TOP, fill=X, pady=10, padx=10)
decrypt_all.pack(side=BOTTOM, fill=X, pady=10, padx=10)

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

# Create Heading (Top Bar)
# password_tree.heading("#0", text="#", anchor=CENTER)
password_tree.heading("Website", text="Website", anchor=W)
password_tree.heading("Password", text="Password", anchor=W)
password_tree.pack(expand=TRUE, fill=BOTH, padx=10, pady=10)

# Add data
password_tree.insert(parent="", index="end", iid=0, values=("reddit", "123"))

password_tree_scroll.configure(command=password_tree.yview)

# heading = ctk.CTkLabel(window, text="Heading", bg_color=("pink", "green"))
# heading.grid(row=0, column=0, sticky="news")

# button = ctk.CTkButton(
#     window, text="Light/Dark", command=lambda: ctk.set_appearance_mode("light")
# )


# button.grid(row=0, column=1, sticky="news")
# run
window.mainloop()
