#coding=utf-8
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
summer=0.0
# TODO заменить значение пропущенного элемента средним арифметическим
for i,ii in enumerate(numbers):
    if ii==None:
        a=i
    else:
        summer+=ii

numbers[a]=summer/(len(numbers))

print("Измененный список:", numbers)
