''' Get flower names from http://www.zaplana.net/flowers/asp/flower_all_en.asp '''
from bs4 import BeautifulSoup
import re
import requests

site = requests.get('http://www.zaplana.net/flowers/asp/flower_all_en.asp')
soup = BeautifulSoup(site.text)

names = soup.find_all('a', href=re.compile(r'display_flower\.asp\?name\='))

genus_file = open('genus', 'w')
species_file = open('species', 'w')

common_first = open('common_first', 'w')
common_second = open('common_second', 'w')

genus = ''
species = ''

first = ''
second = ''

for flower in names:
    name = flower.text
    parts = name.split(' ')
    if genus != parts[0]:
        genus = parts[0]
        genus_file.write('%s\n' % genus)

    if species != parts[1]:
        species = parts[1]
        species_file.write('%s\n' % species)

    common_name = flower.parent.next_sibling.text
    parts = common_name.split(' ')
    if len(parts) == 1:
        common_second.write(common_name)
    else:
        if parts[0] != first:
            first = parts[0]
            common_first.write('%s\n' % parts[0])
        if parts[-1] != second:
            second = parts[-1]
            common_second.write('%s\n' % parts[-1])
