import mysql.connector
import tkinter as tk
from tkinter import messagebox
#codigo para conectar la base de datos (Sebastian ramos jacobo)
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="302",
    )
# CODIGO PARA GUARDAR, CONSULTAR, ACTUALIZAR Y ELIMINAR REGISTROS EN LA BASE DE DATOS
def guardar():
    con = conectar()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO test (nombre, correo, edad) VALUES (%s, %s, %s)",
        (nombre.get(), correo.get(), edad.get()),
    )
    con.commit()
    cur.close()
    con.close()
    messagebox.showinfo("TEST", "Guardado")
    consultar()
#Denise Geraldin Grande Fonseca 
def consultar():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT id, nombre, correo, edad FROM test")
    filas = cur.fetchall()
    cur.close()
    con.close()
    lista.delete(0, tk.END)
    for fila in filas:
        lista.insert(tk.END, f"{fila[0]} | {fila[1]} | {fila[2]} | {fila[3]}")
#CODIGO PARA ACTUALIZAR  Valentina Gutiérrez Romero 
def actualizar():
    con = conectar()
    cur = con.cursor()
    cur.execute(
        "UPDATE test SET nombre=%s, correo=%s, edad=%s WHERE id=%s",
        (nombre.get(), correo.get(), edad.get(), id_registro.get()),
    )
    con.commit()
    cur.close()
    con.close()
    messagebox.showinfo("TEST", "Actualizado")
    consultar()
#FUNCION PARA ELIMINAR OSCAR ISAAC HERRERA LUZ
def eliminar():
    con = conectar()
    cur = con.cursor()
    cur.execute("DELETE FROM test WHERE id=%s", (id_registro.get(),))
    con.commit()
    cur.close()
    con.close()
    messagebox.showinfo("TEST", "Eliminado")
    consultar()

ventana = tk.Tk()
ventana.title("TEST")
tk.Label(ventana, text="Id").grid(row=0, column=0, padx=6, pady=4)
id_registro = tk.Entry(ventana)
id_registro.grid(row=0, column=1, padx=6, pady=4)
tk.Label(ventana, text="Nombre").grid(row=1, column=0, padx=6, pady=4)
nombre = tk.Entry(ventana)
nombre.grid(row=1, column=1, padx=6, pady=4)
tk.Label(ventana, text="Correo").grid(row=2, column=0, padx=6, pady=4)
correo = tk.Entry(ventana)
correo.grid(row=2, column=1, padx=6, pady=4)
tk.Label(ventana, text="Edad").grid(row=3, column=0, padx=6, pady=4)
edad = tk.Entry(ventana)
edad.grid(row=3, column=1, padx=6, pady=4)
lista = tk.Listbox(ventana, width=42)
lista.grid(row=4, column=0, columnspan=2, padx=6, pady=6)
tk.Button(ventana, text="Guardar", command=guardar).grid(row=5, column=0, pady=4)
tk.Button(ventana, text="Consultar", command=consultar).grid(row=5, column=1, pady=4)
tk.Button(ventana, text="Actualizar", command=actualizar).grid(row=6, column=0, pady=4)
tk.Button(ventana, text="Eliminar", command=eliminar).grid(row=6, column=1, pady=4)
ventana.mainloop()