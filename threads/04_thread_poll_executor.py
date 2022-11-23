import logging
from concurrent.futures import ThreadPoolExecutor
import shutil
from urllib.request import urlopen

URLS = [
    "https://ya.ru/",
    "https://practicum.yandex.ru/",
    "https://practicum.yandex.ru/blog",
    "https://business.yandex.ru/",
]

def fetch_url(url):
    with urlopen(url) as response:
        return response.read()

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info(f"Создали пул для копирования файлов...")
    futures = []
    with ThreadPoolExecutor(max_workers=1) as pool:
        pool.submit(shutil.copy, "file1.log", "target1.txt")
        pool.submit(shutil.copy, "target1.txt", "target2.log")
        pool.submit(shutil.copy, "target2.log", "dest1.txt")

    logging.info(f"Создали пул для загрузки данных с указанных web-страниц...")
    with ThreadPoolExecutor() as pool:
        results = pool.map(fetch_url, URLS, chunksize=2)