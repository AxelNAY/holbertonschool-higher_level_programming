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
        with open('data.json', 'w', encoding='utf-8') as file_json:
            json.dump(data, file_json, indent=4)

        return True

    except FileNotFoundError:
        print(f"file not found")
        return False
    except Exception as e:
        print(f"Error")
        return False
