import requests
import time
import json

SCRAPE_DELAY = 60 * 5 # in secs
SEARCH_QUERY = "timex marlin"
CSV_FILE_NAME = "items.csv"

SEARCH_QUERY = SEARCH_QUERY.replace(" ", "+")
vinted_link = f"https://www.vinted.it/api/v2/catalog/items?page=1^&per_page=960^&search_text={SEARCH_QUERY}^&catalog_ids=^&order=newest_first"

vinted_cookies = {}
links = []
catalog = {}

headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'it-fr',
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://www.vinted.it/catalog?search_text=timex+marlin',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        }

def get_vinted_cookies():
    global vinted_cookies
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3',
            'DNT': '1',
            'Sec-GPC': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Priority': 'u=0, i',
    }
    response = requests.head('https://www.vinted.it/', headers=headers)
    headers = response.headers["set-cookie"]
    for cookie_string in headers.split(','):
        parts = cookie_string.strip().split(';')
        if parts:
            name_value = parts[0].strip()
            if '=' in name_value:
                name, value = name_value.split('=', 1)
                vinted_cookies[name] = value

def curl_vinted():
    global catalog
    try:
        response = requests.get(
                vinted_link,
                cookies=vinted_cookies,
                headers=headers,
                )
        response.raise_for_status()
        catalog = json.loads(response.text)
        print("[CURL] scraped successfully")
        return 0
    except requests.exceptions.RequestException as e:
        print(f"[CURL] Error during curl: {e}")
        return 1
    except Exception as e:
        print(f"[CURL] Unexpected error: {e}")
        return 2 

def scrape_vinted():
    get_vinted_cookies()
    while 1:
        if curl_vinted():
            time.sleep(SCRAPE_DELAY)
            get_vinted_cookies()
            continue
        for item in catalog["items"]:
            if item["path"] not in links:
                links.append(item["path"])
                print("Found: " + item["title"] + '\n'
                      "\tAt: " + item["price"]["amount"] + '\n'
                      "\thttps://vinted.it" + item["path"])
                with open(CSV_FILE_NAME, "a") as f:
                    f.write(item["title"].replace(',','') + ',' + item["price"]["amount"] + ',' +
                            "https://vinted.it" + item["path"] + '\n')
        time.sleep(SCRAPE_DELAY)

with open(CSV_FILE_NAME, "r") as f:
    for line in f:
        links.append(line[line.rfind(",https://vinted.it") + 18:-1])
scrape_vinted()
