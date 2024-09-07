import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

# Archivo donde se almacenará la agenda
archivo_agenda = "agenda.txt"

# Función para agendar un turno y guardarlo en el archivo
def agendar_turno(nombre, apellido, dni, fecha, hora):
    with open(archivo_agenda, "a") as archivo:
        archivo.write(f"{nombre},{apellido},{dni},{fecha},{hora}\n")
    messagebox.showinfo("Agendar Turno", f"Turno agendado para {nombre} {apellido}, DNI: {dni} el {fecha} a las {hora}")

# Función para leer la agenda desde el archivo
def leer_agenda():
    agenda = {}
    try:
        with open(archivo_agenda, "r") as archivo:
            for linea in archivo:
                nombre, apellido, dni, fecha, hora = linea.strip().split(",")
                if fecha not in agenda:
                    agenda[fecha] = []
                agenda[fecha].append(f"{hora} - {nombre} {apellido} (DNI: {dni})")
    except FileNotFoundError:
        pass
    return agenda

# Función para mostrar los turnos ocupados
def mostrar_turnos_ocupados():
    agenda = leer_agenda()
    ocupados_texto = ""
    for fecha, horas in agenda.items():
        ocupados_texto += f"Fecha: {fecha}\n"
        for hora in horas:
            ocupados_texto += f"    {hora}\n"
    messagebox.showinfo("Turnos Ocupados", ocupados_texto if ocupados_texto else "No hay turnos ocupados")

# Función para mostrar los turnos disponibles en un rango de horarios
def mostrar_turnos_disponibles():
    fecha = entry_fecha.get()
    hora_inicio = entry_hora_inicio.get()
    hora_fin = entry_hora_fin.get()

    if not fecha or not hora_inicio or not hora_fin:
        messagebox.showwarning("Error", "Por favor, completa todos los campos.")
        return

    agenda = leer_agenda()
    horarios_ocupados = [turno.split(" - ")[0] for turno in agenda.get(fecha, [])]  # Solo tomamos las horas
    horario_actual = datetime.strptime(hora_inicio, "%H:%M")
    fin = datetime.strptime(hora_fin, "%H:%M")

    disponibles_texto = f"Horarios disponibles para el {fecha}:\n"
    
    while horario_actual < fin:
        hora_str = horario_actual.strftime("%H:%M")
        if hora_str not in horarios_ocupados:
            disponibles_texto += f"{hora_str} (disponible)\n"
        else:
            disponibles_texto += f"{hora_str} (ocupado)\n"
        horario_actual += timedelta(minutes=30)

    messagebox.showinfo("Turnos Disponibles", disponibles_texto)

# Función para agendar un turno desde la interfaz gráfica
def agendar_turno_interfaz():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    dni = entry_dni.get()
    fecha = entry_fecha.get()
    hora = entry_hora.get()

    if not nombre or not apellido or not dni or not fecha or not hora:
        messagebox.showwarning("Error", "Por favor, completa todos los campos.")
        return

    agendar_turno(nombre, apellido, dni, fecha, hora)

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda de Turnos")

# Configurar color de fondo (celeste)
root.configure(bg="lightblue")

# Texto de fondo
label_fondo = tk.Label(root, text="ODONTOLOGIA ROZZANO", font=("Arial", 35), fg="black", bg="lightblue")
label_fondo.place(x=20, y=20)  # Puedes ajustar la posición del texto según el diseño que quieras
label_fondo = tk.Label(root, text="🦷", font=("Arial", 100), fg="black", bg="lightblue")
label_fondo.place(x=200, y=100)  # Puedes ajustar la posición del texto según el diseño que quieras


# Etiquetas y entradas para nombre, apellido y DNI
label_nombre = tk.Label(root, text="Nombre:", bg="lightblue",font=45)
label_nombre.pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

label_apellido = tk.Label(root, text="Apellido:", bg="lightblue",font=45)
label_apellido.pack()
entry_apellido = tk.Entry(root)
entry_apellido.pack()

label_dni = tk.Label(root, text="DNI:", bg="lightblue",font=45)
label_dni.pack()
entry_dni = tk.Entry(root)
entry_dni.pack()

# Etiquetas y entradas para la fecha y hora
label_fecha = tk.Label(root, text="Fecha (YYYY-MM-DD):", bg="lightblue",font=45)
label_fecha.pack()
entry_fecha = tk.Entry(root)
entry_fecha.pack()

label_hora = tk.Label(root, text="Hora (HH:MM):", bg="lightblue",font=45)
label_hora.pack()
entry_hora = tk.Entry(root)
entry_hora.pack()

# Botón para agendar un turno
btn_agendar = tk.Button(root, text="Agendar Turno", command=agendar_turno_interfaz,font=45)
btn_agendar.pack(pady=10)

# Etiquetas y entradas para el rango de horarios (disponibles)
label_hora_inicio = tk.Label(root, text="Hora Inicio (HH:MM):", bg="lightblue",font=45)
label_hora_inicio.pack()
entry_hora_inicio = tk.Entry(root)
entry_hora_inicio.pack()

label_hora_fin = tk.Label(root, text="Hora Fin (HH:MM):", bg="lightblue",font=45)
label_hora_fin.pack()
entry_hora_fin = tk.Entry(root)
entry_hora_fin.pack()

# Botón para mostrar turnos disponibles
btn_disponibles = tk.Button(root, text="Mostrar Turnos Disponibles", command=mostrar_turnos_disponibles,font=45)
btn_disponibles.pack(pady=10)

# Botón para mostrar turnos ocupados
btn_ocupados = tk.Button(root, text="Mostrar Turnos Ocupados", command=mostrar_turnos_ocupados,font=45)
btn_ocupados.pack(pady=10)

# Iniciar el bucle principal de tkinter
root.mainloop()



