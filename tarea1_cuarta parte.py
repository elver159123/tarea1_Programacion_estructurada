import tkinter as tk
from tkinter import messagebox


# Funciones para cada opción
def factorial():
    def calcular_factorial():
        try:
            num = int(entry_num.get())
            if num < 0:
                messagebox.showerror("Error", "El número debe ser mayor o igual a 0.")
            else:
                result = 1
                for i in range(1, num + 1):
                    result *= i
                messagebox.showinfo("Factorial", f"El factorial de {num} es: {result}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido.")
    
    ventana_factorial = tk.Toplevel(root)
    ventana_factorial.title("Factorial de un número")
    ventana_factorial.geometry("400x300")
    tk.Label(ventana_factorial, text="Ingrese un número:").pack(pady=10)
    entry_num = tk.Entry(ventana_factorial)
    entry_num.pack(pady=5)
    tk.Button(ventana_factorial, text="Calcular factorial", command=calcular_factorial).pack(pady=10)
    tk.Button(ventana_factorial, text="Regresar al menú", command=ventana_factorial.destroy).pack(pady=10)


def numeros_primos():
    def encontrar_primos():
        try:
            inicio = int(entry_inicio.get())
            fin = int(entry_fin.get())
            primos = []
            for num in range(inicio, fin + 1):
                if num > 1:
                    for i in range(2, num):
                        if num % i == 0:
                            break
                    else:
                        primos.append(num)
            if primos:
                messagebox.showinfo("Números primos", f"Números primos entre {inicio} y {fin}: {', '.join(map(str, primos))}")
            else:
                messagebox.showinfo("Números primos", f"No se encontraron números primos entre {inicio} y {fin}.")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos.")
    
    ventana_primos = tk.Toplevel(root)
    ventana_primos.title("Números primos")
    ventana_primos.geometry("400x300")
    tk.Label(ventana_primos, text="Ingrese el inicio del rango:").pack(pady=10)
    entry_inicio = tk.Entry(ventana_primos)
    entry_inicio.pack(pady=5)
    tk.Label(ventana_primos, text="Ingrese el fin del rango:").pack(pady=10)
    entry_fin = tk.Entry(ventana_primos)
    entry_fin.pack(pady=5)
    tk.Button(ventana_primos, text="Mostrar números primos", command=encontrar_primos).pack(pady=10)
    tk.Button(ventana_primos, text="Regresar al menú", command=ventana_primos.destroy).pack(pady=10)


def sumar_digitos():
    def calcular_suma():
        try:
            num = entry_num.get()
            if len(num) < 2 or not num.isdigit():
                messagebox.showerror("Error", "Por favor ingrese un número entero con más de una cifra.")
            else:
                suma = sum(int(digit) for digit in num)
                messagebox.showinfo("Suma de dígitos", f"La suma de los dígitos es: {suma}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido.")
    
    ventana_suma = tk.Toplevel(root)
    ventana_suma.title("Sumar dígitos")
    ventana_suma.geometry("400x300")
    tk.Label(ventana_suma, text="Ingrese un número de más de una cifra:").pack(pady=10)
    entry_num = tk.Entry(ventana_suma)
    entry_num.pack(pady=5)
    tk.Button(ventana_suma, text="Calcular suma de dígitos", command=calcular_suma).pack(pady=10)
    tk.Button(ventana_suma, text="Regresar al menú", command=ventana_suma.destroy).pack(pady=10)


def invertir_numero():
    def invertir():
        try:
            num = entry_num.get()
            if len(num) < 2 or not num.isdigit():
                messagebox.showerror("Error", "Por favor ingrese un número entero con más de una cifra.")
            else:
                invertido = num[::-1]
                messagebox.showinfo("Invertir número", f"El número invertido es: {invertido}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido.")
    
    ventana_invertir = tk.Toplevel(root)
    ventana_invertir.title("Invertir un número")
    ventana_invertir.geometry("400x300")
    tk.Label(ventana_invertir, text="Ingrese un número de más de una cifra:").pack(pady=10)
    entry_num = tk.Entry(ventana_invertir)
    entry_num.pack(pady=5)
    tk.Button(ventana_invertir, text="Invertir número", command=invertir).pack(pady=10)
    tk.Button(ventana_invertir, text="Regresar al menú", command=ventana_invertir.destroy).pack(pady=10)


def promedio_calificaciones():
    def calcular_promedio():
        try:
            calificaciones = []
            while True:
                calificacion = float(entry_calificacion.get())
                if calificacion == -1:
                    break
                calificaciones.append(calificacion)
                entry_calificacion.delete(0, tk.END)
            if calificaciones:
                promedio = sum(calificaciones) / len(calificaciones)
                messagebox.showinfo("Promedio de calificaciones", f"El promedio es: {promedio:.2f}")
            else:
                messagebox.showinfo("Promedio de calificaciones", "No se ingresaron calificaciones.")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese una calificación válida.")
    
    ventana_promedio = tk.Toplevel(root)
    ventana_promedio.title("Promedio de calificaciones")
    ventana_promedio.geometry("400x300")
    tk.Label(ventana_promedio, text="Ingrese una calificación (-1 para terminar):").pack(pady=10)
    entry_calificacion = tk.Entry(ventana_promedio)
    entry_calificacion.pack(pady=5)
    tk.Button(ventana_promedio, text="Ingresar calificación", command=calcular_promedio).pack(pady=10)
    tk.Button(ventana_promedio, text="Regresar al menú", command=ventana_promedio.destroy).pack(pady=10)


# Función para el menú principal
def menu_principal():
    for widget in root.winfo_children():
        widget.destroy()  # Limpiar la ventana principal
    
    # Etiqueta de bienvenida
    tk.Label(root, text="Seleccione una opción:", font=("Arial", 14), bg="#2E4053", fg="#FFFFFF").pack(pady=10, fill=tk.BOTH)
    
    # Botones para cada opción
    button_width = 30  # Establecemos un ancho fijo para todos los botones
    tk.Button(root, text="1. Factorial de un número", command=factorial, bg="#2980B9", fg="#FFFFFF", width=button_width).pack(pady=5)
    tk.Button(root, text="2. Números primos", command=numeros_primos, bg="#2980B9", fg="#FFFFFF", width=button_width).pack(pady=5)
    tk.Button(root, text="3. Sumar dígitos", command=sumar_digitos, bg="#2980B9", fg="#FFFFFF", width=button_width).pack(pady=5)
    tk.Button(root, text="4. Invertir un número", command=invertir_numero, bg="#2980B9", fg="#FFFFFF", width=button_width).pack(pady=5)
    tk.Button(root, text="5. Promedio de calificaciones", command=promedio_calificaciones, bg="#2980B9", fg="#FFFFFF", width=button_width).pack(pady=5)

# Ventana principal
root = tk.Tk()
root.title("Mi deber de programacion cuarta parte")
root.geometry("400x600")
root.config(bg="#F4F4F9")  # Fondo de la ventana

# Establecemos un estilo de fuente
font_style = ("Arial", 12)

# Configuración de la geometría adaptativa cuando la ventana se maximiza
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Llamar al menú principal al iniciar el programa
menu_principal()

root.mainloop()
