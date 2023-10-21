from bs4 import BeautifulSoup
import requests
import openpyxl
URL1 = 'https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2'
URL2 = 'Cn%3A193870011%2Cn%3A17923671011%2Cn%3A229189&dc&ds=v1%3AjgRE6bvwNYJ0pjK7Yen49gbA8h'
URL3 = 'ODdZSqGCtSxtRuDAE&rnid=17923671011&ref=sr_nr_n_1'
agent1 = 'https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2'
agent2 = 'Cn%3A193870011%2Cn%3A17923671011%2Cn%3A229189&dc&ds=v1%3AjgRE6bvwNYJ0pjK7Yen49gbA8h'
agent3 = 'ODdZSqGCtSxtRuDAE&rnid=17923671011&ref=sr_nr_n_1'
HEADERS = ({'User-Agent': agent1+agent2+agent3, 'Accept-Language': 'en-US, en;q=0.5'})

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'PROCESOR SCRAPING'
sheet.append(['Naziv', 'Cena'])

try:
    source = requests.get(URL1+URL2+URL3, headers=HEADERS)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')

    classprocesori = "s-main-slot s-result-list s-search-results sg-row"
    procesori = soup.find('div', class_=classprocesori).find_all('div', class_="sg-col-inner")
    print(len(procesori))

    for procesor in procesori:
        nazivi = procesor.find('h2', class_="a-size-mini a-spacing-none a-color-base s-line-clamp-4")
        naziv = nazivi.find('span', class_="a-size-base-plus a-color-base a-text-normal").text
        cena = procesor.find('span', class_="a-offscreen").text
        sheet.append([naziv, cena])

except Exception as e:
    print(e)

excel.save('PROCESOR SCRAPE.xlsx')
