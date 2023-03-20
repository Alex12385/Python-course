def OutputAll():

    with open('file.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)


def Search(data):
    with open('file.txt', 'r', encoding='utf-8') as file:
        flag = False
        for line in file:
            if data in line:
                print(line)
                flag = True
        if flag == False:
            print('\n не найдено \n')


def Delete(data):
    with open('file.txt', 'r', encoding="utf-8") as file:
        data = data.lower()
        lines = file.readlines()
        with open('file.txt', 'w', encoding="utf-8") as file:
            for line in lines:
                if data in line.lower():
                    print('\n Контакт удалён! \n')
                else:
                    file.write(line)


def Edit(data):
    with open('file.txt', 'r', encoding="utf-8") as file:
        data = data.lower()
        lines = file.readlines()
        with open('file.txt', 'w', encoding='utf8') as file:
            for line in lines:
                if data in line.lower():
                    new_data = line.split(':')
                    if data in new_data[0].lower():
                        new_data[0] = (input('Введите новое ФИО: ').title())
                    elif data in new_data[1].lower():
                        new_data[1] = (input('Введите новый номер телефона: ').title())
                    new_line = new_data[0] + ':' + new_data[1] + '\n'
                    line = line.replace(line, new_line)
                file.writelines(line)
    print('\n Данные контакта изменены! \n')
