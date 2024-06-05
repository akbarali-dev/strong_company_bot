from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, MenuButton, KeyboardButtonRequestChat
from handlers.users.personal_data import question_answer as qa
from data.client import get_data

web = WebAppInfo(url="https://javthon.uz/")
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💾Ma'lumotlar"),
            KeyboardButton(text='🧰Portfolio')
        ],
        [
            KeyboardButton(text="📞Kontakt"),
            KeyboardButton(text="🏆Sertifikatlar"),
        ],
        [
            KeyboardButton(text="📋Resume"),
            KeyboardButton(text="⁉️Savol javob"),
        ],
        [
            KeyboardButton(text="⚡️Wep saytga o'tish", web_app=web)
        ]
    ],
    resize_keyboard=True
)

question_answer = ReplyKeyboardMarkup(resize_keyboard=True)
questions = get_data('qa')
for qa in questions:
    buttons = [qa['question']]
    question_answer.add(*buttons)
main_btn = ["🏠Asosiy menu"]
chat = KeyboardButton()
chat_btn = ["🏠Asosiy menu", ]
question_answer.add(*main_btn)
