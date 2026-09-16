# Student Records Cleaner

A Python script that reads a messy CSV file of student records, validates
each row against six data-quality checks, and writes only the valid rows
to a cleaned output file. Rejected rows are logged with the specific
reason for rejection.

## Install

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

By default, the script reads from `data/students.csv` and writes to
`data/students_cleaned.csv`. You can override both paths:

| Flag       | Default                      | Description                         |
|------------|------------------------------|-------------------------------------|
| `--input`  | `data/students.csv`          | Path to the input CSV file          |
| `--output` | `data/students_cleaned.csv`  | Path to the cleaned output CSV file |

Example:

```bash
python main.py --input data/students.csv --output data/students_cleaned.csv
```

## Test

```bash
python -m pytest -v
```

The test suite is located in `tests/test_validators.py` and contains
3 tests covering `validate_age`, `validate_email`, and
`detect_empty_cells`.

## Challenges in cleaning broken data

Real student CSV files contain more than just valid rows. During
development, the following challenges shaped the validation logic:

- **Empty rows vs. corrupted rows.** A blank line in the CSV is returned
  by `csv.reader` as an empty list `[]`, not as a row of empty strings.
  Since `all([])` is `True`, an empty row would also match the
  corrupted-row check (`len(row) != len(headers)`). The order in the
  validation pipeline — `EMPTY ROW` before `CORRUPTED ROW` — is what
  makes the classification accurate.

- **Empty cells vs. invalid values.** An empty `age` field is caught by
  the `EMPTY CELL` check before reaching `INVALID AGE`, because
  `EMPTY CELL` runs earlier in the pipeline. This keeps the log
  accurate: an empty cell is a structural problem, not an invalid value.

- **Duplicate IDs and partial failures.** A row's ID is only recorded
  in `seen_ids` after it passes every check. This means a row that
  fails one check does not block a later valid row that shares the
  same ID.

## Known validation limits

The current validation logic is intentionally simple and has known
limits:

- **Email validation is shallow.** `validate_email` only checks for the
  presence of `@` and a dot in the part after it. As a result,
  `@mail.com` and `a@.com` are accepted, even though they are not
  valid email addresses in practice.

- **Age validation only accepts integers between 15 and 80.**
  Non-numeric values such as `???` and out-of-range numbers are
  rejected, but the bounds are hard-coded.

These limits are documented so readers know what the script does and
does not guarantee.
