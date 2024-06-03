from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from handlers.users.data import question_answer as qa

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
for qa in qa:
    buttons = [qa]
    question_answer.add(*buttons)
main_btn = ["🏠Asosiy menu"]
question_answer.add(*main_btn)
