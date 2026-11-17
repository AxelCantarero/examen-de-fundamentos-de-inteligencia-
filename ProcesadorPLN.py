
import re
import unicodedata


class ProcesadorPLN:

    def normalizar(self, texto):

        texto = texto.lower().strip()

        texto = unicodedata.normalize("NFD", texto)

        texto = "".join(
            caracter
            for caracter in texto
            if unicodedata.category(caracter) != "Mn"
        )

        return texto

    def contiene_frase(self, texto, frases):

        for frase in frases:

            frase = self.normalizar(frase)

            patron = (
                r"(?<!\w)"
                + re.escape(frase)
                + r"(?!\w)"
            )

            if re.search(patron, texto):
                return True

        return False

    def extraer_nombre(self, texto):

        patrones = [
            r"me llamo\s+([a-zA-ZáéíóúÁÉÍÓÚñÑ ]+)",
            r"mi nombre es\s+([a-zA-ZáéíóúÁÉÍÓÚñÑ ]+)"
        ]

        for patron in patrones:

            resultado = re.search(
                patron,
                texto,
                re.IGNORECASE
            )

            if resultado:
                return resultado.group(1).strip().title()

        return None

    def analizar(self, texto):

        texto_normalizado = self.normalizar(texto)

        # Opciones del menú numérico
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

        if texto_normalizado in opciones:
            return opciones[texto_normalizado], None

        # Registrar nombre
        if self.contiene_frase(texto_normalizado, [
            "me llamo",
            "mi nombre es"
        ]):

            nombre = self.extraer_nombre(texto)

            if nombre:
                return "nombre", nombre

        # Consultar nombre
        if self.contiene_frase(texto_normalizado, [
            "como me llamo",
            "recuerdas mi nombre",
            "cual es mi nombre"
        ]):
            return "consultar_nombre", None

        # Identidad
        if self.contiene_frase(texto_normalizado, [
            "quien eres",
            "que eres",
            "como te llamas",
            "que es academia"
        ]):
            return "identidad", None

        # Menú
        if self.contiene_frase(texto_normalizado, [
            "menu",
            "mostrar menu",
            "opciones disponibles",
            "que puedes hacer"
        ]):
            return "menu", None

        # Historial
        if self.contiene_frase(texto_normalizado, [
            "historial",
            "ver historial",
            "mis consultas anteriores"
        ]):
            return "historial", None

        # Despedida
        if self.contiene_frase(texto_normalizado, [
            "adios",
            "hasta luego",
            "nos vemos",
            "me despido",
            "hasta pronto",
            "chao"
        ]):
            return "Intent_Despedir", None

        # Saludo
        if self.contiene_frase(texto_normalizado, [
            "hola",
            "buenos dias",
            "buenas tardes",
            "buenas noches",
            "que tal",
            "hey"
        ]):
            return "Intent_Saludar", None

        # Consultar horario
        if self.contiene_frase(texto_normalizado, [
            "horario",
            "horarios de clases",
            "horario de clases",
            "cuando tengo clases",
            "a que hora tengo clases",
            "horario de asignaturas"
        ]):
            return "Intent_Consultar_Horario", None

        # Calendario académico
        if self.contiene_frase(texto_normalizado, [
            "calendario academico",
            "calendario universitario",
            "fechas del semestre",
            "inicio de clases",
            "fin de semestre",
            "periodo academico",
            "cuando comienzan las clases"
        ]):
            return "Intent_Calendario_Academico", None

        # Requisitos y trámites
        if self.contiene_frase(texto_normalizado, [
            "requisitos",
            "tramites",
            "matricula",
            "prematricula",
            "inscripcion",
            "retirar una asignatura",
            "constancia de estudios",
            "certificado de notas",
            "registro academico",
            "donde hago un tramite"
        ]):
            return "Intent_Requisitos_Tramites", None

        # Consultar notas
        if self.contiene_frase(texto_normalizado, [
            "notas",
            "calificaciones",
            "consultar notas",
            "ver mis notas",
            "mis calificaciones",
            "record academico",
            "resultados de evaluacion"
        ]):
            return "Intent_Consultar_Notas", None

        # Información de docentes
        if self.contiene_frase(texto_normalizado, [
            "docente",
            "profesor",
            "profesora",
            "informacion del docente",
            "contactar a un profesor",
            "quien imparte la asignatura",
            "docentes de mi carrera"
        ]):
            return "Intent_Info_Docente", None

        # Becas y beneficios
        if self.contiene_frase(texto_normalizado, [
            "beca",
            "becas",
            "beneficios estudiantiles",
            "ayuda economica",
            "solicitar una beca",
            "requisitos para una beca",
            "apoyo estudiantil"
        ]):
            return "Intent_Becas_Beneficios", None

        # Material de estudio
        if self.contiene_frase(texto_normalizado, [
            "material de estudio",
            "materiales de estudio",
            "biblioteca",
            "libros",
            "documentos de estudio",
            "recursos educativos",
            "material de una asignatura",
            "donde encuentro material"
        ]):
            return "Intent_Material_Estudio", None

        # Explicar un tema
        if self.contiene_frase(texto_normalizado, [
            "explicame",
            "explicar un tema",
            "no entiendo",
            "ayudame a entender",
            "tengo dudas sobre",
            "necesito ayuda con un tema"
        ]):
            return "Intent_Explicar_Tema", None

        # Temas originales del chatbot

        # Python
        if self.contiene_frase(texto_normalizado, [
            "python",
            "que es python",
            "lenguaje python"
        ]):
            return "python", None

        # Programación
        if self.contiene_frase(texto_normalizado, [
            "programacion",
            "que es programacion",
            "que significa programar",
            "que es programar"
        ]):
            return "programacion", None

        # Informática
        if self.contiene_frase(texto_normalizado, [
            "informatica",
            "que es informatica"
        ]):
            return "informatica", None

        # Java
        if self.contiene_frase(texto_normalizado, [
            "java",
            "que es java",
            "lenguaje java"
        ]):
            return "java", None

        # Algoritmos
        if self.contiene_frase(texto_normalizado, [
            "algoritmo",
            "algoritmos",
            "que es un algoritmo"
        ]):
            return "algoritmos", None

        # Bases de datos
        if self.contiene_frase(texto_normalizado, [
            "bases de datos",
            "base de datos",
            "que es una base de datos"
        ]):
            return "bases_datos", None

        # Redes
        if self.contiene_frase(texto_normalizado, [
            "redes",
            "redes informaticas",
            "que son las redes"
        ]):
            return "redes", None

        # Hardware
        if self.contiene_frase(texto_normalizado, [
            "hardware",
            "que es hardware"
        ]):
            return "hardware", None

        # Software
        if self.contiene_frase(texto_normalizado, [
            "software",
            "que es software"
        ]):
            return "software", None

        # Seguridad informática
        if self.contiene_frase(texto_normalizado, [
            "seguridad informatica",
            "que es seguridad informatica"
        ]):
            return "seguridad", None

        # Sistemas operativos
        if self.contiene_frase(texto_normalizado, [
            "sistema operativo",
            "sistemas operativos",
            "que es un sistema operativo"
        ]):
            return "sistemas_operativos", None

        # Internet
        if self.contiene_frase(texto_normalizado, [
            "internet",
            "que es internet"
        ]):
            return "internet", None

        # Ayuda
        if self.contiene_frase(texto_normalizado, [
            "ayuda",
            "necesito ayuda"
        ]):
            return "ayuda", None

        # Agradecimiento
        if self.contiene_frase(texto_normalizado, [
            "gracias",
            "muchas gracias",
            "te agradezco"
        ]):
            return "agradecimiento", None

        return "desconocido", None
