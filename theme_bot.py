from webbrowser import get
import telebot
import get_data as gd


bot = telebot.TeleBot('5982175377:AAE0_kRqWN6XtASVJBjtygqoMu5GMPMSXxA')
global categories, sub_categories
categories, sub_categories = gd.load_data()
global cur_cat
cur_cat = 0
global cur_theme
cur_theme = 0


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global cur_cat, cur_theme, categories, sub_categories
    splitted_text = str(message.text).lower().split()
    if str(message.text).lower() == "привет":
        bot.send_message(
            message.from_user.id, "Привет, чем я могу тебе помочь? Для информации введите /help.")
    elif cur_cat == -1:
        # str1 = gd.get_sub_categories(sub_categories, cur_cat)
        if str(message.text).isdigit():
            cur_cat = int(message.text)
            str1 = gd.get_sub_categories(sub_categories, cur_cat)
            cur_theme = -1
            bot.send_message(
                message.from_user.id, str1)
        else:
            bot.send_message(
                message.from_user.id, "не верно введен номер категорий темы")
    elif cur_theme == -1:
        if str(message.text).isdigit():
            cur_theme = int(message.text)
            data = gd.get_desc(sub_categories, cur_theme)
            cur_cat = 0
            cur_theme = 0
            for item in data:
                desc = item[0]
                img = item[1]
                bot.send_message(
                    message.from_user.id, desc)
                bot.send_photo(chat_id=message.from_user.id, photo=open(img, 'rb'))

        else:
            bot.send_message(
                message.from_user.id, "не верно введен номер достопремичательности")
    elif str(message.text).lower() == "/quest":
        cur_cat = -1
        str1 = gd.get_categories(categories)
        bot.send_message(
            message.from_user.id, str1)
    elif str(message.text).lower() == "/help":
        bot.send_message(
            message.from_user.id, "Описание проекта \n Для того чтобы начать введите слово /quest.")
    else:
        bot.send_message(message.from_user.id, "Для информации введите /help.")


if __name__ == '__main__':
    cur_cat = 0
    cur_theme = 0
    bot.polling(none_stop=True, interval=0)
