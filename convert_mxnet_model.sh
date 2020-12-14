if [ $# -ne 3 ]
then
    echo "USAGE: ./convert_mxnet_model.sh [MXNET_SYMBOL] [MXNET_SYMBOL_PARAMS] [OUTPUT_FILE]"
    exit
fi

SYMBOL_PATH=$1
PARAMS_PATH=$2
OUTPUT_FILE=$3

python3 mxnet_export_onnx.py attention_model_china_v4-symbol.json attention_model_china_v4-0000.params tmp.onnx

./convert_onnx_model.sh tmp.onnx $OUTPUT_FILE

rm tmp.onnx
