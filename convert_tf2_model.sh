if [ $# -ne 2 ]
then
    echo "USAGE: ./convert_tf2_model.sh [TF MODEL DIR PATH] [OUTPUT_FILE_NAME]"
    exit
fi

MODEL_PATH=$1
OUTPUT_FILE_NAME=$2
pip3 install tf2onnx
python3 -m tf2onnx.convert --saved-model ${MODEL_NAME} --output tmp.onnx

./convert_onnx_model.sh tmp.onnx ${OUTPUT_FILE_NAME}
rm tmp.onnx