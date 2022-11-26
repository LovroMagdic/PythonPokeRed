
from random import *
def decide(dictImage):
    for key in dictImage:
        tmp = (10 - (dictImage[key] % 10) ) + dictImage[key]
        dictImage[key] = tmp

    decide = max(dictImage, key=dictImage.get)
    arr.append(decide)
    save = [decide, dictImage[decide]]
    del dictImage[decide]

    decide = max(dictImage, key=dictImage.get)
    arr.append(decide)

    dictImage[save[0]] = save[1]

    if dictImage[arr[0]] == dictImage[arr[1]]:
        rem = randint(0, 1)
        arr.remove(arr[rem])
    return arr[0]

def last_decide(dictImage, last_decision):
    temp = 0
    for key in dictImage:
        tmp = (10 - (dictImage[key] % 10) ) + dictImage[key]
        dictImage[key] = tmp
    print(dictImage)
    
    for key in dictImage:
        temp = temp + dictImage[key]
    temp = temp / 4
    print(temp)
    print(dictImage[last_decision])
    if dictImage[last_decision] < temp:
        choice = decide(dictImage)
        return choice
    else:
        return last_decision


dictImage = {'screen-left.csv': 138, 'screen-up.csv': 117, 'screen-right.csv': 138, 'screen-down.csv': 127}
arr =[]

last_decision = 'screen-left.csv'
choice = last_decide(dictImage, last_decision)
print(choice)