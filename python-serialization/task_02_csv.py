#!/usr/bin/python3
"""Reading data from CSV and converting it into JSON using serialization"""
import csv
import json


def convert_csv_to_json(filename=""):
    """Reading data from CSV and converting it into JSON.

    Args:
        filename: the name of the CSV file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file_csv:
            csvReader = csv.DictReader(file_csv)
            data = [row for row in csvReader]
        with open("data.json", 'w', encoding='utf-8') as file_json:
            json.dump(data, file_json, indent=4)

    except FileNotFoundError:
        print(f"Erreur : Le fichier {filename} n'a pas été trouvé.")
        return False
    except Exception as e:
        print(f"Erreur : {e}")
        return False
