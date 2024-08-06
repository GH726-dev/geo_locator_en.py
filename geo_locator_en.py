import requests

def show_banner():
    banner = '''
    ===========================
    |   Geo Locator Tool      |
    |     By Python           |
    ===========================
    '''
    print(banner)

def get_location(ip=''):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    show_banner()
    ip = input("Enter IP address (leave empty to use current IP): ").strip()
    
    location_data = get_location(ip)
    if location_data:
        print(f"IP: {location_data.get('ip', 'N/A')}")
        print(f"City: {location_data.get('city', 'N/A')}")
        print(f"Region: {location_data.get('region', 'N/A')}")
        print(f"Country: {location_data.get('country', 'N/A')}")
        print(f"Location: {location_data.get('loc', 'N/A')}")
        print(f"ISP: {location_data.get('org', 'N/A')}")
    else:
        print("Unable to retrieve information.")

if __name__ == "__main__":
    main()
