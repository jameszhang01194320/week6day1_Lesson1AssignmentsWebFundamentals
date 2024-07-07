
# 1. Exploring Web Technologies and Python Programming
# Objective:
# The aim of this assignment is to deepen your understanding and practical skills in web technologies and Python programming. You will explore the functionalities of the World Wide Web, web architectures, and the Python programming language, particularly focusing on setting up environments, API interactions, and data handling.

# Problem Statement:
# You are tasked with creating a Python application that interfaces with a public API, fetches data, and processes it. This application should provide insights into how different web architectures work and demonstrate your ability to set up a Python environment, make API requests, and handle JSON data.
def d():
    print("="*25)
# Task 1: Setting Up a Python Virtual Environment and Installing Packages

# Create a new Python virtual environment in your project directory.
# Activate the virtual environment.
# Install the requests packages.

"""
Solution:
Open a command prompt, entering the following command:

python -m venv venv
.\\venv\\scripts\\activate
(venv) pip install requests
"""

# Task 2: Fetching Data from the Pokémon API

# Write a Python script to make a GET request to the Pokémon API (https://pokeapi.co/api/v2/pokemon/pikachu).
# Extract and print the name and abilities of the Pokémon.
# Expected Outcome:
# The script should output the name of the Pokémon (Pikachu) and a list of its abilities.


d()

import requests
# send GET
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
# check response status 200
if response.status_code == 200:
    data = response.json()
    # extract (name, abilities)
    name = data['name']
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    print(f"Name: {name}")
    print(f"Abilities: {abilities}")
else:
    print("Failed to retrieve data. Status code:", response.status_code)

d()
#  Task 3: Analyzing and Displaying Data

# Modify the script to fetch data for three different Pokémon.
import requests

# Define 3 Pokémon's name
pokemon_names = ["pikachu", "bulbasaur", "charmander"]

for name in pokemon_names:

    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        pokemon_name = data['name']

        abilities = [ability['ability']['name'] for ability in data['abilities']]

        print(f"Name: {pokemon_name}")
        print(f"Abilities: {abilities}")

    else:
        print(f"Failed to retrieve data for {name}. Status code:", response.status_code)
d()

# Create 2 functions to calculate and return the average weight of these Pokémon.
# Print the names, abilities, and average weight of the three Pokémon.
# Code Example:

# def fetch_pokemon_data(pokemon_name):
#     return #json response

# def calculate_average_weight(pokemon_list):
#     return #average weight

# pokemon_names = ["pikachu", "bulbasaur", "charmander"]
# Expected Outcome:
# The script should display the names and abilities of the three chosen Pokémon and their average weight. The function should correctly calculate and return the average weight based on the data fetched from the API.
import requests

# Get Pokémon Data
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for {pokemon_name}. Status code:", response.status_code)
        return None

# calculate average weight
def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

# Main()
pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data_list = []

for name in pokemon_names:
    data = fetch_pokemon_data(name)
    
    if data:
        pokemon_data_list.append(data)
        
        # get Pokémon name
        pokemon_name = data['name']
        abilities = [ability['ability']['name'] for ability in data['abilities']]

        print(f"Name: {pokemon_name}")
        print(f"Abilities: {abilities}")


# average weight
if pokemon_data_list:
    average_weight = calculate_average_weight(pokemon_data_list)
    print(f"Average Weight: {average_weight:.2f}")