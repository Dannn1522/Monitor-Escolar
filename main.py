from sistema.login import Login

from modelos.materia import Materia
from modelos.actividad import Actividad
from modelos.sesion import SesionEstudio

from servicios.analizador import Analizador
from servicios.recomendacion import Recomendacion


# MENU

def mostrar_menu():

    print("\n========== MENU ==========")

    print("1. Registrar materias")
    print("2. Registrar sesiones")
    print("3. Ver analisis")
    print("4. Ver recomendaciones")
    print("5. Salir")


# LOGIN

login = Login()
login.iniciar_sesion()


# LISTAS

materias = []
sesiones = []


# OBJETOS

analizador = Analizador()
recomendador = Recomendacion()


# CICLO PRINCIPAL

while True:

    mostrar_menu()

    opcion = input(
        "\nSeleccione una opcion: "
    )


    # REGISTRAR MATERIAS

    if opcion == "1":

        try:

            cantidad = int(
                input(
                    "\nCuantas materias desea agregar: "
                )
            )

        except:

            print(
                "\n Debes ingresar un numero."
            )

            continue


        for i in range(cantidad):

            nombre = input(
                f"Nombre de la materia #{i+1}: "
            )

            materia = Materia(
                i + 1,
                nombre
            )

            materias.append(materia)

            print(
                "✅ Materia registrada correctamente."
            )


    # REGISTRAR SESIONES

    elif opcion == "2":

        if len(materias) == 0:

            print(
                "\n Opcion invalida."
            )

            print(
                "⚠️ Primero debes registrar materias."
            )

        else:

            print("\n========== MATERIAS ==========")

            for materia in materias:

                print(
                    materia.id_materia,
                    "-",
                    materia.nombre
                )

            try:

                id_materia = int(
                    input(
                        "\nSeleccione materia: "
                    )
                )

            except:

                print(
                    "\n Debes ingresar un numero."
                )

                continue


            if id_materia < 1 or id_materia > len(materias):

                print(
                    "\n Materia invalida."
                )

                continue


            materia_seleccionada = (
                materias[id_materia - 1]
            )

            actividad_nombre = input(
                "Actividad: "
            )

            actividad = Actividad(
                1,
                actividad_nombre
            )

            fecha = input(
                "Fecha: "
            )

            try:

                duracion = int(
                    input(
                        "Duracion en minutos: "
                    )
                )

                concentracion = int(
                    input(
                        "Concentracion (1-10): "
                    )
                )

            except:

                print(
                    "\n Debes ingresar numeros validos."
                )

                continue


            sesion = SesionEstudio(
                len(sesiones) + 1,
                materia_seleccionada,
                actividad,
                fecha,
                duracion,
                concentracion
            )

            sesiones.append(sesion)

            print(
                "\n✅ Sesion registrada correctamente."
            )


    # ANALISIS

    elif opcion == "3":

        if len(sesiones) == 0:

            print(
                "\n No hay sesiones registradas."
            )

        else:

            promedio = (
                analizador
                .calcular_promedio_productividad(
                    sesiones
                )
            )

            print(
                "\n========== ANALISIS =========="
            )

            print(
                " PROMEDIO GENERAL:",
                round(promedio, 1)
            )

            t_total, t_efectivo, t_perdido = (
                analizador
                .calcular_balance_tiempo(
                    sesiones
                )
            )

            print(
                "⏰ Tiempo total:",
                t_total
            )

            print(
                " Tiempo efectivo:",
                round(t_efectivo, 1)
            )

            print(
                " Tiempo perdido:",
                round(t_perdido, 1)
            )

            mejor = (
                analizador
                .mejor_sesion(
                    sesiones
                )
            )

            print(
                " Mejor sesion:",
                mejor.materia.nombre
            )

            datos = (
                analizador
                .productividad_por_materia(
                    sesiones
                )
            )

            print(
                "\n PRODUCTIVIDAD POR MATERIA:"
            )

            for materia, valor in datos.items():

                print(
                    "➡️",
                    materia,
                    ":",
                    valor
                )


    # RECOMENDACIONES

    elif opcion == "4":

        recomendaciones = (
            recomendador
            .generar_recomendaciones(
                sesiones,
                analizador
            )
        )

        print("\n========== RECOMENDACIONES ==========")

        for r in recomendaciones:

            print("-", r)


    # SALIR

    elif opcion == "5":

        print(
            "\n👋 Gracias por usar el sistema."
        )

        print(
            " Nunca dejes de aprender."
        )

        break


    # ERROR

    else:

        print(
            "\n ERROR: Opcion invalida."
        )