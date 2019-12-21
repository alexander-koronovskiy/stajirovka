import csv

SAMPLEDATA_A = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]

SAMPLEDATA_P = ["first_name,last_name,id_card".split(","),
            "Tyrese,Hirthe,6309".split(","),
            "Jules,Dicki,6815".split(","),
            "Dedric,Medhurst,3138".split(",")
            ]


# извлечение данных из файла, и перезапись их в словарь
def write_to_dict(data):
    my_list = []
    fieldnames = data[0]
    for values in data[1:]:
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)
    return fieldnames, my_list


# запись данных
def write_csv_file(path, fieldnames, data):
    with open(path, "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


# чтение csv-файла
def read_csv_file(csv_path):
    reader = csv.reader(csv_path)
    filename = ""
    for row in reader:
        filename += (" ".join(row))
    s = list()
    with open(filename, "r") as f_obj:
        for row in f_obj:
            s.append(row[:-1:].split(","))
    return s


if __name__ == "__main__":
    '''
    In_data_a
    date - дата в формате YYYY-MM-DD
    campaign - название рекламной кампании
    id - идентификатор источника рекламы
    ad_id - идентификатор баннера, который использовался в рекламной кампании
    os - операционная система мобильного устройства, на которое были совершены установки.
    installs - количество установок рекламируемого мобильного приложения
    app - название мобильного приложения

    In_data_p
    date - дата в формате YYYY-MM-DD
    campaign_id - идентификатор рекламной кампании
    ad_id - идентификатор баннера, который использовался в рекламной кампании
    spend - сумма, которая была потрачена на рекламу мобильного приложения 

    out
    app - название мобильного приложения
    date - дата в формате YYYY-MM-DD
    campaign - название рекламной кампании
    os - операционная система мобильного устройства, на которое были совершены установки
    installs -  количество установок рекламируемого мобильного приложения 
    spend - сумма потраченная на рекламу
    cpi - (cost per install) стоимость одной установки, используя значения spend и installs
    '''

    # чтение данных из файлов
    a = read_csv_file("in_data_a.csv")
    p = read_csv_file("in_data_p.csv")

    # получение наименования полей
    fields_a = write_to_dict(a)[0]
    fields_p = write_to_dict(p)[0]

    # получение полей данных
    data_a = write_to_dict(a)[1]
    data_p = write_to_dict(p)[1]

    # вывод полей
    print("data a:", fields_a, "data p:", fields_p)
    print(len(data_a), len(data_p))

    # список для вывода
    data_out = list()

    # значения 'Date', 'Campaign', 'ad_id', должны совпадать со значениями из _p
    # если совпадает - конкатенируем найденное, совмещаем все в одну строчку-словарь
    for p_i in data_p:
        for a_i in data_a:
            if a_i.get('Date')==p_i.get('date') and \
                a_i.get('Campaign')==p_i.get('campaign') and \
                    a_i.get('ad_id')==p_i.get('ad_id'):
                print(a_i.get('ad_id'))

    # убираем найденное значение из второго массива _p
    # берем следующее значение из массива _a, ищем среди оставшихся элементов массива _p

    # для полученого ключа вычислить значение по ф-ле cpi = spend / installs
