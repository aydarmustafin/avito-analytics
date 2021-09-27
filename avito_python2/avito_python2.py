from faker import Faker
import csv


file = []
with open('Corp_Summary.csv') as File:
    reader = csv.DictReader(File, delimiter=';')
    for row in reader:
        file.append(row)
    print(file)


def make_hierarchy(df: list):
    '''Создает словарь, в котором каждому департаменту сопоставляется список из входящих в него отделов'''
    hierarchy_dict = {}
    for row in df:
        if row['Департамент'] not in hierarchy_dict:
            hierarchy_dict[row['Департамент']] = [row['Отдел']]
        elif row['Отдел'] not in hierarchy_dict[row['Департамент']]:
            hierarchy_dict[row['Департамент']].append(row['Отдел'])
    return hierarchy_dict


def describe_department(df: list):
    '''Создает словарь, котором каждому департаменту сопоставляется словарь, содержащий информацию о зарплатах в нем'''
    dep_dict = {}
    for row in df:
        if row['Департамент'] not in dep_dict:
            dep_dict[row['Департамент']] = {'Численность': 1, 'Мин. оклад': float(row['Оклад']), 'Макс. оклад': float(row['Оклад']), 'Ср. оклад': float(row['Оклад'])}
        else:
            dep_dict[row['Департамент']]['Ср. оклад'] = (dep_dict[row['Департамент']]['Ср. оклад'] * dep_dict[row['Департамент']]['Численность'] + float(row['Оклад'])) / (1+dep_dict[row['Департамент']]['Численность'])
            dep_dict[row['Департамент']]['Численность'] = dep_dict[row['Департамент']]['Численность'] + 1
            dep_dict[row['Департамент']]['Мин. оклад'] = min(dep_dict[row['Департамент']]['Мин. оклад'], float(row['Оклад']))
            dep_dict[row['Департамент']]['Макс. оклад'] = max(dep_dict[row['Департамент']]['Макс. оклад'], float(row['Оклад']))
    return dep_dict


def hierarchy_output(hierarchy: dict):
    '''Выводит иерархию департамент-отдел в читабельном виде'''
    for key, value in hierarchy.items():
        print(f"{key}:   {', '.join(e for e in value)}")


def department_description_output(description: dict):
    '''Выводит описание департментов по з/п в читабельном виде'''
    for department, value in description.items():
        print(department, end=':   ')
        for feature, number in value.items():
            print(f'{feature} - {round(number)}', end=',   ')
        print()


print()

hierarchy_output(make_hierarchy(file))

print()

department_description_output(describe_department(file))


def describe_department_to_csv(description: dict):
    '''Сначала переводит формат полученных данных в удобный для перевода в csv, затем сохраняет в csv-файл'''
    list_for_csv = [['Департамент', 'Мин. оклад', 'Макс. оклад', 'Ср. оклад']]
    for department in description:
        department_list = list(description[department].values())
        department_list.insert(0, department)
        list_for_csv.append(department_list)

    avito_csv = open('csv_for_avito1.csv', 'w')
    with avito_csv:
        writer = csv.writer(avito_csv)
        writer.writerows(list_for_csv)

    return list_for_csv


describe_department_to_csv(describe_department(file))
