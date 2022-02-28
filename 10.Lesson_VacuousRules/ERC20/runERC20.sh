solc-select use 0.8.0

certoraRun ERC20Fixed.sol:ERC20 --verify ERC20:ERCVacuity.spec \
--send_only \
--rule_sanity \
--optimistic_loop \
--msg "$1"


