def send_email(massage, recipient, sender = "university.help@gmail.com"):
    log_ = False
    log_2 = False
    log_3 = True
    for i in sender:
        for j in recipient:
            if i == "@" and j == "@":
                log_ = True
    if (recipient[-4:] == ".com" or recipient[-3:] == ".ru" or recipient[-4:] == ".net") and \
            (sender[-4:] == ".com" or sender[-3:] == ".ru" or sender[-4:] == ".net"):
        log_2 = True
    if sender != "university.help@gmail.com":
        log_3 = False

    if log_ != True or log_2 != True:
        print( "Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif log_3 == False:
        print( "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
    elif log_ == True and log_2 == True:
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')