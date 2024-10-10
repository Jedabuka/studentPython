from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.insert(button1).resize_keyboard = True
kb.insert(button2).resize_keyboard = True


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    male = State()
    activity = State()

@dp.message_handler(commands=['start'])
async def start(message):
    print('Хочет стартовать!')
    await message.answer('Привет! Я помогу тебе узнать твою суточную норму калорий', reply_markup=kb)

@dp.message_handler(text=['Информация'])
async def set_info(message):
    await message.answer('Версия 0.1.2\n'
                         'Aвтор: Евгений Геннадьевич Лаптев\n'
                         'Мой телеграм: @EvgenLap')

@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.answer('Введите свой возраст (полных лет):')
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
    if data['male'] == 'ж' or 'Ж':
        calories = ((10 * float(data['weight'].replace(',', '.')) + 6.25 * float(data['growth'].replace(',', '.')) -
                     5 * float(data['age'].replace(',', '.')) - 161) * float(data['activity'].replace(',', '.')))
        await message.answer(f'Ваша норма калорий c учётом активности = {round(calories, 1)} (ккал)')
    elif data['male'] == 'м' or 'М':
        calories = ((10 * float(data['weight'].replace(',', '.')) + 6.25 * float(data['growth'].replace(',', '.')) -
                     5 * float(data['age'].replace(',', '.')) + 5) * float(data['activity'].replace(',', '.')))
        await message.answer(f'Ваша суточная норма калорий c учётом активности = {round(calories, 1)} (ккал)')
    await state.finish()

@dp.message_handler()
async def all_message(message):
    print('С нами поздоровались!')
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

