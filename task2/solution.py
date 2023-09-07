from typing import Tuple, Dict
import csv
import requests
import logging
import collections

from bs4 import BeautifulSoup, element


from utils import save, buffering_load as load


def find_content_elements(e: element.Tag) -> Dict[str, int]:
	groups = e.find_all('div', attrs={'class': 'mw-category-group'})
	
	return {
		group.find('h3').text : len(group.find_all('li'))\
			for group in groups
	}

def main(skip_latin=True):
	page_url = 'http://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
	
	result = {}
	while (page_url):
		page_raw = load(page_url)
		page = BeautifulSoup(page_raw, features="html.parser")
		page_partition = page.body.find('div', attrs={'id': 'mw-pages'})
		
		page_categories = find_content_elements(page_partition)
		for title, items_count in page_categories.items():
			if title not in result.keys():
				result[title] = 0
			result[title] += items_count
		
		page_url = None
		
		# finding next page
		anchors = page_partition.find_all(
			'a', recursive=False,
			attrs={'title': 'Категория:Животные по алфавиту'},
		)
		if 'A' in page_categories.keys() and skip_latin:
			result.pop('A', None)
			break
		for anchor in anchors:
			if anchor.text == 'Следующая страница':
				page_url = 'http://ru.wikipedia.org{route}'.format(route=anchor['href'])
				break
	save(collections.OrderedDict(sorted(result.items())), 'beasts.csv')

if __name__ == "__main__":
	logging.getLogger().setLevel(logging.INFO)

	main(skip_latin=False)
