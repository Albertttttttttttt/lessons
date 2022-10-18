while True:
	name = input('Введите имя: ')
	if name == 'стоп': break
	count = int(input('Введите число предметов: '))
	if count == 'стоп': break
	sum = 0
	for i in range(count):
		try: sum += int(input('Введите число баллов: '))
		except: exit()
	if sum >= 80: print('Наградить дипломом')
	elif sum >= 50: print('Наградить похвальной грамотой')
	else: print('Выдать грамоту об участии')