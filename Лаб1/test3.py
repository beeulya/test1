list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
first_team=[]
second_team=[]
# индекс середины
middle_index = len(list_players) // 2
#first_team=[None]*middle_index
#second_team=[None]*middle_index
for i,ii in enumerate(list_players):
    if i<middle_index:
        first_team.append(ii)
    else:
        second_team.append(ii)
print(first_team)
print(second_team)