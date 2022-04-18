from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainM = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="📚TEST VARIANTIGA BUYURTMA"),
        KeyboardButton(text="🔠 Natijalarni bilish")
    ],
    [
        KeyboardButton(text="🛑 DTM Yangiliklari 🛑"),
        KeyboardButton(text="🎥 Video qo'llanma")
    ]

],
    resize_keyboard=True,
)

back = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Ortga qaytish"),
    ],

],
    resize_keyboard=True,
)

test = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="🇸🇱 O'zbekcha"),
        KeyboardButton(text="🇷🇺 Pусский")
    ],
    [
        KeyboardButton(text="Ortga qaytish")
    ]

],
    resize_keyboard=True,
)

uzbek = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="MATEMATIKA"),
        KeyboardButton(text="KIMYO")
    ],
    [
        KeyboardButton(text="BIOLOGIYA"),
        KeyboardButton(text="KIMYO")
    ],
    [
        KeyboardButton(text="ONA TILI"),
        KeyboardButton(text="TARIX")
    ],
    [
        KeyboardButton(text="INGLIZ TILI"),
        KeyboardButton(text="GEOGRAFIYA"),

    ],
    [
        KeyboardButton(text="NEMIS TILI"),
        KeyboardButton(text="FRANSUZ TILI")
    ],
    [
        KeyboardButton(text="Ortga qaytish")
    ]

],
    resize_keyboard=True,
)

rus = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="МАТЕМАТИКА"),
        KeyboardButton(text="ХИМИЯ")
    ],
    [
        KeyboardButton(text="БИОЛОГИЯ"),
        KeyboardButton(text="ФИЗИКА")
    ],
    [
        KeyboardButton(text="ИСТОРИЯ"),
        KeyboardButton(text="РУССКИЙ ЯЗЫК")
    ],
    [
        KeyboardButton(text="ГЕОГРАФИЯ"),
        KeyboardButton(text="АНГЛИЙСКИЙ ЯЗЫК"),

    ],
    [
        KeyboardButton(text="НЕМЕЦКИЙ ЯЗЫК"),
        KeyboardButton(text="ФРАНЦУЗСКИЙ ЯЗЫК"),

    ],
    [
        KeyboardButton(text="Ortga qaytish")
    ]

],
    resize_keyboard=True,
)
