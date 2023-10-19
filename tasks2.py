#task1
HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

tasks = []

run = True

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    print(tasks)
  elif command == "add":
    task = input("Введите название задачи: ")
    tasks.append(task)
    print("Задача добавлена")
  elif command == "exit":
    run = False
    print('Спасибо за использование! До свидания!')
  else: 
    print("Неизвестная команда")
    break

print("До свидания!")


#task2

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""


tasks = []
tod = []
tom = []
oth = []

run = True

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    print(tasks)
    print(tod)
    print(tom)
    print(oth)
  elif command == "add":
    task = input("Введите название задачи: ")
    date = input("Введите дату: ")
    if date == 'сегодня':
      tod.append(task)
    elif date == 'завтра':
      tom.append(task)
    else:
      oth.append(task)
    print("Задача добавлена")
  elif command == "exit":
    run = False
    print('Спасибо за использование! До свидания!')
  else: 
    print("Неизвестная команда")
    break

print("До свидания!")

