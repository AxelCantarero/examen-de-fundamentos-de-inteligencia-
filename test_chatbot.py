
import unittest

from ProcesadorPLN import ProcesadorPLN
from GestorDialogo import GestorDialogo
from Memoria import Memoria


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


        


if __name__ == "__main__":
    unittest.main(verbosity=2)
