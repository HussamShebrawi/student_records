import csv
import logging
import argparse


logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s - %(message)s',
    filename='logs/student_records.log')

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

def print_summary(total, valid, invalid):
    logging.info(f"Summary: {total} total, {valid} valid, {invalid} invalid")

parser = argparse.ArgumentParser(description="Clean and validate a CSV file of student records.")

parser.add_argument(
    "--input",
    default='data/students.csv',
    help="Path to the input CSV file (default: data/students.csv)")

parser.add_argument(
    "--output",
    default='data/students_cleaned.csv', 
    help="Path to the cleaned output CSV file (default: data/students_cleaned.csv)")

args=parser.parse_args()



valid_rows = []
seen_ids = set()

try:
     
    input_filename = args.input
    output_filename = args.output
    
    with open(input_filename, 'r') as input_file:
        reader = csv.reader(input_file)
        

        try:
            headers = next(reader)
        except StopIteration:
            raise EmptyFileError(f"input file is empty: {input_filename}")
        
        total_rows_read=0
        
        for row_number, row in enumerate(reader, start=2):
            
            total_rows_read +=1
            
            # 1. EMPTY ROW
            if all(field.strip() == "" for field in row):
                logging.warning(f"[EMPTY ROW] Row {row_number}: all fields are empty")
                continue
            
            # 2. CORRUPTED ROW
            if len(row) != len(headers):
                logging.warning(f"[CORRUPTED ROW] Row {row_number}: Expected {len(headers)} columns, got {len(row)}")
                continue
            
            # 3. DUPLICATE ID
            current_id = row[0].strip()
            if current_id in seen_ids:
                logging.warning(f"[DUPLICATE ID] Row {row_number}: ID '{current_id}' already seen")
                continue
            
            
            # 4. EMPTY CELL
            empty = detect_empty_cells(row, headers)
            if empty:
                for field_name in empty:
                    logging.warning(f"[EMPTY CELL] Row {row_number}: '{field_name}' is empty or whitespace")
                continue 
            
            # 5. INVALID AGE
            if not validate_age(row[2]):
                logging.warning(f"[INVALID AGE] Row {row_number}: age value '{row[2]}' is invalid (must be 15-80)")
                continue
            
            # 6. INVALID EMAIL
            if not validate_email(row[3]):
                logging.warning(f"[INVALID EMAIL] Row {row_number}: email '{row[3]}' format is invalid")
                continue
            

            valid_rows.append(row)
            seen_ids.add(current_id)
        
        invalid_rows_count = total_rows_read - len(valid_rows)

    

    # Write cleaned output: only rows that passed all 6 validation checks.
    # Using newline='' to avoid extra blank lines on Windows.
    with open(output_filename, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(valid_rows) 
    
    print_summary(total_rows_read, len(valid_rows), invalid_rows_count)

    
except FileNotFoundError:
    logging.error(f"could not find file: {input_filename}")
except EmptyFileError as e:
    logging.error(f'{e}')