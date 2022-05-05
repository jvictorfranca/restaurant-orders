import csv


def read_csv(path):
    try:
        with open(path) as file_object:
            data = csv.reader(file_object)
            answer = [object for object in data]
            return answer

    except FileNotFoundError:
        print(f"Arquivo inexistente: '{path}'")


def get_working_days(path):
    days = set()
    answer = read_csv(path)
    for order in answer:
        days.add(order[2])
    return days


def get_person_days(path, name):
    days = set()
    answer = read_csv(path)
    for order in answer:
        if order[0] == name:
            days.add(order[2])
    return days


def get_plates(path):
    plates = set()
    answer = read_csv(path)
    for order in answer:
        plates.add(order[1])
    return plates


def get_person_plates(path, name):
    plates = set()
    answer = read_csv(path)
    for order in answer:
        if order[0] == name:
            plates.add(order[1])
    return plates


def get_person_order_dict(path, name):
    answer = read_csv(path)
    orders_array = [order[1] for order in answer if order[0] == name]
    orders_dict = {}
    for order in orders_array:
        if order in orders_dict:
            orders_dict[order] += 1
        else:
            orders_dict[order] = 1
    return orders_dict


def get_days_dict_most_frequent(path):
    answer = read_csv(path)

    days_dict = {}
    for order in answer:
        if order[2] in days_dict:
            days_dict[order[2]] += 1
        else:
            days_dict[order[2]] = 1
    most_frequent = list(days_dict.keys())[0]
    for item in days_dict.keys():
        if days_dict[item] > days_dict[most_frequent]:
            most_frequent = item
    return most_frequent


def get_order_most_frequent(path, name):
    person_dict = get_person_order_dict(path, name)
    most_ordered = list(person_dict.keys())[0]
    for item in person_dict.keys():
        if person_dict[item] > person_dict[most_ordered]:
            most_ordered = item
    return most_ordered


def get_how_many_plates(path, name, plate):
    answer = read_csv(path)
    quantity = 0
    for order in answer:
        if name == order[0] and plate == order[1]:
            quantity += 1
    return quantity


def analyze_log(path_to_file):
    if path_to_file.split(".")[1] != "csv":
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        first_answer = str(get_order_most_frequent(path_to_file, 'maria'))
        second_answer = str(get_how_many_plates(
            path_to_file, "arnaldo", "hamburguer"))
        third_answer = str(get_plates(path_to_file) - get_person_plates(
            path_to_file, 'joao'))
        forth_answer = str(get_working_days(path_to_file).difference(
            get_person_days(path_to_file, 'joao')))
        with open('data/mkt_campaign.txt', mode="w") as f:
            f.write(first_answer)
            f.write('\n')
            f.write(second_answer)
            f.write('\n')
            f.write(third_answer)
            f.write('\n')
            f.write(forth_answer)
    except TypeError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
