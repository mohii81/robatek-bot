import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# دریافت توکن از متغیر محیطی (در render تنظیم می‌شود)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# منوی اصلی
main_keyboard = ReplyKeyboardMarkup(
    [["📦 مشاهده کاتالوگ محصولات"], ["ℹ️ درباره ما", "📞 تماس با ما"]],
    resize_keyboard=True
)

# زیرمنوی کاتالوگ
catalog_keyboard = ReplyKeyboardMarkup(
    [["🛁 شیرآلات البرز", "🟣 محصولات پرنیان", "🔴 محصولات آلتون"], ["🔙 بازگشت"]],
    resize_keyboard=True
)

# تابع شروع
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "به ربات شرکت توکل تجارت اسپادانا خوش آمدید 🌐\nلطفاً یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=main_keyboard
    )

# مدیریت پیام‌ها
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📦 مشاهده کاتالوگ محصولات":
        await update.message.reply_text("یکی از برندهای زیر را انتخاب کنید:", reply_markup=catalog_keyboard)

    elif text == "🛁 شیرآلات البرز":
        await send_pdf(update, "pdfs/alborz.pdf", "📄 کاتالوگ شیرآلات البرز")

    elif text == "🟣 محصولات پرنیان":
        await send_pdf(update, "pdfs/parnian.pdf", "📄 کاتالوگ محصولات پرنیان")

    elif text == "🔴 محصولات آلتون":
        await send_pdf(update, "pdfs/altun.pdf", "📄 کاتالوگ محصولات آلتون")

    elif text == "🔙 بازگشت":
        await update.message.reply_text("به منوی اصلی بازگشتید.", reply_markup=main_keyboard)

    elif text == "ℹ️ درباره ما":
        await update.message.reply_text(
            """شرکت *توکل تجارت اسپادانا* با هدف ارائه بهترین و باکیفیت‌ترین محصولات بهداشتی و ساختمانی فعالیت خود را آغاز کرده است.
این مجموعه با بهره‌گیری از برندهای معتبر مانند *آلتون، پرنیان و البرز*، تلاش دارد نیازهای مشتریان در زمینه تجهیزات آشپزخانه، شیرآلات و هود را به بهترین شکل ممکن تأمین کند.
ما همواره به کیفیت، مشتری‌مداری و خدمات پس از فروش متعهد هستیم.""",
            parse_mode='Markdown'
        )

    elif text == "📞 تماس با ما":
        await update.message.reply_text(
            "شماره‌های تماس شرکت:\n"
"☎ 37352955\n"
           "☎ 37352956\n"
            "☎ 37352957\n"
            "📲 09912629410\n"
            "📲 09912629411\n"
            "📲 09912629412"
        )

    else:
        await update.message.reply_text("لطفاً یکی از گزینه‌های منو را انتخاب کنید.")

# تابع ارسال PDF
async def send_pdf(update: Update, file_path: str, caption: str):
    try:
        with open(file_path, 'rb') as f:
            await update.message.reply_document(document=f, caption=caption)
    except FileNotFoundError:
        await update.message.reply_text("❗ فایل مربوط به این برند یافت نشد.")

# اجرای ربات
if name == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    print("🤖 ربات در حال اجراست...")
    app.run_polling()
