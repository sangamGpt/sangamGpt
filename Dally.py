# filename: telegram_bot_mobile_fixed.py  
import asyncio  
from datetime import datetime, timedelta, timezone  
import json  
import os  
from telegram import Bot  
import aiohttp

BOT_TOKEN = "8192173095:AAEaaCfU4RmZwy0sUB-QYVqaI5cYCR6nsPI"  
CHAT_ID = -1002959515963  
IST = timezone(timedelta(hours=5, minutes=30))  
MESSAGES_FILE = "messages.json"  

# Load messages  
if os.path.exists(MESSAGES_FILE):  
    with open(MESSAGES_FILE, "r") as f:  
        messages_list = json.load(f)  
else:  
    messages_list = []  

bot = Bot(token=BOT_TOKEN)  

# ===== Scheduler (daily messages) =====
async def scheduler():
    sent_today = set()  # ट्रैक करेगा कि कौन सा मैसेज आज भेजा गया
    while True:
        now = datetime.now(IST)
        today_str = now.strftime("%Y-%m-%d")  # आज की तारीख
        for i, msg in enumerate(messages_list):
            msg_time = datetime.strptime(msg["time"], "%H:%M").replace(
                year=now.year, month=now.month, day=now.day, tzinfo=IST
            )
            msg_id = f"{i}_{today_str}"  # यूनिक आईडी आज के दिन के लिए
            if now >= msg_time and now < msg_time + timedelta(seconds=60):
                if msg_id not in sent_today:
                    try:
                        await bot.send_message(chat_id=CHAT_ID, text=msg["text"])
                        print(f"✅ Daily message sent: {msg['text']} at {msg['time']}")
                        sent_today.add(msg_id)
                    except Exception as e:
                        print("❌ Error sending message:", e)
        # रोज़ रात 12 बजे sent_today रीसेट करें ताकि अगले दिन फिर से भेजे
        if now.hour == 0 and now.minute == 0:
            sent_today.clear()
        await asyncio.sleep(30)

# ===== Poll Telegram Messages =====
async def poll_messages():  
    offset = None  
    while True:  
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?timeout=60"  
        if offset:  
            url += f"&offset={offset}"  
        async with aiohttp.ClientSession() as session:  
            async with session.get(url) as resp:  
                data = await resp.json()  
        for result in data.get("result", []):  
            offset = result["update_id"] + 1  
            msg = result.get("message")  
            if not msg:  
                continue  
            text = msg.get("text", "")  
            chat_id = msg["chat"]["id"]  

            if text.startswith("/start"):  
                await bot.send_message(chat_id=chat_id, text="✅ Bot running.\nCommands:\n/add HH:MM text\n/list\n/remove index")  

            elif text.startswith("/add"):  
                parts = text.split(maxsplit=2)  
                if len(parts) < 3:  
                    await bot.send_message(chat_id=chat_id, text="Usage: /add HH:MM message_text")  
                    continue  
                time_str = parts[1]  
                message_text = parts[2]  
                try:  
                    datetime.strptime(time_str, "%H:%M")  
                except ValueError:  
                    await bot.send_message(chat_id=chat_id, text="Time format must be HH:MM")  
                    continue  
                messages_list.append({"time": time_str, "text": message_text})  
                with open(MESSAGES_FILE, "w") as f:  
                    json.dump(messages_list, f, indent=2)  
                await bot.send_message(chat_id=chat_id, text=f"✅ Added daily message at {time_str}: {message_text}")  

            elif text.startswith("/list"):  
                if not messages_list:  
                    await bot.send_message(chat_id=chat_id, text="No messages scheduled.")  
                    continue  
                msg_text = "Scheduled daily messages:\n"  
                for i, m in enumerate(messages_list, start=1):  
                    msg_text += f"{i}. {m['time']} → {m['text']}\n"  
                await bot.send_message(chat_id=chat_id, text=msg_text)  

            elif text.startswith("/remove"):  
                parts = text.split()  
                if len(parts) < 2:  
                    await bot.send_message(chat_id=chat_id, text="Usage: /remove index")  
                    continue  
                try:  
                    index = int(parts[1]) - 1  
                    removed = messages_list.pop(index)  
                    with open(MESSAGES_FILE, "w") as f:  
                        json.dump(messages_list, f, indent=2)  
                    await bot.send_message(chat_id=chat_id, text=f"✅ Removed message: {removed['text']} at {removed['time']}")  
                except (ValueError, IndexError):  
                    await bot.send_message(chat_id=chat_id, text="Invalid index.")  
        await asyncio.sleep(1)  

# ===== Run everything =====  
async def main():  
    print("✅ Bot started. Listening...")  
    asyncio.create_task(scheduler())  
    await poll_messages()  

asyncio.run(main())
