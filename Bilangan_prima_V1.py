import os
import tkinter as tk
from tkinter import ttk

os.system("cls")

# Layar
layar = tk.Tk()
layar.configure(bg="white")
layar.geometry("300x150")
layar.title("Prima Bukan ya?")
layar.resizable(False, False)

ANGKA = tk.StringVar()

# Fungsi cek bilangan prima
def Pengecek(angka):
    if angka <= 1:
        return False
    for i in range(2, angka):
        if angka % i == 0:
            return False
    return True

# Fungsi tombol
def cek_angka():
    try:
        angka = int(ANGKA.get())
        if Pengecek(angka):
            pesan = f"{angka} adalah bilangan prima!"
            hasil_label.config(text=pesan, foreground="green")
        else:
            pesan = f"{angka} bukan bilangan prima!"
            hasil_label.config(text=pesan, foreground="red")
    except ValueError:
        hasil_label.config(text="Masukkan angka yang valid!", foreground="black")

# Frame
input_frame = ttk.Frame(layar)
input_frame.pack(padx=10, fill="x", expand=True)

# Label input
Angka_label = ttk.Label(input_frame, text="Angka")
Angka_label.pack(padx=10, fill="x", expand=True)

# Input angka
Angka_input = ttk.Entry(input_frame, textvariable=ANGKA)
Angka_input.pack(padx=10, fill="x", expand=True)

# Tombol cek
Tombol_cek = ttk.Button(input_frame, text="Cek!", command=cek_angka)
Tombol_cek.pack(padx=10, pady=10, fill="x", expand=True)

# Label hasil (kosong dulu, nanti diisi saat tombol ditekan)
hasil_label = ttk.Label(input_frame, text="", foreground="blue")
hasil_label.pack(padx=10, fill="x", expand=True)

layar.mainloop()
