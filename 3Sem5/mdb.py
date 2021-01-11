import pymongo
import time
import requests
from bs4 import BeautifulSoup as bs




def delay(m=1):
    time.sleep(m)


def FEFU(position, surname='', name='', o_name='', cabinet='', phone='', mail='None'):
    return {
        'Должность': position,
        'Фамилия': surname,
        'Имя': name,
        'Очесство': o_name,
        'Кабинет': cabinet,
        'Телефон': phone,
        'Почта': mail
    }
def parser_FEFU():
    client = pymongo.MongoClient('localhost', 27017)
    db = client['FEFU_Bot']
    coll = db['People']
    db.drop_collection(coll)
    url_list_for_parser = ['https://www.dvfu.ru/about/rectorate/5520/', 'https://www.dvfu.ru/about/rectorate/4915/',
                           'https://www.dvfu.ru/about/rectorate/22008/', 'https://www.dvfu.ru/about/rectorate/288/',
                           'https://www.dvfu.ru/about/rectorate/4925/', 'https://www.dvfu.ru/about/rectorate/4917/',
                           'https://www.dvfu.ru/about/rectorate/32416/', 'https://www.dvfu.ru/about/rectorate/4921/',
                           'https://www.dvfu.ru/about/rectorate/37260/', 'https://www.dvfu.ru/about/rectorate/4923/',
                           'https://www.dvfu.ru/about/rectorate/33014/', 'https://www.dvfu.ru/about/rectorate/4913/']
    for url in url_list_for_parser:
        #delay()
        req = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}).text
        soup = bs(req, 'html.parser')
        main_FIO = soup.find('div', class_='author-name h1')
        try:
            l_FIO = main_FIO.text.split(' ')
        except AttributeError:
            l_FIO = ['Пусто', 'Пусто', 'Пусто']
        ###
        main_POS = soup.find('div', class_='author-dolj h3 mt-0 mb-4')
        ###
        main = soup.find('div', class_='mission mb-4')
        main_ADD = main.find('div', class_='block-address')
        main_PHN = main.find('div', class_='block-phone')
        main_EML = main.find('div', class_='block-email')
        main_data = FEFU(main_POS.text.rstrip('   '), l_FIO[0], l_FIO[1], l_FIO[2], main_ADD.text, main_PHN.text, main_EML.text)
        print(main_data)
        coll.insert_one(main_data)
        ###
        ###
        """delay()
        helpers = soup.find('div', class_='helpers hidden-xs')
        helpers_FIO = helpers.find_all('div', class_='helpers-title')
        helpers_POS = helpers.find_all('div', class_='helpers-num')
        helpers_ADD = helpers.find_all('div', class_='block-address')
        helpers_PHN = helpers.find_all('div', class_='block-phone')
        helpers_EML = helpers.find_all('div', class_='block-email')
        for helper in enumerate(helpers_FIO):
            l_FIO = helper[1].text.split(' ')
            try:
                h_POS = helpers_POS[helper[0]].text
            except IndexError:
                h_POS = None
            try:
                h_ADD = helpers_ADD[helper[0]].text
            except IndexError:
                h_ADD = None
            try:
                h_PHN = helpers_PHN[helper[0]].text
            except IndexError:
                h_PHN = None
            try:
                h_EML = helpers_EML[helper[0]].text
            except IndexError:
                h_EML = None
    
            data = FEFU(h_POS, l_FIO[0], l_FIO[1], l_FIO[2], h_ADD, h_PHN, h_EML)
            print(data)
            coll.insert_one(data)"""
