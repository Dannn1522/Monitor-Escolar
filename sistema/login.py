class Login:

    def __init__(self):

        self.usuario = ""

    def iniciar_sesion(self):

        print("========== BIENVENIDO/A AL GESTOR DE ESTUDIO ==========")

        self.usuario = input(
            "Ingresa tu nombre: "
        )

        print(
            f"\nHola {self.usuario}, "
            f"bienvenido/a al sistema.\n"
        )
