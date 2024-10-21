from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states.states import Form
from keyboards import get_command_keyboard, get_navigation_keyboard, get_level_keyboard, get_course_action_keyboard
from services.cat_api import get_cat_image

router = Router()

courses = {
    "Программирование": {
        "junior": ["Курс A", "Курс B"],
        "middle": ["Курс C", "Курс D"],
        "senior": ["Курс E"]
    },
    "Аналитика": {
        "junior": ["Курс F", "Курс G"],
        "middle": ["Курс H"],
        "senior": ["Курс I", "Курс J"]
    },
    "Тестирование": {
        "junior": ["Курс K"],
        "middle": ["Курс L", "Курс M"],
        "senior": ["Курс N"]
    }
}


@router.message(Command("start"))
async def start_handler(message: types.Message, state: FSMContext):
    user_first_name = message.from_user.first_name
    await message.answer(f"Добро пожаловать, {user_first_name}! 🌟 Воспользуйтесь командами ниже.", reply_markup=get_command_keyboard())
    await state.clear()

@router.message(Command(commands=['help']))
async def help_handler(message: types.Message):
    help_text = (
        "Вот список доступных команд:\n\n"
        "/start - Начать работу с ботом\n"
        "/Обучение - Выбрать направление и уровень обучения\n"
        "/О нас - Узнать больше о нашем университете\n"
        "/Здесь котики - Получить картинку милого котика 🐱\n"
        "/help - Получить помощь и список команд\n\n"
        "Если у вас есть вопросы, не стесняйтесь обращаться к нам!"
    )
    await message.answer(help_text)

@router.message(lambda message: message.text == "Обучение")
async def level_handler(message: types.Message, state: FSMContext):
    await message.answer("Выберите направление обучения:", reply_markup=get_navigation_keyboard())
    await state.set_state(Form.CHOOSE_DIRECTION)

@router.message(lambda message: message.text == "О нас")
async def info_handler(message: types.Message):
    await message.answer("Добро пожаловать в наш университет. Мы предлагаем разнообразные курсы...")

@router.message(lambda message: message.text == "Здесь котики")
async def cat_handler(message: types.Message):
    cat_image_url = await get_cat_image()
    if cat_image_url:
        await message.answer_photo(photo=cat_image_url)
    else:
        await message.reply("Не удалось получить картинку котика, пожалуйста, попробуйте еще раз.")

@router.message(Form.CHOOSE_DIRECTION)
async def choose_direction_handler(message: types.Message, state: FSMContext):
    direction = message.text
    if direction not in courses:
        await message.answer("Выберите одно из направлений.", reply_markup=get_navigation_keyboard())
        return

    await state.update_data(direction=direction)
    await message.answer("Выберите уровень:", reply_markup=get_level_keyboard())
    await state.set_state(Form.CHOOSE_LEVEL)

@router.message(Form.CHOOSE_LEVEL)
async def choose_level_handler(message: types.Message, state: FSMContext):
    level = message.text.lower()

    if level == "назад":
        await message.answer("Выберите направление обучения:", reply_markup=get_navigation_keyboard())
        await state.set_state(Form.CHOOSE_DIRECTION)
        return

    user_data = await state.get_data()
    direction = user_data.get("direction")

    if level not in courses[direction]:
        await message.answer("Выберите один из уровней.", reply_markup=get_level_keyboard())
        return

    available_courses = courses[direction][level]
    course_list = "\n".join(available_courses)

    await message.answer(f"Доступные курсы:\n{course_list}", reply_markup=get_course_action_keyboard())
    await state.set_state(Form.COURSE_ACTION)

@router.message(Form.COURSE_ACTION)
async def course_action_handler(message: types.Message, state: FSMContext):
    action = message.text
    if action == "Записаться":
        await message.answer("Вы успешно записаны на курс!", reply_markup=get_command_keyboard())
        await state.clear()
    elif action == "Назад":
        await message.answer("Выберите направление обучения:", reply_markup=get_navigation_keyboard())
        await state.set_state(Form.CHOOSE_DIRECTION)
    else:
        await message.answer("Пожалуйста, используйте кнопки на экране.")
