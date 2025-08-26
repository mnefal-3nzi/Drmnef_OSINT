import requests
import re

def check_url_safety(url):
    result = {}
    try:
        r = requests.get(f"https://urlscan.io/api/v1/search/?q=domain:{url}", timeout=10)
        if r.status_code == 200 and r.json().get('results'):
            result['Found on urlscan.io'] = True
        else:
            result['Found on urlscan.io'] = False
    except Exception as e:
        result['Error (urlscan.io)'] = str(e)

    result['Google Dork'] = f"https://www.google.com/search?q=\"{url}\"+site:pastebin.com+OR+site:anonfiles.com+OR+site:hastebin.com"
    return result