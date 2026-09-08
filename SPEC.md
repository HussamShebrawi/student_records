# SPEC.md — Student Records Validation Specification

## Error Definitions

### 1. EMPTY CELL
- **Description:** A field contains no data or only whitespace characters.
- **Detection:** `field == ''` or `field.isspace()` is True.
- **Error Message:** `[EMPTY CELL] Row {row_number}: '{field_name}' is empty or whitespace`
- **Severity:** Warning (processing continues)

### 2. EMPTY ROW
- **Description:** All fields in a row are empty or contain only whitespace.
- **Detection:** `all(field.strip() == "" for field in row)` is True.
- **Error Message:** `[EMPTY ROW] Row {row_number}: all fields are empty`
- **Severity:** Skip (row is ignored, processing continues)

### 3. CORRUPTED ROW
- **Description:** A row has a different number of columns than the header row.
- **Detection:** `len(row) != len(headers)`
- **Error Message:** `[CORRUPTED ROW] Row {row_number}: Expected {expected} columns, got {actual}`
- **Severity:** Skip (row is ignored, processing continues)

### 4. INVALID AGE
- **Description:** The age value is not a valid integer between 15 and 80 (inclusive).
- **Detection:**
  - Empty or whitespace → invalid
  - Not a digit string → invalid
  - Integer &lt; 15 or &gt; 80 → invalid
- **Error Message:** `[INVALID AGE] Row {row_number}: age value '{value}' is invalid (must be 15-80)`
- **Severity:** Error (must be fixed, but other fields are still validated)

### 5. DUPLICATE ID
- **Description:** An ID appears in more than one row (primary key violation).
- **Detection:** `current_id in seen_ids` where `seen_ids` is a `set()`.
- **Error Message:** `[DUPLICATE ID] Row {row_number}: ID '{current_id}' already seen`
- **Severity:** Skip (row is ignored, processing continues)

### 6. INVALID EMAIL
- **Description:** The email format is invalid (must contain '@' and a dot after '@').
- **Detection:**
  - No '@' symbol → invalid
  - No '.' after '@' → invalid
- **Error Message:** `[INVALID EMAIL] Row {row_number}: email '{value}' format is invalid`
- **Severity:** Error (must be fixed, but other fields are still validated)

## Processing Pipeline (Order of Checks)

1. EMPTY ROW
2. CORRUPTED ROW
3. DUPLICATE ID
4. EMPTY CELL
5. INVALID AGE
6. INVALID EMAIL