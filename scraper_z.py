import requests
from bs4 import BeautifulSoup
import csv
from random import randint
from time import sleep

csv_datoteka = open('muska_imena.csv', 'w')
csv_writer = csv.writer(csv_datoteka)

for page in range(1, 19):
    url = "https://www.znacenje-imena.com/imena/hrvatska/muska?page="
    body = requests.get(url + str(page))

    body_text = body.content

    soup = BeautifulSoup(body_text, 'html.parser')

    for divs in soup.find_all('div', class_='col-sm-3 col-xs-6'):
        ime = divs.a.text
        brojevi = divs.span.text
        broj = brojevi[4:]
        csv_writer.writerow([ime, broj])

    sleep(randint(1, 2))

csv_datoteka.close()
