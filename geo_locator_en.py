import requests
import ipaddress

def show_banner():
    # Green color using ANSI code
    green = '\033[92m'
    reset = '\033[0m'  # Reset color to default
    
    banner = f"""
    {green}===========================
    | *▇▇▏◥▇◣┊◢▇◤▕▇▇*li.   |
    | *▇▇▏▃▆▅▎▅▆▃▕▇▇*li.   |
    | *▇▇▏╱▔▕▎▔▔╲▕▇▇*li.   |
    | *▇▇◣◣▃▅▎▅▃◢◢▇▇*li.   |
    | *▇▇▇◣◥▅▅▅◤◢▇▇▇*li.   |
    | *▇▇▇▇◣╲▇╱◢▇▇▇▇*li.   |
    ==========================={reset}
    """
    print(banner)

def get_location(ip=''):
    try:
        if not ip:
            response = requests.get("https://ipinfo.io/json")
        else:
            response = requests.get(f"https://ipinfo.io/{ip}/json")
        
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        data = response.json()
        return data
            
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    show_banner()
    ip = input("Enter IP address (leave empty to use current IP): ").strip()
    
    if ip:
        try:
            ipaddress.ip_address(ip)  # Validate the IP address
        except ValueError:
            print("Invalid IP address format.")
            return
    
    location_data = get_location(ip)  # Call the function with the IP address
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
