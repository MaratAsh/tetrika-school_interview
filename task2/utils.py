import csv
import requests
import logging


from decor import file_buffering


def save(countings: dict, file_name):
	with open(file_name, 'w', newline='', encoding="utf-8") as csvfile:
		writer = csv.writer(csvfile, delimiter=',',
							quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for category, count in countings.items():
			writer.writerow([category, str(count)])


def load(target_url: str):
	logging.info('loading file from the web \'{}\''.format(target_url))
	response = requests.get(target_url)
	if response.status_code != 200:
		logging.info('failed to load \'{}\''.format(target_url))
		return None
	return response.content.decode("utf-8")

buffering_load = file_buffering(load)

