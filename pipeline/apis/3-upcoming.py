import requests
from datetime import datetime

if __name__ == '__main__':
    """Pipeline API"""
    url = "https://api.spacexdata.com/v4/launches/upcoming"

    try:
        r = requests.get(url)
        r.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print("Error fetching launches:", e)
        exit(1)

    launches = r.json()
    if not launches:  # Check if API returned empty data
        print("No upcoming launches found.")
        exit(1)

    recent = 0
    launch_name, date, rocket_number, launch_number = "", "", "", ""

    for dic in launches:
        new = int(dic["date_unix"])
        if recent == 0 or new < recent:
            recent = new
            launch_name = dic["name"]
            date = dic["date_local"]
            rocket_number = dic["rocket"]
            launch_number = dic["launchpad"]

    # Fetch rocket details
    rurl = f"https://api.spacexdata.com/v4/rockets/{rocket_number}"
    try:
        rocket_res = requests.get(rurl)
        rocket_res.raise_for_status()
        rocket_name = rocket_res.json().get("name", "Unknown Rocket")
    except requests.exceptions.RequestException:
        rocket_name = "Unknown Rocket"

    # Fetch launchpad details
    lurl = f"https://api.spacexdata.com/v4/launchpads/{launch_number}"
    try:
        launchpad_res = requests.get(lurl)
        launchpad_res.raise_for_status()
        launchpad_data = launchpad_res.json()
        launchpad_name = launchpad_data.get("name", "Unknown Launchpad")
        launchpad_local = launchpad_data.get("locality", "Unknown Location")
    except requests.exceptions.RequestException:
        launchpad_name, launchpad_local = "Unknown Launchpad", "Unknown Location"

    # Print final result
    string = f"{launch_name} ({date}) {rocket_name} - {launchpad_name} ({launchpad_local})"
    print(string)
