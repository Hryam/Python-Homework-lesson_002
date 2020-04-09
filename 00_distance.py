#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

#from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

# TODO здесь заполнение словаря
Moscow_London = ((sites['Moscow'][0]-sites['London'][0])**2+(sites['Moscow'][1]-sites['London'][1])**2)**.5 
London_Paris = ((sites['London'][0]-sites['Paris'][0])**2+(sites['London'][1]-sites['Paris'][1])**2)**.5
Moscow_Paris = ((sites['Moscow'][0]-sites['Paris'][0])**2+(sites['Moscow'][1]-sites['Paris'][1])**2)**.5

distances ['Moscow']={}
distances ['Moscow']['London'] = Moscow_London
distances ['Moscow']['Paris'] = Moscow_Paris

distances ['Paris']={}
distances ['Paris']['Moscow']=Moscow_Paris
distances ['Paris']['London']=London_Paris

distances['London']={}
distances['London']['Moscow']=Moscow_London
distances['London']['Paris']=London_Paris


print(distances)
вернул все взад


