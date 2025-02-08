
# Find Currency of Country

import pycountry

def get_currency(country_name):
    try:
        country=pycountry.countries.lookup(country_name)
        currency=pycountry.currencies.get(numeric=country.numeric)
        return f'Currency of {country_name} is {currency.name}'
    
    except:
        return 'Country not found for currency information '
    
country_name=input('Enter Country name : ')

print(get_currency(country_name))