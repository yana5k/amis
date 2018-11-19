List = ["apple", "Apple", "car", "Action", "computer", "work", "Python", "Art", "art"] #дано список довільних текстових елементів
def ListRec(List):#рекурсивна функція
    if List == []:#блок перевірки кінця рекурсії/можливості початку
        return
    if List[0][0] == "A":#блок-тіло
        print (List[0])
    ListRec(List[1:])#рекурсивний перехід


ListRec(List)