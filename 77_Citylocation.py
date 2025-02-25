# City Location
import webbrowser

def show_location(city_name):
    # Generate the Google Earth URL (Google Maps in Earth mode)
    url = f"https://earth.google.com/web/search/{city_name}"
    
    # Open in the default web browser
    webbrowser.open(url)

# Example usage
city = input("Enter a city name: ")
show_location(city)
