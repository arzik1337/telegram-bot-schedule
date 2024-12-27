from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import json
import config

try:
    with open('schedule.json', 'r', encoding='utf-8') as f:
        schedule_data = json.load(f)
except FileNotFoundError:
    schedule_data = {}

ADMIN_ID = config.ADMIN_ID # Для добавления расписания по JSON через бота (можно и через файл schedule.json)

# Запуск бота (/start)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id == ADMIN_ID:
        keyboard = [
            [InlineKeyboardButton("Добавить расписание", callback_data="add_schedule")],
            [InlineKeyboardButton("Просмотреть расписание", callback_data="view_schedule")],
        ]
    else:
        keyboard = [
            [InlineKeyboardButton("Просмотреть расписание", callback_data="view_schedule")],
            [InlineKeyboardButton("Добавить расписание", callback_data="add_schedule")],
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Выберите действие:", reply_markup=reply_markup)

# Обработчик ответов бота на нажатия
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if query.data == "add_schedule":
        if user_id == ADMIN_ID:
            await query.edit_message_text("Отправьте расписание в формате JSON.")
        else:
            await query.edit_message_text("У вас нет прав для добавления расписания.")

    elif query.data == "view_schedule":
        keyboard = [
            [InlineKeyboardButton("5-е классы", callback_data="view_5_classes"),
             InlineKeyboardButton("6-е классы", callback_data='view_6_classes'),
             InlineKeyboardButton("7-е классы", callback_data="view_7_classes"),
             InlineKeyboardButton("8-е классы", callback_data="view_8_classes"),
             InlineKeyboardButton("9-е классы", callback_data="view_9_classes"),
             InlineKeyboardButton("10-е классы", callback_data="view_10_classes"),
             InlineKeyboardButton("11-е классы", callback_data="view_11_classes")],
            [InlineKeyboardButton("Назад", callback_data="back_to_main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Выберите группу классов для просмотра расписания:", reply_markup=reply_markup)

    # Расписания 5-х классов
    elif query.data == "view_5_classes":
        keyboard = [
            [InlineKeyboardButton("5А", callback_data="view_5А"),
             InlineKeyboardButton("5Б", callback_data="view_5Б")],
            [InlineKeyboardButton("Назад", callback_data="view_schedule")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Выберите класс из 5-х классов для просмотра расписания:", reply_markup=reply_markup)

    # Расписания 6-х классов
    elif query.data == "view_6_classes":
        keyboard = [
            [InlineKeyboardButton("6А", callback_data="view_6А")],
            [InlineKeyboardButton("Назад", callback_data="view_schedule")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Выберите класс из 6-х классов для просмотра расписания:", reply_markup=reply_markup)

    # Расписания 7-х классов
    elif query.data == "view_7_classes":
        keyboard = [
            [InlineKeyboardButton("7А", callback_data="view_7А"),
             InlineKeyboardButton("7Б", callback_data="view_7Б"),
             InlineKeyboardButton("7В", callback_data="view_7В")],
            [InlineKeyboardButton("Назад", callback_data="view_schedule")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Выберите класс из 7-х классов для просмотра расписания:", reply_markup=reply_markup)

    # Расписания 8-х классов
    elif query.data == "view_8_classes":
        keyboard = [
            [InlineKeyboardButton("8А", callback_data="view_8А"),
             InlineKeyboardButton("8Б", callback_data="view_8Б")],
            [InlineKeyboardButton("Назад", callback_data="view_schedule")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Выберите класс из 8-х классов для просмотра расписания:", reply_markup=reply_markup)

    # Расписания 9-х классов
    elif query.data == "view_9_classes":
        keyboard = [
            [InlineKeyboardButton("9А", callback_data="view_9А"),
             InlineKeyboardButton("9Б", callback_data="view_9Б")],
            [InlineKeyboardButton("Назад", callback_data="view_schedule")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Выберите класс из 9-х классов для просмотра расписания:", reply_markup=reply_markup)

    # Расписания 10-х классов
    elif query.data == "view_10_classes":
        keyboard = [
            [InlineKeyboardButton("10А", callback_data="view_10А")],
            [InlineKeyboardButton("Назад", callback_data="view_schedule")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Выберите класс из 10-х классов для просмотра расписания:", reply_markup=reply_markup)

    # Расписания 11-х классов
    elif query.data == "view_11_classes":
        keyboard = [
            [InlineKeyboardButton("11А", callback_data="view_11А")],
            [InlineKeyboardButton("Назад", callback_data="view_schedule")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Выберите класс из 11-х классов для просмотра расписания:", reply_markup=reply_markup)

    # Для фикса багов, связанных с выводом расписания
    elif query.data.startswith("view_"):
        class_name = query.data.split("_")[1]
        class_schedule = schedule_data.get(class_name, None)
        if class_schedule:
            schedule_text = "\n".join([f"{day}: {schedule}" for day, schedule in class_schedule.items()])
            await query.edit_message_text(f"Расписание для {class_name}:\n{schedule_text}")
        else:
            await query.edit_message_text(f"Расписание для класса {class_name} не найдено.")

    # Задает правильный формат для расписания
    elif query.data.startswith("view_7А") or query.data.startswith("view_8А") or query.data.startswith(
            "view_9А") or query.data.startswith("view_10А") or query.data.startswith("view_11А"):
        class_name = query.data.split("_")[1].upper()
        class_schedule = schedule_data.get(class_name, None)

        if class_schedule:
            schedule_text = ""
            for day, lessons in class_schedule.items():
                schedule_text += f"{day}:\n{lessons}\n\n"
            await query.edit_message_text(f"Расписание для класса {class_name}:\n{schedule_text}")
        else:
            await query.edit_message_text(f"Расписание для класса {class_name} не найдено.")

    # Кнопки "назад"
    elif query.data == "back_to_main_menu":
        keyboard = [
            [InlineKeyboardButton("Добавить расписание", callback_data="add_schedule")],
            [InlineKeyboardButton("Просмотреть расписание", callback_data="view_schedule")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Выберите действие:", reply_markup=reply_markup)

    elif query.data == "back":
        await start(update, context)

# Функция для добавления расписания. Необязательно использовать её, она нужна была просто для галочки
async def add_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != ADMIN_ID:
        await update.message.reply_text("У вас нет прав для добавления расписания.")
        return

    try:
        schedule = json.loads(update.message.text)
        schedule_data.update(schedule)
        with open('schedule.json', 'w', encoding='utf-8') as f:
            json.dump(schedule_data, f, ensure_ascii=False, indent=4)
        await update.message.reply_text("Расписание успешно обновлено.")
    except json.JSONDecodeError:
        await update.message.reply_text("Ошибка: Неверный формат JSON.")

# Основная функция
def main():
    app = ApplicationBuilder().token(config.TOKEN).build()

    # Обработчик команды /start
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(CommandHandler("schedule", add_schedule))

    # Запуск бота
    app.run_polling()

if __name__ == "__main__":
    main()
