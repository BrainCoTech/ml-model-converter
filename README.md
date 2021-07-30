# ml-model-converter
Convert machine learning models for deployment.
Only supports MacOS for now.

NOTE: Make sure you have python3 installed, if python3 is unavailable from sys env, create an alias

# Tensorflow to MNN

## Tensorflow 2.x to MNN
```
./convert_tf2_model.sh [INPUT_MODEL_DIR] [OUTPUT file]
```

## Tensorflow 1.x
```
./convert_tf1_model.sh [INPUT_PB_MODEL_FILE] [OUTPUT file]
```

# MxNet to MNN
```
./convert_mxnet_model.sh [SYMBOL_FILE] [PARAMS_FILE] [OUTPUT_FILE]
```

# Convert ONNX to MNN
```
./convert_onnx_model.sh [INPUT MODEL FILE] [OUTPUT_FILE]
```

# Converting TF2 to lite and C header.
```
python3 tf2_to_tflite.py [DIR_NAME] [TFLITE_NAME].tflite
python3 mnn_to_c_header.py [TFLITE_NAME].tflite [TFLITE_HEADER].h STARK_MODEL
```

