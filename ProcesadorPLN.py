
import re
import unicodedata


class ProcesadorPLN:

    def normalizar(self, texto):

        texto = texto.lower().strip()

        texto = unicodedata.normalize("NFD", texto)

        texto = "".join(
            caracter for caracter in texto
            if unicodedata.category(caracter) != "Mn"
        )

        return texto

    def contiene_frase(self, texto, frases):

        for frase in frases:

            patron = (
                r"(?<!\w)" +
                re.escape(frase) +
                r"(?!\w)"
            )

            if re.search(patron, texto):
                return True

        return False

    def extraer_nombre(self, texto):

        patron = (
            r"^\s*(?:hola[, ]+)?"
            r"(?:me llamo|mi nombre es)\s+"
            r"([\w]+(?:\s+[\w]+){0,2})"
            r"\s*[.!?]*\s*$"
        )

        resultado = re.search(
            patron,
            texto,
            re.IGNORECASE
        )

        if resultado:
            nombre = resultado.group(1).strip()
            return nombre.title()

        return None

    def analizar(self, texto):

        mensaje = self.normalizar(texto)

        # Opciones numéricas del menú
        opciones = {
            "1": "python",
            "2": "programacion",
            "3": "informatica",
            "4": "bases_datos",
            "5": "redes",
            "6": "seguridad",
            "7": "sistemas_operativos",
            "8": "hardware",
            "9": "ayuda",
            "10": "historial",
            "0": "despedida"
        }

        if mensaje in opciones:
            return opciones[mensaje], None

        # Consultar el nombre del usuario
        if self.contiene_frase(mensaje, [
            "como me llamo",
            "cual es mi nombre",
            "recuerdas mi nombre",
            "sabes mi nombre"
        ]):
            return "consultar_nombre", None

        # Identificar al chatbot
        if self.contiene_frase(mensaje, [
            "como te llamas",
            "quien eres",
            "que eres"
        ]):
            return "identidad", None

        # Reconocer cuando el usuario proporciona su nombre
        nombre = self.extraer_nombre(texto)

        if nombre:
            return "nombre", nombre

        # Despedidas
        if self.contiene_frase(mensaje, [
            "adios",
            "hasta luego",
            "nos vemos",
            "salir",
            "terminar"
        ]):
            return "despedida", None

        # Agradecimientos
        if self.contiene_frase(mensaje, [
            "gracias",
            "muchas gracias",
            "te agradezco"
        ]):
            return "agradecimiento", None

        # Saludos
        if self.contiene_frase(mensaje, [
            "hola",
            "buenos dias",
            "buenas tardes",
            "buenas noches",
            "hey"
        ]):
            return "saludo", None

        # Menú e historial
        if self.contiene_frase(mensaje, [
            "menu",
            "mostrar opciones",
            "ver opciones"
        ]):
            return "menu", None

      # Consultar historial
        if self.contiene_frase(mensaje, [
            "historial",
            "ver historial",
            "mostrar historial",
            "ver conversacion",
            "mostrar conversacion",
            "mis mensajes",
            "mensajes anteriores"
        ]):
            return "historial", None

        # Temas académicos
        temas = {

            "python": [
                "python",
                "lenguaje python"
            ],

            "programacion": [
                "programacion",
                "programar",
                "codigo fuente"
            ],

            "informatica": [
                "informatica",
                "computacion"
            ],

            "java": [
                "java",
                "lenguaje java"
            ],

            "algoritmos": [
                "algoritmo",
                "algoritmos"
            ],

            "bases_datos": [
                "base de datos",
                "bases de datos",
                "mysql",
                "postgresql",
                "sql server"
            ],

            "redes": [
                "redes",
                "red informatica",
                "redes informaticas",
                "lan",
                "wan",
                "wlan"
            ],

            "hardware": [
                "hardware",
                "memoria ram",
                "procesador",
                "placa madre"
            ],

            "software": [
                "software",
                "programas informaticos"
            ],

            "seguridad": [
                "seguridad informatica",
                "ciberseguridad",
                "virus informatico"
            ],

            "sistemas_operativos": [
                "sistema operativo",
                "sistemas operativos",
                "windows",
                "linux",
                "android"
            ],

            "internet": [
                "internet",
                "red mundial"
            ],

            "horario": [
                "horario",
                "clases",
                "asignaturas"
            ]
        }

        for intencion, palabras in temas.items():

            if self.contiene_frase(mensaje, palabras):
                return intencion, None

        # Ayuda
        if self.contiene_frase(mensaje, [
            "ayuda",
            "que puedes hacer",
            "opciones disponibles"
        ]):
            return "ayuda", None

        return "desconocido", None
