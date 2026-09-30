# FetchIP

A Python command-line tool that finds your public IP address and shows geolocation information about it. You can enter any IP address manually or let the tool detect your own.

## Features

- Automatic detection of your public IP address (scraped from [myip.dk](https://www.myip.dk))
- Manual IP address input
- Geolocation lookup via the [ipinfo.io](https://ipinfo.io) API
- Error handling for network and parsing errors

## Tech stack

- Python 3
- Requests
- Beautiful Soup 4

## Installation

```bash
git clone https://github.com/jirimdf/FetchIP.git
cd FetchIP
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Choose an option in the menu:

1. Enter an IP address manually
2. Detect your public IP address automatically

The tool then prints the following information:

- City
- Region
- Country
- Location (latitude, longitude)
- Organization (ISP)
- Postal code
- Timezone

## Notes

- Automatic detection depends on the HTML structure of myip.dk, so it may stop working if the website changes. Manual input uses only the ipinfo.io API.

## License

This project is licensed under the [MIT License](LICENSE).
