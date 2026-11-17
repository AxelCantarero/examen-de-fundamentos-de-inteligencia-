
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

    def obtener_respuesta(self, intencion):

        return self.informacion.get(
            intencion,
            self.informacion["desconocido"]
        )
