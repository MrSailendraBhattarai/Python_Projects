
# Check Secure Websites
import requests

def check_website_security(url):
    try:
        # Send a request to the URL and check the protocol used
        response = requests.get(url, timeout=10)

        # Check if the website uses HTTPS
        if response.url.startswith("https://"):
            print(f"The website '{url}' is secure (HTTPS).")
        else:
            print(f"The website '{url}' is not secure (HTTP).")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing the website '{url}': {e}")

# Example usage
url =input('Enter Url : ')
check_website_security(url)
