import requests

def analyze_ip(ip):
    result = {}
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()
        if data['status'] == 'success':
            result = {
                'IP': ip,
                'Country': data.get('country'),
                'Region': data.get('regionName'),
                'City': data.get('city'),
                'ISP': data.get('isp'),
                'Organization': data.get('org'),
                'AS': data.get('as'),
                'Latitude': data.get('lat'),
                'Longitude': data.get('lon'),
                'Google Maps': f"https://maps.google.com/?q={data.get('lat')},{data.get('lon')}"
            }
        else:
            result = {'Error': data.get('message')}
    except Exception as e:
        result = {'Error': str(e)}
    return result