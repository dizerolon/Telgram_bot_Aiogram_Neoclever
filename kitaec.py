import time
import logging

from aiogram import Bot, Dispatcher, executor, types


TOKEN = "6100760731:AAEj7pUVRC-NRrrd3QpJBp_glqpe1zeQDts"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')




if __name__ == '__main__':
    executor.start_polling(dp)