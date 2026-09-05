import csv

def detect_empty_cells(row_data, headers):
    empty_cells = []
    for index, cell in enumerate(row_data):
        if cell == '':
            empty_cells.append(headers[index])
    return empty_cells

def validate_age(age_string):
    """Check if email contains '@' and a dot after '@', return True if valid else False."""
    if age_string == '':
        return False
    if not age_string.isdigit():
        return False
    number = int(age_string)
    if number < 0 or number > 120:
        return False
    return True

def validate_email(email):
    if "@" not in email:
        return False
    parts = email.split("@")
    if "." in parts[1]:
        return True
    return False


try:
    with open('data/students.csv', 'r') as data:
        reader = csv.reader(data)
        headers = next(reader)
        
        for row_number, row in enumerate(reader, start=2):
            if len(row) != len(headers):
                print(f"Line {row_number}: CORRUPTED ROW at line")
                continue
            
            empty = detect_empty_cells(row, headers)
            if empty:
                print(f"Line {row_number}: Empty cells in {empty}")
            
            if not validate_age(row[2]):
                print(f"Line {row_number}: Invalid age {row[2]}")
            
            if not validate_email(row[3]):
                print(f"line {row_number}: Invalid email {row[3]}")
                
except FileNotFoundError:
    print("Error: The file data/students.csv was not found.")