def d():
    print("="*25)
# 2. Exploring the Digital Cosmos with Python and the Web
# Objective:
# The aim of this assignment is to apply your understanding of Python programming, web architecture, and API interactions. You will set up a Python environment, make requests to a web API, and process the received data. This assignment is designed to enhance your practical skills in web development and data manipulation using Python.

# Problem Statement:
# Imagine you are a developer tasked with creating a feature for a web application that provides users with insightful information about various space objects. Your application will fetch data from a publicly available space API, process this data, and display it in a user-friendly format.

# Task 1: Set up a Python Virtual Environment and Install Required Packages

# Create a new virtual environment in Python.
# Activate the virtual environment.
# Install the requests package for making HTTP requests.
# Expected Outcome:
# A successfully created and activated virtual environment with the requests package installed.

"""
Solution:
Open a command prompt, entering the following command:

python -m venv venv
.\\venv\\scripts\\activate
(venv) pip install requests
"""

# Task 2: Fetch Data from a Space API

# Write a Python script that makes a GET request to a space API (e.g., The Solar System OpenData) to fetch data about planets.
# Parse the JSON response and extract information about each planet, such as its name, mass, and orbit period.
# Code Example:
# import requests

# def fetch_planet_data():
#     url = "https://api.le-systeme-solaire.net/rest/bodies/"
#     response = requests.get(url)
#     planets = response.json()['bodies']

#     #process each planet info
#     for planet in planets:
#         if planet['isPlanet']:
#             name = #get planet English name
#             mass = #get planet mass
#             orbit_period = #get planet orbit period
#             print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

# fetch_planet_data()

# Expected Outcome:

# Planet: Uranus, Mass: 8.68127, Orbit Period: 30685.4 days
# Planet: Neptune, Mass: 1.02413, Orbit Period: 60189.0 days
# Planet: Jupiter, Mass: 1.89819, Orbit Period: 4332.589 days
# Planet: Mars, Mass: 6.41712, Orbit Period: 686.98 days
# Planet: Mercury, Mass: 3.30114, Orbit Period: 87.969 days
# Planet: Saturn, Mass: 5.68336, Orbit Period: 10759.22 days
# Planet: Earth, Mass: 5.97237, Orbit Period: 365.256 days
# Planet: Venus, Mass: 4.86747, Orbit Period: 224.701 days


# Task 3: Data Presentation and Analysis

# Solution:

import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)
        data = response.json()
        planets = data.get('bodies', [])
        
        planet_data = []
        
        for planet in planets:
            if planet.get('isPlanet', False):
                name = planet.get('englishName', 'Unknown')
                # mass = planet['mass']['massValue'] * (10 ** planet['mass']['massExponent']) if 'mass' in planet else None
                mass = planet['mass']['massValue'] if 'mass' in planet and 'massValue' in planet['mass'] else 'N/A'
            
                orbit_period = planet.get('sideralOrbit', None)
                print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
                planet_info = {
                    'name': name,
                    'mass': mass,
                    'orbit_period': orbit_period
                }
                planet_data.append(planet_info)
        
        return planet_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None
    except KeyError as e:
        print(f"KeyError: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

d()


def find_heaviest_planet(planets):
    if not planets:
        return None
    
    heaviest_planet = max(planets, key=lambda x: x['mass'] if x['mass'] is not None else float('-inf'))
    return heaviest_planet

def find_longest_orbit_planet(planets):
    if not planets:
        return None
    
    longest_orbit_planet = max(planets, key=lambda x: x['orbit_period'] if x['orbit_period'] is not None else float('-inf'))
    return longest_orbit_planet

def main():
    planets = fetch_planet_data()
    
    if planets is None:
        print("Failed to fetch planet data. Exiting.")
        return
    
    heaviest_planet = find_heaviest_planet(planets)
    longest_orbit_planet = find_longest_orbit_planet(planets)
    
    if heaviest_planet:
        print(f"Heaviest Planet: {heaviest_planet['name']}, Mass: {heaviest_planet['mass']}")
    
    if longest_orbit_planet:
        print(f"Planet with Longest Orbit Period: {longest_orbit_planet['name']}, Orbit Period: {longest_orbit_planet['orbit_period']} days")

if __name__ == "__main__":
    main()
