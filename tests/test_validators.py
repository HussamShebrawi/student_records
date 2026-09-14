from main import validate_age


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