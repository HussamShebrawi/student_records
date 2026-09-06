def count_empty_cells(row):
    empty_count = 0
    for cell in row:
        if cell.strip() == "":
            empty_count += 1
    return empty_count

sample_row = ["101", "", "Ahmad", "", "ahmad@mail.com"]
print(count_empty_cells(sample_row))