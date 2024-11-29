import tkinter as tk
from tkinter import messagebox


def mayor_menor():
    def verificar():
        try:
            numero = int(entry_num.get())
            if numero > 10:
                resultado_label.config(text="Es mayor que 10")
            else:
                resultado_label.config(text="Es menor que 10")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido.")

    ventana = tk.Toplevel(root)
    ventana.title("Mayor o menor")
    tk.Label(ventana, text="Ingrese un número:").pack(pady=5)
    entry_num = tk.Entry(ventana)
    entry_num.pack(pady=5)
    tk.Button(ventana, text="Verificar", command=verificar).pack(pady=5)
    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack(pady=5)


def positivo_negativo():
    def verificar():
        try:
            numero = int(entry_num.get())
            if numero > 0:
                resultado_label.config(text="Es positivo")
            elif numero < 0:
                resultado_label.config(text="Es negativo")
            else:
                resultado_label.config(text="Es cero")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido.")

    ventana = tk.Toplevel(root)
    ventana.title("Positivo o negativo")
    tk.Label(ventana, text="Ingrese un número:").pack(pady=5)
    entry_num = tk.Entry(ventana)
    entry_num.pack(pady=5)
    tk.Button(ventana, text="Verificar", command=verificar).pack(pady=5)
    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack(pady=5)


def par_impar():
    def verificar():
        try:
            numero = int(entry_num.get())
            if numero % 2 == 0:
                resultado_label.config(text="Es par")
            else:
                resultado_label.config(text="Es impar")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido.")

    ventana = tk.Toplevel(root)
    ventana.title("Par o impar")
    tk.Label(ventana, text="Ingrese un número:").pack(pady=5)
    entry_num = tk.Entry(ventana)
    entry_num.pack(pady=5)
    tk.Button(ventana, text="Verificar", command=verificar).pack(pady=5)
    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack(pady=5)


def aprobado_reprobado():
    def verificar():
        try:
            calificacion = float(entry_num.get())
            if calificacion >= 7:
                resultado_label.config(text="Aprobado")
            else:
                resultado_label.config(text="Reprobado")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese una calificación válida.")

    ventana = tk.Toplevel(root)
    ventana.title("Aprobado o reprobado")
    tk.Label(ventana, text="Ingrese una calificación:").pack(pady=5)
    entry_num = tk.Entry(ventana)
    entry_num.pack(pady=5)
    tk.Button(ventana, text="Verificar", command=verificar).pack(pady=5)
    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack(pady=5)


# Ventana principal
root = tk.Tk()
root.title("Mi Deber de Programación")

# Etiquetas de bienvenida
tk.Label(root, text="Bienvenido a mi deber de programación", font=("Arial", 14)).pack(pady=10)
tk.Label(root, text="Selecciona una opción de acuerdo al ejercicio:", font=("Arial", 12)).pack(pady=10)

# Botones para las opciones
tk.Button(root, text="1. Mayor o menor", width=30, command=mayor_menor).pack(pady=5)
tk.Button(root, text="2. Número positivo o negativo", width=30, command=positivo_negativo).pack(pady=5)
tk.Button(root, text="3. Par o impar", width=30, command=par_impar).pack(pady=5)
tk.Button(root, text="4. Aprobado o reprobado", width=30, command=aprobado_reprobado).pack(pady=5)

# Inicia el bucle de la aplicación
root.mainloop()
