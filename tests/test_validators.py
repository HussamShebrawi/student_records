from main import validate_age, validate_email, detect_empty_cells


def test_validate_age_accepts_valid_and_rejects_invalid_and_checks_boundaries():
    # Valid age (within 15-80)
    assert validate_age("20") is True

    # Invalid: not a number
    assert validate_age("twentyone") is False

    # Boundary: minimum (15) — should be valid
    assert validate_age("15") is True

    # Boundary: maximum (80) — should be valid
    assert validate_age("80") is True

    # Boundary: below minimum (14) — should be invalid
    assert validate_age("14") is False

    # Boundary: above maximum (81) — should be invalid
    assert validate_age("81") is False

    # Invalid: empty string
    assert validate_age("") is False


def test_validate_email_accepts_valid_and_rejects_invalid_format():
    # Valid: contains '@' and '.' after it
    assert validate_email("ali@example.com") is True

    # Invalid: no '@' symbol
    assert validate_email("ali.example.com") is False

    # Invalid: '@' but no '.' after it
    assert validate_email("ali@example") is False
    

def test_detect_empty_cells_returns_only_empty_or_whitespace_field_names():
    headers = ["id", "name", "age", "email"]
    row = ["1", "Ali", "", "   "]

    # Only 'age' (empty) and 'email' (whitespace-only) should be reported
    assert detect_empty_cells(row, headers) == ["age", "email"]
