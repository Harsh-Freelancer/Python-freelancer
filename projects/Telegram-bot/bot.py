import requests
import telegram
from telegram.ext import Updater, CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
API_KEY = "YOUR_OPENWEATHER_API_KEY"

def start(update, context):
    update.message.reply_text("👋 Hi! I'm Weather Bot\n\nSend /weather city name\nExample: /weather Delhi")

def get_weather(update, context):
    if not context.args:
        update.message.reply_text("❌ Please provide city name\nExample: /weather Mumbai")
        return
    
    city = " ".join(context.args)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]
            
            message = f"🌍 City: {city}\n"
            message += f"🌡️ Temperature: {temp}°C\n"
            message += f"🤔 Feels like: {feels_like}°C\n"
            message += f"💧 Humidity: {humidity}%\n"
            message += f"🌥️ Condition: {description}\n"
            message += f"💨 Wind Speed: {wind_speed} m/s"
            
            update.message.reply_text(message)
        else:
            update.message.reply_text("❌ City not found! Please check the name.")
    
    except:
        update.message.reply_text("❌ Error fetching weather data. Try again!")

def help_command(update, context):
    update.message.reply_text("📌 Commands:\n/start - Start bot\n/weather city - Get weather\n/help - Show this menu")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("weather", get_weather))
    dp.add_handler(CommandHandler("help", help_command))
    
    updater.start_polling()
    print("✅ Bot is running...")
    updater.idle()

if __name__ == "__main__":
    main()