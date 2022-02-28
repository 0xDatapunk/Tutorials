solc-select use 0.7.6

certoraRun BankWithLoops.sol:Bank --verify Bank:Loops.spec \
--send_only \
--optimistic_loop \
--loop_iter 3 \
--msg "$1"