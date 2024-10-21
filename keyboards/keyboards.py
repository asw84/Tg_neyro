from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_command_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Обучение"),
                KeyboardButton(text="О нас"),
                KeyboardButton(text="Здесь котики")
            ]
        ],
        resize_keyboard=True,
    )


def get_navigation_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Программирование"), KeyboardButton(text="Аналитика"), KeyboardButton(text="Тестирование")]
        ],
        resize_keyboard=True
    )

def get_level_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="junior"), KeyboardButton(text="middle"), KeyboardButton(text="senior")],
            [KeyboardButton(text="Назад")]
        ],
        resize_keyboard=True
    )

def get_course_action_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Записаться"), KeyboardButton(text="Назад")]
        ],
        resize_keyboard=True
    )