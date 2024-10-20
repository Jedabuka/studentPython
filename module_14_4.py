from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import get_all_products
import asyncio
import sqlite3


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
kb.insert(button1).resize_keyboard = True
kb.insert(button2).resize_keyboard = True
kb.add(button3).resize_keyboard = True

kb2 = InlineKeyboardMarkup()
in_button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
in_button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb2.insert(in_button1)
kb2.insert(in_button2)

kb3 = InlineKeyboardMarkup(row_width=4)
in_button3 = InlineKeyboardButton(text='Персик', callback_data='product_buying')
in_button4 = InlineKeyboardButton(text='Гранат', callback_data='product_buying')
in_button5 = InlineKeyboardButton(text='Манго', callback_data='product_buying')
in_button6 = InlineKeyboardButton(text='Ананас', callback_data='product_buying')
kb3.insert(in_button3).resize_keyboard = True
kb3.insert(in_button4).resize_keyboard = True
kb3.insert(in_button5).resize_keyboard = True
kb3.insert(in_button6).resize_keyboard = True

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    male = State()
    activity = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я помогу тебе узнать твою суточную норму калорий', reply_markup=kb)


@dp.message_handler(text='Информация')
async def set_info(message):
    await message.answer('Версия 0.1.2\n'
                         'Aвтор: Евгений Геннадьевич Лаптев\n'
                         'Мой телеграм: @EvgenLap')


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    res = get_all_products()
    with open('picture/persik1.webp', 'rb') as per:
        await message.answer_photo(per, f'Название: {res[0][0]} | Описание: {res[0][1]} | Цена: {res[0][2]}')
    with open('picture/granat2.jpg', 'rb') as gran:
        await message.answer_photo(gran, f'Название: {res[1][0]} | Описание: {res[1][1]} | Цена: {res[1][2]}')
    with open('picture/mango3.jpg', 'rb') as man:
        await message.answer_photo(man, f'Название: {res[2][0]} | Описание: {res[2][1]} | Цена: {res[2][2]}')
    with open('picture/ananas4.jpg', 'rb') as an:
        await message.answer_photo(an, f'Название: {res[3][0]} | Описание: {res[3][1]} | Цена: {res[3][2]}')
    await message.answer('Выберите продукт для покупки:', reply_markup=kb3)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: (10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (г) + 5) x A\n'
                              'для женщин: (10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (г) – 161) x A\n'
                              '\n'
                              'A – это уровень активности человека, его различают обычно по пяти\n'
                              'степеням физических нагрузок в сутки:\n'
                              '\n'
                              '•  Минимальная активность: A = 1,2.\n'
                              '•  Слабая активность: A = 1,375.\n'
                              '•  Средняя активность: A = 1,55.\n'
                              '•  Высокая активность: A = 1,725.\n'
                              '•  Экстра-активность: A = 1,9 (под эту категорию обычно подпадают люди,\n'
                              'занимающиеся, например, тяжелой атлетикой, или другими силовыми\n'
                              'видами спорта с ежедневными тренировками, а также те, кто\n'
                              'выполняет тяжелую физическую\n'
                              'работу).\n'
                              )
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст (полных лет):')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост (в см):')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес (в кг):')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_male(message, state):
    await state.update_data(weight=message.text)
    await message.answer('Какой у вас пол "м" или "ж"?:')
    await UserState.male.set()


@dp.message_handler(state=UserState.male)
async def set_activity(message, state):
    await state.update_data(male=message.text)
    await message.answer('Как вы оцениваете свою активность?\n'
                         '\n'
                         'A – это уровень активности человека, его различают обычно по пяти\n'
                         'степеням физических нагрузок в сутки:\n'
                         '\n'
                         '•  Минимальная активность: A = 1,2.\n'
                         '•  Слабая активность: A = 1,375.\n'
                         '•  Средняя активность: A = 1,55.\n'
                         '•  Высокая активность: A = 1,725.\n'
                         '•  Экстра-активность: A = 1,9 (под эту категорию обычно подпадают люди,\n'
                         'занимающиеся, например, тяжелой атлетикой, или другими силовыми\n'
                         'видами спорта с ежедневными тренировками, а также те, кто\n'
                         'выполняет тяжелую физическую\n'
                         'работу).\n'
                         '\n'
                         '(введите цифру активности):')
    await UserState.activity.set()


@dp.message_handler(state=UserState.activity)
async def send_calories(message, state):
    await state.update_data(activity=message.text)
    data = await state.get_data()
    if data['male'] in ['ж', 'Ж']:
        calories_w = ((10 * float(data['weight'].replace(',', '.')) + 6.25 * float(data['growth'].replace(',', '.')) -
                       5 * float(data['age'].replace(',', '.')) - 161) * float(data['activity'].replace(',', '.')))
        await message.answer(f'Ваша норма калорий c учётом активности = {round(calories_w, 1)} (ккал)')
    elif data['male'] in ['м', 'М']:
        calories_m = ((10 * float(data['weight'].replace(',', '.')) + 6.25 * float(data['growth'].replace(',', '.')) -
                       5 * float(data['age'].replace(',', '.')) + 5) * float(data['activity'].replace(',', '.')))
        await message.answer(f'Ваша суточная норма калорий c учётом активности = {round(calories_m, 1)} (ккал)')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
