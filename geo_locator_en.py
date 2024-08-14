import requests

def show_banner():
    banner = '''
▇▇▏◥▇◣┊◢▇◤▕▇▇ 
▇▇▏▃▆▅▎▅▆▃▕▇▇ 
▇▇▏╱▔▕▎▔▔╲▕▇▇
▇▇◣◣▃▅▎▅▃◢◢▇▇ 
▇▇▇◣◥▅▅▅◤◢▇▇▇ 
▇▇▇▇◣╲▇╱◢▇▇▇▇  
    print(banner)

def get_location(ip=''):
    try:
        if not ip:
            response = requests.get("https://ipinfo.io/json")
        else:
            response = requests.get(f"https://ipinfo.io/{ip}/json")
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    show_banner()
    ip = input("Enter IP address (leave empty to use current IP): ").strip()
    
    if ip:
        parts = ip.split('.')
        if len(parts) != 4 or not all(part.isdigit() and 0 <= int(part) <= 255 for part in parts):
            print("Invalid IP address format.")
            return
    
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
