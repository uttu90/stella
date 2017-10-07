import xlwt

def write_array(array, sheet, column):
    for row, value in enumerate(array):
        print type(value)
        sheet.write(row + 2, column, value)


def write_dict(data, sheet, column):
    index = 0
    for key in sorted(data.keys()):
        print key
        if type(data[key]) is dict:
            sheet.write(0, column + index, key)
            for xkey in sorted(data[key].keys()):
                sheet.write(1, column + index, xkey)
                write_array(data[key][xkey], sheet, column + index)
                index += 1
        else:
            sheet.write(1, column + index, key)
            write_array(data[key], sheet, column + index)
            index += 1


if __name__ == '__main__':
    wb = xlwt.Workbook()
    ws = wb.add_sheet('test1')
    adict = {
        'a': {
            'b': [1, 3, 4],
            'e': [3, 3, 5]
        },
        'c': {
            'd': [4, 5, 6]
        }
    }
    bdict = {
        'a': [1, 2, 3, 5],
        'b': [1, 2, 3, 5],
    }
    write_dict(adict, ws, 0)
    wb.save('test.xls')
