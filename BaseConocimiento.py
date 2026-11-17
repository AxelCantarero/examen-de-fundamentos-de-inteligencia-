
class BaseConocimiento:

    def __init__(self):

        self.informacion = {

            "Intent_Saludar": (
                "¡Hola! Soy AcademIA, tu asistente de orientación "
                "académica del CUR Las Minas de URACCAN. "
                "¿En qué puedo ayudarte?"
            ),

            "Intent_Consultar_Horario": (
                "Para consultar tu horario de clases, revisa los "
                "canales oficiales de comunicación del CUR Las Minas "
                "o consulta con la coordinación de tu carrera. "
                "Así podrás obtener el horario actualizado de tus "
                "asignaturas."
            ),

            "Intent_Calendario_Academico": (
                "Para conocer las fechas de inicio y finalización "
                "de clases, matrículas, evaluaciones y otras "
                "actividades, consulta el calendario académico "
                "oficial de URACCAN o solicita información en "
                "el CUR Las Minas."
            ),

            "Intent_Requisitos_Tramites": (
                "Para realizar trámites relacionados con matrícula, "
                "inscripción, constancias, retiros de asignaturas "
                "o documentos académicos, consulta en Registro "
                "Académico del CUR Las Minas. Los requisitos pueden "
                "variar según el trámite, por lo que debes "
                "confirmarlos antes de realizarlo."
            ),

            "Intent_Consultar_Notas": (
                "Puedes consultar tus calificaciones e historial "
                "académico mediante el Portal Estudiantil de URACCAN. "
                "Si tienes problemas para ingresar o encuentras "
                "algún error en tus notas, solicita ayuda en "
                "Registro Académico del CUR Las Minas."
            ),

            "Intent_Info_Docente": (
                "Si necesitas información sobre un docente, "
                "sus asignaturas o cómo comunicarte con él, "
                "puedes consultar con la coordinación de tu carrera "
                "en el CUR Las Minas."
            ),

            "Intent_Becas_Beneficios": (
                "Para recibir información sobre becas y beneficios "
                "estudiantiles, debes dirigirte al área de Bienestar "
                "Estudiantil del CUR Las Minas. Allí puedes consultar "
                "los tipos de becas disponibles, sus requisitos y "
                "los períodos de solicitud. Recuerda que las "
                "convocatorias tienen fechas establecidas."
            ),

            "Intent_Material_Estudio": (
                "Si necesitas libros, documentos o recursos "
                "académicos, puedes consultar los servicios de "
                "Biblioteca de URACCAN. También puedes preguntar "
                "a tu docente por los materiales correspondientes "
                "a la asignatura."
            ),

            "Intent_Explicar_Tema": (
                "¡Claro! Puedo ayudarte a comprender temas "
                "académicos, explicarte conceptos y desarrollar "
                "ejemplos. Dime qué tema o asignatura necesitas "
                "estudiar."
            ),

            "Intent_Despedir": (
                "¡Hasta pronto! Gracias por utilizar AcademIA. "
                "Muchos éxitos en tus estudios."
            ),

            "desconocido": (
                "No logré comprender tu consulta. Puedes preguntarme "
                "sobre horarios, calendario académico, trámites, "
                "notas, docentes, becas, materiales de estudio "
                "o temas académicos."
            )
        }

    def obtener_respuesta(self, intencion, entidades=None):
        """
        Retorna la respuesta para una intención dada. Si se proporcionan
        entidades extraídas, contextualiza la respuesta dinámicamente.
        """
        if entidades:
            if intencion == "Intent_Consultar_Horario" and entidades.get("asignatura"):
                asig = entidades["asignatura"].title()
                return (
                    f"Para consultar el horario específico de la asignatura '{asig}', "
                    "revisa los canales oficiales del CUR Las Minas o consulta con "
                    "la coordinación de tu carrera."
                )

            if intencion == "Intent_Requisitos_Tramites" and entidades.get("tramite"):
                tram = entidades["tramite"].title()
                return (
                    f"Para el trámite de '{tram}', debes dirigirte a Registro Académico "
                    "del CUR Las Minas con tus documentos en regla y verificar los "
                    "requisitos y fechas habilitadas."
                )

            if intencion == "Intent_Info_Docente":
                if entidades.get("asignatura"):
                    asig = entidades["asignatura"].title()
                    return (
                        f"Para consultar información sobre el docente a cargo de la asignatura "
                        f"'{asig}', dirígete a la coordinación de tu carrera en el CUR Las Minas."
                    )
                if entidades.get("docente"):
                    doc = entidades["docente"].title()
                    return (
                        f"Para comunicarte con {doc}, consulta los horarios de atención "
                        "y datos de contacto en la coordinación de carrera del CUR Las Minas."
                    )

            if intencion == "Intent_Calendario_Academico" and entidades.get("periodo"):
                per = entidades["periodo"].title()
                return (
                    f"Respecto a las fechas para '{per}', puedes verificar el cronograma "
                    "oficial en el calendario académico de URACCAN o en Registro Académico."
                )

            if intencion == "Intent_Material_Estudio" and entidades.get("asignatura"):
                asig = entidades["asignatura"].title()
                return (
                    f"Para acceder a bibliografía y materiales de '{asig}', puedes consultar "
                    "la Biblioteca de URACCAN o solicitar la guía didáctica a tu docente."
                )

        return self.informacion.get(
            intencion,
            self.informacion["desconocido"]
        )
