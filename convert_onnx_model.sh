if [ $# -ne 2 ]
then
    echo "USAGE: ./convert_onnx_model.sh [ONNX_FILE_NAME] [OUTPUT_FILE_NAME]"
    exit
fi

ONNX_FILE_NAME=$1
OUTPUT_FILE_NAME=$2
./mnn-mac/MNNConvert -f ONNX --modelFile $ONNX_FILE_NAME --MNNModel $OUTPUT_FILE_NAME --bizCode biz