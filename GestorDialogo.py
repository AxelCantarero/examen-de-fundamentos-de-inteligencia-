
from Memoria import Memoria
from ProcesadorPLN import ProcesadorPLN
from BaseConocimiento import BaseConocimiento
from respuestas import RESPUESTAS


class GestorDialogo:

    def __init__(self):

        self.memoria = Memoria()
        self.procesador = ProcesadorPLN()
        self.base_conocimiento = BaseConocimiento()
        self.finalizar = False

    def responder(self, mensaje):

        self.memoria.guardar_mensaje(
            "Usuario",
            mensaje
        )

        intencion, dato = self.procesador.analizar(mensaje)

        # Registrar nombre
        if intencion == "nombre":

            self.memoria.guardar_nombre(dato)

            respuesta = (
                f"¡Mucho gusto, {dato}! "
                "¿En qué puedo ayudarte?"
            )

        # Consultar nombre
        elif intencion == "consultar_nombre":

            nombre = self.memoria.obtener_nombre()

            if nombre:

                respuesta = f"Tu nombre es {nombre}."

            else:

                respuesta = (
                    "Todavía no me has indicado tu nombre. "
                    "Puedes decirme: Me llamo [tu nombre]."
                )

        # Consultar identidad
        elif intencion == "identidad":

            respuesta = RESPUESTAS.get(
                "identidad",
                "Soy AcademIA, tu asistente académico."
            )

        # Mostrar menú
        elif intencion == "menu":

            respuesta = RESPUESTAS.get(
                "menu",
                "Puedes consultar temas académicos y orientación universitaria."
            )

        # Consultar historial
        elif intencion == "historial":

            historial = self.memoria.obtener_historial()

            if historial:

                respuesta = self.memoria.mostrar_historial()

            else:

                respuesta = "Todavía no hay mensajes registrados."

        # Despedida
        elif intencion in ["despedida", "Intent_Despedir"]:

            nombre = self.memoria.obtener_nombre()

            if nombre:

                respuesta = (
                    f"¡Hasta pronto, {nombre}! "
                    "Gracias por utilizar AcademIA."
                )

            else:

                respuesta = self.base_conocimiento.obtener_respuesta(
                    "Intent_Despedir"
                )

            self.finalizar = True

        # Saludo
        elif intencion == "Intent_Saludar":

            nombre = self.memoria.obtener_nombre()

            if nombre:

                respuesta = (
                    f"¡Hola nuevamente, {nombre}! "
                    "¿En qué puedo orientarte?"
                )

            else:

                respuesta = self.base_conocimiento.obtener_respuesta(
                    intencion
                )

        # Consultas de temas originales y respuestas existentes
        elif intencion in RESPUESTAS:

            respuesta = RESPUESTAS[intencion]

        # Nuevas consultas de orientación académica
        else:

            respuesta = self.base_conocimiento.obtener_respuesta(
                intencion
            )

        # Guardar respuesta del chatbot
        self.memoria.guardar_mensaje(
            "Chatbot",
            respuesta
        )

        return respuesta
