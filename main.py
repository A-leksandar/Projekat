from bs4 import BeautifulSoup
import requests
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'AMAZON TOP 20 KNJIGA GODINE'
sheet.append(['Naslov', 'Autor', 'Cena'])

URL = 'https://www.amazon.com/gp/browse.html?rw_useCurrentProtocol=1&node=17276804011&ref_=bhp_brws_boty21'
agent = 'https://www.amazon.com/gp/browse.html?rw_useCurrentProtocol=1&node=17276804011&ref_=bhp_brws_boty21'
HEADERS = ({'User-Agent': agent, 'Accept-Language': 'en-US, en;q=0.5'})

try:
    source = requests.get(URL, headers=HEADERS)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')

    knjige = soup.find('ol', class_="a-carousel").find_all('li')

    for knjiga in knjige:
        naslov = knjiga.find('span', class_="a-truncate-full").text
        autori = knjiga.find('span', class_="a-truncate acs-product-block__contributor a-size-base")
        autor = autori.find('span', class_="a-truncate-full").text
        cena = knjiga.find('span', class_="a-offscreen").text
        sheet.append([naslov, autor, cena])

except Exception as e:
    print(e)

excel.save('AMAZON TOP 20 KNJIGA GODINE.xlsx')
