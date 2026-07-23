import os
import asyncio
import requests
from bs4 import BeautifulSoup
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not TELEGRAM_TOKEN or not CHAT_ID:
    raise ValueError("TELEGRAM_TOKEN ou CHAT_ID não foram encontrados no arquivo .env!")

URL_EVENTO = ""

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
}

async def notificar(texto):
    """Envia uma mensagem de texto para o Telegram."""
    bot = Bot(token=TELEGRAM_TOKEN)
    async with bot:
        await bot.send_message(
            chat_id=CHAT_ID, 
            text=texto, 
            parse_mode="Markdown"
        )

def checar_status():
    """Realiza a requisição na página e verifica disponibilidade."""
    try:
        response = requests.get(URL_EVENTO, headers=HEADERS, timeout=10)
        
        if response.status_code != 200:
            print(f"Erro ao acessar a página. Status code: {response.status_code}")
            return False

        conteudo_texto = response.text.lower()
        termos_esgotado = ["esgotado", "sold out", "não há ingressos disponíveis"]
        
        esta_esgotado = any(termo in conteudo_texto for termo in termos_esgotado)
        
        return not esta_esgotado

    except Exception as e:
        print(f"Exceção ao verificar status: {e}")
        return False

async def main():
    await notificar("bot de ingressos Iniciado!*\nMonitorando disponibilidade...")
    
    ja_notificou = False

    while True:
        tem_ingresso = checar_status()
        
        if tem_ingresso and not ja_notificou:
            mensagem = (
                "🚨 *INGRESSO DETECTADO!*\n\n"
                f"Parece que há disponibilidade para o evento do dia 30.\n"
                f"[Acessar Ticketmaster]({URL_EVENTO})"
            )
            await notificar(mensagem)
            ja_notificou = True
        elif not tem_ingresso:
            ja_notificou = False

        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())