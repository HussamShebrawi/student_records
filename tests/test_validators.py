import pytest
from main import (
    validate_age,
    validate_email,
    detect_empty_cells,
    clean_csv,
    EmptyFileError,
)


def test_validate_age_accepts_valid_and_rejects_invalid_and_checks_boundaries():
    assert validate_age("15") is True
    assert validate_age("80") is True
    assert validate_age("14") is False
    assert validate_age("81") is False
    assert validate_age("") is False
    assert validate_age("abc") is False


def test_validate_email_accepts_valid_and_rejects_invalid_format():
    assert validate_email("student@example.com") is True
    assert validate_email("invalid-email") is False
    assert validate_email("no-at-sign.com") is False
    assert validate_email("no-dot@domain") is False


def test_detect_empty_cells_returns_only_empty_or_whitespace_field_names():
    headers = ["student_id", "name", "age", "email", "grade", "major"]
    row = ["1010", "  ", "20", "", "A", "CS"]
    assert detect_empty_cells(row, headers) == ["name", "email"]


def test_clean_csv_raises_empty_file_error_for_empty_input(tmp_path):
    empty_input = tmp_path / "empty.csv"
    empty_input.write_text("")

    output_file = tmp_path / "cleaned.csv"

    with pytest.raises(EmptyFileError):
        clean_csv(empty_input, output_file)

        
def test_clean_csv_handles_header_only_file_without_errors(tmp_path):
    header_content = "student_id,name,age,email,grade,major\n"
    header_input = tmp_path / "header_only.csv"
    header_input.write_text(header_content)

    output_file = tmp_path / "cleaned.csv"

    clean_csv(header_input, output_file)

    assert output_file.exists()
    output_lines = output_file.read_text().strip().splitlines()
    assert len(output_lines) == 1
    assert output_lines[0] == "student_id,name,age,email,grade,major"