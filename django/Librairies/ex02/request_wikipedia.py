import json, requests, dewiki, sys

def search_title(title):
    search = requests.Session()
    url = "https://fr.wikipedia.org/w/api.php"
    params = {
        "action": "opensearch",
        "namespace": "0",
        "search": title,
        "limit": "5",
        "format": "json"
    }
    headers = {
    "User-Agent": "MonProjetWikipedia/1.0 (mon.email@example.com)"
}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        return None
    data = response.json()
    if len(data[1]) > 0:
        return(data[1][0])
    return None


def get_page_content(title):
    search = requests.Session()
    url = "https://fr.wikipedia.org/w/api.php"
    params = {
    "action": "query",
    "titles": title,
    "prop": "extracts",
    "explaintext": True,
    "redirects": True,
    "format": "json",
}
    headers = {
    "User-Agent": "MonProjetWikipedia/1.0 (mon.email@example.com)"
}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        return None
    content = response.json()
    pages = content["query"]["pages"]
    page = next(iter(pages.values())) #on recupere les valeurs qui se trouvent dans dictionnaire page
    if "extract" not in page:
        return None
    return (page["extract"])
    


def main(args):
   
    if (len(args) != 2):
        print("Wrong number of arguments")
        return 1
    title = search_title(args[1])
    if title is None:
        print('article not found')
        return 1
    result = get_page_content(title)
    if result is None:
        print(f'Could not retrieved content for {title}')
        return 1
    title = title.replace(' ', '_')
    try:
        with open(f'{title}.wiki','w') as file:
            file.write(result)
            return 0
    except Exception as e:
        print (f"Error: could not write file '{title}")
        return 1
    
if __name__ == "__main__":
    main(sys.argv)
