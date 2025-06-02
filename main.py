
import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# توکن ربات از متغیر محیطی گرفته می‌شود
TOKEN = os.environ.get("BOT_TOKEN")

# دکمه‌های اصلی
main_menu = [["مشاهده کاتالوگ محصولات"], ["درباره ما", "تماس با ما"]]

# دکمه‌های کاتالوگ
catalog_menu = [["شیرآلات البرز"], ["محصولات پرنیان"], ["محصولات آلتون"], ["بازگشت"]]

# هندلر شروع
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "به ربات شرکت توکل تجارت اسپادانا خوش آمدید 🌐",
        reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    )

# هندلر پیام‌ها
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "مشاهده کاتالوگ محصولات":
        await update.message.reply_text(
            "لطفاً یکی از دسته‌بندی‌های زیر را انتخاب کنید:",
            reply_markup=ReplyKeyboardMarkup(catalog_menu, resize_keyboard=True)
        )
    elif text == "شیرآلات البرز":
        await send_pdf(update, "alborz.pdf")
    elif text == "محصولات پرنیان":
        await send_pdf(update, "parnian.pdf")
    elif text == "محصولات آلتون":
        await send_pdf(update, "altun.pdf")
    elif text == "درباره ما":
        await update.message.reply_text(
            "شرکت توکل تجارت اسپادانا با سال‌ها تجربه در زمینه عرضه لوازم بهداشتی و ساختمانی مانند هود، سینک، شیرآلات و فر توکار، "
            "همواره تلاش کرده تا بهترین محصولات را با مناسب‌ترین قیمت به مشتریان خود ارائه دهد."
        )
    elif text == "تماس با ما":
        await update.message.reply_text(
            "☎37352955
☎37352956
☎37352957
📲09912629410
📲09912629411
📲09912629412"
        )
    elif text == "بازگشت":
        await update.message.reply_text(
            "بازگشت به منوی اصلی:",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
        )
    else:
        await update.message.reply_text("لطفاً یکی از گزینه‌ها را انتخاب کنید.")

# ارسال PDF
async def send_pdf(update: Update, filename: str):
    file_path = os.path.join("pdfs", filename)
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            await update.message.reply_document(document=f)
    else:
        await update.message.reply_text("فایل مورد نظر یافت نشد.")

# اجرای اپلیکیشن
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
