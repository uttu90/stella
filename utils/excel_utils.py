__author__ = 'TuHV'

# Excel utils to get data


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


def read_table_to_matrix(sheet, col_start, col_end, row_start, row_end):
    data = []
    for row in range(row_start, row_end):
        data.append(sheet.row_values(rowx=row, start_colx=col_start, end_colx=col_end))
    return data

import numpy as np


def array_sum(array, shape=None):
    if not shape:
        return np.sum(array)
    array_shape = array.shape
    axis = 1 if array_shape[0] in shape else 0
    return np.sum(array, axis=axis).reshape(shape)


def array_mean(array, shape=None):
    if not shape:
        return np.mean(array)
    array_shape = array.shape
    axis = 1 if array_shape[0] in shape else 0
    return np.mean(array, axis=axis).reshape(shape)


def get_variable_now(
        array_values,
        I_Flag1,
        I_Flag2,
        I_Simulation_Time,
        I_InputDataYears,
        subCatchment,
        I_RelArea):
    if array_values[0].shape[1] == 1:
        if I_Flag1:
            result = (array_values[0] +
                      (array_values[1] - array_values[0]) *
                      (int(I_Simulation_Time/365) - I_InputDataYears[0]) /
                      (I_InputDataYears[1] - I_InputDataYears[0]))
        elif I_Flag2:
            result = (array_values[1] +
                      (array_values[2] - array_values[1]) *
                      (int(I_Simulation_Time/365) - I_InputDataYears[1]) /
                      (I_InputDataYears[2] - I_InputDataYears[1]))
        else:
            result = (array_values[2] +
                      (array_values[3] - array_values[2]) *
                      (int(I_Simulation_Time/365) - I_InputDataYears[2]) /
                      (I_InputDataYears[3] - I_InputDataYears[2]))
    else:
        if I_Flag1:
            result = np.divide(
                (array_values[0] +
                 (array_values[1] - array_values[0]) *
                 (int(I_Simulation_Time/365) - I_InputDataYears[0]) /
                 (I_InputDataYears[1] - I_InputDataYears[0])),
                array_sum(array_values[0], shape=(subCatchment, 1)),
                out=np.zeros_like(array_values[0]),
                where=I_RelArea != 0)
        elif I_Flag2:
            result = np.divide(
                (array_values[1] +
                 (array_values[2] - array_values[1]) *
                 (int(I_Simulation_Time/365) - I_InputDataYears[1]) /
                 (I_InputDataYears[2] - I_InputDataYears[1])),
                array_sum(array_values[1], shape=(subCatchment, 1)),
                out=np.zeros_like(array_values[0]),
                where=I_RelArea != 0)
        else:
            result = np.divide(
                (array_values[2] +
                 (array_values[3] - array_values[2]) *
                 (int(I_Simulation_Time/365) - I_InputDataYears[2]) /
                 (I_InputDataYears[3] - I_InputDataYears[2])),
                array_sum(array_values[2], shape=(subCatchment, 1)),
                out=np.zeros_like(array_values[0]),
                where=I_RelArea != 0)
        result = np.multiply(I_RelArea > 0, result)
    return result


def array_to_maps(array_id, array, input_map):
    output_map = 0 * input_map
    for index, value in enumerate(array):
        output_map += (input_map == array_id[index]) * value
    return output_map


def write_array(array, sheet, column):
    for row, value in enumerate(array):
        # print type(value)
        sheet.write(row + 2, column, value)


def write_dict(data, sheet, column):
    index = 0
    for key in sorted(data.keys()):
        # print key
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


def write_params(sheet, time, *args):
    for index in range(0, len(args), 2):
        if time == 1:
            sheet.write(0, index, args[index])
        sheet.write(time, index, args[index+1])
