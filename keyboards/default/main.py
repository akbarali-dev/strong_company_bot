from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, MenuButton, KeyboardButtonRequestChat
from handlers.users.personal_data import question_answer as qa
from data.client import get_data
from loader import db

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


def question_btn(questions):
    question_answer = ReplyKeyboardMarkup(resize_keyboard=True)
    for qa in questions:
        buttons = [qa['question']]
        question_answer.add(*buttons)
    main_btn = ["🏠Asosiy menu"]
    question_answer.add(*main_btn)
    return question_answer
