import sys
import tensorflow as tf

if len(sys.argv) is not 3:
    print("USAGE:python tf2_to_tflite.py [SAVED_MODEL_DIR] [OUTPUT_MODEL_NAME]")
    exit(0)

SAVED_MODEL_DIR = sys.argv[1]
OUTPUT_MODEL_NAME = sys.argv[2]
converter = tf.lite.TFLiteConverter.from_saved_model(SAVED_MODEL_DIR)

tflite_model = converter.convert()

# Save the model.
with open(OUTPUT_MODEL_NAME, 'wb') as f:
  f.write(tflite_model)