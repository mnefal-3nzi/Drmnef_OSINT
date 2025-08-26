import socket
import whois
import requests

def analyze_domain(domain):
    result = {}

    # WHOIS Lookup
    try:
        w = whois.whois(domain)
        result['Whois Info'] = {
            'Registrar': w.registrar,
            'Creation Date': str(w.creation_date),
            'Expiration Date': str(w.expiration_date),
            'Name Servers': w.name_servers,
            'Emails': w.emails
        }
    except Exception as e:
        result['Whois Info'] = f'Error: {e}'

    # DNS Lookup
    try:
        ip = socket.gethostbyname(domain)
        result['IP Address'] = ip
    except Exception as e:
        result['IP Address'] = f'Error: {e}'

    # GeoIP
    try:
        geo = requests.get(f"http://ip-api.com/json/{ip}").json()
        result['GeoIP'] = {
            "Country": geo.get("country"),
            "City": geo.get("city"),
            "ISP": geo.get("isp"),
            "Org": geo.get("org"),
            "AS": geo.get("as")
        }
    except Exception as e:
        result['GeoIP'] = f'Error: {e}'

    return result