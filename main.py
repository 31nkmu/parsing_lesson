from bs4 import BeautifulSoup as bs
import requests
import csv


def get_html(url):
    response = requests.get(url)
    return response.text


def get_soup(html):
    soup = bs(html, 'lxml')
    return soup


def get_data(soup):
    catalog = soup.find('div', class_='grid-list asdads')
    phones = catalog.find_all('div', class_='ty-column4')
    for phone in phones:
        try:
            title = phone.find('a', class_='product-title').text
        except AttributeError:
            title = ''
        try:
            img = phone.find('img', class_='ty-pict').get('data-ssrc')
        except AttributeError:
            img = ''
        try:
            price = phone.find('span', class_='ty-price-update').text
        except AttributeError:
            price = ''
        write_csv({'title': title, 'img': img, 'price': price})


def get_page(soup):
    page = html.find('a', class_='cm-history ty-pagination__item hidden-phone ty-pagination__range cm-ajax cm-ajax-full-render')


def write_csv(data):
    with open('phones.csv', 'a') as file:
        names = ['title', 'img', 'price']
        writer = csv.DictWriter(file, delimitr=',', fieldnames=names)
        writer.writerow(data)


def main():
    BASE_URL = 'https://svetofor.info/sotovye-telefony-i-aksessuary/vse-smartfony/smartfony-s-podderzhkoy-4g-ru'
    html = get_html(BASE_URL)
    soup = get_soup(html)
    page = get_page(soup)
    get_data(soup)


if __name__ == '__main__':
    main()
