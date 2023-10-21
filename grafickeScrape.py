from bs4 import BeautifulSoup
import requests
import openpyxl
URL = 'https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A193870011%2Cn%3A17923671011%2Cn%3A284822%2Cp_36%3A1253506011&dc&qid=1684962053&rnid=386442011&ref=sr_nr_p_36_4&ds=v1%3AysKQjwo36l6mFWQym6hYUFE4xcnpqDbelo4NNGDnMG8'
agent1 = 'https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2'
agent2 = 'Cn%3A193870011%2Cn%3A17923671011%2Cn%3A229189&dc&ds=v1%3AjgRE6bvwNYJ0pjK7Yen49gbA8h'
agent3 = 'ODdZSqGCtSxtRuDAE&rnid=17923671011&ref=sr_nr_n_1'
HEADERS = ({'User-Agent': agent1+agent2+agent3, 'Accept-Language': 'en-US, en;q=0.5'})

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'SCRAPING GRAFICKIH KARTICA'
sheet.append(['Naziv', 'Cena'])

try:
    source = requests.get(URL, headers=HEADERS)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')

    classgrafickekartice = "s-main-slot s-result-list s-search-results sg-row"
    grafickeKartice = soup.find('div', class_=classgrafickekartice).find_all('div', class_="sg-col-inner")

    for grafickaKartica in grafickeKartice:
        nazivi = grafickaKartica.find('h2', class_="a-size-mini a-spacing-none a-color-base s-line-clamp-4")
        naziv = nazivi.find('span', class_="a-size-base-plus a-color-base a-text-normal").text
        cena = grafickaKartica.find('span', class_="a-offscreen").text
        sheet.append([naziv, cena])

except Exception as e:
    print(e)

excel.save('SCRAPE GRAFICKIH KARTICA.xlsx')
