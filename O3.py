def passage(score):
		print(score>50)
		return score>50
        
for i in range(int(input('Введите кол-во учеников: '))):
	if passage(int(input('Введите свою оценку: '))) == False:
		print('Готовтесь к передаче')