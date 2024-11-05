# TODO Напишите функцию find_common_participants

def find_common_participants (str1, str2, spl_arg=','):
    list1=str1.split(spl_arg)
    list2=str2.split(spl_arg)

    common_list=list(set(list1).intersection(list2))
    common_list.sort()
    return common_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants=find_common_participants(participants_first_group,participants_second_group,'|')
print("Общие участники: ", common_participants)