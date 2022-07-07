#!/usr/bin/python3

import sys
import os

import numpy as np

from enum import IntEnum  # Enum declarations

var_name = "MODEL"
header_name = "SLEEP_MODEL.h"

# Transpile any binary data to native C char array.
def data_to_char_array(data, var_name, align_flag=True):
    output = "static const unsigned char " + var_name + "[]={"
    if align_flag:
        output = "alignas(8) " + output

    data_str = ','.join(str(byte) for byte in data)
    output = output + data_str + "};"
    return output

"""
def data_to_char_array(data, array_var_name):
    output = "static const unsigned char " + array_var_name +  "[]={"
    data_str = ','.join(str(byte) for byte in data)
    output = output + data_str + "};"
    return output
"""

if __name__ == "__main__":

    print(sys.argv[0])
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("USAGE:python binary_to_c_header.py [MODEL_FILE] [OUTPUT_HEADER_NAME(Optional)] [VAR_NAME(Optional)]")
        exit(0)

    if len(sys.argv) > 3:
        var_name = sys.argv[3]
    if len(sys.argv) > 2:
        header_name = sys.argv[2]

    model_file_name = sys.argv[1]

    model_path = os.path.join("workspace", model_file_name)

    with open(model_path, mode='rb') as file: # b is important -> binary
        model = file.read()
        header_content = data_to_char_array(model, var_name)

        output_path = os.path.join("workspace", header_name)

        with open(output_path, 'w') as out:
            out.write(header_content)