# Parašykite žaidimą, kuris iš svetainės http://quotes.toscrape.com/ pateiks citatas
# žaidėjui reikės atspėti autorių
# Žaidėjui neatspėjus, reikės pasufleruoti autoriaus inicialus
# dar kartą neatspėjus - gimimo datą ir vietą
# Jeigu žaidėjas neatspėja iš 3 kartų, jam atspausdinamas teisingas atsakymas ir paklausiama, ar nori tęsti.

from bs4 import BeautifulSoup
import requests
from random import randint

url = 'http://quotes.toscrape.com/'
link = requests.get(url)

soup = BeautifulSoup(link.content, 'html.parser')

quote_list = []
quotes = soup.select('.text')
for quote in quotes:
    quote_list.append(quote.get_text())

author_list = []
authors = soup.select('.author')
for author in authors:
    author_list.append(author.get_text())

# hint - pateikiami inicialai
hint_initials = []
for author in authors:
    full_name = author.get_text()
    splitted = full_name.split()
    first_name = splitted[0]
    last_name = splitted[1]
    initials = first_name[0] + '.' +  last_name[0] + '.'
    hint_initials.append(initials)

# hint - pateikiama gimimo data ir vieta
hint_born = []

while True:
    random_number = randint(1,9)
    print(quote_list[random_number])
    answer = input('Guess author of the quote: ')
    if answer == author_list[random_number]:
        print('You are corrent')
    else:
        print(f'HINT: {hint_initials[random_number]}')
        second_answer = input('Guess again: ')
        if second_answer == author_list[random_number]:
            print('You are corrent')
        else:
            print('You are still wrong')
    print(f'Corrent answer was {author_list[random_number]}')
    exit = input('Do you want to play more? Y/N ')
    if exit == 'N':
        break
    else:
        continue