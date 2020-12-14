#!/usr/bin/python3

import sys

import mxnet as mx
import numpy as np
from mxnet.contrib import onnx as onnx_mxnet

print(sys.argv[0])
if len(sys.argv) != 4:
    print("USAGE:python mxnet_exort_onnx.py [MODEL_FILE] [PARAMS_file] [OUTPUT_FILE]")
    exit(0)


#print ('Argument List:', str(sys.argv))
symbol_file = sys.argv[1]
params_file = sys.argv[2]
output_file = sys.argv[3]

# https://mxnet.cdn.apache.org/versions/1.7.0/api/python/docs/tutorials/deploy/export/onnx.htmlhttps://mxnet.cdn.apache.org/versions/1.7.0/api/python/docs/tutorials/deploy/export/onnx.html
onnx_mxnet.export_model(symbol_file, params_file, [(1,1,1250)], input_type=np.float32, onnx_file_path=output_file, verbose=False)

# Load the model along with the transformations
#net = mx.gluon.SymbolBlock.imports(symbol_file=symbol_file, input_names=['data'], param_file=params_file, ctx=mx.cpu())