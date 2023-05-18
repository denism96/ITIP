groupmates = [
{
	 "name": "Александр",
	 "surname": "Гусев",
	 "exams": ['КПТ', 'История', 'АИС'],
	 "marks": [5, 5, 4]
},
{
	 "name": "Александр",
	 "surname": "Сытов",
	 "exams": ['АИС', 'История', 'ИТиП'],
	 "marks": [5, 3, 5]
},
{
	 "name": "Анастасия",
	 "surname": "Гольцова",
	 "exams": ['История', 'Социологоия', 'ИТиП'],
	 "marks": [5, 3, 3]
}
]

def sortbyavg(avg, studlist):
    for i in studlist:
        if sum(i["marks"])/len(i["marks"]) >= avg:
            print(i["name"], i["surname"])
target = float(input("Введите средний балл: "))
sortbyavg(target, groupmates)
