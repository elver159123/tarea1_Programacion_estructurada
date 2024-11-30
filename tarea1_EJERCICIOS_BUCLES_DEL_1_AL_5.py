import tkinter as tk
from tkinter import messagebox

# Funciones para cada opción
def imprimir_numeros():
    numeros = ', '.join(str(i) for i in range(1, 11))
    messagebox.showinfo("Números del 1 al 10", f"Números: {numeros}")

def suma_primeros_10():
    suma = sum(range(1, 11))
    messagebox.showinfo("Suma de los primeros 10 números", f"La suma es: {suma}")

def tabla_multiplicar():
    def mostrar_tabla():
        try:
            numero = int(entry_numero.get())
            resultado = "\n".join([f"{numero} x {i} = {numero * i}" for i in range(1, 11)])
            messagebox.showinfo(f"Tabla de multiplicar de {numero}", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido.")
    
    ventana_tabla = tk.Toplevel(root)
    ventana_tabla.title("Tabla de multiplicar")
    ventana_tabla.geometry("400x300")
    tk.Label(ventana_tabla, text="Ingrese un número:").pack(pady=10)
    entry_numero = tk.Entry(ventana_tabla)
    entry_numero.pack(pady=5)
    tk.Button(ventana_tabla, text="Mostrar tabla", command=mostrar_tabla).pack(pady=10)
    tk.Button(ventana_tabla, text="Regresar al menú", command=ventana_tabla.destroy).pack(pady=10)

def contar_pares():
    def obtener_rango():
        try:
            inicio = int(entry_inicio.get())
            fin = int(entry_fin.get())
            pares = [str(i) for i in range(inicio, fin + 1) if i % 2 == 0]
            if pares:
                messagebox.showinfo("Números pares", f"Números pares: {', '.join(pares)}")
            else:
                messagebox.showinfo("Números pares", "No hay números pares en el rango ingresado.")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos.")
    
    ventana_pares = tk.Toplevel(root)
    ventana_pares.title("Contar números pares")
    ventana_pares.geometry("400x300")
    tk.Label(ventana_pares, text="Ingrese el inicio del rango:").pack(pady=10)
    entry_inicio = tk.Entry(ventana_pares)
    entry_inicio.pack(pady=5)
    tk.Label(ventana_pares, text="Ingrese el fin del rango:").pack(pady=10)
    entry_fin = tk.Entry(ventana_pares)
    entry_fin.pack(pady=5)
    tk.Button(ventana_pares, text="Mostrar números pares", command=obtener_rango).pack(pady=10)
    tk.Button(ventana_pares, text="Regresar al menú", command=ventana_pares.destroy).pack(pady=10)

def contador_regresivo():
    def obtener_rango():
        try:
            inicio = int(entry_inicio.get())
            fin = int(entry_fin.get())
            if inicio < fin:
                messagebox.showerror("Error", "El inicio debe ser mayor que el fin para el contador regresivo.")
            else:
                contador = [str(i) for i in range(inicio, fin - 1, -1)]
                messagebox.showinfo("Contador regresivo", f"Contador: {', '.join(contador)}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos.")
    
    ventana_contador = tk.Toplevel(root)
    ventana_contador.title("Contador regresivo")
    ventana_contador.geometry("400x300")
    tk.Label(ventana_contador, text="Ingrese el inicio del rango:").pack(pady=10)
    entry_inicio = tk.Entry(ventana_contador)
    entry_inicio.pack(pady=5)
    tk.Label(ventana_contador, text="Ingrese el fin del rango:").pack(pady=10)
    entry_fin = tk.Entry(ventana_contador)
    entry_fin.pack(pady=5)
    tk.Button(ventana_contador, text="Mostrar contador", command=obtener_rango).pack(pady=10)
    tk.Button(ventana_contador, text="Regresar al menú", command=ventana_contador.destroy).pack(pady=10)

# Función principal del menú
def menu_principal():
    for widget in root.winfo_children():
        widget.destroy()  # Limpiar la ventana principal
    
    # Etiqueta de bienvenida
    tk.Label(root, text="Seleccione una opción:", font=("times new roman", 14), bg="#2E4053", fg="#FFFFFF").pack(pady=10, fill=tk.BOTH)
    
    # Botones para cada opción
    button_width = 30  # Establecemos un ancho fijo para todos los botones
    tk.Button(root, text="1. Imprimir números del 1 al 10", command=imprimir_numeros, bg="#2980B9", fg="#FFFFFF", width=button_width).pack(pady=5)
    tk.Button(root, text="2. Suma de los primeros 10 números", command=suma_primeros_10, bg="#2980B9", fg="#FFFFFF", width=button_width).pack(pady=5)
    tk.Button(root, text="3. Tabla de multiplicar", command=tabla_multiplicar, bg="#2980B9", fg="#FFFFFF", width=button_width).pack(pady=5)
    tk.Button(root, text="4. Contar números pares", command=contar_pares, bg="#2980B9", fg="#FFFFFF", width=button_width).pack(pady=5)
    tk.Button(root, text="5. Contador regresivo", command=contador_regresivo, bg="#2980B9", fg="#FFFFFF", width=button_width).pack(pady=5)

# Ventana principal
root = tk.Tk()
root.title("Mi deber de programacion tercera parte")
root.geometry("500x300")
root.config(bg="#F4F4F9")  # Fondo de la ventana

# Establecemos un estilo de fuente
font_style = ("Arial", 12)

# Configuración de la geometría adaptativa cuando la ventana se maximiza
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Llamar al menú principal al iniciar el programa
menu_principal()

root.mainloop()
