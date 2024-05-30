#!/usr/bin/python3
"""Reading data from CSV and converting it into JSON using serialization"""
import csv
import json


def convert_csv_to_json(filename=""):
    """Reading data from CSV and converting it into JSON.

    Args:
        filename: the name of the CSV file."""
    try:
        jsonArray = []

        with open(filename, 'r', encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            for rows in csvReader:
                jsonArray.append(rows)

        with open("data.json", 'w', encoding='utf-8') as jsonf:
            jsonString = json.dumps(jsonArray, indent=4)
            jsonf.write(jsonString)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {csv_filename} n'a pas été trouvé.")
        return False
    except Exception as e:
        print(f"Erreur : {e}")
        return False
