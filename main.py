import csv

def is_normal(x):
    if x == '':
        return True
    if x.isdigit():
        return True
    if x.isalpha():
        return True
    return False

def is_corrupted_row(x):
    for cell in x:
        if is_normal(cell):
            return False
    return True

empty_rows = []
corrupted_rows = []
empty_cells = []
duplicate_ids = []
invalid_ages = []
invalid_emails = []

with open('data/students.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    line_number = 1
    seen_ids = set()
    for row in reader:
        line_number += 1

        if len(row) == 0:
            empty_rows.append('EMPTY ROW at line '+ str(line_number))
            continue

        if is_corrupted_row(row):
            corrupted_rows.append("CORRUPTED ROW at line "+ str(line_number)+ ":" + str(row))
            continue

        if row[0] != '':
            if row[0] in seen_ids:
                duplicate_ids.append("DUPLICATE ID at line "+ str(line_number)+ " : "+ row[0])
            else:
                seen_ids.add(row[0])
  
        if row[2] != '' and not row[2].isdigit():
            invalid_ages.append("INVALID AGE at line "+ str(line_number)+ " : "+ row[2])

        if row[3] != '' and ('@' not in row[3] or '.' not in row[3]):
            invalid_emails.append("INVALID EMAIL at line "+ str(line_number)+ " : "+ row[3])

  
        for j in range(len(row)):
            if row[j] == '':
                empty_cells.append("EMPTY CELL at line "+ str(line_number)+ " column "+ headers[j])

print("=== EMPTY ROWS ===")
for item in empty_rows:
    print(item)

print("\n=== CORRUPTED ROWS ===")
for item in corrupted_rows:
    print(item)

print("\n=== EMPTY CELLS ===")
for item in empty_cells:
    print(item)

print("\n=== DUPLICATE IDS ===")
for item in duplicate_ids:
    print(item)

print("\n=== INVALID AGES ===")
for item in invalid_ages:
    print(item)

print("\n=== INVALID EMAILS ===")
for item in invalid_emails:
    print(item)