# Parašykite programą, kuri nuskaitytų delfi antraštes, patikrintų, ar jos turi dvitaškį.
# Dalį iki dvitaškio sudėtų į vieną sarašą, dalį po dvitaškio į kitą.
# Antrą sarašą išmaišykite.
# Tuomet atspausdinkite pirmas dalis iš pirmo sarašo, prie jų prijunkite antras dalis iš antro sąrašo.
# Turėtume gauti panašių variantų:
#     Orai : už 9 šlakius teks sumokėti 26 tūkstančius eurų
#     Antradienio vakare kauniečius išgąsdino termofikacijos elektrinė : ar bus naujagimių bumas?
# Sukurkite blogų žodžių sąrašą, pagal kurį išsifiltruoja pranešimai apie COVID, mirtis ir t.t. Išfiltruokite ankstyvoje stadijoje, kol dar antraštės neperskirtos.

from bs4 import BeautifulSoup
import requests
from random import shuffle

url = 'https://www.15min.lt/'
link = requests.get(url)

soup = BeautifulSoup(link.text, 'html.parser')

headlines_list = []
first_part = []
second_part = []
bad_words = ['COVID', 'mirt', 'avarij', 'gaisr', 'kar']

headlines = soup.select('h4')
for element in headlines:
    name = element.get_text().strip()
    headlines_list.append(name)

for title in headlines_list:
    if ':' in title:
        if not any(word in title for word in bad_words):
            splitted = title.split(':')
            first_part.append(splitted[0])
            second_part.append(splitted[1])

shuffle(second_part)

for name in range(len(first_part)):
    print(first_part[name], ':', second_part[name])