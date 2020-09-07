# Riddle Python / Загадки на питоне. 
# 
# Answers / right / wrong
right = 0
wrong = 0
# First riddle
flag1 = 0
answer1 = 'утюг'
riddle1 = print(('{0:*^30}'.format('ПЕРВАЯ ЗАГАДКА')), """\n
	В Полотняной стране
По реке Простыне
Плывет пароход
То назад, то вперед,
А за ним такая гладь —
Ни морщинки не видать.
""")
while ( flag1 != 1 ):
	choose = input('Ответ: ')
	if (answer1 == str.lower(choose)):
	    print('\nПравильно! ', choose, '!\n')
	    right += 1
	    flag1 = 1
	else:
		print('\nНеправильно!\n')
		wrong += 1
		flag1 = 1

# Second riddle
flag2 = 0
answer2 = 'чайник'
riddle2 = print(('{0:*^30}'.format('ВТОРАЯ ЗАГАДКА')), """\n
В брюшке — баня,
В носу — решето,
Нос — хоботок,
На голове — пупок,
Всего одна рука
Без пальчиков,
И та — на спине
Калачиком.
""")
while ( flag2 != 1 ):
	choose = input('Ответ: ')
	if (answer2 == str.lower(choose)):
	    print('\nПравильно! ', choose, '!\n')
	    right += 1
	    flag2 = 1
	else:
		print('\nНеправильно!\n')
		wrong += 1
		flag2 = 1

# Third riddle
flag3 = 0
answer3 = 'год'
riddle3 = print(('{0:*^30}'.format('ТРЕТЬЯ ЗАГАДКА')), """\n
Стоит дуб,
В нем двенадцать гнезд,
В каждом гнезде
По четыре яйца,
В каждом яйце
По семи цыпленков.
""")
while ( flag3 != 1 ):
	choose = input('Ответ: ')
	if ( answer3 == str.lower(choose) ):
	    print('\nПравильно! ', choose, '!\n')
	    right += 1
	    flag3 = 1
	else:
		print('\nНеправильно!\n')
		wrong += 1
		flag3 = 1

# THE END
print('{0:*^30}'.format('КОНЕЦ'))
print('\nВсего дано ответов: ', wrong+right)
print('Правильных: ', right)
print('Неправильных:', wrong, '\n')
print('{0:*^30}'.format(''))