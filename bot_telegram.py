import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from GestorDialogo import GestorDialogo

# Configurar registro básico en consola
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Diccionario para mantener una sesión/memoria independiente por cada usuario
sesiones_usuarios: dict[int, GestorDialogo] = {}

def obtener_gestor(chat_id: int) -> GestorDialogo:
    if chat_id not in sesiones_usuarios:
        sesiones_usuarios[chat_id] = GestorDialogo()
    return sesiones_usuarios[chat_id]

async def comando_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    # Reinicia o crea la sesión del estudiante al iniciar
    sesiones_usuarios[chat_id] = GestorDialogo()
    bienvenida = (
        "¡Hola! Soy *AcademIA*, tu asistente de orientación académica del CUR Las Minas de URACCAN.\n\n"
        "Puedes preguntarme sobre horarios, matrícula, becas, docentes o calendario académico."
    )
    await update.message.reply_text(bienvenida, parse_mode="Markdown")

async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    texto_usuario = update.message.text.strip()

    gestor = obtener_gestor(chat_id)
    respuesta = gestor.responder(texto_usuario)

    await update.message.reply_text(respuesta)

    # Si el usuario se despidió (ej. "salir", "adiós"), limpiamos su sesión
    if getattr(gestor, "finalizar", False):
        sesiones_usuarios.pop(chat_id, None)

def main() -> None:
    TOKEN = "9280072208:AAEY0mAU2lPLXObb0s_bhfVwDZqPgNEaBBM"

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", comando_start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))

    print("Bot AcademIA activo en Telegram. Presiona Ctrl+C para detener.")
    app.run_polling()

if __name__ == "__main__":
    main()