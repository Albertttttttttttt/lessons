def main(input):
    if 'расп' in input.lower():
        timetable()
    if 'трен' in input.lower():
        troy()
    if 'оплат' in input.lower():
        koul()
    if 'название' in input.lower():
        hool()
    if 'сайт' in input.lower():
        srap()


def timetable():
    print('Часы работы спорткомплекса Пн - с 9:00 до 20:00 Ср - 9:00 до 20:00 Пт - 9:00 до 20:00')
    print('Вы хотите посетить тренировку? Введите - да/нет')
    t1=input()
    s1={}
    if t1=='да':
        print('Выберите день недели')
        t2=input()
        print('Введите время с 9 до 20')
        t3=int(input())
        if 8<=t3<=23:
            s1[t2]=t3
            print('Вы записались на', s1)
def troy():
    print('Хорошей тренировки!')
def koul():
    print('К оплате за месяц - 6200')
def hool():
    print('Фитнес-клуб «FORWARD FITNESS», ул. Кирова, д.44')
def srap():
    print('http://forward-fitness.ru/')