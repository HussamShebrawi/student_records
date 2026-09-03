import csv

def detect_empty_cells(row_data, headers):
    empty_cells = []
    for index, cell in enumerate(row_data):
        if cell == '':
            empty_cells.append(headers[index])
    return empty_cells

def validate_age(age_string):
    if age_string == '':
        return False
    if not age_string.isdigit():
        return False
    number = int(age_string)
    if number < 0 or number > 120:
        return False
    return True

try:
    with open('data/students.csv', 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        
        for row_number, row in enumerate(reader, start=2):
            if len(row) < len(headers):
                print(f"Line {row_number}: Row has {len(row)} columns, expected {len(headers)}")
                continue
            
            empty = detect_empty_cells(row, headers)
            if empty:
                print(f"Line {row_number}: Empty cells in {empty}")
            
            if not validate_age(row[2]):
                print(f"Line {row_number}: Invalid age {row[2]}")
                
except FileNotFoundError:
    print("Error: The file data/students.csv was not found.")