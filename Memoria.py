
class Memoria:

    def __init__(self):
        self.nombre_usuario = None
        self.historial = []

    def guardar_nombre(self, nombre):
        self.nombre_usuario = nombre

    def obtener_nombre(self):
        return self.nombre_usuario

    def guardar_mensaje(self, usuario, mensaje):
        self.historial.append({
            "usuario": usuario,
            "mensaje": mensaje
        })

    def obtener_historial(self):
        return self.historial

    def mostrar_historial(self):

        if not self.historial:
            return "Todavía no hay mensajes registrados."

        resultado = "\n===== HISTORIAL DE CONVERSACION =====\n"

        for registro in self.historial:

            resultado += (
                f"{registro['usuario']}: "
                f"{registro['mensaje']}\n"
            )

        resultado += "=====================================\n"

        return resultado

    def limpiar_historial(self):
        self.historial.clear()
