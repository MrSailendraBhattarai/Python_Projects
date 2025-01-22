#pip install countryinfo

from countryinfo import CountryInfo

user=input("Entry Country to View Details>> ")

country=CountryInfo(user)
print("Capital : ",country.capital())
print('Currency : ',country.currencies())
print('Languages : ',country.languages())
print('Border Sharing With : ',country.borders())


