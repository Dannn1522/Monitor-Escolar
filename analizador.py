class Analizador:


    # PROMEDIO GENERAL

    def calcular_promedio_productividad(
        self,
        sesiones
    ):

        if len(sesiones) == 0:

            return 0

        suma = 0

        for sesion in sesiones:

            suma += (
                sesion
                .calcular_productividad()
            )

        promedio = (
            suma / len(sesiones)
        )

        return promedio


    # MEJOR SESION

    def mejor_sesion(
        self,
        sesiones
    ):

        if len(sesiones) == 0:

            return None

        mejor = sesiones[0]

        for sesion in sesiones:

            if (
                sesion.calcular_productividad()
                >
                mejor.calcular_productividad()
            ):

                mejor = sesion

        return mejor


    # PRODUCTIVIDAD POR MATERIA

    def productividad_por_materia(
        self,
        sesiones
    ):

        resultados = {}

        for sesion in sesiones:

            nombre = (
                sesion.materia.nombre
            )

            productividad = (
                sesion
                .calcular_productividad()
            )

            if nombre not in resultados:

                resultados[nombre] = 0

            resultados[nombre] += productividad

        return resultados


    # BALANCE DE TIEMPO

    def calcular_balance_tiempo(
        self,
        sesiones
    ):

        tiempo_total = 0
        tiempo_efectivo = 0

        for sesion in sesiones:

            tiempo_total += (
                sesion.duracion
            )

            tiempo_efectivo += (
                sesion.duracion
                *
                (
                    sesion.concentracion / 10
                )
            )

        tiempo_perdido = (
            tiempo_total
            -
            tiempo_efectivo
        )

        return (
            tiempo_total,
            tiempo_efectivo,
            tiempo_perdido
        )
