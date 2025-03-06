from tkinter import *
from tkinter import ttk
import tkinter as tk

#Comportement du bouton de conversion
def convert_temperature():
    try:
        if selected_unit.get() == 'Celsius':
            # Converti Celsius en Fahrenheit
            celsius = float(entry_temperature.get())
            fahrenheit = (celsius * 9/5) + 32
            label_result.config(text=f"{fahrenheit:.2f} °F")
        else:
            # Converti Fahrenheit en Celsius
            fahrenheit = float(entry_temperature.get())
            celsius = (fahrenheit - 32) * 5/9
            label_result.config(text=f"{celsius:.2f} °C")
    except ValueError:
        label_result.config(text="Invalid input")

#Créer la fenêtre principale
root = Tk()
root.title("Convertisseur de température")

#Contient et organise les widgets
frame_input = ttk.Frame(root, padding="10")
frame_input.grid(row=0, column=0)

#Permet à la fenêtre de s'agrandir et de se centrée
frame_input.grid_rowconfigure(1, weight=1)
frame_input.grid_columnconfigure(0, weight=1)
frame_input.grid_columnconfigure(1, weight=1)

#Permet à la fenêtre d'être redimensionnée
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#Entré des températures
entry_temperature = ttk.Entry(frame_input, width=10)
entry_temperature.grid(row=0, column=0, padx=5, pady=5)

#Liste déroulante, permet de choisir le paramètre de température
selected_unit = tk.StringVar(value='Celsius')
unit_selector = ttk.Combobox(frame_input, textvariable=selected_unit, values=['Celsius', 'Fahrenheit'])
unit_selector.grid(row=0, column=1, padx=5, pady=5)

#Bouton de conversion
button_convert = ttk.Button(frame_input, text="Convertir", command=convert_temperature)
button_convert.grid(row=0, column=2, padx=5, pady=5)

#Label affichant le résultat
label_result = ttk.Label(root, text="")
label_result.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
