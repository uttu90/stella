import xlwt

def write_array(array, sheet, column):
    for row, value in enumerate(array):
        sheet.write(row + 1, column, value)


def write_dict(data, sheet, column):
    index = 0
    for key in data.keys():
        sheet.write(0, column + index, key)
        write_array(data[key], sheet, column + index)
        index += 1
