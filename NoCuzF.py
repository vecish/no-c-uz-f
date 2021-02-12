import tkinter as tk

def celsius_to_fahrenheit():
    
    celsius = ent_temperature.get()
    fahrenheit = (32) + (9/5)*(float(celsius))
    lbl_result["text"] = f"{round(fahrenheit, 2)} \N{DEGREE fahrenheit}"

# jauna loga izveidošana
window = tk.Tk()
window.title("C to F")
window.resizable()

# ievades logs
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=8)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE celsius}")

# Izvietojums, kur ievadīt grādus un atbildes vieta
ent_temperature.grid(row=0, column=0)
lbl_temp.grid(row=0, column=1)

# pogas izveidošana ar tekstu, krāsu, h un platumu.
btn_convert = tk.Button(
    master=window,
    text="JEB TAS IR = ",
    width=12,
    height=2,
    bg="yellow",
    fg="black",
    bd=5,
    command=celsius_to_fahrenheit)

lbl_result = tk.Label(master=window,
    width=12,
    height=2,
    text="\N{DEGREE fahrenheit}", 
    fg="white", 
    bg="black")

# Izvietojums ievadei, pogai un rezultātam.

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# aiziet
window.mainloop()