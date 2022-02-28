solc-select use 0.8.6

certoraRun SpartaProtocolPool.sol:SpartaProtocolPool --verify SpartaProtocolPool:spartan.spec \
--optimistic_loop \
--loop_iter 3 \
--msg "$1" 