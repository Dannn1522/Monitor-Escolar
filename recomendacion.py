class Recomendacion:


    def generar_recomendaciones(
        self,
        sesiones,
        analizador
    ):

        if len(sesiones) == 0:

            return [
                " Aun no tienes sesiones registradas.",
                " Empieza a registrar tus sesiones y descubre como mejorar academicamente."
            ]

        recomendaciones = []

        promedio = (
            analizador
            .calcular_promedio_productividad(
                sesiones
            )
        )


        # RECOMENDACIONES GENERALES

        if promedio < 200:

            recomendaciones.append(
                " Tu rendimiento actual puede mejorar bastante."
            )

            recomendaciones.append(
                " Intenta leer mas sobre los temas que se te dificultan."
            )

            recomendaciones.append(
                " Ver videos educativos puede ayudarte a entender mejor los conceptos."
            )

            recomendaciones.append(
                " Realiza resumenes o mapas mentales para reforzar el aprendizaje."
            )

            recomendaciones.append(
                " Estudiar con amigos puede ayudarte a resolver dudas mas rapido."
            )

            recomendaciones.append(
                " Divide tus sesiones en bloques pequenos para evitar el cansancio."
            )


        elif promedio >= 200 and promedio < 500:

            recomendaciones.append(
                " Estas avanzando correctamente."
            )

            recomendaciones.append(
                " Sigue practicando ejercicios para fortalecer tus conocimientos."
            )

            recomendaciones.append(
                " Puedes probar nuevas tecnicas como Pomodoro o flashcards."
            )

            recomendaciones.append(
                " Complementa tus estudios con videos y tutoriales interactivos."
            )

            recomendaciones.append(
                " Explicar los temas a otras personas puede ayudarte a aprender mejor."
            )


        else:

            recomendaciones.append(
                " Excelente rendimiento academico."
            )

            recomendaciones.append(
                " Tus habitos de estudio estan dando muy buenos resultados."
            )

            recomendaciones.append(
                " Sigue manteniendo constancia y disciplina."
            )

            recomendaciones.append(
                " Puedes comenzar a profundizar en temas mas avanzados."
            )

            recomendaciones.append(
                " Comparte tus tecnicas de estudio con otros estudiantes."
            )


        # RECOMENDACIONES SEGUN CONCENTRACION

        for sesion in sesiones:

            if sesion.concentracion < 5:

                recomendaciones.append(
                    f" En {sesion.materia.nombre} "
                    f"tu nivel de concentracion fue bajo."
                )

                recomendaciones.append(
                    " Alejate del celular o redes sociales mientras estudias."
                )

                recomendaciones.append(
                    " Intenta usar musica relajante o ambientes silenciosos."
                )

                recomendaciones.append(
                    " Descansa unos minutos entre sesiones largas."
                )

                break


        # MENSAJE FINAL

        recomendaciones.append(
            " Cada esfuerzo que haces hoy te acerca mas a tus metas."
        )

        recomendaciones.append(
            " La disciplina y la constancia son la clave del exito academico."
        )

        return recomendaciones