# FetchIP

[![Tests](https://github.com/jirimdf/FetchIP/actions/workflows/tests.yml/badge.svg)](https://github.com/jirimdf/FetchIP/actions/workflows/tests.yml)

A Python command-line tool that finds your public IP address and shows geolocation information about it. You can enter any IP address manually or let the tool detect your own.

## Features

- Automatic detection of your public IP address
- Manual IP address input
- Geolocation lookup via the [ipinfo.io](https://ipinfo.io) API
- Error handling for network errors

## Tech stack

- Python 3
- Requests
- [ipinfo.io](https://ipinfo.io) API

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

### Example output

```
Choose an option:
1. Enter IP address manually
2. Automatic IP address detection
Your choice: 1
Enter the IP address: 8.8.8.8
City: Mountain View
Region: California
Country: US
Location: 38.0088,-122.1175
Organization: AS15169 Google LLC
Postal code: 94043
Timezone: America/Los_Angeles
```

## Tests

```bash
pip install pytest
python -m pytest
```

The tests mock the ipinfo.io API, so they need no network access. Tests run automatically on every push via GitHub Actions.

## Notes

- Both automatic detection and the lookup use the free ipinfo.io API, which has a rate limit for requests without an API token.

## License

This project is licensed under the [MIT License](LICENSE).
