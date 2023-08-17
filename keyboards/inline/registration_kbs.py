from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


profile_y_n = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Так', callback_data='show_profile'), InlineKeyboardButton(text='Ні', callback_data='no')]
        ]
    )
edit_profile = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Так', callback_data='edit_profile'), InlineKeyboardButton(text='Ні', callback_data='no')]
        ]
    )
w_t_e = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Ім\'я', callback_data='edit_name'), InlineKeyboardButton(text='Email', callback_data='edit_email'), InlineKeyboardButton(text='Вік', callback_data='edit_age')]
        ]
    )