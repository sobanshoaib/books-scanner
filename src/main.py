import customtkinter as ck

ck.set_appearance_mode("dark")
ck.set_default_color_theme("blue")
app = ck.CTk()
app.geometry("500x500")
app.title("Books Scanner")


def check_isbn_input(isbn_value):
    return isbn_value.isdigit() or isbn_value == ""


button_scan = ck.CTkButton(app, text="Scan ISBN")
button_scan.place(relx=0.5, rely=0.4, anchor="center")

validate_isbn = app.register(check_isbn_input)
isbn_entry = ck.CTkEntry(
    app,
    placeholder_text="Enter ISBN number",
    width=250,
    validate="key",
    validatecommand=(validate_isbn, "%P")
)
isbn_entry.place(relx=0.5, rely=0.6, anchor="center")

def submit_isbn():
    isbn_entered = isbn_entry.get()

button_submit_isbn = ck.CTkButton(app, text="Submit", command=submit_isbn)
button_submit_isbn.place(relx=0.5, rely=0.7, anchor="center")



app.mainloop()
