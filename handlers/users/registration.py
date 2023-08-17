from aiogram import types
from aiogram.dispatcher import FSMContext


from loader import dp
from states import Registration
from keyboards.inline import profile_y_n, edit_profile, w_t_e

async def act(message):
    await message.answer('Хочете переглянути свій профіль?', reply_markup=profile_y_n)
    await Registration.profile.set()

@dp.message_handler(commands='registration')
async def reg(message: types.Message):
    await message.answer('Давайте зарєєструємо вас!\n Будь ласка, вкажіть ваше ім\'я')
    await Registration.enter_name.set()

@dp.message_handler(state=Registration.enter_name)
async def enter_name(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer(f'Супер! Ваше ім\'я записано як "{data["name"]}".\n Тепер вкажіть свою електронну адресу')
    await Registration.enter_email.set()

@dp.message_handler(state=Registration.enter_email)
async def enter_email(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
    await message.answer(f'Чудово! Вашу електронну адресу записано як "{data["email"]}".\n Тепер вкажіть свій вік')
    await Registration.enter_age.set()

@dp.message_handler(state=Registration.enter_age)
async def enter_age(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await message.answer(f'Добре! Ваш вік записано як "{data["age"]}".')
    await message.answer('Хочете переглянути свій профіль?', reply_markup=profile_y_n)
    await Registration.profile.set()

@dp.callback_query_handler(text='show_profile', state=Registration.profile)
async def show_profile(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        name = data['name']
        email = data['email']
        age = data['age']
    await call.message.answer(f'Ось ваш профіль:\nІм\'я: {name}\nEmail: {email}\nВік: {age}')
    await call.message.answer('Хочете змінити щось у профілі?', reply_markup=edit_profile)

@dp.callback_query_handler(text='edit_profile', state=Registration.profile)
async def w_t_e_in_profile(call: types.CallbackQuery):
    await call.message.edit_text('Що саме хочете змінити у профілі?', reply_markup=w_t_e)

@dp.callback_query_handler(text='edit_name', state=Registration.profile)
async def edit_name(call: types.CallbackQuery):
    await call.message.answer('Добре, введіть нове ім\'я')
    await Registration.set_new_name.set()

@dp.message_handler(state=Registration.set_new_name)
async def set_new_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer(f'Чудово! Тепер ваше ім\'я записано як "{data["name"]}"')
    await act(message)
@dp.callback_query_handler(text='edit_email', state=Registration.profile)
async def edit_email(call: types.CallbackQuery):
    await call.message.answer('Добре, введіть новий email')
    await Registration.set_new_email.set()

@dp.message_handler(state=Registration.set_new_email)
async def set_new_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
    await message.answer(f'Чудово! Тепер ваш email записано як "{data["email"]}"')
    await act(message)

@dp.callback_query_handler(text='edit_age', state=Registration.profile)
async def edit_age(call: types.CallbackQuery):
    await call.message.answer('Добре, введіть нове значення віку')
    await Registration.set_new_age.set()

@dp.message_handler(state=Registration.set_new_age)
async def set_new_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await message.answer(f'Чудово! Тепер ваш вік записано як "{data["age"]}"')
    await act(message)

@dp.callback_query_handler(text='no', state='*')
async def finish(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Дякуємо за використання!❤️')
    await state.reset_state()