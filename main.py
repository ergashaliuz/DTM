import logging

from aiogram import Bot, Dispatcher, executor, types
from keyboards import keyboard
from keyboards.keyboard import back
from testlar import variyantlar, javoblar
from aiogram.dispatcher import FSMContext

API_TOKEN = '5256667812:AAHSY_idO5xNWGZCdGCB8qkPfuVLzQRRYyo'
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from checker import compare

logging.basicConfig(level=logging.INFO)
import re
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
import sub

CHANNELS = ['-1001559756714','-1001198756366','-1001457889806']
soni = len(CHANNELS)


@dp.message_handler(text=["/start", "Ortga qaytish"])
async def welcome(msg: types.Message, state: FSMContext):
    final = 1
    keyb = InlineKeyboardMarkup()
    for channel in CHANNELS:
        status = await sub.check(user_id=msg.from_user.id, channel=channel)
        link = await bot.get_chat(channel)
        silka = await link.export_invite_link()
        keyb.add(InlineKeyboardButton(text="Kanalga kirish", url=silka))
        final *= status
    if not final:
        await msg.answer(f"*Assalomu alaykum! Botimizdan foydalanish uchun siz avval {soni} ta kanalimizga obuna bo'lishingiz kerak obuna bo'lgach  /start ni bosing*",parse_mode="markdown", reply_markup=keyb)
    else:
        name = msg.from_user.full_name
        await msg.answer(f"Salom {name}", reply_markup=keyboard.mainM)
        await state.finish()


@dp.message_handler(text="📚TEST VARIANTIGA BUYURTMA")
async def test(msg: types.Message):
    await msg.answer("📖 Test varianti qaysi tilda bo'lishini ko'rsating: 👇", reply_markup=keyboard.test)


@dp.message_handler(text="🇸🇱 O'zbekcha")
async def testlar(msg: types.Message, state: FSMContext):
    await msg.answer("📗 Kerakli fanni tanlang: 👇", reply_markup=keyboard.uzbek)
    await state.set_state("test")


@dp.message_handler(text="🇷🇺 Pусский")
async def testlar(msg: types.Message, state: FSMContext):
    await msg.answer("📗 Выберите нужную науку: 👇", reply_markup=keyboard.rus)
    await state.set_state("testru")


@dp.message_handler(text="🛑 DTM Yangiliklari 🛑")
async def news(msg: types.Message):
    await msg.answer(
        "🛑 Abituriyentlar uchun eng so‘ngi va ishonchli yangiliklar bizning kanalda \n\n ➖➖➖➖➖➖➖➖➖➖ \n\n [@Dtm_Xabarlari](https://t.me/Davlat_test_markazi_abitu)",
        parse_mode="markdown", disable_web_page_preview=True)


@dp.message_handler(text="🔠 Natijalarni bilish")
async def results(msg: types.Message, state: FSMContext):
    await msg.answer("*Quyidagi formatda test varianti javoblarini jo‘nating:\n\ntest raqami/abcdd*\nMasalan: "
                     "1011/abcde....", reply_markup=back, parse_mode="markdown")
    await state.set_state("result")


@dp.message_handler(state="result")
async def tekshir(msg: types.Message, state: FSMContext):
    try:
        test_number = msg.text[:-31]
        string = msg.text
        yuborildi = re.sub(r'.', '', string, count=5)
        arr = list(yuborildi)
        javob = javoblar.javoblar[0][test_number]
        arr2 = list(javob)
        res = await compare(arr, arr2)
        result = len(res)
        from datetime import datetime
        now = datetime.now()
        xatolar = str()
        current_time = now.strftime("%H:%M:%S")
        await msg.answer(
            f"👤 Foydalanuvchi ismi: {msg.from_user.full_name}\n📖 Test nomeri: {test_number}\n✏️ Jami savollar soni: 30 "
            f"ta\n✅ To'g'ri javoblar soni: {30 - int(result)} ta\n❌ Xato javoblar: {result} ta\n🕐{current_time}")
        for r in res:
            xatolar += f"{int(r)+1})\n"

        await msg.answer(f"Quyidagi savollarda xato qilgansiz\n\n{xatolar}")
        await state.finish()
    except:
        await msg.answer("Qandaydir xatolik yuz berdi /start buyrug'ini bosing va javoblar sonini tekshirib qayta "
                         "urinib ko'ring...")
        await state.finish()


@dp.message_handler(text=["/start", "Ortga qaytish"])
async def send(msg: types.Message, state: FSMContext):
    await state.finish()
    name = msg.from_user.full_name
    await msg.answer(f"Salom {name}", reply_markup=keyboard.mainM)


@dp.message_handler(state="test")
async def send(msg: types.Message, state: FSMContext):
    matn = msg.text
    try:
        await msg.answer_document(variyantlar.variyantlar[0][matn],
                                  caption=f"Fan : {msg.text.title()}\nTest raqami : {variyantlar.variyantlar[1][matn]}\nKimga {msg.from_user.full_name}",
                                  parse_mode="markdown")
    except:
        await msg.answer(f"Salom {msg.from_user.full_name}", reply_markup=keyboard.mainM)
        await state.finish()


@dp.message_handler(state="testru")
async def send(msg: types.Message, state: FSMContext):
    matn = msg.text
    try:
        await msg.answer_document(variyantlar.variyantlar[2][matn],
                                  caption=f"*Наука* : {msg.text.title()}\n*Номер теста :* {variyantlar.variyantlar[3][matn]}\n*Кому* {msg.from_user.full_name}",
                                  parse_mode="markdown")
    except:
        await msg.answer(f"Salom {msg.from_user.full_name}", reply_markup=keyboard.mainM)
        await state.finish()

@dp.message_handler(text="🎥 Video qo'llanma")
async def teach(msg: types.Message):
    await msg.answer_video("https://t.me/testiszlar/29",caption="*Botdan qanday foydalanishni bilmasangiz ushbu videoni ko'ring*",parse_mode="markdown")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
