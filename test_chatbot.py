
import unittest

from ProcesadorPLN import ProcesadorPLN
from GestorDialogo import GestorDialogo
from Memoria import Memoria
from EstructuraPLN import INTENCIONES, ENTIDADES


class PruebasChatbot(unittest.TestCase):

    def setUp(self):
        self.procesador = ProcesadorPLN()
        self.chatbot = GestorDialogo()
        self.memoria = Memoria()

    # Prueba de normalización
    def test_normalizar(self):
        resultado = self.procesador.normalizar("PROGRAMACIÓN")
        self.assertEqual(resultado, "programacion")

    # Prueba de identificación del nombre
    def test_extraer_nombre(self):
        resultado = self.procesador.analizar("Me llamo Axel")
        self.assertEqual(resultado, ("nombre", "Axel"))

    # Prueba de memoria del nombre
    def test_recordar_nombre(self):
        self.chatbot.responder("Me llamo Axel")
        respuesta = self.chatbot.responder("¿Cómo me llamo?")

        self.assertIn("Axel", respuesta)

    # Prueba del tema Python
    def test_consultar_python(self):
        intencion, dato = self.procesador.analizar(
            "¿Qué es Python?"
        )

        self.assertEqual(intencion, "python")

    # Prueba de bases de datos
    def test_bases_datos(self):
        intencion, dato = self.procesador.analizar(
            "Explícame las bases de datos"
        )

        self.assertEqual(intencion, "bases_datos")

    # Prueba de menú
    def test_menu(self):
        respuesta = self.chatbot.responder("menu")

        self.assertIn("MENU ACADEMICO", respuesta)

    # Prueba de historial
    def test_historial(self):
        self.chatbot.responder("Hola")
        respuesta = self.chatbot.responder("historial")

        self.assertIn("Usuario: Hola", respuesta)

    # Prueba de respuesta desconocida
    def test_fallback(self):
        intencion, dato = self.procesador.analizar(
            "¿Cuál es el color de mi camisa?"
        )

        self.assertEqual(intencion, "desconocido")

    # Prueba de despedida
    def test_despedida(self):
        self.chatbot.responder("salir")

        self.assertTrue(self.chatbot.finalizar)

    # Prueba de almacenamiento del historial
    def test_memoria(self):
        self.memoria.guardar_mensaje("Usuario", "Hola")

        historial = self.memoria.obtener_historial()

        self.assertEqual(len(historial), 1)
        self.assertEqual(historial[0]["mensaje"], "Hola")

    # ===== PRUEBAS DE LA ESTRUCTURA DE LENGUAJE NATURAL =====

    # 1. Verificar existencia de al menos 10 intenciones
    def test_minimo_10_intenciones(self):
        self.assertGreaterEqual(len(INTENCIONES), 10)

    # 2. Verificar existencia de al menos 20 frases por cada intención
    def test_minimo_20_frases_por_intencion(self):
        for nombre_intent, datos in INTENCIONES.items():
            frases = datos["frases"]
            self.assertGreaterEqual(
                len(frases),
                20,
                f"La intención {nombre_intent} tiene menos de 20 frases ({len(frases)})"
            )

    # 3. Verificar existencia de al menos 5 entidades principales
    def test_minimo_5_entidades(self):
        entidades_requeridas = ["asignatura", "docente", "tramite", "periodo", "estudiante"]
        for entidad in entidades_requeridas:
            self.assertIn(entidad, ENTIDADES)
        self.assertGreaterEqual(len(ENTIDADES), 5)

    # 4. Prueba de reconocimiento de las 10 intenciones
    def test_reconocimiento_10_intenciones(self):
        casos = [
            ("Buenos días", "Intent_Saludar"),
            ("Hasta luego nos vemos", "Intent_Despedir"),
            ("¿Dónde puedo ver mi horario de clases?", "Intent_Consultar_Horario"),
            ("¿Cuándo es el inicio de clases y el fin de semestre?", "Intent_Calendario_Academico"),
            ("Necesito una constancia de estudios en registro", "Intent_Requisitos_Tramites"),
            ("¿Dónde puedo consultar mis calificaciones y notas?", "Intent_Consultar_Notas"),
            ("¿Quién es el docente o profesor encargado?", "Intent_Info_Docente"),
            ("¿Cuáles son los requisitos para una beca estudiantil?", "Intent_Becas_Beneficios"),
            ("Necesito material de estudio y libros de la biblioteca", "Intent_Material_Estudio"),
            ("Ayúdame a entender este tema, tengo dudas sobre la lección", "Intent_Explicar_Tema"),
        ]

        for frase, intent_esperado in casos:
            intencion, _ = self.procesador.analizar(frase)
            self.assertEqual(
                intencion,
                intent_esperado,
                f"Fallo al reconocer '{frase}'. Esperado: {intent_esperado}, Obtenido: {intencion}"
            )

    # 5. Prueba de extracción de las 5 entidades
    def test_extraccion_5_entidades(self):
        consulta = (
            "Me llamo Axel y necesito solicitar una constancia de estudios "
            "con el profesor Carlos para el primer semestre en la materia de redes"
        )
        entidades = self.procesador.extraer_entidades(consulta)

        self.assertEqual(entidades["estudiante"], "Axel")
        self.assertEqual(entidades["tramite"], "constancia de estudios")
        self.assertEqual(entidades["docente"], "Carlos")
        self.assertEqual(entidades["periodo"], "primer semestre")
        self.assertEqual(entidades["asignatura"], "redes")

    # 6. Prueba de contextualización de respuesta con entidades en GestorDialogo
    def test_respuesta_contextualizada(self):
        chatbot = GestorDialogo()
        respuesta = chatbot.responder("¿Cuál es el trámite para matrícula?")
        self.assertIn("matricula", respuesta.lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
