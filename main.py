import csv

class EmptyFileError(Exception):
    pass

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
    if "@" not in email:
        return False
    parts = email.split("@")
    if "." in parts[1]:
        return True
    return False


valid_rows = []
seen_ids = set()

try:
    input_filename = 'data/students.csv'
    output_filename = 'data/students_cleaned.csv'
    
    with open(input_filename, 'r') as input_file:
        reader = csv.reader(input_file)
        

        try:
            headers = next(reader)
        except StopIteration:
            raise EmptyFileError(f"input file is empty: {input_filename}")
        
        row_count = 0
        for row_number, row in enumerate(reader, start=2):
            row_count += 1
            
            # 1. EMPTY ROW
            if all(field.strip() == "" for field in row):
                print(f"[EMPTY ROW] Row {row_number}: all fields are empty")
                continue
            
            # 2. CORRUPTED ROW
            if len(row) != len(headers):
                print(f"[CORRUPTED ROW] Row {row_number}: Expected {len(headers)} columns, got {len(row)}")
                continue
            
            # 3. DUPLICATE ID
            current_id = row[0].strip()
            if current_id in seen_ids:
                print(f"[DUPLICATE ID] Row {row_number}: ID '{current_id}' already seen")
                continue
            
            
            # 4. EMPTY CELL
            empty = detect_empty_cells(row, headers)
            if empty:
                for field_name in empty:
                    print(f"[EMPTY CELL] Row {row_number}: '{field_name}' is empty or whitespace")
                continue 
            
            # 5. INVALID AGE
            if not validate_age(row[2]):
                print(f"[INVALID AGE] Row {row_number}: age value '{row[2]}' is invalid (must be 15-80)")
                continue
            
            # 6. INVALID EMAIL
            if not validate_email(row[3]):
                print(f"[INVALID EMAIL] Row {row_number}: email '{row[3]}' format is invalid")
                continue
            

            valid_rows.append(row)
            seen_ids.add(current_id)
        

        if row_count == 0:
            raise EmptyFileError(f"input file is empty: {input_filename}")
    

# Write cleaned output: only rows that passed all 6 validation checks.
# Using newline='' to avoid extra blank lines on Windows.
    with open(output_filename, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(valid_rows) 
    
except FileNotFoundError:
    print("Error: The file data/students.csv was not found.")
except EmptyFileError as e:
    print(e)