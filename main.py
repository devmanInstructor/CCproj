import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def shorten_link(token, link):
  payload = {
    'long_url': link
  }

  headers = {
    'Authorization': f'Bearer {token}'
  }

  url = 'https://api-ssl.bitly.com/v4/bitlinks'
  response = requests.post(url, json=payload, headers=headers)
  response.raise_for_status()
  return response.json()['link']


def count_clicks(token, bitlink):
  headers = {
    'Authorization': f'Bearer {token}'
  }

  url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
  response = requests.get(url, headers=headers)
  response.raise_for_status()
  return response.json()['total_clicks']


def get_netloc_and_path(link):
  parsed = urlparse(link)
  return f'{parsed.netloc}{parsed.path}'


def is_link_a_bitlink(token, link):
  headers = {
    'Authorization': f'Bearer {token}'
  }

  url = f'https://api-ssl.bitly.com/v4/bitlinks/{get_netloc_and_path(link)}'
  response = requests.get(url, headers=headers)
  return response.ok


if __name__ == '__main__':
  load_dotenv()
  token = os.getenv('BITLY_GA_TOKEN')
  parser = argparse.ArgumentParser(
    description='Сокращение ссылок'
  )
  parser.add_argument('link', help='Ссылка для сокращения или битлинк для получения информации о нем')
  link = parser.parse_args().link

  if is_link_a_bitlink(token, link):
    try:
      print('Кол-во кликов: ', count_clicks(token, get_netloc_and_path(link)))
    except requests.exceptions.HTTPError as error:
      exit('Ошибка в получении количества кликов по битлинку:\n{0}'.format(error))
  else:
    try:
      print('Битлинк: ', shorten_link(token, link))
    except requests.exceptions.HTTPError as error:
      exit('Ошибка в создании битлинка:\n{0}'.format(error))

