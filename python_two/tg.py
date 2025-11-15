from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import random

bot = Bot(token="8236571950:AAHwpy_mAxs_DGjldUBf7loibwLJK2fc05w")
dp = Dispatcher()

# Упражнения для памяти
exercises = [
    "🔢 Запомни последовательность: 7 2 9 4 1 (через 10 секунд скажи)",
    "🔄 Повтори в обратном порядке: кошка-солнце-река-книга",
    "🎯 Запомни расположение: A B C\nD E F\nG H I (где была буква E?)",
    "📚 Прочитай и воспроизведи: 'Быстрая коричневая лиса прыгает через ленивую собаку'",
    "🔡 Запомни цифры: 35972 (повтори через 15 секунд)"
]

@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="🎯 Новое упражнение")],
            [types.KeyboardButton(text="📊 Статистика")],
            [types.KeyboardButton(text="💡 Советы")]
        ],
        resize_keyboard=True
    )
    await message.answer(
        "Тренируй память! Выбери опцию:",
        reply_markup=keyboard
    )

@dp.message(lambda message: message.text == "🎯 Новое упражнение")
async def new_exercise(message: types.Message):
    exercise = random.choice(exercises)
    await message.answer(f"🎯 Упражнение:\n\n{exercise}")

@dp.message(lambda message: message.text == "📊 Статистика")
async def stats(message: types.Message):
    await message.answer("📊 Ты выполнил 12 упражнений\n🔥 Текущая серия: 3 дня подряд")

@dp.message(lambda message: message.text == "💡 Советы")
async def tips(message: types.Message):
    await message.answer("💡 Советы по тренировке памяти:\n• Занимайся регулярно\n• Используй ассоциации\n• Повторяй через интервалы")

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))