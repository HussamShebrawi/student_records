def count_invalid_ages(age_list):
    invalid_count = 0
    for age_text in age_list:
        if not age_text.isdigit():
            invalid_count += 1
            print(age_text,invalid_count)
    return invalid_count

sample_ages = ["19", "abc", "", "25", "x1"]
print(count_invalid_ages(sample_ages))