from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from handlers.users.personal_data import contacts, portfolios
from .callback_data import portfolio_data


def contact_menu(contacts):
    btns = InlineKeyboardMarkup(row_width=1)

    for c in contacts:
        contact = InlineKeyboardButton(text=c['name'], url=c['link'])
        btns.insert(contact)
    return btns


def portfolio_menu(portfolios):
    portfolio_btn = InlineKeyboardMarkup(row_width=1)
    for p in portfolios:
        portfolio = InlineKeyboardButton(text=p['title'],
                                         callback_data=portfolio_data.new(name='portfolio' + str(p['id'])))
        portfolio_btn.insert(portfolio)
    return portfolio_btn

# ])
