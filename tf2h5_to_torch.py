import tensorflow as tf
import tf2onnx
import onnx

_TF_H5_MODEL_NAME = "tf_model.h5"
_ONNX_MODEL_NAME = "DUMMY.onnx"

loaded_model = tf.keras.models.load_model(_TF_H5_MODEL_NAME)

# Convert the model to ONNX format
onnx_model, _ = tf2onnx.convert.from_keras(loaded_model)

# onnx.save(onnx_model, _ONNX_MODEL_NAME)
# onnx_model = onnx.load_model(_ONNX_MODEL_NAME)

# Convert ONNX model to PyTorch
pytorch_model = ConvertModel(onnx_model)


