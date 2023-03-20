# Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных


while True:
    choise = int(input('Введите нужное действие: \n 1 - Добавить в справочник \
        \n 2 - Вывести всех \n 3 - Поиск по фамилии \n 4 - Изменить контакт \n 5 - удалить контакт \n 6 - Выход \n'))
    match choise: 
        case 1: 
            import input1
            input1.Input(input('Введите имя: '), input('Введите номер: '))
        case 2: 
            from output import OutputAll
            OutputAll()
        case 3:
            from output import Search
            Search(input('Введите фамилию: '))
        case 4:
            from output import Edit
            Edit(input('Введите фамилию или номер контакта, которые хотите изменить: ')) 
        case 5:
            from output import Delete
            Delete(input('Введите фамилию или номер контакта, которые хотите изменить: '))   
        case 6: break