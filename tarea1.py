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
    ventana.configure(bg="#f82d97")  # Fondo rosa brillante

    tk.Label(ventana, text="Ingrese un número:", bg="#f82d97", fg="#e7c500", font=("Arial", 12)).pack(pady=5)
    entry_num = tk.Entry(ventana)
    entry_num.pack(pady=5)
    tk.Button(ventana, text="Verificar", bg="#2ef8a0", fg="black", command=verificar).pack(pady=5)
    resultado_label = tk.Label(ventana, text="", bg="#f82d97", fg="#e830ce", font=("Arial", 10))
    resultado_label.pack(pady=5)
    tk.Button(ventana, text="Volver al menú principal", bg="#c501e2", fg="white", command=ventana.destroy).pack(pady=5)


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
    ventana.configure(bg="#e830ce")  # Fondo rosa magenta

    tk.Label(ventana, text="Ingrese un número:", bg="#e830ce", fg="#2ef8a0", font=("Arial", 12)).pack(pady=5)
    entry_num = tk.Entry(ventana)
    entry_num.pack(pady=5)
    tk.Button(ventana, text="Verificar", bg="#e7c500", fg="black", command=verificar).pack(pady=5)
    resultado_label = tk.Label(ventana, text="", bg="#e830ce", fg="#c501e2", font=("Arial", 10))
    resultado_label.pack(pady=5)
    tk.Button(ventana, text="Volver al menú principal", bg="#f82d97", fg="white", command=ventana.destroy).pack(pady=5)


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
    ventana.configure(bg="#2ef8a0")  # Fondo verde menta

    tk.Label(ventana, text="Ingrese un número:", bg="#2ef8a0", fg="#c501e2", font=("Arial", 12)).pack(pady=5)
    entry_num = tk.Entry(ventana)
    entry_num.pack(pady=5)
    tk.Button(ventana, text="Verificar", bg="#f82d97", fg="black", command=verificar).pack(pady=5)
    resultado_label = tk.Label(ventana, text="", bg="#2ef8a0", fg="#e7c500", font=("Arial", 10))
    resultado_label.pack(pady=5)
    tk.Button(ventana, text="Volver al menú principal", bg="#e830ce", fg="white", command=ventana.destroy).pack(pady=5)


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
    ventana.configure(bg="#e7c500")  # Fondo amarillo

    tk.Label(ventana, text="Ingrese una calificación:", bg="#e7c500", fg="#f82d97", font=("Arial", 12)).pack(pady=5)
    entry_num = tk.Entry(ventana)
    entry_num.pack(pady=5)
    tk.Button(ventana, text="Verificar", bg="#c501e2", fg="white", command=verificar).pack(pady=5)
    resultado_label = tk.Label(ventana, text="", bg="#e7c500", fg="#2ef8a0", font=("Arial", 10))
    resultado_label.pack(pady=5)
    tk.Button(ventana, text="Volver al menú principal", bg="#e830ce", fg="white", command=ventana.destroy).pack(pady=5)


# Ventana principal
root = tk.Tk()
root.title("Mi Deber de Programación")
root.geometry("500x300")
root.configure(bg="#37023a")  # Fondo fucsia intenso

# Contenedor principal
frame = tk.Frame(root, bg="#37023a")
frame.pack(expand=True, fill="both", padx=10, pady=10)

# Etiquetas de bienvenida
tk.Label(frame, text="Bienvenido a mi deber de programación", font=("times new roman", 16), bg="#37023a", fg="#2ef8a0").pack(pady=10)
tk.Label(frame, text="Selecciona una opción:", font=("times new roman", 14), bg="#37023a", fg="#e7c500").pack(pady=10)

# Botones para las opciones
tk.Button(frame, text="1. Mayor o menor", width=30, bg="#e7c500", fg="black", command=mayor_menor).pack(pady=5)
tk.Button(frame, text="2. Número positivo o negativo", width=30, bg="#2ef8a0", fg="black", command=positivo_negativo).pack(pady=5)
tk.Button(frame, text="3. Par o impar", width=30, bg="#f82d97", fg="white", command=par_impar).pack(pady=5)
tk.Button(frame, text="4. Aprobado o reprobado", width=30, bg="#e830ce", fg="white", command=aprobado_reprobado).pack(pady=5)

# Inicia el bucle de la aplicación
root.mainloop()
