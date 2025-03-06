import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    intros = [
        "Hey, foodie! Your culinary bot is ready to dish out some fun!",
        "Welcome to the food zone—I’m your tasty sidekick!",
        "Yo, hungry human! Let’s spice up your day with food talk!"
    ]
    await update.message.reply_text(random.choice(intros))

# Command: /foodquote
async def foodquote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quotes = [
        "Life is short—eat the dessert first!",
        "Food is my love language, and I’m fluent!",
        "Cooking is like love: it should be entered into with abandon or not at all."
    ]
    await update.message.reply_text(f"Foodie wisdom: {random.choice(quotes)}")

# Command: /foodcombo
async def foodcombo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    combos = [
        "Pizza topped with mac ‘n’ cheese—carb heaven awaits!",
        "Tacos with a side of sushi—fusion gone wild!",
        "Ice cream drizzled with hot sauce—sweet heat, baby!"
    ]
    await update.message.reply_text(f"Try this crazy combo: {random.choice(combos)}")

# Command: /foodmood
async def foodmood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    moods = [
        "You’re giving off burger vibes—juicy and bold!",
        "Your mood screams ramen—slurpy and cozy!",
        "I’m sensing dessert energy—sweet and unstoppable!"
    ]
    await update.message.reply_text(random.choice(moods))

# Message handler (non-command text)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()
    if "hungry" in msg or "food" in msg:
        await update.message.reply_text("Same, fam! What’s your craving—salty, sweet, or chaotic?")
    elif "pizza" in msg:
        await update.message.reply_text("Pizza? You’re speaking straight to my doughy heart!")
    elif "cake" in msg or "sweet" in msg:
        await update.message.reply_text("Sugar rush incoming—save me a slice!")
    elif "no" in msg or "not" in msg:
        await update.message.reply_text("Not hungry? Lies! Your stomach’s growling louder than me!")
    else:
        food_twists = [
            "...pairs well with fries!",
            "...sounds like a recipe for chaos!",
            "...chef’s is incoming!"
        ]
        await update.message.reply_text(f"{update.message.text} {random.choice(food_twists)}")

# Unknown command handler
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    oops = [
        "Did you mean to order takeout instead?",
        "That’s not on the menu, my friend!",
        "My recipe book doesn’t have that command!"
    ]
    await update.message.reply_text(random.choice(oops))

def main():
    # Replace with your token from BotFather
    TOKEN = '7580980227:AAGFmUYNUiBnj8KR6fqbz4P_4oIPKEhnn84'

    # Create the Application instance
    application = Application.builder().token(TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("foodquote", foodquote))
    application.add_handler(CommandHandler("foodcombo", foodcombo))
    application.add_handler(CommandHandler("foodmood", foodmood))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    # Start the bot
    print("Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()