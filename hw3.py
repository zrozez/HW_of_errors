spendings = [140, 30, 999, 145, 538, 878, 901, 613, 471, 286, 147, 90]
income = [300, 40, 0, 4000, 8911, 73, 85, 0, 9000, 941, 658, 190]

koef_of_year = 0
for i in range(12):
    try:
        koef_of_month = spendings[i]/income[i]
    except:
        koef_of_month = 0
    koef_of_year += koef_of_month
print('Средний коэффициент распределения расходов = ', koef_of_year/12)
