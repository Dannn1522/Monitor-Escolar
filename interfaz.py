# interfaz.py

from tkinter import *
from tkinter import messagebox

from modelos.materia import Materia
from modelos.actividad import Actividad
from modelos.sesion import SesionEstudio

from servicios.analizador import Analizador
from servicios.recomendacion import Recomendacion


# LISTAS

materias = []
sesiones = []


# OBJETOS

analizador = Analizador()
recomendador = Recomendacion()


# FUNCION REGISTRAR MATERIA

def registrar_materia():

    nombre = entry_materia.get()

    if nombre == "":

        messagebox.showerror(
            "Error",
            "Ingrese una materia"
        )

        return

    materia = Materia(
        len(materias) + 1,
        nombre
    )

    materias.append(materia)

    lista_materias.insert(
        END,
        nombre
    )

    entry_materia.delete(0, END)

    messagebox.showinfo(
        "Correcto",
        "Materia registrada correctamente"
    )


# FUNCION REGISTRAR SESION

def registrar_sesion():

    if len(materias) == 0:

        messagebox.showerror(
            "Error",
            "Primero registre materias"
        )

        return

    try:

        materia_index = (
            lista_materias.curselection()[0]
        )

        materia = materias[materia_index]

        actividad_nombre = (
            entry_actividad.get()
        )

        fecha = entry_fecha.get()

        duracion = int(
            entry_duracion.get()
        )

        concentracion = int(
            entry_concentracion.get()
        )

        actividad = Actividad(
            1,
            actividad_nombre
        )

        sesion = SesionEstudio(
            len(sesiones) + 1,
            materia,
            actividad,
            fecha,
            duracion,
            concentracion
        )

        sesiones.append(sesion)

        messagebox.showinfo(
            "Correcto",
            "Sesion registrada correctamente"
        )

        entry_actividad.delete(0, END)
        entry_fecha.delete(0, END)
        entry_duracion.delete(0, END)
        entry_concentracion.delete(0, END)

    except:

        messagebox.showerror(
            "Error",
            "Ingrese datos validos"
        )


# FUNCION ANALISIS

def ver_analisis():

    if len(sesiones) == 0:

        messagebox.showwarning(
            "Aviso",
            "No hay sesiones registradas"
        )

        return

    promedio = (
        analizador
        .calcular_promedio_productividad(
            sesiones
        )
    )

    t_total, t_efectivo, t_perdido = (
        analizador
        .calcular_balance_tiempo(
            sesiones
        )
    )

    mejor = (
        analizador
        .mejor_sesion(
            sesiones
        )
    )

    texto = (
        f"PROMEDIO: {round(promedio,1)}\n\n"
        f"TIEMPO TOTAL: {t_total}\n"
        f"TIEMPO EFECTIVO: {round(t_efectivo,1)}\n"
        f"TIEMPO PERDIDO: {round(t_perdido,1)}\n\n"
        f"MEJOR SESION: {mejor.materia.nombre}"
    )

    messagebox.showinfo(
        "Analisis",
        texto
    )


# FUNCION RECOMENDACIONES

def ver_recomendaciones():

    recomendaciones = (
        recomendador
        .generar_recomendaciones(
            sesiones,
            analizador
        )
    )

    texto = ""

    for r in recomendaciones:

        texto += f"• {r}\n\n"

    messagebox.showinfo(
        "Recomendaciones",
        texto
    )


# VENTANA

ventana = Tk()

ventana.title(
    "Sistema de Estudio"
)

ventana.geometry(
    "700x600"
)

ventana.config(
    bg="#dbeafe"
)


# TITULO

titulo = Label(
    ventana,
    text="SISTEMA DE PRODUCTIVIDAD",
    font=("Arial", 18, "bold"),
    bg="#dbeafe"
)

titulo.pack(pady=10)


# FRAME MATERIAS

frame_materia = Frame(
    ventana,
    bg="#dbeafe"
)

frame_materia.pack(pady=10)

Label(
    frame_materia,
    text="Materia:",
    bg="#dbeafe"
).grid(row=0, column=0)

entry_materia = Entry(
    frame_materia
)

entry_materia.grid(row=0, column=1)

Button(
    frame_materia,
    text="Registrar Materia",
    command=registrar_materia,
    bg="#60a5fa"
).grid(row=0, column=2, padx=10)


# LISTA MATERIAS

lista_materias = Listbox(
    ventana,
    width=40,
    height=5
)

lista_materias.pack()


# FRAME SESIONES

frame_sesion = Frame(
    ventana,
    bg="#dbeafe"
)

frame_sesion.pack(pady=20)

Label(
    frame_sesion,
    text="Actividad:",
    bg="#dbeafe"
).grid(row=0, column=0)

entry_actividad = Entry(
    frame_sesion
)

entry_actividad.grid(row=0, column=1)

Label(
    frame_sesion,
    text="Fecha:",
    bg="#dbeafe"
).grid(row=1, column=0)

entry_fecha = Entry(
    frame_sesion
)

entry_fecha.grid(row=1, column=1)

Label(
    frame_sesion,
    text="Duracion:",
    bg="#dbeafe"
).grid(row=2, column=0)

entry_duracion = Entry(
    frame_sesion
)

entry_duracion.grid(row=2, column=1)

Label(
    frame_sesion,
    text="Concentracion:",
    bg="#dbeafe"
).grid(row=3, column=0)

entry_concentracion = Entry(
    frame_sesion
)

entry_concentracion.grid(row=3, column=1)

Button(
    frame_sesion,
    text="Registrar Sesion",
    command=registrar_sesion,
    bg="#34d399"
).grid(row=4, column=0, columnspan=2, pady=10)


# BOTONES

Button(
    ventana,
    text="Ver Analisis",
    command=ver_analisis,
    width=20,
    bg="#fbbf24"
).pack(pady=5)

Button(
    ventana,
    text="Ver Recomendaciones",
    command=ver_recomendaciones,
    width=20,
    bg="#f87171"
).pack(pady=5)


# EJECUTAR

ventana.mainloop()