#!/usr/bin/python3

import sys
import requests
from requests import status_codes

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("Usage: <IP> <HOST>")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    if sys.argv[1] == 'HOST':
        url = requests.get(sys.argv[2])
        url = status_codes
        print(url)
