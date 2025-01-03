import customtkinter as ck
from scan import get_image
from books_api import get_books
import books_api

ck.set_appearance_mode("dark")
ck.set_default_color_theme("blue")
app = ck.CTk()
app.geometry("500x500")
app.title("Books Scanner")


#check to see input is numbers only
def check_isbn_input(isbn_value):
    return isbn_value.isdigit() or isbn_value == ""


#clear screen
def clear_screen():
    for i in app.winfo_children():
        i.place_forget()

def book_details(isbn_final):
    clear_screen()
    info_books = get_books(isbn_final)
    title_book = info_books[0]
    author_book = info_books[1]

    if title_book not in ["Error", "''"] or author_book not in ["Error", "''"]: 
        label_title = ck.CTkLabel(
            app,
            text=f"Title={title_book}"
        )
        label_title.place(relx=0.5, rely=0.3, anchor="center")

        label_author = ck.CTkLabel(
            app,
            text=f"Title={author_book}"
        )
        label_author.place(relx=0.5, rely=0.4, anchor="center")
    else:
        label_error = ck.CTkLabel(
            app,
            text=f"Error. Could not find info"
        )
        label_error.place(relx=0.5, rely=0.3, anchor="center")

    # label_error = ck.CTkLabel(
    #     app,
    #     text=f"Error. Could not find info"
    # )
    # label_error.place(relx=0.5, rely=0.3, anchor="center")



def submit_isbn():
    isbn_final = isbn_entry.get()
    book_details(isbn_final)
    # return isbn_entered

#get isbn after scanning and populate the textbox with it
def get_isbn_scan():
    isbn_scan = get_image()
    if isbn_scan and isbn_scan != "Cancelled":
        isbn_entry.delete(0, "end")
        isbn_entry.insert(0, isbn_scan)
    # else:
    #     print


def home_screen():
    clear_screen()
    global isbn_entry
    validate_isbn = app.register(check_isbn_input)

    #place the scan button
    button_scan = ck.CTkButton(
        app, 
        text="Scan ISBN",
        command=get_isbn_scan
        )
    button_scan.place(relx=0.5, rely=0.4, anchor="center")

    #place the isbn input textbox
    isbn_entry = ck.CTkEntry(
        app,
        placeholder_text="Enter ISBN number",
        width=250,
        validate="key",
        validatecommand=(validate_isbn, "%P")
        )
    isbn_entry.place(relx=0.5, rely=0.6, anchor="center")

    #submit the isbn number button
    button_submit_isbn = ck.CTkButton(
        app, 
        text="Submit", 
        command=submit_isbn
        )
    button_submit_isbn.place(relx=0.5, rely=0.7, anchor="center")

def main():
    home_screen()

if __name__ == '__main__': 
    main()
    app.mainloop()
