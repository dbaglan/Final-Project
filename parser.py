import requests

def fetchPage (page):
    url = "https://kolesa.kz/cars/"
    if(page > 1):
        url = url + '?page=' + page
        
    payload = {}
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,kk;q=0.6,ay;q=0.5',
    'cache-control': 'max-age=0',
    'cookie': 'klssid=ccfgprnl6l945n5ss4af5h5ldt; _gid=GA1.2.817099256.1733633879; _ym_uid=1733633880492231160; _ym_d=1733633880; _ym_isad=1; _gat=1; _gcl_au=1.1.282404141.1733633880; _tt_enable_cookie=1; _ttp=Qt9IWjzDeUYNEXX_KG1-A8JMJrX.tt.1; kl_cdn_host=//alakcell-kz.kcdn.online; ssaid=00815980-b521-11ef-84ea-a76349522c23; _ym_visorc=b; _ga=GA1.1.1325987782.1733633879; __tld__=null; _ga_J2EHNEPMTC=GS1.1.1733633881.1.0.1733633888.53.0.958881996; gh_show=1; _ga_K434WRXPFF=GS1.1.1733633880.1.1.1733633900.40.0.2098214587',
    'priority': 'u=0, i',
    'referer': 'https://kolesa.kz/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

fetchPage(1)


