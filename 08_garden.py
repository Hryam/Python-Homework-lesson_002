#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код

print ("Всего цветов в саду :" , len(garden))
garden_set = {garden[0], garden[1], garden[2], garden[3], garden[4], garden[5], garden[6],}
print ('В саду растут:' , garden_set) 
print ("Всего цветов на лугу :", len(meadow))
meadow_set = {meadow[0], meadow[1], meadow[2], meadow[3], meadow[4], meadow[5], meadow[6],}
print ('На лугу растут:', meadow_set)

# выведите на консоль все виды цветов
# TODO здесь ваш код
all_flower = garden_set|meadow_set
print ('Всего видов цветов:' , all_flower)
# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
flower_gardem_and_meadow = garden_set&meadow_set
print ('Цветы которые растут и в саду и на лугу:' , flower_gardem_and_meadow)
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
flower_only_garden = garden_set - meadow_set
print('Цветы растущие только в саду:' , flower_only_garden)
# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
flower_only_meadow = meadow_set - garden_set
print('Цветы растущие только на лугу:' ,flower_only_meadow)