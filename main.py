import asyncio
import time
from telegram import Bot

TELEGRAM_TOKEN = "SEU_TOKEN_AQUI"
CHAT_ID = "SEU_CHAT_ID_AQUI"

async def notificar(texto):
    bot = Bot(token=TELEGRAM_TOKEN)
    async with bot:
        await bot.send_message(chat_id=CHAT_ID, text=texto, parse_mode="Markdown")

def checar_status():
    return True

async def main():
    await notificar("iniciado com sucesso!")
    
    while True:
        alerta = checar_status()
        
        if alerta:
            await notificar("ingresso detectado")

        await asyncio.sleep(300)

if __name__ == "__main__":
    asyncio.run(main())