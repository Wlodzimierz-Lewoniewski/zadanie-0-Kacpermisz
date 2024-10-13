#Przykład otrzymania wartości wprowadzonej przy użyciu funkcji input().
import re

zdania = int(input("Podaj liczbę zdań: "))
i = 0
j = 0
lista_z = []

while i < zdania:
    zdanie = input("Podaj zdanie numer "+str(i+1)+": ")
    lista_z.append(zdanie)
    i += 1

slowa = int(input("Podaj liczbę słów: "))

while j < slowa:
    lista_i = []
    lista_s = []
    slowo = input("Podaj slowo numer "+str(j+1)+": ").lower()
    for i, zdanie in enumerate(lista_z):
        wyr = re.findall(r'\b\w+\b', zdanie.lower())
        count = wyr.count(slowo)
        lista_s.append((i, count))
    sort = sorted(lista_s, key=lambda x: x[1], reverse=True)
    for index, count in sort:
        if count > 0:
            lista_i.append(index)
    print(lista_i)
    j += 1
