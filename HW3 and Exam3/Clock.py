# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 13:38:14 2022

@author: brock
"""

starttime = int(input('When to start?'))

direction = input('1 for After or 2 for before')

hours = int(input('How many hours?'))

if '1' == direction:
    print('Going Forward or after')
    remainder = hours % 12
    time = starttime
    for index in range (0, remainder):
        time =+ 1
        if 13 == time:
            time = 1
    print (f'Clock reads {time}:00')
else:
    print('Going Back or before')
    remainder = hours % 12
    time = starttime
    for index in range (0, remainder):
        time -= 1
        if 1 == time:
            time = 13
    print (f'Clock reads {time}:00')
    