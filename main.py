
from GestorDialogo import GestorDialogo


def iniciar_chatbot():

    chatbot = GestorDialogo()

    print("\n" + "=" * 50)
    print("       CHATBOT DE ASISTENCIA ACADEMICA")
    print("=" * 50)

    print("\nChatbot: ¡Bienvenido!")
    print("Chatbot: Soy tu asistente académico.")
    print("Chatbot: Puedes escribir 'menu' para ver las opciones.")
    print("Chatbot: Escribe 'salir' para finalizar.\n")

    while not chatbot.finalizar:

        try:

            mensaje = input("Usuario: ").strip()

            if not mensaje:

                print(
                    "\nChatbot: Por favor, escribe un mensaje.\n"
                )

                continue

            respuesta = chatbot.responder(mensaje)

            print(f"\nChatbot: {respuesta}\n")

        except KeyboardInterrupt:

            print("\n\nChatbot: Conversación interrumpida.")
            break

        except Exception as error:

            print("\nChatbot: Ocurrió un error inesperado.")
            print("Detalle:", error)


if __name__ == "__main__":
    iniciar_chatbot()
