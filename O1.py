
def badge(amount):
    
	for i in range(amount):
        
		print('«Колледж Сириус»\n«Имя: ____»\n«Группа: ____»',end='\n\n')
	return '«Готово! Заберите бейджики.»'
print(badge(int(input('Введите число учеников: '))))