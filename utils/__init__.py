def read_array_data(sheet, col_start, col_end, row_start, row_end):
    data = {}
    for col in range(col_start, col_end):
        col_values = sheet.col_values(colx=col, start_rowx=row_start, end_rowx=row_end)
        data[col_values[0]] = col_values[1:]
    return data

def read_table_data(sheet, col_start, col_end, row_start, row_end):
    data = {}
    keys = sheet.col_values(colx=col_start, start_rowx=row_start+1, end_rowx=row_end)
    for col in range(col_start + 1, col_end):
        col_values = sheet.col_values(col, start_rowx=row_start, end_rowx=row_end)
        data[col_values[0]] = {}
        for index, value in enumerate(col_values[1:]):
            data[col_values[0]][keys[index]] = value
    return data