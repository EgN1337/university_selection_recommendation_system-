import telebot
from telebot import types
import main, subjects_matcher, points_matcher, dormitory_matcher, activities_matcher

token = '6550268003:AAFr52wDo6WxQWyCXso3UJV1xEj9i2Tk3Ec'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def get_started(message):
    par_name = bot.send_message(message.chat.id,
                                text="Добрый день, абитуриент! Вас приветствует бот по подбору Вашей будущей Альма-Матер! Как я могу обращаться к Вам?")
    bot.register_next_step_handler(par_name, user_name_getter)
    

@bot.message_handler(commands=['rules'])
def get_rules_started(message):
    rule_command = bot.send_message(message.chat.id,
                                text="Добрый день, админ! Вы вошли в режим администрирования правил рекомендательной системы. Вы можете написать ВСЕ ПРАВИЛА, чтобы посмотреть все правила, хранимые на сервере или же Вы можете ДОБАВИТЬ или УДАЛИТЬ существующее правило.")
    bot.register_next_step_handler(rule_command, rule_editor)
    
def rule_editor(message):
    if message.text == "Все правила":
        bot.send_message(message.chat.id, text= str(main.rules_printer()))
    elif message.text == "Добавить":
        first_op_adder(message)
    elif message.text == "Удалить":
        rule_deleter(message)
    else:
        bot.send_message(message.chat.id, text=f"Такой команды взаимодействия с правилами нет. Повторите попытку: /rules")
    
    
def rule_deleter(message):
    id_for_delete = bot.send_message(message.chat.id, text = f"Введите ID правила, которое нужно удалить")
    bot.register_next_step_handler(id_for_delete, next_step_adder)
    
def next_step_adder(message):
    try:
        main.rule_deleter(str(message.text))
        bot.send_message(message.chat.id, text = f"Правило удалено!")
    except:
        bot.send_message(message.chat.id, text = f"Ошибка!")

left_value = ""

def first_op_adder(message):
    first_op = bot.send_message(message.chat.id, text = f"Введите Ваше правило по шаблону: <   Данное1   Оператор    Данное2   >")
    bot.register_next_step_handler(first_op, argument_adder)
    
def argument_adder(message):
    left_value = str(message.text)
    bot.send_message(message.chat.id, text = f"Правило добавлено успешно")
    main.rule_adder(left_value)


def user_name_getter(message):
    main.name = message.text
    par_subjects = bot.send_message(message.chat.id, text=f"Отлично, {main.name}, какие предметы Вы сдавали?")
    main.label = True
    bot.register_next_step_handler(par_subjects, user_subjects_getter)



def user_subjects_getter(message):
    if (main.label == True):
        main.subjects = message.text
    par_points = bot.send_message(message.chat.id, text="Какое количество баллов Вам удалось набрать?")
    bot.register_next_step_handler(par_points, user_points_getter)


def user_points_getter(message):
    try:
        main.points = int(message.text)
        par_additional_points = bot.send_message(message.chat.id,
                                             text="Если у Вас есть дополнительные баллы (золотая медаль, олимпиады и так далее), " +
                                             "то, пожалуйста, введите их. Если нет, достаточно написать :Нет:")
        bot.register_next_step_handler(par_additional_points, user_additional_points_getter)
    except:
        main.label = False
        bot.send_message(message.chat.id, text="Вы ввели некорректное число баллов. Пожалуйста, повторите.")
        user_subjects_getter(message)

def user_additional_points_getter(message):
    try:
        main.additional_points = int(message.text)
    except:
        main.additional_points = int(0)
    par_city = bot.send_message(message.chat.id, text="Укажите город, в котором вы проживаете")
    bot.register_next_step_handler(par_city, user_city_getter)

def user_city_getter(message):
    main.city = message.text
    new_city = bot.send_message(message.chat.id, text= "Вы собираетесь учиться в другом городе?")
    bot.register_next_step_handler(new_city, user_new_city_getter)
    
def user_new_city_getter(message):
    main.new_city = message.text
    par_residence = bot.send_message(message.chat.id, text="Скажите, есть ли необходимость в общежитии?")
    bot.register_next_step_handler(par_residence, user_residence_wish_getter)


def user_residence_wish_getter(message):
    main.residence = message.text
    bot.send_message(message.chat.id,
                     text=f"Все данные о Вас получены, {main.name}. Генерируем результат... Ожидайте...")
    name = main.name
    subjects = main.subjects
    points = main.points
    additional_points = main.additional_points
    city = main.city
    new_city = main.new_city
    residence = main.residence
    if residence == 'Да':
        result_residence = "Есть необходимость в предоставлении общежития"
    else:
        result_residence = "Нет необходимости в предоставлении общежития"

    bot.send_message(message.chat.id, text=f"Информация о Вас: \n"
                                           f"Ваше имя: {name}; \n"
                                           f"Город проживания: {city}; \n"
                                           f"Готовность к переезду в другой город: {new_city}; \n"
                                           f"Предметы, которые Вы сдавали: {subjects}; \n"
                                           f"Количество баллов за предметы: {points}; \n"
                                           f"Дополнительные баллы: {additional_points}; \n"
                                           f"Общее количество баллов: {str(int(points) + int(additional_points))}; \n"
                                           f"{result_residence}.")
    main.print_current_result()
    main.minimum_distance_between_city()
    
    
    distance_dict = main.nearest_city_to_live_finder()
    subjects_dict = subjects_matcher.subjects_matcher(main.subjects)
    points_dict   = points_matcher.points_matcher(main.points , main.additional_points)
    dorm_dict     = dormitory_matcher.dorm_matcher(main.residence)
    activity_dict = activities_matcher.act_matcher()
    
    result_dict = {}
    for item in distance_dict:
        result_dict[f'{item[0]}'] = item[1]
        
    for item in subjects_dict:
        result_dict[f'{item[0]}'] = float(result_dict.get(f'{item[0]}')) + float(item[2]/3)
        
    for item in points_dict:
        result_dict[f'{item[0]}'] = float(result_dict.get(f'{item[0]}')) + float(item[2]/3)
        
    for item in dorm_dict:
        result_dict[f'{item[0]}'] = float(result_dict.get(f'{item[0]}')) + item[1]
        
    for item in activity_dict:
        result_dict[f'{item[0]}'] = float(result_dict.get(f'{item[0]}')) + item[1]
        
        
    print(distance_dict)
    print(subjects_dict)
    print(points_dict)
    print(dorm_dict)
    print(activity_dict)
    
    print(" ")
    sort_data = sorted(result_dict.items(), key=lambda x: x[1], reverse=True)
    sort_data_dict = dict(sort_data)
    print(sort_data_dict)
    
    bot.send_message(message.chat.id, text=f"Поздравляем! Наиболее подходящий Вам университет найден! Это - {list(sort_data_dict.keys())[0]} с вероятностью {float(float(list(sort_data_dict.values())[0])*100/4)}")
    bot.send_message(message.chat.id, text=f"Топ 5 наиболее подходящих Вам вуз-ов: \n"
                                           f"1) {list(sort_data_dict.keys())[0]} с вероятностью {float(float(list(sort_data_dict.values())[0])*100/4)}; \n"
                                           f"2) {list(sort_data_dict.keys())[1]} с вероятностью {float(float(list(sort_data_dict.values())[1])*100/4)}; \n"
                                           f"3) {list(sort_data_dict.keys())[2]} с вероятностью {float(float(list(sort_data_dict.values())[2])*100/4)}; \n"
                                           f"4) {list(sort_data_dict.keys())[3]} с вероятностью {float(float(list(sort_data_dict.values())[3])*100/4)}; \n"
                                           f"5) {list(sort_data_dict.keys())[4]} с вероятностью {float(float(list(sort_data_dict.values())[4])*100/4)}; \n"
                                           f"Спасибо за то, что пользуетесь нашим ботом! ")
    bot.send_message(message.chat.id, text=f"Для возобновления работы бота нужно повторно написать /start")


bot.polling(none_stop=True)
