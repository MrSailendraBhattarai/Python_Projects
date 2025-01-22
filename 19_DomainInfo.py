# PIP install python-whois
# Domain information
import whois
user=input('Enter Domain  to Get information :')
domain_info=whois.whois(user)
for key,value in domain_info.items():
    print(key,':',value)