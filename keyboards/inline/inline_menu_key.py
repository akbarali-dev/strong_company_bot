from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from handlers.users.personal_data import contacts, portfolios
from .callback_data import portfolio_data
from data.client import get_data

contact_menu = InlineKeyboardMarkup(row_width=1)

for c in get_data('contact'):
    contact = InlineKeyboardButton(text=c['name'], url=c['link'])
    contact_menu.insert(contact)

portfolio_menu = InlineKeyboardMarkup(row_width=1)
for p in get_data('portfolio'):
    portfolio = InlineKeyboardButton(text=p['title'], callback_data=portfolio_data.new(name='portfolio'+str(p['id'])))
    portfolio_menu.insert(portfolio)

# ])
