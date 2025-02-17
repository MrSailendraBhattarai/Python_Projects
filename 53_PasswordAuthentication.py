
# Password Authentication
import getpass

stored_username='admin'
stored_password='admin123'

username=input('Enter UserName : ')
password=getpass.getpass('Enter Your Password : ')

if username==stored_username and password == stored_password:
    print('Access Granted. Welcome ')
else:
    print('Invalid Username or Password ')