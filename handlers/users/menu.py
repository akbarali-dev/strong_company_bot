from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram import types
import logging
from loader import dp
from .personal_data import question_answer as qa_data, person_image, certificate_images
from keyboards.default.main import question_answer as qa_btn, menu
from keyboards.inline.inline_menu_key import contact_menu, portfolio_menu
from data.client import get_data


# @dp.callback_query_handler(text='aiogram')
# async def show_menu(message: CallbackQuery):
#     logging.info(message)
#     await message.answer("Quyidagilarni biribi tanlang")


@dp.message_handler(Text("💾Ma'lumotlar"))
async def show_menu(message: Message):
    data = get_data('data')
    print()
    answer = f"""
    <b>Asosiy Ma'lumotlar</b>
    
<b>👤Ism:</b> {data['full_name']}

<b>🟢Yosh:</b> {data['age']}

<b>💻Kasbi:</b> {data['job_title']}

<b>📍Manzil:</b> {data['location']}

<b>🎓Ta'lim:</b> {data['educations']} 
    """
    await message.answer_photo(data['image_link'], caption=answer)


@dp.message_handler(Text("⁉️Savol javob"))
async def show_menu(message: Message):
    await message.answer("Quyidagilarni biribi tanlang", reply_markup=qa_btn)


@dp.message_handler(Text("🏠Asosiy menu"))
async def main_menu(message: Message):
    await message.answer("Quyidagilarni biribi tanlang", reply_markup=menu)


@dp.message_handler(Text("🏆Sertifikatlar"))
async def main_menu(message: Message):
    album = types.MediaGroup()
    certificates = get_data("file", 'S')
    for image in certificates:
        album.attach_photo(image['file_link'])
    await message.answer_media_group(media=album)


# todo get document id
@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def get_document_id(message: Message):
    a = f'{person_image}'
    await message.reply(f'<code>{message.document.file_id}</code>')


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(f'<code>{message.photo[-1].file_id}</code>')


@dp.message_handler(Text("📋Resume"))
async def get_resume(message: Message):
    album = types.MediaGroup()
    certificates = get_data("file", 'R')
    for doc in certificates:
        album.attach_document(doc['file_link'])
    # document_id = "BQACAgIAAxkBAAODZlxzYH7DkSiV9_-KUO-LZrvrlRYAAng4AAI1uhBJ_kr5ti_agV01BA"
    await message.answer_media_group(media=album)


@dp.message_handler(Text("🧰Portfolio"))
async def get_resume(message: Message):
    await message.answer("Quyidagilardan birini tanlang", reply_markup=portfolio_menu)


@dp.message_handler(Text("📞Kontakt"))
async def get_resume(message: Message):
    await message.answer("______ Kontaktlat ______", reply_markup=contact_menu)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def question_answer(message: Message):
    answers = get_data('qa', message.text)
    await message.answer(answers['answer'])
