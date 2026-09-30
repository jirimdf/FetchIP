import ipaddress

import requests

API_URL = "https://ipinfo.io"
TIMEOUT = 10

FIELDS = [
    ("city", "City"),
    ("region", "Region"),
    ("country", "Country"),
    ("loc", "Location"),
    ("org", "Organization"),
    ("postal", "Postal code"),
    ("timezone", "Timezone"),
]


def get_public_ip():
    response = requests.get(f"{API_URL}/json", timeout=TIMEOUT)
    response.raise_for_status()
    ip_address = response.json().get("ip")
    if not ip_address:
        raise ValueError("Unable to retrieve public IP")
    print(f"Your public IP: {ip_address}")
    return ip_address


def is_valid_ip(ip_address):
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False


def get_data_info(ip_address):
    response = requests.get(f"{API_URL}/{ip_address}/json", timeout=TIMEOUT)
    response.raise_for_status()
    data = response.json()

    if data.get("bogon"):
        print(f"{ip_address} is a private or reserved address, so it has no location.")
        return data

    for key, label in FIELDS:
        print(f"{label}: {data.get(key) or 'Unknown'}")
    return data


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


def ask_ip_address():
    while True:
        ip_address = input("Enter the IP address: ").strip()
        if is_valid_ip(ip_address):
            return ip_address
        print("Invalid IP address, try again.")


def main():
    try:
        choice = get_user_input()
        ip_address = ask_ip_address() if choice == 1 else get_public_ip()
        get_data_info(ip_address)
    except (requests.RequestException, ValueError) as e:
        print(f"Information retrieval error: {e}")
    except (KeyboardInterrupt, EOFError):
        print("\nExiting..")


if __name__ == "__main__":
    main()
