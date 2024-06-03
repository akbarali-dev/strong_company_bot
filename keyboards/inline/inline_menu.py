from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from handlers.users.data import contacts

contact_menu = InlineKeyboardMarkup(row_width=1)

for c in contacts:
    contact = InlineKeyboardButton(text=c, url=contacts[c])
    contact_menu.insert(contact)
