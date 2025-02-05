import telebot

# API Token for the bot that what created in BotFather
API_TOKEN = '7670771467:AAH9Skw-LmgG24zOgRRMu6RSTQkLnyvcBow'
# Creating a bot object
bot = telebot.TeleBot(API_TOKEN)

# Handling the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Xdezo Bot! I will help you to find the suitable courses for you in Xdezo Academy. Just type /courses to get started.")

# Handling the /courses command
@bot.message_handler(commands=['courses']) 
def send_courses(message):
    bot.reply_to(message, "We have 15 courses available for you: \n1. Complete Graphics Design Masterclass Course \n2. Complete UI/UX Design Masterclass Course\n3. Full Stack Web Development with PHP Laravel Course \n4. Full Stack Web Development with Python Django Course \n5. Mobile App Development with Dart and Flutter including NodeJS \n6. MERN Full Stack Web Development Course \n7. Complete Digital Marketing Masterclass Course \n8. Complete SEO Masterclass Course \n9. Complete Python Programming Course \n10. Complete Java Programming Course \n11. Front-End Development with React JS Course \n12. Back-End Development with PHP Laravel Course \n13. Back-End Development with Python Django Course \n14. Complete Photography with Photoshop Course \n15. Complete WordPress Development Course  ")   

#Handeling the /price command
@bot.message_handler(commands=['price'])
def send_price(message):
    bot.reply_to(message, "The price of each courses is Rs. 30000/- only. There will be 30% discount on each course. If you want to pay the ful payment at time you will get extra 10% of discount. So the course fee with be Rs.18000. If you are coming with a group of 5 or more you will get more 5% discount on each course. So the course fee will be Rs.15000/- only.")

#Handling the /contact command
@bot.message_handler(commands=['contact'])
def send_contact(message):
    bot.reply_to(message, "You can contact us on phonenumber 061591922 or email us at: academy@xdezo.com")

#Handeling the /location command
@bot.message_handler(commands=['location'])
def send_location(message):
    bot.reply_to(message, "We are located at: Way to Ratna Chowk, Sugam Marga, Pokhara 33700 (Opposite to Ratna Jyoti School)")  

#Handeling the /course_duration command
@bot.message_handler(commands=['course_duration'])
def send_course_duration(message):
    bot.reply_to(message, "The duration of each course is 2 months. The classes will be held 5 days a week from Sunday-Thrusday. The classes will be 1hour per day. The classes will be held in both online and offline mode.")    

#handeling the /internship command
@bot.message_handler(commands=['internship'])
def send_internship(message):
    bot.reply_to(message, "After completing the enrolled courses the students well be able to apply for the intership. Internship will be 5days in a week (Sunday-Throusday) from 11:00-15:00. The students will be provided with the certificate after the completion of the internship.")

#handeling the /code_camp command
@bot.message_handler(commands=['code_camp'])
def send_code_camp(message):
    bot.reply_to(message, "Code Camp and design assessment will be held for course enrolled students. They must have to attend the code camp and design assessment.The purpose of this test is to evaluate students abilities and skills. The students will be provided with the certificate after the completion of the code camp and design assessment. ")


#Handeling the /enroll command
@bot.message_handler(commands=['enroll'])
def send_enroll(message):
    bot.reply_to(message, "You can enroll in the courses by visiting our office at RatnaChowk, Pokhara, Nepal")
# Handling the /help command
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "You can use the following commands: \n1. /start - To start the bot \n2. /courses - To get the list of courses \n3. /price - To get the price of courses \n4. /contact - To get the contact information \n5. /location - To get the location of Xdezo Academy \n6. /course_duration - To get the duration of courses \n7. /internship - To get the information about internship \n8. /code_camp - To get the information about code camp \n9. /enroll - To get the information about enrollment")


#handle the /exit command
@bot.message_handler(commands=['exit'])
def send_exit(message):
    bot.reply_to(message, "Thank you for using Xdezo Bot. Hope to see you soon.")

# Handling all other messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Running the bot
bot.polling()       