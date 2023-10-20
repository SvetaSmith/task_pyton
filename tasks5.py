token =""

import telebot
import random

bot = telebot.TeleBot(token)

HELP = """
/help - напечатать справку
/add - добавить задачу
/show  -  показать список задач на дату
/random - добавить случайную задачу"""

RANDOM_TASKS = ["Записаться на курс",
                "Почитать книгу",
                "Посмотреть фильм",
                "Поесть"]

tasks={}

def add_todo(date,task):
  if date in tasks :
    tasks[date].append(task)
  else:
    tasks[date] = []
    tasks[date] = [task]

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['add','todo'])
def add(message):
    command = message.text.split(maxsplit=2)
    if len(command)==1:
        text = "Введите дату и задачу"
    if len(command)==2:
        text = "Введите задачу"
    if len(command)>2:
        date = command[1].lower()
        task = command[2]
        if len(task)>2:
            add_todo(date,task)
            text = "задача " + task + " добавлена на дату " +date
        else:
            text ="Ошибка, введите более длинное название задачи"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['random'])
def random_add(message):
    date = "today"
    task = random.choice(RANDOM_TASKS)
    add_todo(date,task)
    text = "задача " + task + " добавлена на дату " +date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['show'])
def show(message):
    command = message.text.split(maxsplit=1)

    if len(command)<2:
        bot.send_message(message.chat.id, 'введите дату')
    else :
        date = command[1].lower()
        text =''
        if date in tasks:
            text=date.upper() + "\n"
            for task in tasks[date]:
                text = text + '[] ' + task+ "\n"
        else :
            text = "задач на эту дату нет"
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['print'])
def print_com(message):
    command = message.text.split(maxsplit=1)
    text =''
    if len(command)<2:
        text = 'введите дату или список дат'
        bot.send_message(message.chat.id, text)
    else:
        dateList = command[1:len(command)][0].split()
        for date in dateList:
            if date in tasks:
                text= text +date.upper() + "\n"
                for task in tasks[date]:
                    text = text + '[] ' + task+ "\n"
            else :
                text = "задач на эту дату нет"
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)


