import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Alumno:
    def __init__(self, ci, apellidos, nombre, nota):
        self.ci = ci
        self.apellidos = apellidos
        self.nombre = nombre
        self.nota = nota
        self.calificacion = self.calcular_calificacion()

    def calcular_calificacion(self):
        if self.nota < 5:
            return "SS"
        elif 5 <= self.nota < 7:
            return "AP"
        elif 7 <= self.nota < 9:
            return "NT"
        elif self.nota >= 9:
            return "SB"

class GestorCalificaciones:
    def __init__(self, root):
        self.alumnos = {}
        self.root = root
        self.root.title("Organizacion de calificaciones")
        self.root.geometry("800x600")
        self.root.configure(bg="#80BFFF")  # Fondo turquesa
        self.crear_interfaz()

    def crear_interfaz(self):
        frame_botones = tk.Frame(self.root, bg="#80BFFF")  # Fondo turquesa en el frame
        frame_botones.pack(pady=5)

        botones = [
            ("Mostrar alumnos", self.mostrar_alumnos),
            ("Introducir alumno", self.introducir_alumno),
            ("Eliminar alumno", self.eliminar_alumno),
            ("Consultar alumno", self.consultar_alumno),
            ("Modificar nota", self.modificar_nota),
            ("Suspensos", self.mostrar_suspensos),
            ("Aprobados", self.mostrar_aprobados),
            ("Candidatos a MH", self.mostrar_candidatos),
        ]

        for i, (texto, comando) in enumerate(botones):
            # Botones con fondo negro, texto blanco y tipografía Times New Roman
            tk.Button(frame_botones, text=texto, command=comando, width=20, height=1, font=("Times New Roman", 12), 
                      bg="black", fg="white").grid(row=i // 3, column=i % 3, padx=5, pady=5)

        # Frame para la tabla
        self.frame_tabla = tk.Frame(self.root, bg="#80BFFF")  # Fondo turquesa en el frame
        self.frame_tabla.pack(pady=5)

        self.tabla = ttk.Treeview(self.frame_tabla, columns=("ci", "apellidos", "nombres", "nota", "calificacion"), show="headings")
        self.tabla.heading("ci", text="CI")
        self.tabla.heading("apellidos", text="APELLIDOS")
        self.tabla.heading("nombres", text="NOMBRES")
        self.tabla.heading("nota", text="NOTA")
        self.tabla.heading("calificacion", text="CALIFICACION")

        self.tabla.column("ci", width=120, anchor="center")
        self.tabla.column("apellidos", width=180, anchor="center")
        self.tabla.column("nombres", width=180, anchor="center")
        self.tabla.column("nota", width=60, anchor="center")
        self.tabla.column("calificacion", width=100, anchor="center")

        self.tabla.pack()

    def limpiar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

    def mostrar_alumnos(self):
        self.limpiar_tabla()
        if not self.alumnos:
            messagebox.showinfo("Información", "No hay alumnos registrados.")
            return
        alumnos_ordenados = sorted(self.alumnos.values(), key=lambda a: a.ci)
        for alumno in alumnos_ordenados:
            self.tabla.insert("", tk.END, values=(alumno.ci, alumno.apellidos, alumno.nombre, f"{alumno.nota:.1f}", alumno.calificacion))

    def validar_datos(self, ci, apellidos, nombre, nota):
        if not ci.isdigit() or len(ci) != 10:
            return "El CI debe ser un número de 10 dígitos."
        if not apellidos.replace(" ", "").isalpha() or len(apellidos) > 24:
            return "Los apellidos deben contener solo letras y máximo 24 caracteres."
        if not nombre.replace(" ", "").isalpha() or len(nombre) > 24:
            return "El nombre debe contener solo letras y máximo 24 caracteres."
        try:
            nota = float(nota)
            if nota < 1 or nota > 10:
                return "La nota debe estar entre 1 y 10."
        except ValueError:
            return "La nota debe ser un número válido entre 1 y 10."
        return None

    def introducir_alumno(self):
        def guardar():
            ci, apellidos, nombre, nota = entry_ci.get(), entry_apellidos.get(), entry_nombre.get(), entry_nota.get()
            error = self.validar_datos(ci, apellidos, nombre, nota)
            if error:
                messagebox.showerror("Error", error)
            else:
                nota = float(nota)
                self.alumnos[ci] = Alumno(ci, apellidos, nombre, nota)
                messagebox.showinfo("Éxito", "Alumno añadido correctamente.")
                ventana.destroy()
                self.mostrar_alumnos()

        ventana = tk.Toplevel(self.root)
        ventana.title("Introducir Alumno")
        ventana.geometry("300x200")

        tk.Label(ventana, text="CI:").grid(row=0, column=0, pady=5)
        tk.Label(ventana, text="Apellidos:").grid(row=1, column=0, pady=5)
        tk.Label(ventana, text="Nombre:").grid(row=2, column=0, pady=5)
        tk.Label(ventana, text="Nota:").grid(row=3, column=0, pady=5)

        entry_ci = tk.Entry(ventana)
        entry_apellidos = tk.Entry(ventana)
        entry_nombre = tk.Entry(ventana)
        entry_nota = tk.Entry(ventana)

        entry_ci.grid(row=0, column=1)
        entry_apellidos.grid(row=1, column=1)
        entry_nombre.grid(row=2, column=1)
        entry_nota.grid(row=3, column=1)

        tk.Button(ventana, text="Guardar", command=guardar, bg="black", fg="white", font=("Times New Roman", 12)).grid(row=4, columnspan=2, pady=10)

    def eliminar_alumno(self):
        def eliminar():
            ci = entry_ci.get()
            if ci in self.alumnos:
                del self.alumnos[ci]
                messagebox.showinfo("Éxito", "Alumno eliminado.")
                ventana.destroy()
                self.mostrar_alumnos()
            else:
                messagebox.showerror("Error", "No existe un alumno con ese CI.")

        ventana = tk.Toplevel(self.root)
        ventana.title("Eliminar Alumno")
        ventana.geometry("300x100")

        tk.Label(ventana, text="CI:").grid(row=0, column=0, pady=5)
        entry_ci = tk.Entry(ventana)
        entry_ci.grid(row=0, column=1)
        tk.Button(ventana, text="Eliminar", command=eliminar, bg="black", fg="white", font=("Times New Roman", 12)).grid(row=1, columnspan=2, pady=10)

    def consultar_alumno(self):
        def consultar():
            ci = entry_ci.get()
            alumno = self.alumnos.get(ci)
            if alumno:
                messagebox.showinfo("Información del Alumno", f"CI: {alumno.ci}\nApellidos: {alumno.apellidos}\nNombre: {alumno.nombre}\nNota: {alumno.nota:.1f}\nCalificación: {alumno.calificacion}")
            else:
                messagebox.showerror("Error", "No existe un alumno con ese CI.")

        ventana = tk.Toplevel(self.root)
        ventana.title("Consultar Alumno")
        ventana.geometry("300x100")

        tk.Label(ventana, text="CI:").grid(row=0, column=0, pady=5)
        entry_ci = tk.Entry(ventana)
        entry_ci.grid(row=0, column=1)
        tk.Button(ventana, text="Consultar", command=consultar, bg="black", fg="white", font=("Times New Roman", 12)).grid(row=1, columnspan=2, pady=10)

    def modificar_nota(self):
        def modificar():
            ci = entry_ci.get()
            nueva_nota = entry_nota.get()
            alumno = self.alumnos.get(ci)
            if alumno:
                # No se valida el CI, ya que estamos modificando el alumno existente
                try:
                    nueva_nota = float(nueva_nota)
                    if 1 <= nueva_nota <= 10:
                        alumno.nota = nueva_nota
                        alumno.calificacion = alumno.calcular_calificacion()
                        messagebox.showinfo("Éxito", "Nota modificada correctamente.")
                        ventana.destroy()
                        self.mostrar_alumnos()
                    else:
                        messagebox.showerror("Error", "La nota debe estar entre 1 y 10.")
                except ValueError:
                    messagebox.showerror("Error", "La nota debe ser un número válido.")
            else:
                messagebox.showerror("Error", "No existe un alumno con ese CI.")

        ventana = tk.Toplevel(self.root)
        ventana.title("Modificar Nota")
        ventana.geometry("300x150")

        tk.Label(ventana, text="CI:").grid(row=0, column=0, pady=5)
        tk.Label(ventana, text="Nueva Nota:").grid(row=1, column=0, pady=5)

        entry_ci = tk.Entry(ventana)
        entry_nota = tk.Entry(ventana)

        entry_ci.grid(row=0, column=1)
        entry_nota.grid(row=1, column=1)

        tk.Button(ventana, text="Modificar", command=modificar, bg="black", fg="white", font=("Times New Roman", 12)).grid(row=2, columnspan=2, pady=10)

    def mostrar_suspensos(self):
        self.limpiar_tabla()
        suspensos = [a for a in self.alumnos.values() if a.nota < 7]
        if not suspensos:
            messagebox.showinfo("Información", "No hay suspensos.")
        for alumno in suspensos:
            self.tabla.insert("", tk.END, values=(alumno.ci, alumno.apellidos, alumno.nombre, f"{alumno.nota:.1f}", alumno.calificacion))

    def mostrar_aprobados(self):
        self.limpiar_tabla()
        aprobados = [a for a in self.alumnos.values() if a.nota >= 7]
        if not aprobados:
            messagebox.showinfo("Información", "No hay aprobados.")
        for alumno in aprobados:
            self.tabla.insert("", tk.END, values=(alumno.ci, alumno.apellidos, alumno.nombre, f"{alumno.nota:.1f}", alumno.calificacion))

    def mostrar_candidatos(self):
        self.limpiar_tabla()
        candidatos = [a for a in self.alumnos.values() if a.nota == 10]
        if not candidatos:
            messagebox.showinfo("Información", "No hay candidatos a MH.")
        for alumno in candidatos:
            self.tabla.insert("", tk.END, values=(alumno.ci, alumno.apellidos, alumno.nombre, f"{alumno.nota:.1f}", alumno.calificacion))


if __name__ == "__main__":
    root = tk.Tk()
    gestor = GestorCalificaciones(root)
    root.mainloop()
