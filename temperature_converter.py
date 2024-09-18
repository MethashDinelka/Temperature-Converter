import tkinter as tk
from tkinter import ttk

def convert_temperature(label):
    tp = entry.get()
    temp_celsius = (int(tp) - 32) * 5/9
    label.configure(text=f"The temperature (in Celsius) : {temp_celsius:.2f}°C",font=('Copperplate Gothic Bold',15),fg='blue')
    print("© Methash Dinelka 2k24 - Project 01")


width, height = 540,450

root = tk.Tk()

display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()
left = int((display_width/2)-(width/2))
top = int((display_height/2)-(height/2))

# Create the main window
root.configure(bg="lightblue")
root.title("Temperature Converter")
root.iconbitmap("logo.ico")
root.geometry(f"{width}x{height}+{left}+{top}")
root.resizable(False, False)


l2 = tk.Label(root,text="FAHRENHEIT TO CELSIUS CONVERTER",font=("FarCry", 20),fg="green")
l2.grid(row=1, column=0, columnspan=4, pady=10)

# Create labels and entry fields
label_1 = tk.Label(root, text="Enter the temperature (In Farenheit) :",font=('Times New Roman',15))
label_1.grid(row=3, column=1)

entry = ttk.Entry(root,width=30)
entry.grid(row=4, column=0, columnspan=4, pady=10)

style = ttk.Style()
style.configure("my.TButton", font=("Perpetua Titling MT", 12, "bold"), foreground="blue", background="yellow")

button = ttk.Button(root, text="Convert", command=lambda: convert_temperature(label_2),padding=(10, 10),style="my.TButton")
button.grid(row=5, column=0, columnspan=4, pady=10)

label_2 = tk.Label(root)
label_2.grid(row=6, column=0, columnspan=4)

label_end = ttk.Label(root,text="""Web    : www.methash-dinelka.blogspot.com
E-mail : methash@outlook.com
 © Methash Dinelka 2k24 
""")
label_end.grid(row=14, column=2, columnspan=5)

root.mainloop()
