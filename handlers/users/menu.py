from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import types
from loader import dp
from .data import question_answer as qa_data
from keyboards.default.main import question_answer as qa_btn, menu
from keyboards.inline.inline_menu import contact_menu


@dp.message_handler(Text("💾Ma'lumotlar"))
async def show_menu(message: Message):
    answer = """
    <b>_________Asosiy Ma'lumotlar_________</b>
    
<b>👤Ism:</b> Akbarali Asqaraliyev

<b>🟢Yosh:</b> 21

<b>💻Kasbi:</b> Fullstack developer

<b>📍Manzil:</b> Toshkent

<b>🎓Ta'lim:</b> Tugallanmagan oliy ta'lim 
    """
    await message.answer(answer)


@dp.message_handler(Text("⁉️Savol javob"))
async def show_menu(message: Message):
    await message.answer("Quyidagilarni biribi tanlang", reply_markup=qa_btn)


@dp.message_handler(Text("🏠Asosiy menu"))
async def main_menu(message: Message):
    await message.answer("Quyidagilarni biribi tanlang", reply_markup=menu)


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def get_document_id(message: Message):
    await message.reply(message.document.file_id)


@dp.message_handler(Text("📋Resume"))
async def get_resume(message: Message):
    document_id = "BQACAgIAAxkBAAODZlxzYH7DkSiV9_-KUO-LZrvrlRYAAng4AAI1uhBJ_kr5ti_agV01BA"
    await message.answer_document(document_id, caption="Resume")


@dp.message_handler(Text("📞Kontakt"))
async def get_resume(message: Message):
    await message.answer("______ Kontaktlat ______", reply_markup=contact_menu)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def question_answer(message: Message):
    if message.text in qa_data:
        await message.answer(qa_data[message.text])
