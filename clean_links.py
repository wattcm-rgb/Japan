import json
import os

# Change to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Read the restaurants.json file
with open('restaurants.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Remove all tabelog_link fields from each restaurant
for destination in data['destinations'].values():
    for restaurant in destination:
        restaurant.pop('tabelog_link', None)

# Write back the cleaned JSON
with open('restaurants.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Successfully removed all tabelog_link entries from restaurants.json")
