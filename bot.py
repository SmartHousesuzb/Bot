#!/usr/bin/env python
import telebot
import os

TOKEN = '735757926:AAFi7LDidiaceZvPDzFBxlRNNFj64lhUYeU'

bot = telebot.TeleBot(TOKEN)


def log(message, answer):
    print('\n')
    from datetime import datetime
    print(datetime.now())
    print('Сообщение от {0} , (id = {1}) \n Текст - {2}'.format(message.from_user.first_name, str(message.from_user.id),
                                                                message.text))
    print(answer)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    rus = '🇷🇺Русский'
    uzb = "🇺🇿O'zbek tili"
    us = '🇺🇸English'
    user_markup.row(rus, us)
    user_markup.row(uzb)
    answer = '\n\n🇷🇺 Пожалуйста, выберите ваш язык' \
             '\n\n🇺🇸 Please select your language' \
             '\n\n🇺🇿 Iltimos, tilingizni tanlang'
    log(message, answer)
    bot.send_message(message.from_user.id, answer, reply_markup=user_markup)


@bot.message_handler(commands=['gh'])
def send_welcome(message):
    answer = 'Говно'
    log(message, answer)
    bot.reply_to(message, answer)


@bot.message_handler(commands=['mbc'])
def send_welcome(message):
    answer = 'Говно'
    log(message, answer)
    bot.reply_to(message, answer)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    answer = '@artykov013'
    log(message, answer)
    bot.reply_to(message, answer)


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    # Русский язык
    if message.text == '🇷🇺Русский':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('🏙Жилые комплексы', '🎁Бонусы , акции')
        user_markup.row('📞Наши контакты', '🗺Локация')
        user_markup.row('🔙 🌍')
        answer = '🇷🇺Русский язык' \
                 '\n\nЗдравствуйте вас приветствует \nкомпания OOO "SMARTHOUSES"' \
                 '\n\nНаше удобное меню поможет \nвам узнать всю подробную \nинформацию о наших проектах' \
                 '\n\nСпасибо за внимание'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '🎁Бонусы , акции':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Главное меню')
        answer = '🎁Скидка 40 млн сум при покупке квартиры на втором этаже'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '🗺Локация':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Офис', '🏙ЖК "OLMAZOR"')
        user_markup.row('⬅Главное меню')
        answer = '🗺Локация'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '🏙ЖК "OLMAZOR"':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Главное меню')
        answer = '🗺Локация'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
        bot.send_location(message.from_user.id, 41.3522330, 69.2198860)
    elif message.text == 'Офис':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Главное меню')
        answer = '🗺Локация'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
        bot.send_location(message.from_user.id, 41.3343450, 69.2279560)
    elif message.text == '📞Наши контакты':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Главное меню')
        answer = 'Контактный номер :\n+998 94 666 64 44\n+998 78 122 05 05' \
                 '\nТелеграм канал :\n@smarthouses1' \
                 '\nFacebook : \nhttps://www.facebook.com/smarthousesuz/' \
                 '\nInstagram: https://www.instagram.com/smart.houses/'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == 'Скоро':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Назад')
        answer = '🕑Скоро'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '🏙Жилые комплексы':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('ЖК "OLMAZOR"')
        user_markup.row('Скоро')
        user_markup.row('Скоро')
        user_markup.row('⬅Главное меню')
        answer = '🏙Жилые комплексы'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '⬅Главное меню':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('🏙Жилые комплексы', '🎁Бонусы , акции')
        user_markup.row('📞Наши контакты', '🗺Локация')
        user_markup.row('🔙 🌍')
        answer = '🇷🇺Русский' \
                 '\n\nГлавное меню'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == 'ЖК "OLMAZOR"':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('📋Информация\nо ЖК "OLMAZOR"', 'Фотогалерея\nЖК "OLMAZOR"')
        user_markup.row('🏢Квартиры', '💳Цены')
        user_markup.row('⬅Назад')
        answer = '🇷🇺Русский' \
                 '\n\nГлавное меню'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '📋Информация\nо ЖК "OLMAZOR"':
        answer = "🇷🇺Русский" \
                 '\n\nЖилой комплекс "ОЛМАЗОР" \nТихо и уютно \nПредставляем вам жилой комплекс "ОЛМАЗОР", расположенный в одном из уютных районов города.' \
                 'Комплекс расположен вдали от городского шума и дает каждому гражданину полное спокойствие.' \
                 'Инфраструктура вокруг комплекса хорошо развита, супермаркеты, школы, детские сады и парки развлечений находятся в очень коротком радиусе.' \
                 'Территория нашего комплекса включает детские площадки, зеленую зону, беседки и камеры видеонаблюдения по всему комплексу.' \
                 'Во всех квартирах были установлены два контурных котла, радиаторы и входные двери от турецкой бренда "EVEREST", а в доме была установлена немецкая компания "safereach".'
        log(message, answer)
        bot.send_message(message.from_user.id, answer)
    elif message.text == '⬅Назад':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('ЖК "OLMAZOR"')
        user_markup.row('Скоро')
        user_markup.row('Скоро')
        user_markup.row('⬅Главное меню')
        answer = '🇷🇺Русский' \
                 '\n\nЖК "OLMAZOR"'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '⬅Назад':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Главное меню')
        answer = '🇷🇺Русский' \
                 '\n\nCкоро'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '🏢Квартиры':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('35.5 м²', '67 м²', '94.8 м²')
        user_markup.row('50 м²', '72 м²', '95 м²')
        user_markup.row('53.7 м²', '74 м²', '103.6 м²')
        user_markup.row('53.9 м²', '75.7 м²', '112.6 м²')
        user_markup.row('54.9 м²', '76.2 м²', '119.6 м²')
        user_markup.row('65.7 м²', '82.7 м²', '122.2 м²')
        user_markup.row('⬅Предыдущее меню')
        answer = '🇷🇺Русский' \
                 '\n\nЖК "OLMAZOR"'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '💳Цены':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('1 этаж')
        user_markup.row('2 этаж')
        user_markup.row('3 этаж')
        user_markup.row('4 этаж')
        user_markup.row('5 этаж')
        user_markup.row('6 этаж')
        user_markup.row('7 этаж')
        user_markup.row('8 этаж')
        user_markup.row('⬅Предыдущее меню')
        answer = '🇷🇺Русский' \
                 '\n\nЖК "OLMAZOR"'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '1 этаж':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Вернуться')
        answer = 'Не жилой'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '2 этаж':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Вернуться')
        answer = '7 000 000 за м²'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '3 этаж':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Вернуться')
        answer = '6 000 000 за м²'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '4 этаж':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Вернуться')
        answer = '5 500 000 за м²'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '5 этаж':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Вернуться')
        answer = '4 900 000 за м²'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '6 этаж':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Вернуться')
        answer = '4 700 000 за м²'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '7 этаж':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Вернуться')
        answer = 'Нет в продаже'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '8 этаж':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Вернуться')
        answer = 'Нет в продаже'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '⬅Вернуться':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('1 этаж')
        user_markup.row('2 этаж')
        user_markup.row('3 этаж')
        user_markup.row('4 этаж')
        user_markup.row('5 этаж')
        user_markup.row('6 этаж')
        user_markup.row('7 этаж')
        user_markup.row('8 этаж')
        user_markup.row('⬅Предыдущее меню')
        answer = '🇷🇺Русский' \
                 '\n\nГлавное меню'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '⬅Предыдущее меню':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('📋Информация\nо ЖК "OLMAZOR"', 'Фотогалерея\nЖК "OLMAZOR"')
        user_markup.row('🏢Квартиры', '💳Цены')
        user_markup.row('⬅Назад')
        answer = '🇷🇺Русский'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    # Английский язык
    elif message.text == '🇺🇸English1':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('🔙 🌍')
        answer = '🇺🇸English' \
                 '\n\nOn developing' \
                 '\n\nThanks for your attention'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '🇺🇸English':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('🏙Residential complexes', '🎁Bonuses and promotions')
        user_markup.row('📞Contacts\nSocial networks', '🗺Location')
        user_markup.row('🔙 🌍')
        answer = '🇺🇸English' \
                 '\n\nOur convenient menu will help \nyou to find out all the detailed \ninformation of our company.' \
                 '\n\nThanks for your attention'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '🎁Bonuses and promotions':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Main menu')
        answer = '🎁40 million discount when buying an apartment on the second floor'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '🗺Location':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Office', 'Residential complex\n"OLMAZOR"')
        user_markup.row('⬅Main menu')
        answer = '🗺Location'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == 'Residential complex\n"OLMAZOR"':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Main menu')
        answer = '🗺Location'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
        bot.send_location(message.from_user.id, 41.3522330, 69.2198860)
    elif message.text == 'Office':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Main menu')
        answer = '🗺Location'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
        bot.send_location(message.from_user.id, 41.3343450, 69.2279560)
    elif message.text == '📞Contacts\nSocial networks':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Main menu')
        answer = 'Call center :\n+998 94 666 64 44\n+998 78 122 05 05' \
                 '\nTelegram channel :\n@smarthouses1' \
                 '\nFacebook : \nhttps://www.facebook.com/smarthousesuz/' \
                 '\nInstagram: https://www.instagram.com/smart.houses/'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '🏙Residential complexes':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Residential Complex "Olmazor"')
        user_markup.row('Soon')
        user_markup.row('Soon')
        user_markup.row('⬅Main menu')
        answer = '🏙Residential complexes'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '⬅Main menu':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('🏙Residential complexes', '🎁Bonuses and promotions')
        user_markup.row('📞Contacts\nSocial networks', '🗺Location')
        user_markup.row('🔙 🌍')
        answer = '🇺🇸English' \
                 '\n\nMain menu'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == 'Residential Complex "Olmazor"':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('📋Information\n"OLMAZOR"', 'Portfolio "OLMAZOR"')
        user_markup.row('Apartments', '💳Prices')
        user_markup.row('⬅Back')
        answer = '🇺🇸English' \
                 '\n\nResidential Complex "Olmazor"'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '⬅Previous menu':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('📋Information\n"OLMAZOR"', 'Portfolio "OLMAZOR"')
        user_markup.row('🏢Apartments', '💳Prices')
        user_markup.row('⬅Back')
        answer = '🇺🇸English' \
                 '\n\nResidential Complex "Olmazor"'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '📋Information\n"OLMAZOR"':
        answer = "🇺🇸English" \
                 '\n\nResidential complex "OLMAZOR"\nQuiet and comfortable\nWe present you a residential complex "OLMAZOR", located in one of the cozy areas of the city. The complex is located away from the city noise and gives every citizen complete peace of mind. The infrastructure around the complex is well developed, supermarkets, schools, kindergartens and amusement parks are in a very short radius. The territory of our complex includes playgrounds, a green zone, gazebos and video surveillance cameras throughout the complex. In all the apartments two contour boilers, radiators and entrance doors from the Turkish nonsense "EVEREST" were installed, and the German company "safereach" was installed in the house.'
        log(message, answer)
        bot.send_message(message.from_user.id, answer)
    elif message.text == '⬅Back':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Residential Complex "Olmazor"')
        user_markup.row('Soon')
        user_markup.row('Soon')
        user_markup.row('⬅Main menu')
        answer = '🇺🇸English' \
                 '\n\nResidential Complexes'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == 'Soon':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Back')
        answer = '🇺🇸English' \
                 '\n\nSoon'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '💳Prices':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('1 floor')
        user_markup.row('2 floor')
        user_markup.row('3 floor')
        user_markup.row('4 floor')
        user_markup.row('5 floor')
        user_markup.row('6 floor')
        user_markup.row('7 floor')
        user_markup.row('8 floor')
        user_markup.row('⬅Previous menu')
        answer = '🇺🇸English' \
                 '\n\n"OLMAZOR"'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '⬅Turn back':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('1 floor')
        user_markup.row('2 floor')
        user_markup.row('3 floor')
        user_markup.row('4 floor')
        user_markup.row('5 floor')
        user_markup.row('6 floor')
        user_markup.row('7 floor')
        user_markup.row('8 floor')
        user_markup.row('⬅Previous menu')
        answer = '🇺🇸English' \
                 '\n\n"OLMAZOR"'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '1 floor':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Turn back')
        answer = 'Not residential'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '2 floor':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Turn back')
        answer = '7 000 000  м²'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '3 floor':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Turn back')
        answer = '6 000 000  м²'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '4 floor':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Turn back')
        answer = '5 500 000  м²'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '5 floor':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Turn back')
        answer = '4 900 000  м²'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '6 floor':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Turn back')
        answer = '4 700 000  м²'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '7 floor':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Turn back')
        answer = 'Out of stock'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '8 floor':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Turn back')
        answer = 'Out of stock'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '🏢Apartments':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('35.5 м²', '67 м²', '94.8 м²')
        user_markup.row('50 м²', '72 м²', '95 м²')
        user_markup.row('53.7 м²', '74 м²', '103.6 м²')
        user_markup.row('53.9 м²', '75.7 м²', '112.6 м²')
        user_markup.row('54.9 м²', '76.2 м²', '119.6 м²')
        user_markup.row('65.7 м²', '82.7 м²', '122.2 м²')
        user_markup.row('⬅Previous menu')
        answer = '🇺🇸English' \
                 '\n\n"OLMAZOR"'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    # Узбек тили язык
    elif message.text == "🇺🇿O'zbek tili1":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('🔙 🌍')
        answer = "🇺🇿O'zbek tili" \
                 "\n\nRivojlanish ostida" \
                 "\n\nE'tiboringiz uchun tashakkur"
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == "🇺🇿O'zbek tili":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("🏙Turar-joy komplekslari", '🎁Bonuslar va aksialar')
        user_markup.row("📞Aloqalar\nIjtimoiy tarmoqlar", '🗺Manzil')
        user_markup.row('🔙 🌍')
        answer = "🇺🇿O'zbek tili" \
                 "\n\nBizning qulay menyu sizga\nkompaniyamizning barcha ma'lumotlarini\nbilib olishingiz uchun yordam beradi." \
                 "\n\nE'tiboringiz uchun tashakkur"
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == "🎁Bonuslar va aksialar":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Asosiy menyu')
        answer = "🎁Ikkinchi qavatda kvartira sotib oladiganlarga 40 mln skidka mavjud"
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '🗺Manzil':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Ofis', '"OLMAZOR"')
        user_markup.row('⬅Asosiy menyu')
        answer = '🗺Manzil'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '"OLMAZOR"':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Asosiy menyu')
        answer = '🗺Location'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
        bot.send_location(message.from_user.id, 41.3522330, 69.2198860)
    elif message.text == 'Ofis':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Asosiy menyu')
        answer = '🗺Location'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
        bot.send_location(message.from_user.id, 41.3343450, 69.2279560)
    elif message.text == "📞Aloqalar\nIjtimoiy tarmoqlar":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Asosiy menyu')
        answer = 'Aloqa raqami :\n+998 94 666 64 44\n+998 78 122 05 05' \
                 '\nTelegram kanalimiz :\n@smarthouses1' \
                 '\nFacebook : \nhttps://www.facebook.com/smarthousesuz/' \
                 '\nInstagram: https://www.instagram.com/smart.houses/'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '🏙Turar-joy komplekslari':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Turar-joy kompleks "OLMAZOR"')
        user_markup.row('Tez orada')
        user_markup.row('Tez orada')
        user_markup.row('⬅Asosiy menyu')
        answer = '🏙Turar-joy komplekslari'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '⬅Asosiy menyu':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("🏙Turar-joy komplekslari", '🎁Bonuslar va aksialar')
        user_markup.row("📞Aloqalar\nIjtimoiy tarmoqlar", '🗺Manzil')
        user_markup.row('🔙 🌍')
        answer = "🇺🇿O'zbek tili" \
                 "\n\nAsosiy menyu"
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == 'Turar-joy kompleks "OLMAZOR"':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('📋Ma`lumot\n"OLMAZOR"', '🖼Rasmlar\n"OLMAZOR"')
        user_markup.row('Kvadratlar', '💳Narxlar')
        user_markup.row('⬅Orqaga')
        answer = "🇺🇿O'zbek tili" \
                 '\n\n🏙Turar-joy kompleks "OLMAZOR"'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '📋Ma`lumot\n"OLMAZOR"':
        answer = "🇺🇿O'zbek tili" \
                 "\n\n'OLMAZOR' uy-joy kompleksi \nQo'shimcha va qulay \n Sizga shaharning qulay maydonlaridan birida joylashgan 'OLMAZOR' uy-joy kompleksi." \
                 "Kompleks shahar shovqinidan uzoqda joylashgan va har bir fuqaroga to'la xotirjamlikni beradi." \
                 "Kompleks atrofidagi infratuzilma yaxshi rivojlangan, supermarketlar, maktablar, bolalar bog'lari va o'yin-parklar juda qisqa radiusda." \
                 "Kompleksimiz hududida o'yin maydonchalari, yashil zona, gazebos va video kuzatuv kameralari mavjud." \
                 "Barcha uylarda 'EVEREST' turk nonsensidan ikkita konturli qozon, radiator va kirish eshiklari o'rnatildi va nemis firmasi 'safereach' uyga o'rnatildi."
        log(message, answer)
        bot.send_message(message.from_user.id, answer)
    elif message.text == '⬅Oldingi menyu':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('📋Ma`lumot\n"OLMAZOR"', '🖼Rasmlar\n"OLMAZOR"')
        user_markup.row('Kvadratlar', '💳Narxlar')
        user_markup.row('⬅Orqaga')
        answer = "🇺🇿O'zbek tili" \
                 '\n\n🏙Turar-joy kompleks "OLMAZOR"'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '⬅Orqaga':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Turar-joy kompleks "OLMAZOR"')
        user_markup.row('Tez orada')
        user_markup.row('Tez orada')
        user_markup.row('⬅Asosiy menyu')
        answer = '🏙Turar-joy komplekslari'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == 'Tez orada':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Orqaga')
        answer = 'Tez orada'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '💳Narxlar':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('1 qavat')
        user_markup.row('2 qavat')
        user_markup.row('3 qavat')
        user_markup.row('4 qavat')
        user_markup.row('5 qavat')
        user_markup.row('6 qavat')
        user_markup.row('7 qavat')
        user_markup.row('8 qavat')
        user_markup.row('⬅Oldingi menyu')
        answer = "🇺🇿O'zbek tili" \
                 '\n\n"OLMAZOR"'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '⬅Orqaga qaytmoq':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('1 qavat')
        user_markup.row('2 qavat')
        user_markup.row('3 qavat')
        user_markup.row('4 qavat')
        user_markup.row('5 qavat')
        user_markup.row('6 qavat')
        user_markup.row('7 qavat')
        user_markup.row('8 qavat')
        user_markup.row('⬅Oldingi menyu')
        answer = "🇺🇿O'zbek tili" \
                 '\n\n"OLMAZOR"'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '1 qavat':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Orqaga qaytmoq')
        answer = 'Turar joy emas'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '2 qavat':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Orqaga qaytmoq')
        answer = '7 000 000  м²'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '3 qavat':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Orqaga qaytmoq')
        answer = '6 000 000  м²'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '4 qavat':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Orqaga qaytmoq')
        answer = '5 500 000  м²'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '5 qavat':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Orqaga qaytmoq')
        answer = '4 900 000  м²'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '6 qavat':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Orqaga qaytmoq')
        answer = '4 700 000  м²'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '7 qavat':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Orqaga qaytmoq')
        answer = 'Mavjud emas'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == '8 qavat':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('⬅Orqaga qaytmoq')
        answer = 'Mavjud emas'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif message.text == 'Kvadratlar':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('35.5 м²', '67 м²', '94.8 м²')
        user_markup.row('50 м²', '72 м²', '95 м²')
        user_markup.row('53.7 м²', '74 м²', '103.6 м²')
        user_markup.row('53.9 м²', '75.7 м²', '112.6 м²')
        user_markup.row('54.9 м²', '76.2 м²', '119.6 м²')
        user_markup.row('65.7 м²', '82.7 м²', '122.2 м²')
        user_markup.row('⬅Oldingi menyu')
        answer = "🇺🇿O'zbek tili" \
                 '\n\n"OLMAZOR"'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    # Отправка файлов
    elif message.text == 'Фотогалерея\nЖК "OLMAZOR"':
        directory = 'smth/photo Olmazor'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
            answer.close()
    elif message.text == 'Portfolio "OLMAZOR"':
        directory = 'smth/photo Olmazor'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
            answer.close()
    elif message.text == '🖼Rasmlar\n"OLMAZOR"':
        directory = 'smth/photo Olmazor'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
            answer.close()
    # Kvadratura
    elif message.text == '35.5 м²':
        directory = 'smth/kvadratura/35.5'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
    elif message.text == '50 м²':
        directory = 'smth/kvadratura/50.0'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
    elif message.text == '53.7 м²':
        directory = 'smth/kvadratura/53.7'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
    elif message.text == '53.9 м²':
        directory = 'smth/kvadratura/53.9'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
    elif message.text == '54.9 м²':
        directory = 'smth/kvadratura/54.9'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
    elif message.text == '65.7 м²':
        directory = 'smth/kvadratura/65.7'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
    elif message.text == '67 м²':
        directory = 'smth/kvadratura/67.0'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
    elif message.text == '72 м²':
        directory = 'smth/kvadratura/72.0'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
    elif message.text == '74 м²':
        directory = 'smth/kvadratura/74.0'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
    elif message.text == '75.7 м²':
        directory = 'smth/kvadratura/75.7'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
    elif message.text == '76.2 м²':
        directory = 'smth/kvadratura/76.2'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
    elif message.text == '82.7 м²':
        directory = 'smth/kvadratura/82.7'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
    elif message.text == '94.8 м²':
        directory = 'smth/kvadratura/94.8'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
    elif message.text == '95 м²':
        directory = 'smth/kvadratura/95.0'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
    elif message.text == '103.6 м²':
        directory = 'smth/kvadratura/103.6'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
    elif message.text == '112.6 м²':
        directory = 'smth/kvadratura/112.6'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
    elif message.text == '119.6 м²':
        directory = 'smth/kvadratura/119.6'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
    elif message.text == '122.2 м²':
        directory = 'smth/kvadratura/122.2'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            answer = open(directory + '/' + file, 'rb')
            log(message, answer)
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, answer)
    # Остальное
    elif message.text == '🔙 🌍':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        rus = '🇷🇺Русский'
        uzb = "🇺🇿O'zbek tili"
        us = '🇺🇸English'
        user_markup.row(rus, us)
        user_markup.row(uzb)
        answer = '\n\n🇷🇺 Пожалуйста, выберите ваш язык' \
                 '\n\n🇺🇿 Iltimos, tilingizni tanlang' \
                 '\n\n🇺🇸 Please select your language'
        log(message, answer)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    else:
        answer = '\n\n🇷🇺 Я вас не понял .' \
                 '\n\n🇺🇿 Men sizni tushunmadim .' \
                 '\n\n🇺🇸 I did not understand you .'
        log(message, answer)
        bot.send_message(message.from_user.id, answer)


bot.polling(none_stop=True)
