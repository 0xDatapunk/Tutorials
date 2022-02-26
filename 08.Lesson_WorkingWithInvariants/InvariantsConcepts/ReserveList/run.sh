solc-select use 0.8.12

certoraRun ReserveListFixed.sol:ReserveList \
    --optimistic_loop \
    --settings -copyLoopUnroll=4 \
    --verify ReserveList:ReserveList.spec --msg "$1"
