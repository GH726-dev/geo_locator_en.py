import requests
import ipaddress

def show_banner():
    # اللون الأخضر باستخدام كود ANSI
    green = '\033[92m'
    reset = '\033[0m'  # لإعادة تعيين اللون إلى اللون الافتراضي
    
    banner = f'''
    {green}===========================
    | *▇▇▏◥▇◣┊◢▇◤▕▇▇*li.   |
    | *▇▇▏▃▆▅▎▅▆▃▕▇▇*li.   |
    | *▇▇▏╱▔▕▎▔▔╲▕▇▇*li.   |
    | *▇▇◣◣▃▅▎▅▃◢◢▇▇*li.   |
    | *▇▇▇◣◥▅▅▅◤◢▇▇▇*li.   |
    | *▇▇▇▇◣╲▇╱◢▇▇▇▇*li.   |
    ==========================={reset}
    '''
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
    
    location_data = get_location
