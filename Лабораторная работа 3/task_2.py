# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first, participants_second, spl=','):
    par_f = set(participants_first.split(spl))
    par_s = set(participants_second.split(spl))
    return(list(sorted(par_f.intersection(par_s))))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, '|')