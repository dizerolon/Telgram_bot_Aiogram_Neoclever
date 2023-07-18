from aiogram import types

from bot import dp, bot
from handlers import keyboard


# вытаскиваем текст
def return_txt(file_name):
    with open(file_name, "r", encoding='utf-8') as f:
        text = f.read()
    return text


# ответ на старт
async def start(message: types.Message):  # начало и чтоб при ошибке бот не вырубался
    try:
        await message.answer(return_txt("infa/start.txt"),
                             reply_markup=keyboard.mainmenu)  # отреагируем на сообщение пользователя
    except Exception as e:
        print(e)  # выводим просто ошибку


# ответ на кнопки
async def keyboard_handler(message: types.Message):
    try:
        match message.text:

            case "О нас":
                await message.reply(return_txt("infa/o_nas.txt"))
            case "Наши курсы":
                await message.reply(return_txt("infa/kurs.txt"), reply_markup=keyboard.kurskn)
            case "Связаться с нами":
                await message.reply(return_txt("infa/svyaz.txt"))


            case "Азбука":
                await message.reply(return_txt("pisma/azbuka.txt"))
            case "Чтение за 15 уроков":
                await message.reply(return_txt("pisma/ch_za.txt"))
            case "Техника чтения":
                await message.reply(return_txt("pisma/tech_cht.txt"))



            case "Быстрый счёт":
                await message.reply(return_txt("pisma/bist_sch.txt"))
            case "Счёт в пределах 10 без помощи пальцев":
                await message.reply(return_txt("pisma/sch_v_pred.txt"))
            case "Словарный запас":
                await message.reply(return_txt("pisma/slov_zap.txt"))
            case "Словарные слова":
                await message.reply(return_txt("pisma/slov_slov.txt"))
            case "Техника умножения":
                await message.reply(return_txt("pisma/tabl_umn.txt"))



            case _:
                await message.answer('Такой команды не предусмотрено')
    except Exception as e:
        print(e)


# ответ на кнопки

async def inline_kurs_buttons_handler(call: types.CallbackQuery):
    match call.data:
        case "kursknkcht":
            await call.message.answer(return_txt("infa/kurs1.txt"), reply_markup=keyboard.kurskn1)
            await bot.answer_callback_query(callback_query_id=call.id)
        case "kursknost":
            await call.message.answer(return_txt("infa/kurs2.txt"), reply_markup=keyboard.kurskn2)
            await bot.answer_callback_query(callback_query_id=call.id)


#async def inline_kursL_buttons_handler(call: types.CallbackQuery):
#    match call.data:
        case "kurskn1azbuka":
            await call.message.answer(return_txt("pisma/azbuka.txt"))
            await bot.answer_callback_query(callback_query_id=call.id)
        case "kurskn1chza":
            await call.message.answer(return_txt("pisma/ch_za.txt"))
            await bot.answer_callback_query(callback_query_id=call.id)
        case "kurskn1techcht":
            await call.message.answer(return_txt("pisma/tech_cht.txt"))
            await bot.answer_callback_query(callback_query_id=call.id)


#async def inline_kursR_buttons_handler(call: types.CallbackQuery):
#    match call.data:
        case "kurskn2bistsch":
            await call.message.answer(return_txt("pisma/bist_sch.txt"))
            await bot.answer_callback_query(callback_query_id=call.id)
        case "kurskn2schvpred":
            await call.message.answer(return_txt("pisma/sch_v_pred.txt"))
            await bot.answer_callback_query(callback_query_id=call.id)
        case "kurskn2slovzap":
            await call.message.answer(return_txt("pisma/slov_zap.txt"))
            await bot.answer_callback_query(callback_query_id=call.id)
        case "kurskn2slovslov":
            await call.message.answer(return_txt("pisma/slov_slov.txt"))
            await bot.answer_callback_query(callback_query_id=call.id)
        case "kurskn2techcht":
            await call.message.answer(return_txt("pisma/tabl_umn.txt"))
            await bot.answer_callback_query(callback_query_id=call.id)


# отправляем диспетчеру

def register_client():
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(keyboard_handler, state=None)

    dp.register_callback_query_handler(inline_kurs_buttons_handler)

