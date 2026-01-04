"""Docstrings: Application to practice json file manipulation with python script."""
# necessairy modules
import json
from typing import List, Dict
from pathlib import Path

# folder where main.py lives
BASE_DIR = Path(__file__).resolve().parent

# json objects external to this file with filename as global variables
filename = BASE_DIR/"states.json"
filename2 = BASE_DIR/"players.json"
filename3 = BASE_DIR/"tennis_players.json"
output_file = BASE_DIR/"output"/"person_data.json"

# sources of the json object within this main file
# json string
player_json_string = """
{
        "playerId": 1,
        "name": "Roger Federer",
        "age": 42,
        "skillLevel": "Professional",
        "contact": {
          "email": "roger.federer@example.com",
          "phone": "+1234567890"
        },
        "registeredOn": "2023-10-01"
      }
"""
# dictionary
person_dict = {
    "name": "Bob",
    "languages": ["English", "French"],
    "married": True,
    "age": 32
}

# Functions to work with this internal json objects and json file.
# parsing internal json string with loads() function
def parsing_json_string(json_str: str) -> Dict: 
    data = json.loads(json_str)
    return data

# serializing a python dictionary as a json string using dumps()
def transform_in_jsonString(dictionary: dict):
    return json.dumps(dictionary, indent = 4, sort_keys=True)

# working with external files
def get_json_from_file(filepath: str) -> List:
    """Load and parse JSON data from a file."""
    with open(filepath, mode="r", encoding="UTF-8") as f:
        return json.load(f)

# saving or storing json object in a json file using json dump() function
def save_json_to_file(data, filepath) -> bool:
    with open(filepath, "w", encoding="UTF-8") as file:
        json.dump(data, file, indent = 4, sort_keys=True)
        return True
         

# Driver function
def main():    
    try:
        # Player data from internal file json string
        data = parsing_json_string(player_json_string)    
        print(f"player data: {data}")    
        
        # Retrieving data from filename
        state_data = get_json_from_file(filename)
        for state in state_data:
            print(f'state: {state["state"]} with Capital: {state["capital"]}')
    
        # Retrieving data from filename
        tournament_data = get_json_from_file(filename3)
        print(tournament_data["tournament"]) # tournament's name
        print(tournament_data["players"][2]) # third player's data
        
        # parsing data dictionary as a json strings
        parsed_data = transform_in_jsonString(data)
        print(parsed_data)
        
        # Saving person dictionary to a file
        data_saved = save_json_to_file(person_dict, output_file)
        print(f"data is saved in 'person.json' file: {data_saved}")  
    except FileNotFoundError as er:
        print(f"File not found error, check your file path or existence: {er}")
    except json.JSONDecodeError as json_e:
        print(f"Invalid JSON: {e}")
    except Exception as e:
        print(f"An error happens running your code. Check this: {e}") 
            
# Running the Driver function
if __name__ == "__main__":

    main()
