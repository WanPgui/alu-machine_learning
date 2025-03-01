#!/usr/bin/env python3
'''
    Script that displays the upcoming launch
'''

import requests


def get_upcoming_launch():
    '''
    Prints upcoming SpaceX launch

    Output info:
    - Name of the launch
    - The date (in local time)
    - The rocket name
    - The name (with the locality) of the launchpad
    '''

    url = 'https://api.spacexdata.com/v4/launches/upcoming'
    try:
        response = requests.get(url)
        response.raise_for_status()
        launches = response.json()

        if not launches:
            print("No upcoming launches found.")
            return

        # Sort dict using date_unix
        upcoming_launch = sorted(launches, key=lambda x: x.get('date_unix', 0))[0]

        # Extract data safely
        launch_name = upcoming_launch.get('name', 'Unknown Launch')
        date_local = upcoming_launch.get('date_local', 'Unknown Date')
        rocket_id = upcoming_launch.get('rocket', '')
        launchpad_id = upcoming_launch.get('launchpad', '')

        # Rocket details
        rocket_name = "Unknown Rocket"
        if rocket_id:
            try:
                rocket_url = f'https://api.spacexdata.com/v4/rockets/{rocket_id}'
                rocket_response = requests.get(rocket_url)
                rocket_response.raise_for_status()
                rocket_name = rocket_response.json().get("name", "Unknown Rocket")
            except requests.RequestException:
                pass

        # Launchpad details
        launchpad_name, launchpad_locality = "Unknown Launchpad", "Unknown Location"
        if launchpad_id:
            try:
                launchpad_url = f'https://api.spacexdata.com/v4/launchpads/{launchpad_id}'
                launchpad_response = requests.get(launchpad_url)
                launchpad_response.raise_for_status()
                launchpad_data = launchpad_response.json()
                launchpad_name = launchpad_data.get("name", "Unknown Launchpad")
                launchpad_locality = launchpad_data.get("locality", "Unknown Location")
            except requests.RequestException:
                pass

        # Print final output
        print(f"{launch_name} ({date_local}) {rocket_name} - {launchpad_name} ({launchpad_locality})")

    except requests.RequestException as e:
        print('An error occurred while making an API request:', e)
    except Exception as err:
        print('A general error occurred:', err)


if __name__ == '__main__':
    get_upcoming_launch()
