''' Get flower names from http://www.zaplana.net/flowers/asp/flower_all_en.asp '''
from bs4 import BeautifulSoup
import re
import requests

site = requests.get('http://www.zaplana.net/flowers/asp/flower_all_en.asp')
soup = BeautifulSoup(site.text)

names = soup.find_all('a', href=re.compile(r'display_flower\.asp\?name\='))

genus_file = open('genus', 'w')
species_file = open('species', 'w')

genus = ''
species = ''
for flower in names:
    name = flower.text
    parts = name.split(' ')
    if genus != parts[0]:
        genus = parts[0]
        genus_file.write('%s\n' % genus)

    if species != parts[1]:
        species = parts[1]
        species_file.write('%s\n' % species)
