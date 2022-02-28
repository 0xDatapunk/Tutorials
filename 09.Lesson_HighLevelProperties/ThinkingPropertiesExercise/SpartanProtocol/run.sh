solc-select use 0.8.6

certoraRun SpartaProtocolPool.sol:SpartaProtocolPool --verify SpartaProtocolPool:Spartan.spec \
--optimistic_loop \
--msg "$1" \
--rule tokenAmountDecreaseSameTime 