class SesionEstudio:

    def __init__(
        self,
        id_sesion,
        materia,
        actividad,
        fecha,
        duracion,
        concentracion
    ):

        self.id_sesion = id_sesion
        self.materia = materia
        self.actividad = actividad
        self.fecha = fecha
        self.duracion = duracion
        self.concentracion = concentracion

    def calcular_productividad(self):

        return (
            self.duracion
            *
            self.concentracion
        )