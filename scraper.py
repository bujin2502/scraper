import requests
from bs4 import BeautifulSoup
import csv
from random import randint
from time import sleep

csv_datoteka = open('imena.csv', 'w')
csv_writer = csv.writer(csv_datoteka)

for page in range(1, 33):
    url = "https://www.znacenje-imena.com/imena/hrvatska?page="
    body = requests.get(url + str(page))

    body_text = body.content

    soup = BeautifulSoup(body_text, 'html.parser')

    for divs in soup.find_all('div', class_='col-sm-3 col-xs-6'):
        ime = divs.a.text
        print(ime)
        print()
        csv_writer.writerow([ime])
    sleep(randint(1, 2))

csv_datoteka.close()
