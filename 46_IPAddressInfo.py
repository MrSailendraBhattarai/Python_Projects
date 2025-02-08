
# Ip Address information

import urllib.request as urllib2
import json

while True:
    ip = input('Enter Targeted IP: ')
    url = 'http://ip-api.com/json/'

    try:
        # Make the request to the API
        response = urllib2.urlopen(url + ip)
        data = response.read()
        values = json.loads(data)

        # Check if the status is 'fail'
        if values.get('status') == 'fail':
            print(f"Error: Could not retrieve information for IP {ip}.")
        else:
            # Print IP information with checks for missing fields
            print('IP : ' + values.get('query', 'N/A'))
            print('CITY : ' + values.get('city', 'N/A'))
            print('ISP : ' + values.get('isp', 'N/A'))
            print('Country : ' + values.get('country', 'N/A'))
            print('Region : ' + values.get('region', 'N/A'))
            print('Timezone : ' + values.get('timezone', 'N/A'))

    except Exception as e:
        print(f"Error: {e}")
    
    break


