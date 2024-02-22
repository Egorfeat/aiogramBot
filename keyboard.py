from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButtonPollType
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="random-number"),
            KeyboardButton(text='Смайлики')
        ],
        [
            KeyboardButton(text='Калькулятор'),
            KeyboardButton(text='Спец.Кнопки'),
            KeyboardButton(text='Ссылки')
        ]
    ],
    # Позволяет изменить размер кнопки
    resize_keyboard=True,
    #Клавиатура будет скрыватся после первого использования
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    #Для чатов.Кнопки появляются у того кто вызвал бота
    selective=True
)

links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="GitHub", url="https://github.com/Egorfeat" ),
            InlineKeyboardButton(text="Telegram", url="tg://resolve?domain=Eg0rfeat" )
        ]
    ]
)

spec_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отправить гео', request_location=True),
            KeyboardButton(text='Отправить контакт', request_contact=True),
            KeyboardButton(text='Создать Викторину', request_poll=KeyboardButtonPollType())
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)


def calc_kb():
    items = [
        '1', '2', '3', '/',
        '4', '5', '6', '*',
        '7', '8', '9', '-',
        '0', '.', '=', '+',
    ]

    builder = ReplyKeyboardBuilder()
    # [builder.button(text=item) for item in items]
    for item in items:
        builder.button(text=item)
    builder.button(text='Назад')
    builder.adjust(4, 4, 4, 4, )

    return builder.as_markup(resize_keyboard = True)