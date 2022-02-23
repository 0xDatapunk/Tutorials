solc-select use 0.8.12

certoraRun ReserveListFixed.sol:ReserveList \
    --verify ReserveList:ReserveList.spec --msg "$1"
