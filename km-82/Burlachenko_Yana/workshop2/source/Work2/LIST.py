def maxAge(smth):#рекурсивна ф-ція, що знаходить найбільший вік студента через порівняння елементів та відкидання найменшого
	if len(smth) == 1:#блок перевірки кінця
		return smth[0]["age"]
	if smth[0]['age'] > smth[1]['age']:#порівняння елементів
		del smth[1] #видалення меншого
	else:
		del smth[0] #видалення меншого
	return maxAge(smth)

def addMark(smth, name, disc, mark):#ф-ція, яка додає інформацію про оцінки з відповідних предметів для того чи іншого студента
	for i in smth:
		if i["name"] == name: #знаходження конкретного елемента(ім'я студента)
			i["marks"][disc] = mark #безпосереднє додавання інформації
	return

def getNames(smth):#ф-ція, що створює список з імен студентів
	NameList = [] #створення порожнього списку
	for i in smth:
		NameList.append(i["name"])#додавання елементів(конкретно - імен)
		return NameList

smth = [             #список, що складається зі словників
	{
	"name":"Bob",
		"age":20,
		"marks":{
				"Math":98,
				"Python":100
				}
	},

	{
		"name":"Boba",
		"age":19,
		"marks":{
				"Physics":98
				}
	},

	{
		"name":"Boban",
		"age":22,
		"marks":{
				}
	}
]

print(maxAge(smth.copy()))#виклик ф-ції, що рахує максимальний вік
addMark(smth, 'Boba', 'Mathan', 96)#виклик ф-ції, що додає інформації про бали з конкретного предмета
print(smth)#список з додаванням оцінок
print(getNames(smth))#виклик ф-ції, що створює список імен студентів