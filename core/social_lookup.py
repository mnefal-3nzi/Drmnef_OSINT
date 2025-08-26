import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

def parse_twitter(username):
    url = f"https://twitter.com/{username}"
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code != 200:
            return {"Error": f"User not found or protected ({r.status_code})"}
        soup = BeautifulSoup(r.text, "html.parser")
        name = soup.find("title").text.strip().replace(" / X", "")
        return {
            "Platform": "Twitter",
            "Username": username,
            "Profile URL": url,
            "Name": name
        }
    except Exception as e:
        return {"Error": str(e)}

def parse_instagram(username):
    url = f"https://www.instagram.com/{username}/"
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code != 200:
            return {"Error": f"User not found ({r.status_code})"}
        soup = BeautifulSoup(r.text, "html.parser")
        meta = soup.find("meta", property="og:description")
        img = soup.find("meta", property="og:image")
        if meta:
            description = meta["content"].split("-")[0].strip()
        else:
            description = "N/A"
        return {
            "Platform": "Instagram",
            "Username": username,
            "Profile URL": url,
            "Info": description,
            "Image": img["content"] if img else ""
        }
    except Exception as e:
        return {"Error": str(e)}

def parse_tiktok(username):
    url = f"https://www.tiktok.com/@{username}"
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code != 200:
            return {"Error": f"User not found ({r.status_code})"}
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.find("title").text.strip()
        img = soup.find("meta", property="og:image")
        return {
            "Platform": "TikTok",
            "Username": username,
            "Profile URL": url,
            "Name": title,
            "Image": img["content"] if img else ""
        }
    except Exception as e:
        return {"Error": str(e)}