import json
from requests import get

info = json.loads(get('https://ipapi.co/json/').text)

print("\033[93m-------We ArE ReApEr------")
print("Current IP details:")
print("Public IP: " + format(info['ip']))
print("City: " + format(info['city']))
print("Region: " + format(info['region']))
print("Region code: " + format(info['region_code']))
print("Country: " + format(info['country_name']))
print("Country Capital: " + format(info['country_capital']))
print("Continent: " + format(info['continent_code']))
print("Postal Code: " + format(info['postal']))
print("Country Calling Code: " + format(info['country_calling_code']))
print("Currency: " + format(info['currency']))
print("ASN: " + format(info['asn']))
print("Organization: " + format(info['org']))