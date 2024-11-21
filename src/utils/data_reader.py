import csv
import json

def read_csv(file_path):
    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        print("CSV data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

def read_json(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        print("JSON data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []
