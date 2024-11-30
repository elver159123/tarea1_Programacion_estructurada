import tkinter as tk
from tkinter import messagebox
import math


# Funciones para cada opción
def saludo_personalizado():
    def mostrar_saludo():
        nombre = entry_nombre.get()
        saludo = f"Hola, {nombre}!"
        messagebox.showinfo("Saludo", saludo)
    
    ventana = tk.Toplevel(root)
    ventana.title("Saludo Personalizado")
    ventana.geometry("300x200")

    frame = tk.Frame(ventana)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    tk.Label(ventana, text="Ingrese su nombre:").pack(pady=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack(pady=5)
    tk.Button(ventana, text="Generar saludo", command=mostrar_saludo).pack(pady=5)
    tk.Button(ventana, text="Regresar al menú", command=ventana.destroy).pack(pady=5)

def suma_dos_numeros():
    def calcular_suma():
        try:
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
            suma = num1 + num2
            messagebox.showinfo("Resultado", f"La suma es: {suma}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")
    
    ventana = tk.Toplevel(root)
    ventana.title("Suma de dos números")
    ventana.geometry("400x200")

    frame = tk.Frame(ventana)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    tk.Label(ventana, text="Ingrese el primer número:").pack(pady=5)
    entry_num1 = tk.Entry(ventana)
    entry_num1.pack(pady=5)
    tk.Label(ventana, text="Ingrese el segundo número:").pack(pady=5)
    entry_num2 = tk.Entry(ventana)
    entry_num2.pack(pady=5)
    tk.Button(ventana, text="Calcular suma", command=calcular_suma).pack(pady=5)
    tk.Button(ventana, text="Regresar al menú", command=ventana.destroy).pack(pady=5)

def numero_par_impar():
    def verificar_par_impar():
        try:
            numero = int(entry_num.get())
            if numero % 2 == 0:
                messagebox.showinfo("Resultado", "El número es par.")
            else:
                messagebox.showinfo("Resultado", "El número es impar.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")
    
    ventana = tk.Toplevel(root)
    ventana.title("Número par o impar")
    ventana.geometry("400x200")

    frame = tk.Frame(ventana)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    tk.Label(ventana, text="Ingrese un número:").pack(pady=5)
    entry_num = tk.Entry(ventana)
    entry_num.pack(pady=5)
    tk.Button(ventana, text="Verificar", command=verificar_par_impar).pack(pady=5)
    tk.Button(ventana, text="Regresar al menú", command=ventana.destroy).pack(pady=5)

def calcular_cuadrado():
    def obtener_cuadrado():
        try:
            numero = float(entry_num.get())
            cuadrado = numero ** 2
            messagebox.showinfo("Resultado", f"El cuadrado de {numero} es: {cuadrado}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")
    
    ventana = tk.Toplevel(root)
    ventana.title("Calcular el cuadrado")
    ventana.geometry("400x200")

    frame = tk.Frame(ventana)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    tk.Label(ventana, text="Ingrese un número:").pack(pady=5)
    entry_num = tk.Entry(ventana)
    entry_num.pack(pady=5)
    tk.Button(ventana, text="Calcular cuadrado", command=obtener_cuadrado).pack(pady=5)
    tk.Button(ventana, text="Regresar al menú", command=ventana.destroy).pack(pady=5)

def calcular_area_circulo():
    def obtener_area():
        try:
            radio = float(entry_radio.get())
            area = math.pi * (radio ** 2)
            messagebox.showinfo("Resultado", f"El área del círculo es: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor válido para el radio.")
    
    ventana = tk.Toplevel(root)
    ventana.title("Calcular el área de un círculo")
    ventana.geometry("400x200")

    frame = tk.Frame(ventana)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    tk.Label(ventana, text="Ingrese el radio del círculo:").pack(pady=5)
    entry_radio = tk.Entry(ventana)
    entry_radio.pack(pady=5)
    tk.Button(ventana, text="Calcular área", command=obtener_area).pack(pady=5)
    tk.Button(ventana, text="Regresar al menú", command=ventana.destroy).pack(pady=5)

# Ventana principal
root = tk.Tk()
root.title("Mi deber de programacion quinta parte")
root.geometry("400x500")
root.resizable(True, True)  # Permitir maximizar la ventana

# Colores vivos
root.config(bg="#FFFCF9")

# Etiquetas de bienvenida
tk.Label(root, text="Bienvenido", font=("times new roman", 14), bg="#FFFCF9").pack(pady=10)
tk.Label(root, text="Selecciona una opción:", font=("Arial", 12), bg="#FFFCF9").pack(pady=10)

# Botones de las opciones
button_style = {'width': 30, 'height': 2, 'font': ('Arial', 12), 'bg': '#FFCE00', 'fg': 'black', 'activebackground': '#FFA500'}

tk.Button(root, text="1. Saludo Personalizado", **button_style, command=saludo_personalizado).pack(pady=10)
tk.Button(root, text="2. Suma de dos números", **button_style, command=suma_dos_numeros).pack(pady=10)
tk.Button(root, text="3. Número par o impar", **button_style, command=numero_par_impar).pack(pady=10)
tk.Button(root, text="4. Calcular el cuadrado", **button_style, command=calcular_cuadrado).pack(pady=10)
tk.Button(root, text="5. Calcular el área de un círculo", **button_style, command=calcular_area_circulo).pack(pady=10)

# Ejecutar la interfaz gráfica
root.mainloop()
