from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram import types
import logging
from loader import dp, db
from .personal_data import question_answer as qa_data, person_image, certificate_images
from keyboards.default.main import question_btn as qa_btn, menu
from keyboards.inline.inline_menu_key import contact_menu, portfolio_menu


# @dp.callback_query_handler(text='aiogram')
# async def show_menu(message: CallbackQuery):
#     logging.info(message)
#     await message.answer("Quyidagilarni biribi tanlang")


@dp.message_handler(Text("💾Ma'lumotlar"))
async def show_menu(message: Message):
    data = await db.select_user_info(bot_id=1474104201)
    answer = f"""
    <b>Asosiy Ma'lumotlar</b>
    
<b>👤Ism:</b> {data['full_name']}

<b>🟢Yosh:</b> {data['age']}

<b>💻Kasbi:</b> {data['job_title']}

<b>📍Manzil:</b> {data['location']}

<b>🎓Ta'lim:</b> {data['educations']} 
    """
    await message.answer_photo(photo=data['image_link'], caption=answer)


@dp.message_handler(Text("⁉️Savol javob"))
async def show_menu(message: Message):
    questions = await db.select_questions(user_id=1474104201)
    await message.answer("Quyidagilarni biribi tanlang", reply_markup=qa_btn(questions))


@dp.message_handler(Text("🏠Asosiy menu"))
async def main_menu(message: Message):
    await message.answer("Quyidagilarni biribi tanlang", reply_markup=menu)


@dp.message_handler(Text("🏆Sertifikatlar"))
async def main_menu(message: Message):
    album = types.MediaGroup()
    certificates = await db.select_file(user_id=1474104201, category='S')
    for image in certificates:
        album.attach_photo(image['file_link'])
    await message.answer_media_group(media=album)


# todo get document id
@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def get_document_id(message: Message):
    a = f'{person_image}'
    await message.reply(f'<code>{message.document.file_id}</code>')


# get file id
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(f'<code>{message.photo[-1].file_id}</code>')


@dp.message_handler(Text("📋Resume"))
async def get_resume(message: Message):
    album = types.MediaGroup()
    documents = await db.select_file(user_id=1474104201, category='R')
    for doc in documents:
        album.attach_document(doc['file_link'])
    await message.answer_media_group(media=album)


@dp.message_handler(Text("🧰Portfolio"))
async def get_resume(message: Message):
    portfolios = await db.select_portfolio(user_id=1474104201)
    await message.answer("Quyidagilardan birini tanlang", reply_markup=portfolio_menu(portfolios))


@dp.message_handler(Text("📞Kontakt"))
async def get_resume(message: Message):
    contacts = await db.select_contacts(user_id=1474104201)
    await message.answer("______ Kontaktlat ______", reply_markup=contact_menu(contacts))


@dp.message_handler(content_types=types.ContentType.TEXT)
async def question_answer(message: Message):
    answers = await db.select_answer(question=message.text, user_id=1474104201)
    await message.answer(answers['answer'])
