import tensorflow as tf
import subprocess, json, os

MODEL_FILE_NAME = "zenlite_model.o"
MODEL_HEADER_FILE_NAME = "zenlite_model.h"
_MODEL_VAR_NAME = "ZENLITE_MODEL"

config = json.load(open(os.path.join(os.getcwd(), "config.json"), encoding='utf-8'))

_ENABLE_QUANTIZATION = False

"""
def representative_dataset():
    for data in [_calibration_dataset]:
        yield [tf.dtypes.cast(data, tf.float32)]
"""


# Transpile any binary data to native C char array.
def data_to_char_array(data, var_name, align_flag=False):
    output = "static const unsigned char " + var_name + "[]={"
    if align_flag:
        output = "alignas(8) " + output

    data_str = ','.join(str(byte) for byte in data)
    output = output + data_str + "};"
    return output


def convert_model(tf2_model_dir, generate_c_header=True):
    workspace_dir = os.path.join(os.getcwd(), config['workspaceDir'])

    model_path = os.path.join(workspace_dir, MODEL_FILE_NAME)

    converter = tf.lite.TFLiteConverter.from_saved_model(tf2_model_dir)
    if _ENABLE_QUANTIZATION:   # and calib_dataset is not None
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        converter.target_spec.supported_types = [tf.float16]
        # ########### Method 2 ############
        # global _calibration_dataset
        # converter.representative_dataset = representative_dataset

    tflite_model = converter.convert()
    with open(model_path, 'wb') as f:
        f.write(tflite_model)

    if not os.path.exists(model_path):
        print("Error: model generation failure.")
        return None

    print("Model generated successfully.")
    if generate_c_header:
        print("Generating C header")
        model_header_path = os.path.join(workspace_dir, MODEL_HEADER_FILE_NAME)
        with open(model_path, mode='rb') as file:  # b is important -> binary
            model = file.read()
            header_content = data_to_char_array(model, _MODEL_VAR_NAME)
            with open(model_header_path, 'w') as out:
                out.write(header_content)
    return model_path


if __name__ == "__main__":
    tf2_saved_model_dir = './workspace/meditation_tf2_model'
    convert_model(tf2_saved_model_dir)
