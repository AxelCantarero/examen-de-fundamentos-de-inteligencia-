
import re
import unicodedata
from EstructuraPLN import INTENCIONES, ENTIDADES
from respuestas import RESPUESTAS


class ProcesadorPLN:

    def __init__(self):
        # Mapeo de temas técnicos de respuestas.py
        self.temas_tecnicos = {
            "bases_datos": [
                "bases de datos",
                "base de datos",
                "que es una base de datos",
                "que son las bases de datos"
            ],
            "python": [
                "python",
                "que es python",
                "lenguaje python"
            ],
            "java": [
                "java",
                "que es java",
                "lenguaje java"
            ],
            "algoritmos": [
                "algoritmo",
                "algoritmos",
                "que es un algoritmo",
                "que son los algoritmos"
            ],
            "programacion": [
                "programacion",
                "que es programacion",
                "que significa programar",
                "que es programar"
            ],
            "redes": [
                "redes informaticas",
                "redes",
                "que son las redes",
                "redes de computadoras"
            ],
            "seguridad": [
                "seguridad informatica",
                "que es seguridad informatica",
                "ciberseguridad"
            ],
            "sistemas_operativos": [
                "sistema operativo",
                "sistemas operativos",
                "que es un sistema operativo"
            ],
            "hardware": [
                "hardware",
                "que es hardware"
            ],
            "software": [
                "software",
                "que es software"
            ],
            "informatica": [
                "informatica",
                "que es informatica"
            ],
            "internet": [
                "internet",
                "que es internet"
            ]
        }

    def normalizar(self, texto):
        """
        Normaliza el texto convirtiéndolo a minúsculas y eliminando
        espacios excedentes y diacríticos/acentos.
        """
        texto = texto.lower().strip()
        texto = unicodedata.normalize("NFD", texto)
        texto = "".join(
            caracter
            for caracter in texto
            if unicodedata.category(caracter) != "Mn"
        )
        return texto

    def contiene_frase(self, texto, frases):
        """
        Verifica si alguna frase de la lista está presente en el texto
        respetando límites de palabra.
        """
        texto_norm = self.normalizar(texto)
        for frase in frases:
            frase_norm = self.normalizar(frase)
            patron = r"(?<!\w)" + re.escape(frase_norm) + r"(?!\w)"
            if re.search(patron, texto_norm):
                return True
        return False

    def extraer_nombre(self, texto):
        """
        Extrae el nombre de un usuario a partir de patrones comunes.
        Delimita el nombre si viene seguido de conectores como 'y', 'que', etc.
        """
        patrones = [
            r"(?:me llamo|mi nombre es)\s+([a-zA-ZáéíóúÁÉÍÓÚñÑ]+(?:\s+[a-zA-ZáéíóúÁÉÍÓÚñÑ]+)?)(?:\s+(?:y|que|con|para|en|\.|\,)|$)",
            r"soy\s+([a-zA-ZáéíóúÁÉÍÓÚñÑ]+)(?:\s+(?:y|que|con|para|en|\.|\,)|$)"
        ]

        for patron in patrones:
            resultado = re.search(patron, texto, re.IGNORECASE)
            if resultado:
                nombre = resultado.group(1).strip()
                palabras = nombre.split()
                conectores = {"para", "de", "del", "en", "con", "y", "que", "a", "por"}
                while len(palabras) > 1 and palabras[-1].lower() in conectores:
                    palabras.pop()
                nombre_limpio = " ".join(palabras).title()
                ignorar = ["un", "una", "el", "la", "estudiante", "alumno"]
                if nombre_limpio.lower() not in ignorar:
                    return nombre_limpio

        return None

    def extraer_entidades(self, texto):
        """
        Extrae las 5 entidades principales definidas en la estructura PLN:
        - asignatura: Asignatura o materia temática.
        - docente: Profesor o coordinador referenciado.
        - tramite: Trámite académico o gestión administrativa.
        - periodo: Período, semestre o fecha académica.
        - estudiante: Nombre o identificación del estudiante.
        """
        entidades = {
            "asignatura": None,
            "docente": None,
            "tramite": None,
            "periodo": None,
            "estudiante": None
        }

        texto_norm = self.normalizar(texto)

        # 1. Asignatura
        for val in ENTIDADES["asignatura"]["valores"]:
            val_norm = self.normalizar(val)
            patron = r"(?<!\w)" + re.escape(val_norm) + r"(?!\w)"
            if re.search(patron, texto_norm):
                entidades["asignatura"] = val
                break

        # 2. Docente
        patron_docente = ENTIDADES["docente"]["patron"]
        match_docente = re.search(patron_docente, texto, re.IGNORECASE)
        if match_docente:
            docente_raw = match_docente.group(1).strip()
            # Si dice "profesor de redes", la frase "de redes" califica asignatura
            if docente_raw.lower().startswith("de "):
                posible_materia = docente_raw[3:].strip().lower()
                if posible_materia in ENTIDADES["asignatura"]["valores"]:
                    entidades["asignatura"] = posible_materia
                    entidades["docente"] = "Profesor de Asignatura"
                else:
                    entidades["docente"] = docente_raw.title()
            else:
                palabras = docente_raw.split()
                conectores = {"para", "de", "del", "en", "con", "y", "que", "a", "por"}
                while len(palabras) > 1 and palabras[-1].lower() in conectores:
                    palabras.pop()
                entidades["docente"] = " ".join(palabras).title()
        else:
            for palabra in ENTIDADES["docente"]["palabras_clave"]:
                palabra_norm = self.normalizar(palabra)
                patron = r"(?<!\w)" + re.escape(palabra_norm) + r"(?!\w)"
                if re.search(patron, texto_norm):
                    entidades["docente"] = palabra.title()
                    break

        # 3. Trámite
        for val in ENTIDADES["tramite"]["valores"]:
            val_norm = self.normalizar(val)
            patron = r"(?<!\w)" + re.escape(val_norm) + r"(?!\w)"
            if re.search(patron, texto_norm):
                entidades["tramite"] = val
                break

        # 4. Período
        for val in ENTIDADES["periodo"]["valores"]:
            val_norm = self.normalizar(val)
            patron = r"(?<!\w)" + re.escape(val_norm) + r"(?!\w)"
            if re.search(patron, texto_norm):
                entidades["periodo"] = val
                break

        # 5. Estudiante
        nombre = self.extraer_nombre(texto)
        if nombre:
            entidades["estudiante"] = nombre

        return entidades

    def analizar(self, texto):
        """
        Determina la intención y posibles datos a partir del texto ingresado.
        Retorna: (intencion, dato)
        """
        texto_normalizado = self.normalizar(texto)

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

        # Agradecimiento
        if self.contiene_frase(texto_normalizado, [
            "gracias",
            "muchas gracias",
            "te agradezco"
        ]):
            return "agradecimiento", None

        # Ayuda
        if self.contiene_frase(texto_normalizado, [
            "ayuda",
            "necesito ayuda"
        ]):
            return "ayuda", None

        # Despedida (utiliza las frases definidas en EstructuraPLN)
        if self.contiene_frase(texto_normalizado, INTENCIONES["Intent_Despedir"]["frases"]):
            return "Intent_Despedir", None

        # Saludo (utiliza las frases definidas en EstructuraPLN)
        if self.contiene_frase(texto_normalizado, INTENCIONES["Intent_Saludar"]["frases"]):
            return "Intent_Saludar", None

        # Intenciones de orientación académica con vocabulario específico
        intenciones_academicas = [
            "Intent_Becas_Beneficios",
            "Intent_Consultar_Horario",
            "Intent_Calendario_Academico",
            "Intent_Consultar_Notas",
            "Intent_Info_Docente",
            "Intent_Material_Estudio",
            "Intent_Requisitos_Tramites"
        ]

        for intent_id in intenciones_academicas:
            if self.contiene_frase(texto_normalizado, INTENCIONES[intent_id]["frases"]):
                return intent_id, None

        # Temas técnicos específicos (prioritarios para respuestas directas de conceptos)
        for tema, frases in self.temas_tecnicos.items():
            if self.contiene_frase(texto_normalizado, frases):
                return tema, None

        # Explicar tema genérico
        if self.contiene_frase(texto_normalizado, INTENCIONES["Intent_Explicar_Tema"]["frases"]):
            return "Intent_Explicar_Tema", None

        return "desconocido", None

    def analizar_completo(self, texto):
        """
        Retorna el análisis completo en lenguaje natural incluyendo
        la intención detectada, el dato primario y las 5 entidades extraídas.
        """
        intencion, dato = self.analizar(texto)
        entidades = self.extraer_entidades(texto)
        return {
            "intencion": intencion,
            "dato": dato,
            "entidades": entidades
        }
