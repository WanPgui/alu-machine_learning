#!/usr/bin/env python3

""" Return location info """

import requests
import sys
import time


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 2-user_location.py <url>")
        sys.exit(1)

    res = requests.get(sys.argv[1])

    if res.status_code == 403:
        rate_limit = int(res.headers.get('X-Ratelimit-Reset', 0))
        current_time = int(time.time())
        diff = (rate_limit - current_time) // 60
        print("Reset in {} min".format(diff))

    elif res.status_code == 404:
        print("Not found")

    elif res.status_code == 200:
        res = res.json()
        print(f"IP: {res.get('ip')}")
        print(f"City: {res.get('city')}")
        print(f"Region: {res.get('region')}")
        print(f"Country: {res.get('country')}")
        print(f"Location (Lat, Long): {res.get('loc')}")
