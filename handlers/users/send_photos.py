from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from keyboards.inline.buy_book import book_keys
from loader import dp, bot


@dp.message_handler(Command("maktab"))
async def send_school(message: types.Message):
    photo_id="https://lh5.googleusercontent.com/p/AF1QipOagrK4-PyFheq6TEvZWWxOkxKGBIeX0y_BmzyS=w431-h240-k-no"
    msg = "<b>Bu yerda sizning joylashishga asosan eng yaqin maktab topib beramiz</b>\n"
    msg += "Buning o'z joylashuvingizga yuboring\n\n"
    await message.reply_photo(photo_id, caption=msg, reply_markup=book_keys)