import requests
import urllib.request
import time
from bs4 import BeautifulSoup


def run_webscrap():
    # set the url you want to webscrap
    url = 'https://www.infodolar.com/cotizacion-dolar-entidad-banco-galicia.aspx'

    # connect to url
    response = requests.get(url)

    # parse HTML and save bs4 object
    soup = BeautifulSoup(response.text, "html.parser")
    a = soup.findAll('td')

    result_list = []
    for p in soup.select('td'):
        result_list.append(p.text.strip())
        print(p.text.strip())
    result_list

    with open('dolar.txt', 'r') as dolar_file:
        new_value = float(result_list[2][1:].replace(',', '.'))
        old_value = float(dolar_file.read()[1:].replace(',', '.'))
        print('####################')
        print('Old Value:', old_value)
        print('New Value:', new_value)
        if new_value > old_value:
            print ("Dolar increase")
        elif new_value == old_value:
            print ("Dolar stable")
        else:
            print ("Dolar decrease")
        print('####################')

    with open('dolar.txt', 'w') as dolar_file:
        dolar_file.write(result_list[2])


if __name__ == '__main__':
    while True:
        run_webscrap()
        time.sleep(3600)