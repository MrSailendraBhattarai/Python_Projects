
# Ip Address information

import requests
import json
import re

def is_valid_ip(ip):
    """Validate IPv4 address format"""
    pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"
    return re.match(pattern, ip) is not None

while True:
    ip = input('Enter Targeted IP (or type "exit" to quit): ').strip()
    
    if ip.lower() == "exit":
        print("Exiting program...")
        break

    if not is_valid_ip(ip):
        print("Invalid IP address format. Please enter a valid IPv4 address.")
        continue

    url = f'http://ip-api.com/json/{ip}'

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        values = response.json()

        if values.get('status') == 'fail':
            print(f"Error: Could not retrieve information for IP {ip}. Reason: {values.get('message', 'Unknown')}")
        else:
            print("\n--- IP Address Information ---")
            print(f"IP       : {values.get('query', 'N/A')}")
            print(f"Country  : {values.get('country', 'N/A')} ({values.get('countryCode', 'N/A')})")
            print(f"Region   : {values.get('regionName', 'N/A')} ({values.get('region', 'N/A')})")
            print(f"City     : {values.get('city', 'N/A')}")
            print(f"ISP      : {values.get('isp', 'N/A')}")
            print(f"Org      : {values.get('org', 'N/A')}")
            print(f"Timezone : {values.get('timezone', 'N/A')}")
            print(f"Latitude / Longitude: {values.get('lat', 'N/A')} / {values.get('lon', 'N/A')}")
            print("-" * 35)

    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to retrieve data. {e}")

