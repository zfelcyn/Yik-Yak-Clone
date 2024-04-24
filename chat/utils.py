# forum/utils.py

import requests

def get_location_from_ip(ip_address):
    API_KEY = '69.166.46.175'
    url = f'http://api.ipstack.com/{ip_address}?access_key={API_KEY}'
    response = requests.get(url)
    data = response.json()
    try:
        city = data.get('city')
        if city:
            print(city)
            return city
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None, None
