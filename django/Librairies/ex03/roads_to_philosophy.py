import requests
import sys
from bs4 import BeautifulSoup

TIMEOUT = 10

def get_page_content(title):
    url = f"https://en.wikipedia.org/wiki/{title}"
    headers = {
        "User-Agent": "MonProjetWikipedia"
    }
    response = requests.get(url, headers=headers, timeout=TIMEOUT)
    if response.status_code != 200:
        return None
    return response.text


def road_to_philo(search, count, list_titles):
    html = get_page_content(search)
    if html is None:
        print("It leads to a dead end !")
        sys.exit(1)

    soup = BeautifulSoup(html, "html.parser")
    main_title = soup.find("span", class_="mw-page-title-main")
    if main_title is None:
        main_title = soup.find("h1", id="firstHeading")

    if main_title is None or main_title.string is None:
        print("It leads to a dead end !")
        sys.exit(1)

    title_str = main_title.string

    if title_str in list_titles:
        print("It leads to an infinite loop !")
        sys.exit(1)

    list_titles.append(title_str)
    count += 1

    if title_str == "Philosophy":
        return count

    div = soup.find("div", id="mw-content-text")
    if div is None:
        print("It leads to a dead end !")
        sys.exit(1)

    for p in div.find_all("p"):
        link = p.find(
            "a",
            id=lambda c: c,
            href=lambda h: h and h.startswith("https://en.wikipedia.org/wiki/"),
        )
        if link and link.get("title"):
            return road_to_philo(link["title"], count, list_titles)

    for ul in div.find_all("ul"):
        link = ul.find(
            "a",
            id=lambda c: c,
            href=lambda h: h and h.startswith("https://en.wikipedia.org/wiki/"),
        )
        if link and link.get("title"):
            return road_to_philo(link["title"], count, list_titles)

    print("It leads to a dead end !")
    sys.exit(1)


def main(args):
    if len(args) != 2:
        print("Wrong number of arguments")
        return 1

    if not args[1].strip():
        print("Error: empty parameter.")
        return 1

    list_titles = []

    try:
        nombre = road_to_philo(args[1], 0, list_titles)
    except requests.exceptions.Timeout:
        print("Error: the request to Wikipedia timed out.")
        return 1
    except requests.exceptions.ConnectionError:
        print("Error: unable to connect to Wikipedia. Please check your internet connection.")
        return 1
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP error occurred ({e}).")
        return 1
    except requests.exceptions.RequestException as e:
        print(f"Error: a network error occurred ({e}).")
        return 1
    except RecursionError:
        print("Error: too many redirections, aborting.")
        return 1
    except Exception as e:
        print(f"Error: an unexpected error occurred ({e}).")
        return 1

    for title in list_titles:
        print(title)

    if nombre is not None:
        print(f"{nombre} roads from {args[1]} to philosophy")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))