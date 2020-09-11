# Riddle Python / Загадки на питоне. 
riddle = {'В Полотняной стране\nПо реке Простыне\nПлывет пароход\nТо назад, то вперед,\nА за ним такая гладь —\nНи морщинки не видать. \n\nОтвет: ':'утюг', '\n\nВ брюшке — баня,\nВ носу — решето,\nНос — хоботок,\nНа голове — пупок,\nВсего одна рука\nБез пальчиков,\nИ та — на спине\nКалачиком.\n\nОтвет: ':'чайник', '\n\nСтоит дуб,\nВ нем двенадцать гнезд,\nВ каждом гнезде\nПо четыре яйца,\nВ каждом яйце\nПо семи цыпленков. \n\nОтвет: ':'год'}
answer_count = [0, 0, 0]

for question in riddle.keys():
	answer = input(question) 
	if answer.lower() == riddle.get(question).lower():
		print('\nВерно!')
		answer_count[0] += 1
		answer_count[1] += 1
	else: 
		print('\nНе верно!')
		answer_count[1] += 1
		answer_count[2] += 1
print('\nВсего дано ответов: ', answer_count[1], '\nВерных: ', answer_count[0], '\nНе верных: ', answer_count[2])
