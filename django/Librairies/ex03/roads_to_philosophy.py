import requests, sys
from bs4 import BeautifulSoup


def get_page_content(title):
    search = requests.Session()
    url = f"https://en.wikipedia.org/wiki/{title}"   
    headers = {
    "User-Agent": "MonProjetWikipedia/1.0 (mon.email@example.com)"
}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    return(response.text)

def road_to_philo(search, count):

    html = get_page_content(search)
    if html is None:
        print('It leads to a dead end !')
        sys.exit(1)
    soup = BeautifulSoup(html, "html.parser")
    main_title = soup.find('span', class_='mw-page-title-main')
    print(main_title.string)
    count += 1
    if main_title.string == 'Philosophy':
        return(count)  
    div = soup.find('div', id='bodyContent')
    for p in div.find_all('p'):
        link = p.find('a', class_=lambda c: not c or 'mw-disambig' not in c, href=lambda h: h and h.startswith('/wiki/'))
        if link:
            search_title = link['title']
            return road_to_philo(search_title, count)
    return None

def main(args):
   
    if (len(args) != 2):
        print("Wrong number of arguments")
        return 1
    nombre = road_to_philo(args[1], count = 0)
    print(f'{nombre + 1 } roads from {args[1]} to philosophy')

            
           
    
if __name__ == "__main__":
    main(sys.argv)
