import aiohttp
import uuid

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton


router = Router()
pending_translations: dict[str, str] = {} # Stores the original text until the user selects a target language.


@router.message(F.text == "/start")
async def start_handler(message: Message) -> None:
    await message.answer("Hello! I'm translator bot. Enter text to translate and I'll do it for you. Example: /translate Hello, how are you?")


@router.message(F.text.startswith("/translate"))
async def translate_handler(message: Message) -> None:
    text = message.text.strip()
    if text == "/translate":
        await message.answer("Please send text to translate. Example: /translate Hello, how are you?")
        return

    text_to_translate = text.split("/translate", 1)[1].strip()
    if not text_to_translate:
        await message.answer("Please send text to translate after the /translate command.")
        return

    languages = {
        "es": "Spanish",
        "fr": "French",
        "de": "German"
    }

    request_id = uuid.uuid4().hex
    pending_translations[request_id] = text_to_translate

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=lang, callback_data=f"translate_{code}_{request_id}") for code, lang in languages.items()]
    ])

    await message.answer("Select the target language:", reply_markup=keyboard)


@router.callback_query(F.data.startswith("translate_"))
async def translate_callback_handler(callback_query: CallbackQuery) -> None:
    API_URL = "https://api.mymemory.translated.net/get"
    callback_parts = callback_query.data.split("_", 2)
    if len(callback_parts) < 3:
        await callback_query.answer("Invalid translation request.", show_alert=True)
        return

    _, target_lang, request_id = callback_parts
    text_to_translate = pending_translations.pop(request_id, None)

    if text_to_translate is None:
        await callback_query.answer("Translation request expired. Please send /translate <text> again.", show_alert=True)
        return

    params = {
        "q": text_to_translate,
        "langpair": f"en|{target_lang}"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL, params=params) as response:
            if response.status == 200:
                data = await response.json()
                translated_text = data["responseData"]["translatedText"]
                await callback_query.answer()
                await callback_query.message.answer(f"Translated text: {translated_text}")
            else:
                await callback_query.answer()
                await callback_query.message.answer("Sorry, an error occurred while translating. Please try again later.")