help_message = 'Привет\nЯ помогу тебе в дтп! тебе нужно отвечать на вопросы и читать.\nВ путь к огромной страховке!'
start_message = 'Привет я создан чтобы помогать в дтп. Начнём?'
messages = {
        0 : "Вы попали в ДТП?",
        1 : "Есть ли второй участник ДТП?",
        2 : "Заглушите автомобиль, включите аварийку, установите аварийный знак не менее,чем за 5 метров от ТС.\nЕсть ли пострадавшие при аварии?",
        3 : "Незамедлительно вызовите скорую и постарайтесь оказать первую помощь пострадавшим.\nМешаете ли вы дорожному движению?",
        4 : "Мешаете ли вы дорожному движению?",
        5 : "Зафиксировать повреждения, наиболее  полно отобразить на снимке произошедшее.\n(Снимок повреждений общим планом и детальным)",
        6 : "Прости, мне нечем тебе помочь, обращайся при дтп!",
        7 : "Оставьте машины в их текущем положении",
        8 : "Зафиксировать повреждения, наиболее  полно отобразить на снимке произошедшее.\n(Снимок повреждений общим планом и детальным).\nНанесенный ущерб менее 400 тыс.р?",
        9 : "Оставьте машины в их текущем положении.\nНанесенный ущерб менее 400 тыс.р?",
        10 : "Дожидаемся наряд ДПС",
        11 : "У второго участника есть действительный страховой полис ОСАГО?",
        12 : "Вы можете самостоятельно оформить европротокол или вызвать аварийных комиссаров",
        13 : "ДТП произошло с другим ТС?",
        14 : "Зафиксируйте повреждения. Вызовите ГАИ, лишь после этих действий вы можете оформлять европротокол с владельцем ТС",
        15 : "При отсутствии пострадавших, тем не менее необходимо включить аварийку, выставить знак и вызвать ГАИ",
        }
def start():
    print(help_message)
    print(start_message)
    print(messages[0])
    a = input().lower()
    if a == "да" or a == "yes":
      analize()
    else:
        print(messages[6])
def analize():
    print(messages[1])
    b = input().lower()
    if b == "да" or b == "yes":
        print(messages[2])
        c = input().lower()
        if c == "да" or c == "yes":
            print(messages[3])
            e = input().lower()
            if e == "да" or e == "yes":
                print(messages[5])
            else:
                print(messages[7])
        else:
            print(messages[4])
            doings()
    else:
        print(messages[13])
        other()
def other():
    d = input().lower()
    if d == "да" or d == "yes":
        print(messages[14])
    else:
        print(messages[15])
def doings():
    f = input().lower()
    if f == "да" or f == "yes":
        print(messages[8])
        g = input().lower()
        if g == "да" or g == "yes":
            print(messages[11])
            h = input().lower()
            if h == "да" or h == "yes":
                print(messages[12])
            else:
                print(messages[10])
        else:
            print(messages[10])
    else:
        print(messages[9])
        profit()
def profit():
    i = input().lower()
    if i == "да" or i == "yes":
        print(messages[12])
    else:
        print(messages[14])

start()
