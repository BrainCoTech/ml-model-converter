#!/usr/bin/python3

import sys

import mxnet as mx
import numpy as np
from mxnet.contrib import onnx as onnx_mxnet

from enum import IntEnum  # Enum declarations

print(sys.argv[0])
if len(sys.argv) < 2 or len(sys.argv) > 4:
    print("USAGE:python mnn_to_c_header.py [MODEL_FILE] [OUTPUT_HEADER_NAME(Optional)(Optional)] [VAR_NAME(Optional)]")
    exit(0)

var_name = "MODEL"
header_name = "MNN_MODEL.h"

# Transpile any binary data to native C char array.
def data_to_char_array(data, array_var_name):
    output = "static const char " + array_var_name +  "[]={"
    data_str = ','.join(str(byte) for byte in data)
    output = output + data_str + "};"
    return output

if len(sys.argv) > 3:
    var_name = sys.argv[3]
if len(sys.argv) > 2:
    header_name = sys.argv[2]

model_file_name = sys.argv[1]

with open(model_file_name, mode='rb') as file: # b is important -> binary
    model = file.read()
    header_content = data_to_char_array(model, var_name)
    with open(header_name, 'a') as out:
        out.write(header_content)