solc-select use 0.8.6

certoraRun popsicle.sol:PopsicleFinance --verify PopsicleFinance:popsicle.spec \
--optimistic_loop \
--msg "$1" \
--rule totalFunds_GE_to_sum_of_all_funds 