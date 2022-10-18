def imt(weight,height):
	return imtc(float(weight / (height * height)))
def imtc(index):
	if index < 18.5: return 'Недостаточный вес'
	elif index >= 18.5 and index < 25: return 'ИМТ в норме'
	elif index >= 25: return 'Избыточный вес'
print(imt(int(input('Введите свой вес: ')),int(input('Введите свой рост: '))))