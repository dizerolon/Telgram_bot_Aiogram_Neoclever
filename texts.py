import pisma

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

@dp.message_handler(commands=['file'])
async def send_file_text(message: Message):
    file_path = 'path/to/file'
    file_text = read_text_from_file(file_path)
    await bot.send_message(chat_id=message.chat.id, text=file_text)

print()