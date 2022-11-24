
from random import *

dictImage = {'screen-left.csv': 138, 'screen-up.csv': 117, 'screen-right.csv': 138, 'screen-down.csv': 127}
arr =[]
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

choice = decide(dictImage)
print(choice)