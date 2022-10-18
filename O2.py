
def discount(scores):
	if scores < 50: print('«Скидка 15%»')
	elif scores < 100: print('«Скидка 25%»')
	else: print('«Скидка 35%»')
discount(int(input('Введите число накопленных баллов: ')))