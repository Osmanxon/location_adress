from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from keyboards.default.location_button import keyboard
from utils.misc.get_distance import choose_shortest
from loader import dp


@dp.callback_query_handler(text="mylocation")
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text="Lokatsiya yuboring:", reply_markup=keyboard)

@dp.message_handler(content_types='location')
async def get_contact(message: Message):
    location=message.location
    latitude=location.latitude
    longitude=location.longitude
    closest_school = choose_shortest(location)

    text="\n\n".join([f"<a href='{url}'>{school_name}</a>\n Masofa: {distance:.1f} km."
                      for school_name, distance, url, school_location in closest_school])

    await message.answer(f"Raxmat. \n"
                         f"Latitude={latitude}\n"
                         f"Longitude={longitude}\n\n"
                         f"{text}", disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove())

    for school_name, distance, url, school_location in closest_school:
        await message.answer_location(latitude=school_location["lat"],
                                      longitude=school_location["lon"])

