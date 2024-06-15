import re
from aiogram.dispatcher.filters import Command, Text
from loader import dp, db
from aiogram.types import Message, CallbackQuery
import logging
from keyboards.inline.inline_menu_key import portfolio_menu
from keyboards.inline.callback_data import portfolio_data
from .personal_data import portfolios


def get_last_number(s):
    match = re.search(r'\d+$', s)
    if match:
        return int(match.group())
    else:
        return None


@dp.callback_query_handler(text_contains='portfolio')
async def show_menu(message: CallbackQuery):
    p_id = get_last_number(message.data)
    p_data = await db.select_portfolio_by_id(id=p_id)

    answer = f"""
    <b>{p_data['title']}</b>
    {p_data['description']}
    <a href='{p_data['link']}'>havola</a>
    """
    portfolio = await db.select_portfolio(user_id=1474104201)
    await message.message.edit_text(answer, reply_markup=portfolio_menu(portfolio))
    await message.answer(cache_time=3)

# @dp.callback_query_handler(portfolio_data)
# async def show_menu(call: CallbackQuery, callback_data: dict):
#     # logging.info(call.from_user.)
#     logging.info(callback_data)
#     await call.message.answer(portfolios[call.message.text])
#     # await call.message.edit_text("Quyidagilarni biribi tanlang", reply_markup=aiogram_keys)
