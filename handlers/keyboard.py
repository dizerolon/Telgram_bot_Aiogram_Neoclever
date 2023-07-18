from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup

# создаём Клавиатуру

mainmenu_o_nas = KeyboardButton('О нас')
mainmenu_kurs = KeyboardButton('Наши курсы')
mainmenu_svyaz = KeyboardButton('Связаться с нами')

mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).row(mainmenu_o_nas, mainmenu_kurs, mainmenu_svyaz)

# как прога понимет, что в означают Кнопки под НАШИ КУРСЫ

kurskn = InlineKeyboardMarkup(row_width=2)  # сколько кнопок в строке
kurskn_kcht = InlineKeyboardButton(text='Курсы чтения', callback_data='kursknkcht')
kurskn_ost = InlineKeyboardButton(text='Остальные курсы', callback_data='kursknost')

# как прога понимет, что в означают Кнопки под НАШИ    КУРСЫ ЧТЕНИЯ


kurskn1 = InlineKeyboardMarkup(row_width=1)  # сколько кнопок в строке
kurskn1_azbuka = InlineKeyboardButton(text='Азбука', callback_data='kurskn1azbuka')
kurskn1_ch_za = InlineKeyboardButton(text='Чтение за 15 уроков', callback_data='kurskn1chza')
kurskn1_tech_cht = InlineKeyboardButton(text='Техника чтения', callback_data='kurskn1techcht')

# как прога понимет, что в означают Кнопки под НАШИ    ОСТАЛНЫЕ КУРСЫ


kurskn2 = InlineKeyboardMarkup(row_width=1)  # сколько кнопок в строке
kurskn2_bist_sch = InlineKeyboardButton(text='Быстрый счёт', callback_data='kurskn2bistsch')
kurskn2_sch_v_pred = InlineKeyboardButton(text='Счёт в пределах 10 без помощи пальцев', callback_data='kurskn2schvpred')
kurskn2_slov_zap = InlineKeyboardButton(text='Словарный запас', callback_data='kurskn2slovzap')
kurskn2_slov_slov = InlineKeyboardButton(text='Словарные слова', callback_data='kurskn2slovslov')
kurskn2_tech_cht = InlineKeyboardButton(text='Техника умножения', callback_data='kurskn2techcht')

# отправляем в диспетчер кнопки курс
kurskn.insert(kurskn_kcht)
kurskn.insert(kurskn_ost)

# отправляем в диспетчер кнопки курс1
kurskn1.insert(kurskn1_azbuka)
kurskn1.insert(kurskn1_ch_za)
kurskn1.insert(kurskn1_tech_cht)

# отправляем в диспетчер кнопки курс2
kurskn2.insert(kurskn2_bist_sch)
kurskn2.insert(kurskn2_sch_v_pred)
kurskn2.insert(kurskn2_slov_zap)
kurskn2.insert(kurskn2_slov_slov)
kurskn2.insert(kurskn2_tech_cht)
