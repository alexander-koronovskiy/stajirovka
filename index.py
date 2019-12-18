'''
создать тестовые csv файлы
прочитать два файла с расширением .csv
вывести для теста некоторые строки
записать содержимое файлов в отдельные массивы
установить соответствие между массивами
создать файл out.csv - и вывести в него массивы
применить программу для 
'''

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


# извлечение данных
def get_params(data):
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
    with open(csv_path, "r") as f_obj:
        s = csv_reader(f_obj)
    return s


def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    s = ""
    for row in reader:
        s += (" ".join(row)) + "\n"
    return s


if __name__ == "__main__":

    # запись первого тестового файла
    file1 = "dict_input_a.csv"
    params = get_params(SAMPLEDATA_A)
    write_csv_file(file1, params[0], params[1])

    # запись второго тестового файла
    file2 = "dict_input_p.csv"
    params = get_params(SAMPLEDATA_P)
    write_csv_file(file2, params[0], params[1])

    # чтение первого файла
    s = read_csv_file(file1)
    print(s)
