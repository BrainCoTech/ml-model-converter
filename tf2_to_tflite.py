import sys
import tensorflow as tf
import numpy as np

_ENABLE_QUANTIZATION = True

if len(sys.argv) != 3:
    print("USAGE:python tf2_to_tflite.py [SAVED_MODEL_DIR] [OUTPUT_MODEL_NAME]")
    exit(0)

SAVED_MODEL_DIR = sys.argv[1]
OUTPUT_MODEL_NAME = sys.argv[2]
converter = tf.lite.TFLiteConverter.from_saved_model(SAVED_MODEL_DIR)

if _ENABLE_QUANTIZATION: # and calib_dataset is not None
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    converter.target_spec.supported_types = [tf.float16]

tflite_model = converter.convert()
    
# Save the model.
with open(OUTPUT_MODEL_NAME, 'wb') as f:
  f.write(tflite_model)
