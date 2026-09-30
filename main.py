import requests


def get_public_ip():
    response = requests.get("https://ipinfo.io/json", timeout=10)
    ip_address = response.json().get("ip")
    if ip_address:
        print(f"Your public IP: {ip_address}")
        return ip_address
    else:
        return "Unable to retrieve public IP"

def get_data_info(ip_address):
    # API
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    data = response.json()

    city = data.get('city')
    region = data.get('region')
    country = data.get('country')
    loc = data.get('loc')
    org = data.get('org')
    postal = data.get('postal')
    timezone = data.get('timezone')

    print(f"City: {city}")
    print(f"Region: {region}")
    print(f"Country: {country}")
    print(f"Location: {loc}")
    print(f"Organization: {org}")
    print(f"Postal code: {postal}")
    print(f"Timezone: {timezone}")

def get_user_input():
    while True:
        try:
            choice = int(input("Choose an option:\n1. Enter IP address manually\n2. Automatic IP address detection\nYour choice: "))
            if choice in [1, 2]:
                return choice
            else:
                print("Enter a valid choice (1 or 2).")
        except ValueError:
            print("Enter a valid choice (1 or 2).")

def main():
    choice = get_user_input()

    if choice == 1:
        ip_address = input("Enter the IP address: ")
    elif choice == 2:
        ip_address = get_public_ip()
    else:
        print("Invalid IP address.")

    try:
        get_data_info(ip_address)
    except Exception as e:
        print(f"Information retrieval error: {e}")

if __name__ == "__main__":
    main()
