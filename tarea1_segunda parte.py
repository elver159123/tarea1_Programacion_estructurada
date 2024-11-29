import tkinter as tk
from tkinter import messagebox
import random

# Función para el descuento en la tienda
def descuento_tienda():
    def calcular_descuento():
        try:
            cantidad = float(entry_cantidad.get())
            descuento = float(entry_descuento.get())
            if descuento in [25, 50, 75]:
                total = cantidad * (1 - descuento / 100)
                resultado_label.config(text=f"Precio final: ${total:.2f}")
            else:
                messagebox.showerror("Error", "Descuento no válido. Use 25, 50 o 75.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos.")

    ventana = tk.Toplevel(root)
    ventana.title("Descuento en una tienda")
    tk.Label(ventana, text="Cantidad de dinero:").pack(pady=5)
    entry_cantidad = tk.Entry(ventana)
    entry_cantidad.pack(pady=5)
    tk.Label(ventana, text="Descuento (25, 50, 75):").pack(pady=5)
    entry_descuento = tk.Entry(ventana)
    entry_descuento.pack(pady=5)
    tk.Button(ventana, text="Calcular", command=calcular_descuento).pack(pady=5)
    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack(pady=5)

# Función para edad para votar
def edad_para_votar():
    def verificar_edad():
        try:
            edad = int(entry_edad.get())
            if edad >= 18:
                resultado_label.config(text="Puedes votar.")
            else:
                resultado_label.config(text="No puedes votar.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese una edad válida.")

    ventana = tk.Toplevel(root)
    ventana.title("Edad para votar")
    tk.Label(ventana, text="Ingrese su edad:").pack(pady=5)
    entry_edad = tk.Entry(ventana)
    entry_edad.pack(pady=5)
    tk.Button(ventana, text="Verificar", command=verificar_edad).pack(pady=5)
    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack(pady=5)

# Función para mayor de tres números
def mayor_de_tres_numeros():
    def verificar_mayor():
        try:
            nums = [float(entry1.get()), float(entry2.get()), float(entry3.get())]
            mayor = max(nums)
            resultado_label.config(text=f"El mayor es: {mayor}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos.")

    ventana = tk.Toplevel(root)
    ventana.title("Mayor de tres números")
    tk.Label(ventana, text="Ingrese tres números:").pack(pady=5)
    entry1 = tk.Entry(ventana)
    entry1.pack(pady=5)
    entry2 = tk.Entry(ventana)
    entry2.pack(pady=5)
    entry3 = tk.Entry(ventana)
    entry3.pack(pady=5)
    tk.Button(ventana, text="Calcular", command=verificar_mayor).pack(pady=5)
    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack(pady=5)

# Función para clasificación de edades
def clasificacion_edades():
    def clasificar():
        try:
            edad = int(entry_edad.get())
            if edad <= 12:
                resultado_label.config(text="Eres un niño.")
            elif edad <= 17:
                resultado_label.config(text="Eres un adolescente.")
            else:
                resultado_label.config(text="Eres un adulto.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese una edad válida.")

    ventana = tk.Toplevel(root)
    ventana.title("Clasificación de edades")
    tk.Label(ventana, text="Ingrese su edad:").pack(pady=5)
    entry_edad = tk.Entry(ventana)
    entry_edad.pack(pady=5)
    tk.Button(ventana, text="Clasificar", command=clasificar).pack(pady=5)
    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack(pady=5)

# Función para la calculadora básica
def calculadora_basica():
    def calcular():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            suma = num1 + num2
            resta = num1 - num2
            multi = num1 * num2
            division = num1 / num2 if num2 != 0 else "Infinito (división por 0)"
            resultado_label.config(
                text=f"Suma: {suma}\nResta: {resta}\nMultiplicación: {multi}\nDivisión: {division}"
            )
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos.")

    ventana = tk.Toplevel(root)
    ventana.title("Calculadora básica")
    tk.Label(ventana, text="Ingrese dos números:").pack(pady=5)
    entry1 = tk.Entry(ventana)
    entry1.pack(pady=5)
    entry2 = tk.Entry(ventana)
    entry2.pack(pady=5)
    tk.Button(ventana, text="Calcular", command=calcular).pack(pady=5)
    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack(pady=5)

# Función para determinar si es un año bisiesto
def determinar_bisiesto():
    def verificar_bisiesto():
        try:
            year = int(entry_year.get())
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                resultado_label.config(text=f"{year} es un año bisiesto.")
            else:
                resultado_label.config(text=f"{year} no es un año bisiesto.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un año válido.")

    ventana = tk.Toplevel(root)
    ventana.title("Determinar año bisiesto")
    tk.Label(ventana, text="Ingrese un año:").pack(pady=5)
    entry_year = tk.Entry(ventana)
    entry_year.pack(pady=5)
    tk.Button(ventana, text="Verificar", command=verificar_bisiesto).pack(pady=5)
    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack(pady=5)

# Función para validar contraseñas
def validar_contraseña():
    def verificar_contraseña():
        contraseña = entry_contraseña.get()
        if contraseña == "12345":
            messagebox.showinfo("Acceso", "Acceso concedido.")
        else:
            messagebox.showerror("Error", "Contraseña incorrecta.")

    ventana = tk.Toplevel(root)
    ventana.title("Validar contraseña")
    tk.Label(ventana, text="Ingrese la contraseña:").pack(pady=5)
    entry_contraseña = tk.Entry(ventana, show="*")
    entry_contraseña.pack(pady=5)
    tk.Button(ventana, text="Verificar", command=verificar_contraseña).pack(pady=5)

# Función para el juego de números
def juego_de_numeros():
    def adivinar():
        try:
            numero_aleatorio = random.randint(1, 10)
            numero_usuario = int(entry_numero.get())
            if numero_usuario == numero_aleatorio:
                resultado_label.config(text="¡Acertaste!")
            else:
                resultado_label.config(text=f"Fallaste. El número era {numero_aleatorio}.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")

    ventana = tk.Toplevel(root)
    ventana.title("Juego de Números")
    tk.Label(ventana, text="Adivina el número (1-10):").pack(pady=5)
    entry_numero = tk.Entry(ventana)
    entry_numero.pack(pady=5)
    tk.Button(ventana, text="Adivinar", command=adivinar).pack(pady=5)
    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack(pady=5)

# Función para calcular el signo zodiacal
def calcular_signo_zodiacal():
    def determinar_signo():
        try:
            dia = int(entry_dia.get())
            mes = int(entry_mes.get())
            if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
                signo = "Aries"
            elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
                signo = "Tauro"
            elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
                signo = "Géminis"
            elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
                signo = "Cáncer"
            elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
                signo = "Leo"
            elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
                signo = "Virgo"
            elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
                signo = "Libra"
            elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
                signo = "Escorpio"
            elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
                signo = "Sagitario"
            elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
                signo = "Capricornio"
            elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
                signo = "Acuario"
            elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
                signo = "Piscis"
            resultado_label.config(text=f"Tu signo zodiacal es: {signo}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese datos válidos.")

    ventana = tk.Toplevel(root)
    ventana.title("Calcular signo zodiacal")
    tk.Label(ventana, text="Día de nacimiento:").pack(pady=5)
    entry_dia = tk.Entry(ventana)
    entry_dia.pack(pady=5)
    tk.Label(ventana, text="Mes de nacimiento:").pack(pady=5)
    entry_mes = tk.Entry(ventana)
    entry_mes.pack(pady=5)
    tk.Button(ventana, text="Determinar Signo", command=determinar_signo).pack(pady=5)
    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack(pady=5)

# Función para el sistema de calificaciones
def sistema_de_calificaciones():
    def calificar():
        try:
            calificacion = float(entry_calificacion.get())
            if calificacion >= 90:
                resultado_label.config(text="Calificación: A")
            elif calificacion >= 80:
                resultado_label.config(text="Calificación: B")
            elif calificacion >= 70:
                resultado_label.config(text="Calificación: C")
            elif calificacion >= 60:
                resultado_label.config(text="Calificación: D")
            else:
                resultado_label.config(text="Calificación: F")
        except ValueError:
            messagebox.showerror("Error", "Ingrese una calificación válida.")

    ventana = tk.Toplevel(root)
    ventana.title("Sistema de calificaciones")
    tk.Label(ventana, text="Ingrese su calificación:").pack(pady=5)
    entry_calificacion = tk.Entry(ventana)
    entry_calificacion.pack(pady=5)
    tk.Button(ventana, text="Calificar", command=calificar).pack(pady=5)
    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack(pady=5)

# Función para control de acceso
def control_de_acceso():
    def verificar_usuario():
        usuario = entry_usuario.get()
        contraseña = entry_contraseña.get()
        if usuario == "admin" and contraseña == "admin123":
            messagebox.showinfo("Acceso", "Acceso concedido.")
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    ventana = tk.Toplevel(root)
    ventana.title("Control de acceso")
    tk.Label(ventana, text="Nombre de usuario:").pack(pady=5)
    entry_usuario = tk.Entry(ventana)
    entry_usuario.pack(pady=5)
    tk.Label(ventana, text="Contraseña:").pack(pady=5)
    entry_contraseña = tk.Entry(ventana, show="*")
    entry_contraseña.pack(pady=5)
    tk.Button(ventana, text="Acceder", command=verificar_usuario).pack(pady=5)

# Ventana principal
root = tk.Tk()
root.title("Aplicación Multitareas")
root.geometry("400x600")

# Etiqueta de bienvenida
tk.Label(root, text="Seleccione una opción del menú:", font=("Arial", 14)).pack(pady=10)

# Crear botones para cada opción
tk.Button(root, text="1. Descuento en una tienda", command=descuento_tienda).pack(pady=5)
tk.Button(root, text="2. Edad para votar", command=edad_para_votar).pack(pady=5)
tk.Button(root, text="3. Mayor de tres números", command=mayor_de_tres_numeros).pack(pady=5)
tk.Button(root, text="4. Clasificación de edades", command=clasificacion_edades).pack(pady=5)
tk.Button(root, text="5. Calculadora básica", command=calculadora_basica).pack(pady=5)
tk.Button(root, text="6. Determinar año bisiesto", command=determinar_bisiesto).pack(pady=5)
tk.Button(root, text="7. Validar contraseña", command=validar_contraseña).pack(pady=5)
tk.Button(root, text="8. Juego de números", command=juego_de_numeros).pack(pady=5)
tk.Button(root, text="9. Calcular signo zodiacal", command=calcular_signo_zodiacal).pack(pady=5)
tk.Button(root, text="10. Sistema de calificaciones", command=sistema_de_calificaciones).pack(pady=5)
tk.Button(root, text="11. Control de acceso", command=control_de_acceso).pack(pady=5)

root.mainloop()

