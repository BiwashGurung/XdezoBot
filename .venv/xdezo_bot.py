import telebot
import mysql.connector
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# API Token for the bot that was created in BotFather
API_TOKEN = '7670771467:AAH9Skw-LmgG24zOgRRMu6RSTQkLnyvcBow'

# Creating a bot object
bot = telebot.TeleBot(API_TOKEN)

# Connect to MariaDB (XAMPP)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="XE",
    database="xdezo_bot"
)
cursor = db.cursor()

# Dictionary to track user states
ENROLLMENT_STATE = {}

VALID_CERT_IDS = {
    "CERT12345": "Biwash Gurung",
    "CERT67890": "Hemanta Gururng",
    "CERT11223": "Prabin Thapa"
}

# Creating a function to display the main menu with inline buttons
def main_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("📚 Courses", callback_data="courses"),
        InlineKeyboardButton("💰 Price", callback_data="price"),
        InlineKeyboardButton("📞 Contact", callback_data="contact"),
        InlineKeyboardButton("📍 Location", callback_data="location"),
        InlineKeyboardButton("📅 Duration", callback_data="course_duration"),
        InlineKeyboardButton("💼 Internship", callback_data="internship"),
        InlineKeyboardButton("💻 Code Camp", callback_data="code_camp"),
        InlineKeyboardButton("📝 Enroll", callback_data="enroll"),
        InlineKeyboardButton("🗒️ Check Certificate", callback_data="certificate"),
        InlineKeyboardButton("❓ Help", callback_data="help"),
        InlineKeyboardButton("🚪 Exit", callback_data="exit")
    )
    return markup

# Handling the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, 
        "Welcome to Xdezo Bot! I will help you to find the suitable courses for you in Xdezo Technologies. Click a button below to get started:",
        reply_markup=main_menu()
    )

# Handling button clicks using callback queries
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    responses = {
        "courses": "We have 15 courses available for you: \n1. Complete Graphics Design Masterclass Course \n2. Complete UI/UX Design Masterclass Course\n3. Full Stack Web Development with PHP Laravel Course \n4. Full Stack Web Development with Python Django Course \n5. Mobile App Development with Dart and Flutter including NodeJS \n6. MERN Full Stack Web Development Course \n7. Complete Digital Marketing Masterclass Course \n8. Complete SEO Masterclass Course \n9. Complete Python Programming Course \n10. Complete Java Programming Course \n11. Front-End Development with React JS Course \n12. Back-End Development with PHP Laravel Course \n13. Back-End Development with Python Django Course \n14. Complete Photography with Photoshop Course \n15. Complete WordPress Development Course ",
        "price": "The price of each course is Rs. 30000/- only. There will be a 30% discount on each course. If you want to pay the full payment at the time, you will get an extra 10% discount. So the course fee will be Rs. 18000. If you are coming with a group of 5 or more, you will get an additional 5% discount on each course. So the course fee will be Rs. 15000/- only.",
        "contact": "You can contact us at 📞 061591922 or email us at: xdezotechnologies@gmail.com",
        "location": "📍 We are located at: Way to Ratna Chowk, Sugam Marga, Pokhara 33700.",
        "course_duration": "Each course lasts 2 months, 5 days a week (Sunday-Thursday), 1 hour per day.",
        "internship": "After completing a course, students can apply for a 5-day-a-week internship from 11:00-15:00 with a certification.",
        "code_camp": "Code Camp and design assessment are mandatory to evaluate students' skills. Certificates are awarded upon completion.",
        "certificate": "Please enter your certification ID to verify it.",
        "help": "Use the buttons below to get information about courses, price, location, and more.",
        "exit": "Thank you for using Xdezo Bot! Hope to see you soon. 👋"
    }

    if call.data in responses:
        bot.send_message(call.message.chat.id, responses[call.data], reply_markup=main_menu())
    
    # Handle enroll button press
    if call.data == "enroll":
        bot.send_message(call.message.chat.id, "Let's start your enrollment! Please enter your full name:")
        ENROLLMENT_STATE[call.message.chat.id] = {"step": "name"}

# Handling the certification ID verification
@bot.message_handler(func=lambda message: message.text.startswith("CERT"))
def verify_certificate(message):
    cert_id = message.text.strip()
    if cert_id in VALID_CERT_IDS:
        bot.send_message(message.chat.id, f"✅ Certification ID {cert_id} is VALID and issued to {VALID_CERT_IDS[cert_id]} by Xdezo Technologies.")
    else:
        bot.send_message(message.chat.id, "❌ Invalid Certification ID. Please check and try again.")

# Handling the enrollment process
@bot.message_handler(func=lambda message: message.chat.id in ENROLLMENT_STATE)
def enrollment_process(message):
    chat_id = message.chat.id
    step = ENROLLMENT_STATE[chat_id]["step"]

    if step == "name":
        ENROLLMENT_STATE[chat_id]["name"] = message.text
        bot.send_message(chat_id, "Enter your email:")
        ENROLLMENT_STATE[chat_id]["step"] = "email"

    elif step == "email":
        ENROLLMENT_STATE[chat_id]["email"] = message.text
        bot.send_message(chat_id, "Enter your phone number:")
        ENROLLMENT_STATE[chat_id]["step"] = "phone"

    elif step == "phone":
        ENROLLMENT_STATE[chat_id]["phone"] = message.text
        bot.send_message(chat_id, "Enter the course you want to enroll in:")
        ENROLLMENT_STATE[chat_id]["step"] = "course"

    elif step == "course":
        ENROLLMENT_STATE[chat_id]["course"] = message.text

        # Save to MariaDB
        cursor.execute(
            "INSERT INTO enrollments (name, email, phone, course) VALUES (%s, %s, %s, %s)",
            (ENROLLMENT_STATE[chat_id]["name"], ENROLLMENT_STATE[chat_id]["email"], ENROLLMENT_STATE[chat_id]["phone"], ENROLLMENT_STATE[chat_id]["course"])
        )
        db.commit()

        bot.send_message(chat_id, f"✅ Enrollment successful!\n"
                                  f"👤 Name: {ENROLLMENT_STATE[chat_id]['name']}\n"
                                  f"📧 Email: {ENROLLMENT_STATE[chat_id]['email']}\n"
                                  f"📞 Phone: {ENROLLMENT_STATE[chat_id]['phone']}\n"
                                  f"📚 Course: {ENROLLMENT_STATE[chat_id]['course']}\n"
                                  "We will contact you soon!")

        # Remove user from the enrollment state
        del ENROLLMENT_STATE[chat_id]


# Running the bot
while True:
    try:
        bot.polling(none_stop=True, interval=0.5)
    except Exception as e:
        print(f"Error: {e}")
