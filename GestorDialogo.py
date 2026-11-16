
from Memoria import Memoria
from ProcesadorPLN import ProcesadorPLN
from respuestas import RESPUESTAS


class GestorDialogo:

    def __init__(self):

        self.memoria = Memoria()
        self.procesador = ProcesadorPLN()
        self.finalizar = False

    def responder(self, mensaje):

        self.memoria.guardar_mensaje(
            "Usuario",
            mensaje
        )

        intencion, dato = self.procesador.analizar(mensaje)

        # Guardar nombre
        if intencion == "nombre":

            self.memoria.guardar_nombre(dato)

            respuesta = (
                f"¡Mucho gusto, {dato}! "
                "Ya recuerdo tu nombre. ¿En qué puedo ayudarte?"
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

            respuesta = RESPUESTAS["identidad"]

        # Mostrar menú
        elif intencion == "menu":

            respuesta = RESPUESTAS["menu"]

        # Mostrar historial
        elif intencion == "historial":

            historial = self.memoria.obtener_historial()

            if historial:
               respuesta = self.memoria.mostrar_historial()
            else:
               respuesta = "Todavía no hay mensajes registrados."

        # Despedida
        elif intencion == "despedida":

            nombre = self.memoria.obtener_nombre()

            if nombre:
                respuesta = (
                    f"¡Hasta pronto, {nombre}! "
                    "Gracias por utilizar el chatbot académico."
                )

            else:
                respuesta = RESPUESTAS["despedida"]

            self.finalizar = True

        # Saludos personalizados
        elif intencion == "saludo":

            nombre = self.memoria.obtener_nombre()

            if nombre:
                respuesta = f"¡Hola nuevamente, {nombre}!"

            else:
                respuesta = RESPUESTAS["saludo"]

        # Respuestas académicas y fallback
        else:

            respuesta = RESPUESTAS.get(
                intencion,
                RESPUESTAS["desconocido"]
            )

        self.memoria.guardar_mensaje(
            "Chatbot",
            respuesta
        )

        return respuesta
