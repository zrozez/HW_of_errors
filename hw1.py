example = {
	   'iceberg': ['cold', 15, {'a', 'b'}, 33.98, 15/2, False],
	   'fire': ['hot', 46, ['cha', 'ching'], 81.13],
	   'earth': ['solid', 100, (13, 31, 1), 90.01, {'b':'c'}]
	   }

elements = ['fire', 'storm', 'cloud', 'iceberg', 'volcano', 'earth']

def sum_of_args(dicti, lst):
    for i in lst:
        try:
            values = dicti[i]
            summa = 0
            for l in values:
                try:
                    summa += l
                except:
                    continue
            print(i, '-', summa)
        except:
            print('Ключа', i, 'не существует!')
    return

sum_of_args(example, elements)
