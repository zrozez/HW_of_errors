names = ['dhhgfjjhsa.txt', 'hhdsdahffh.txt', 'afdgdhjsds.txt', 
	'sggjghddss.txt', 'fjdjgdghdf.txt', 'sjssahjfga.txt', 
	'agsgdjhhfj.txt', 'gafadhadda.txt', 'hdagajfhhj.txt', 
	'fhjhafhdfa.txt']

import random

def wrt (names):
    cr = open(random.choice(names), 'a')
    for i in names:
        try:
            l = open(i, 'r')
            cr.write('Sakhizova Roza')
            print(i, 'записан')
        except:
            print(i, '- такого файла не существует')
    return
wrt(names)
