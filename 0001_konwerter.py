# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 13:08:41 2022
version 1.0.0.0
@author: Dawid_PC
feat Malgo i Rose
"""


#Program pobiera od uzytkownika wartosci w minutach i przelicza je na godziny


#pobranie od użytkownika wartosci do konwersji
user_value = int(input('Podaj wartosc minut do zamiany na godziny '))

hours = int(user_value/60)
minutes = user_value%60

#dopasowanie wyswietlanego opisu na podstawie wartosci
if hours ==1:
    hours_desc = " godzina"
elif hours in(2,3,4):
    hours_desc = " godziny"
else:
    hours_desc = " godzin"
if minutes ==1:
    minutes_desc = " minuta"
elif minutes in(2,3,4):
    minutes_desc = " minuty"
else:
    minutes_desc = " minut"
#wygenerowanie wiadomosci dla uzytkownika
print("podana przez Ciebie wartosc to ",hours, hours_desc, " i ",minutes,minutes_desc)
input("potwierdź enter aby zakonczyc dzialanie programu")