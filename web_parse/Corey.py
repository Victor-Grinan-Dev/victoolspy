from bs4 import BeautifulSoup
import requests

URL = 'https://wahapedia.ru/wh40k9ed/factions/space-marines/'

with open(URL) as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

