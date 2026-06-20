#!/usr/bin/env python3
import json
import os

def generate_maps_url(lat, lng):
    """Generate a reliable Google Maps URL from coordinates"""
    return f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"

def fix_json_file(filepath):
    """Fix all google_maps_link entries in a JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    updated = False
    
    # Handle restaurants.json structure
    if 'destinations' in data:
        for city, restaurants in data['destinations'].items():
            for restaurant in restaurants:
                if 'coordinates' in restaurant and restaurant['coordinates']:
                    lat = restaurant['coordinates']['lat']
                    lng = restaurant['coordinates']['lng']
                    new_url = generate_maps_url(lat, lng)
                    if restaurant.get('google_maps_link') != new_url:
                        restaurant['google_maps_link'] = new_url
                        updated = True
    
    # Handle attractions_by_location.json structure
    if 'locations' in data:
        for city, categories in data['locations'].items():
            for category in ['top_10', 'hidden_gems']:
                if category in categories:
                    for attraction in categories[category]:
                        if 'coordinates' in attraction and attraction['coordinates']:
                            lat = attraction['coordinates']['lat']
                            lng = attraction['coordinates']['lng']
                            new_url = generate_maps_url(lat, lng)
                            if attraction.get('google_maps_link') != new_url:
                                attraction['google_maps_link'] = new_url
                                updated = True
    
    # Handle animal_cafes.json structure
    if 'cities' in data:
        for city, cafes in data['cities'].items():
            for cafe in cafes:
                if 'coordinates' in cafe and cafe['coordinates']:
                    lat = cafe['coordinates']['lat']
                    lng = cafe['coordinates']['lng']
                    new_url = generate_maps_url(lat, lng)
                    if cafe.get('google_maps_link') != new_url:
                        cafe['google_maps_link'] = new_url
                        updated = True
    
    # Write back if updated
    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✓ Updated {filepath}")
        return True
    else:
        print(f"✗ No changes needed for {filepath}")
        return False

# Fix all JSON files
base_dir = 'C:/Users/Watt/Desktop/Coding Stuff/Build a presentation'
files_to_fix = [
    'restaurants.json',
    'attractions_by_location.json',
    'animal_cafes.json'
]

total_updated = 0
for filename in files_to_fix:
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        if fix_json_file(filepath):
            total_updated += 1
    else:
        print(f"✗ File not found: {filepath}")

print(f"\nCompleted! {total_updated} file(s) updated.")
