"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
def sum_in_line(line):
    res = 0
    for el in line.split():
        try:
            res += int(el)
        except ValueError:
            pass
    return res

key_list = []
with open("subjects.txt", "r", encoding='utf-8') as file:
    work_list = file.read().split()
    key_list = [work_list[i] for i in range(0, len(work_list) - 1, 7)]

lessons = []
with open("subjects.txt", "r", encoding='utf-8') as file:
    for line in file:
        lessons.append((sum_in_line(line)))

subj_dict = dict(zip(key_list, lessons))
print(subj_dict)