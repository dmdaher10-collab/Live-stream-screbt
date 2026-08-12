import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# إعدادات التسجيل (Logging) باش نعرفو يلا كاين شي خطأ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# تعويض 'YOUR_TOKEN_HERE' بـ التوكن الحقيقي ديال البوت ديالك
TOKEN = '8791089759:AAGsaAuIOkOZyKe416EagvbFLp613hRSlIQ'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('مرحباً! صيفط لي الأمر بحال هكا:\n/live اسم_القناة رابط_الفيديو')

async def live_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # كنشوفو واش المستعمل صيفط السمية والرابط
    if len(context.args) < 2:
        await update.message.reply_text('⚠️ عفاك استعمل الفورما الصحيحة:\n/live [الاسم] [الرابط]')
        return

    name = context.args[0]
    link = context.args[1]

    # الرسالة اللي كترجع بحال اللي في الصور
    # كلمة "معاينة" مع الرابط كتخلي التيليجرام يبين الفيديو مباشرة
    response_text = (
        f"✅ بدأ البث\n\n"
        f"📺 **{name}**\n\n"
        f"👁️ معاينة:\n"
        f"{link}"
    )

    await update.message.reply_text(response_text, parse_mode='Markdown')

def main():
    # كنبداو البوت
    application = Application.builder().token(TOKEN).build()

    # إضافة الأوامر
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("live", live_handler))

    # تشغيل البوت
    print("البوت خدام دابا...")
    application.run_polling()

if __name__ == '__main__':
    main()
