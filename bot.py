import asyncio
import os
import aiohttp
from dotenv import load_dotenv
from openai import AsyncOpenAI
from pydantic import BaseModel, Field

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MY_TELEGRAM_CHAT_ID = os.getenv("MY_TELEGRAM_CHAT_ID") # Ваш личный Telegram ID

openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)

# --- RSS Фиды для поиска вакансий ---
# DOU и Djinni предоставляют публичные RSS-ленты по фильтрам QA Automation
JOBS_RSS_FEEDS = [
    "https://jobs.dou.ua/vacancies/feeds/?category=QA",
    "https://djinni.co/jobs/rss/?primary_keyword=QA+Automation",
    "https://djinni.co/jobs/rss/?primary_keyword=QA+Lead",
    "https://djinni.co/jobs/rss/?primary_keyword=SDET"
]

class JobFilterResult(BaseModel):
    is_relevant: bool = Field(description="Подходит ли под Senior AQA / SDET / QA Lead")
    match_score: int
    role_title: str
    cover_letter: str = Field(description="Сопроводительное письмо на английском")

async def send_telegram_notification(text: str):
    """Отправка сообщения в ваш Telegram через Bot API."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    async with aiohttp.ClientSession() as session:
        await session.post(url, json={
            "chat_id": MY_TELEGRAM_CHAT_ID,
            "text": text,
            "parse_mode": "HTML"
        })

async def run_job_search():
    """Основной цикл авто-поиска."""
    print("🔎 Запуск авто-поиска новых вакансий...")
    # Здесь подключается RSS-парсер (feedparser) или Selenium/Playwright для LinkedIn
    # При обнаружении новой вакансии вызывается аналитик OpenAI и отправляется уведомление
    
    # Пример вызова отправки:
    # await send_telegram_notification("🎯 Найдена новая вакансия...")

if __name__ == "__main__":
    asyncio.run(run_job_search())