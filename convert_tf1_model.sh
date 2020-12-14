if [ $# -ne 2 ]
then
    echo "USAGE: ./convert_tf1_model.sh [TF MODEL DIR PATH] [OUTPUT_FILE_NAME]"
    exit
fi

MODEL_PATH=$1
OUTPUT_FILE=$2

./mnn-mac/MNNConvert -f TF --modelFile $MODEL_PATH --MNNModel $OUTPUT_FILE --bizCode biz