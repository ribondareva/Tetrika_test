import urllib.request
from urllib.parse import urlsplit, urlunsplit, quote
from bs4 import BeautifulSoup
import csv
import time

BASE = "https://ru.wikipedia.org"
START = "/wiki/Категория:Животные_по_алфавиту"


def get_html(url: str) -> str:
    full = url if url.startswith("http") else BASE + url
    parts = urlsplit(full)  # (scheme, netloc, path, query, frag)
    # кодируем path и query, оставляя /, ?, =, & и %
    path = quote(parts.path, safe="/%")
    query = quote(parts.query, safe="=&%")
    full_encoded = urlunsplit((parts.scheme, parts.netloc, path, query, ""))

    with urllib.request.urlopen(full_encoded) as resp:
        return resp.read().decode("utf-8")


def get_animals_and_next(url):
    soup = BeautifulSoup(get_html(url), "html.parser")
    animals = []

    groups = soup.find_all("div", class_="mw-category-group")
    for group in groups:
        for li in group.find_all("li"):
            name = li.text.strip()
            if name:
                animals.append(name)

    next_link = soup.find("a", string="Следующая страница")
    next_href = next_link.get("href") if next_link else None

    return animals, next_href


def parse_all():
    stats = {}
    current_url = START

    while current_url:
        print(f"Обрабатываем: {current_url}")
        animals, next_url = get_animals_and_next(current_url)

        for animal in animals:
            first_letter = animal[0].upper()
            if 'А' <= first_letter <= 'Я' or first_letter == 'Ё':
                stats[first_letter] = stats.get(first_letter, 0) + 1

        current_url = next_url
        time.sleep(0.2)

    return stats


def write_csv(stats):
    with open("beasts.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for letter, count in sorted(stats.items()):
            writer.writerow([letter, count])


if __name__ == "__main__":
    stats = parse_all()
    write_csv(stats)
    print("Файл beasts.csv создан")
