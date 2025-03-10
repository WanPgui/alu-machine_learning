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

        # Print the full response using .format() instead of f-string
        print("Full Response: {}".format(res))

        # Check if the 'location' field exists and print it
        if 'location' in res:
            print("Location: {}".format(res['location']))

        # If 'location' is not found, try combining city, region, and country
        elif 'city' in res and 'region' in res and 'country' in res:
            print("Location: {}".format(res['city']))  # Now printing just the city (e.g., Tilburg)

        # If 'loc' (latitude, longitude) is found, print it
        elif 'loc' in res:
            print("Location (Lat, Long): {}".format(res['loc']))

        else:
            print("Location info not found in response.")
