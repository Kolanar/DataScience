from matplotlib import pyplot as plt
plt.rcParams['axes.facecolor'] = 'none'

years = [1950,1960,1970,1980,1990,2000,2010] # Годы
gdp = [300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3] # ВВП

"""
Линейная диаграма
"""
# Создать линейную диаграму: годы по оси x, ВВП по оси y
plt.plot(years,gdp, color='green', marker='o', linestyle='solid')
# Добавить название диаграмы
plt.title('Номинальный ввп')
# Добавить подпись к оси y
plt.ylabel('Млрд $')
plt.show()


"""
Столбчатый график
"""
movies = ['Энни Холл','Бен-Гур','Касабланка','Ганди','Вестсайдская история']
num_oscars = [5,11,3,8,10]
plt.bar(range(len(movies)),num_oscars)
plt.title('Мои любимые фильмы')
plt.ylabel('Кол-во наград')
plt.xticks(range(len(movies)), movies) # Пометить ось x названиями фильмов в центре каждого столбца
plt.show()

"""
Использование столбчатого графика для гистрограммы
"""

from collections import Counter

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0] # оценки

# Сгрупировать оценки подецильно но разместить 100 вместе с отметками 90 и выше
histogram = Counter(min(grade // 10*10,90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()], # Сдвинуть столбец влево на 5
        list(histogram.values()),          # Высота столбца
        10)                                # Ширина каждого столбца 10

plt.axis([-5,105,0,5]) # Ось x от -5 до 105,
                       # Ось y от 0 до 5

plt.xticks([10 * i for i in range(11)]) # метки по оси x: 0, 10,...,100
plt.xlabel('Дециль')
plt.ylabel('Число студентов')
plt.title('Распределение оценок за экзамен')
plt.show()

"""
Линейные графики
"""

variance = [1,2,4,8,16,32,64,128,256] # Дисперсия - Мера разброса значений случайной величины относительно её математического ожидания
bias_squared  = [256,128,64,32,16,8,4,2,1] # Квадрат Смещения

total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

# Метод plt.plot можно вызвать много раз
# Что бы показать несколько графиков на одной и той же диаграмме

# Зеленая сплошная линия
plt.plot(xs, variance, 'g-', label='дисперсия')
# Красная штрихпунктирная
plt.plot(xs, bias_squared, 'r-', label='смещение^2')
# Синяя пунктирная
plt.plot(xs,total_error,'b:', label='Суммарная ошибка')

# Если для каждой линии задано название label
# То легенда будет показана автоматически

# loc=9 означает 'наверху посередине'
plt.legend(loc=9)
plt.xlabel('Сложность модели')
plt.title('Компромисс между смещением и дисперсией')
plt.show()

"""
Диаграммы рассеяния
"""

friends = [70,65,72,63,71,64,60,64,67] # Друзья
minutes = [175,170,205,120,220,130,105,145,190] # Минуты
labels = ['a','b','c','d','e','f','g','h','i'] # Метки

plt.scatter(friends,minutes)

# Назначить метку для каждой точки

for label, friend_count, minute_count in zip(labels,friends,minutes):
        plt.annotate(label,
                     xy=(friend_count,minute_count), # Задать метку
                     xytext=(5,-5),                  # И немного сместить её
                     textcoords='offset points')

plt.title('Число минут против числа друзей')
plt.xlabel('Число друзей')
plt.ylabel('Число минут, проводимых на сайте ежедневно')
plt.show()