import customtkinter as ctk
from tkinter.filedialog import askopenfilename
import master


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

    #def show():
        #print(var.get())
        #print(entry2.get())
        #print(entry1.get())

root = ctk.CTk()
root.geometry("800x800")
root.title("Excel to MySQL")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

loc = None
hstn_var = ctk.StringVar(root)
usrn_var = ctk.StringVar(root)
pwd_var = ctk.StringVar(root)
dtb_var = ctk.StringVar(root)

def choose():

    filename = askopenfilename(
    title='Open a Excel file',
    #initialdir='/',
    filetypes=[("Excel files", ".xlsx .xls"),
                ('CSV files',"*.csv")]
    )
    # show an "Open" dialog box and return the path to the selected file
    # print(filename)
    global loc
    loc = filename
    display_file = ctk.CTkLabel(master=frame, text=loc)
    display_file.pack(padx=10, pady=10)


label1 = ctk.CTkLabel(master=frame, text="Data Transfer from Excel to MySQL", font=("Roboto", 26))
label1.pack(pady=12, padx=10)

file_choose = ctk.CTkButton(master=frame, text="Choose File", command=choose).pack()

label2 = ctk.CTkLabel(master=frame, text="MySQL Login", font=("Roboto", 20))
label2.pack(pady=12, padx=10)

label3 = ctk.CTkLabel(master=frame, text="Enter Hostname:", font=("Verdana", 16), text_color="grey")
label3.pack()
hostname = ctk.CTkEntry(master=frame, width=300, placeholder_text="Hostname", textvariable=hstn_var, font=("Verdana", 15))
hostname.pack(pady=12, padx=10)

label4 = ctk.CTkLabel(master=frame, text="Enter Username:", font=("Verdana", 16), text_color="grey")
label4.pack()
username = ctk.CTkEntry(master=frame, width=300, placeholder_text="Username", textvariable=usrn_var, font=("Verdana", 15))
username.pack(pady=12, padx=10)

label5 = ctk.CTkLabel(master=frame, text="Enter Database name:", font=("Verdana", 16), text_color="grey")
label5.pack()
database = ctk.CTkEntry(master=frame, width=300, placeholder_text="Database name", textvariable=dtb_var, font=("Verdana", 15))
database.pack(pady=12, padx=10)

label6 = ctk.CTkLabel(master=frame, text="Enter Password:", font=("Verdana", 16), text_color="grey")
label6.pack()
password = ctk.CTkEntry(master=frame, width=300, placeholder_text="Password", show = "*", textvariable=pwd_var,font=("Verdana", 15))
password.pack(pady=12, padx=10)

var = ctk.IntVar()
checkbox = ctk.CTkCheckBox(master=frame, text="Create New Database", variable=var)
checkbox.pack(pady=12, padx=10)

def main():
    display_text, dtfont = master.dtc(loc, hstn_var.get(), usrn_var.get(), pwd_var.get(), dtb_var.get())
    display_label = ctk.CTkLabel(master=frame, text=display_text, font=dtfont, text_color="grey")
    display_label.pack()

data_transfer = ctk.CTkButton(master=frame, text="Transfer the Data", width=20, command= main)
data_transfer.pack(padx=5, pady=5)

close = ctk.CTkButton(root, text="Close Window", width=10, command= root.destroy)
close.pack(padx=5, pady=5)

root.mainloop()