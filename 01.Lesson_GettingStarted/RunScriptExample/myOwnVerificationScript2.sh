# format: <relative/path/to/solidity/file>:<contrac_name> --verify <contract_name>:<relative/path/to/spec/file>

certoraRun BankLesson1/Bank.sol:Bank --verify Bank:BankLesson1/Parametric.spec \
  --solc solc7.0 \
  --rule validityOfTotalFundsWithVars \
  --msg "$1"


# run validityOfTotalFundsWithVars "a message of your choice taken as an input"