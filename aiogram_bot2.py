import asyncio
import random
import keyboard

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject

# Включаем логирование, чтобы не пропустить важные сообщения

# Объект бота
bot = Bot(token=, parse_mode="HTML")

# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command ("start"))
async def start(message: Message):
    await message.answer(f"Hello, <b>{message.from_user.first_name}</b>", reply_markup=keyboard.main_kb)

@dp.message(Command (commands = ['rn',"random-number"])) # / 1-100
async def get_random_number(message: Message, command: CommandObject):
    a, b = [int(n) for n in command.args.split('-')]
    rnum = random.randint(a, b)

    await message.reply(f"Random number: {rnum}")

@dp.message()
async def echo(message: Message):
    msg = message.text.lower()

    if msg == 'ссылки':
        await message.answer("Вот ваши ссылки:", reply_markup=keyboard.links_kb)
    elif msg == 'спец.кнопки':
        await message.answer('Спец.Кнопки:', reply_markup=keyboard.spec_kb)
    elif msg == 'калькулятор':
        await message.answer("Введите выражение:", reply_markup=keyboard.calc_kb())

@dp.message()
async def echo(message: Message):
    await message.answer(f"Я не понимаю тебя!")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())