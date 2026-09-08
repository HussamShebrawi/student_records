import csv

def detect_empty_cells(row_data, headers):
    empty_cells = []
    for index, field in enumerate(row_data):
        if field == '' or field.isspace():
            empty_cells.append(headers[index])
    return empty_cells

def validate_age(age_string):
    if age_string == '' or age_string.isspace():
        return False
    if not age_string.isdigit():
        return False
    number = int(age_string)
    if number < 15 or number > 80:
        return False
    return True

def validate_email(email):
    """Check if email contains '@' and a dot after '@', return True if valid else False."""
    if "@" not in email:
        return False
    parts = email.split("@")
    if "." in parts[1]:
        return True
    return False

seen_ids = set()

try:
    with open('data/students.csv', 'r') as data:
        reader = csv.reader(data)
        headers = next(reader)
        
        for row_number, row in enumerate(reader, start=2):
            
            if all(field.strip() == "" for field  in row):
                print(f"[EMPTY ROW] Row {row_number}: {row} all fields are empty ")
                continue
            
            if len(row) != len(headers):
                print(f"[CORRUPTED ROW] Row {row_number}: Expected {len(headers)} columns, got {len(row)}")
                continue
            
            current_id = row[0].strip()
            if current_id in seen_ids:
                print(f"[DUPLICATE ID] Row {row_number}: ID '{current_id}' already seen")
                continue
            seen_ids.add(current_id)
            
            empty = detect_empty_cells(row, headers)
            if empty:
                for field_name in empty:
                    print(f"[EMPTY CELL] Row {row_number}: '{field_name}' is empty or whitespace")            
            
            if not validate_age(row[2]):
                print(f"[INVALID AGE] Row {row_number}: age value '{row[2]}' is invalid (must be 15-80)")
            
            if not validate_email(row[3]):
                print(f"[INVALID EMAIL] Row {row_number}: email '{row[3]}' format is invalid")
                
except FileNotFoundError:
    print("Error: The file data/students.csv was not found.")