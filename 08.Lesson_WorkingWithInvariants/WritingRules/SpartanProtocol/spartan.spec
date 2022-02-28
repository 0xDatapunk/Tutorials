methods {	
	init_pool() 
	add_liquidity() returns (uint256) 
    remove_liquidity(uint) 
	swap(address) 
    getContractAddress() envfree
	getToken0DepositAddress() returns (address) envfree
    getToken1DepositAddress() returns (address) envfree
    sync() envfree

    getToken0Amount() returns (uint) envfree
    getToken1Amount() returns (uint) envfree
    getK() returns (uint) envfree

    totalSupply() returns (uint256) envfree
    balanceOf(address) returns (uint256) envfree
    transfer(address, uint256) returns (bool)
    transferFrom(address,address, uint256) returns (bool)
    getAllowance(address , address)  returns (uint256) envfree
    approve(address , uint256 )  returns (bool) 
    increase_allowance(address , uint ) 
    decrease_allowance(address , uint )    
}

// ***High-level*** - Solvency - Total supply of tokens is greater or equal to the balances of each user
invariant supply_GE_single_user_balance()
    forall address user. totalSupply() >= balanceOf(user)

// ***High-level*** - Solvency - Total supply of tokens is greater or equal to the balances of all user
ghost sum_of_all_funds() returns uint256{
    // for the constructor - assuming that on the constructor the value of the ghost is 0
    init_state axiom sum_of_all_funds() == 0;
}

hook Sstore balances[KEY address user] uint256 new_balance
    // the old value ↓ already there
    (uint256 old_balance) STORAGE {
  
  havoc sum_of_all_funds assuming sum_of_all_funds@new() == sum_of_all_funds@old() + new_balance - old_balance;
}

invariant totalFunds_GE_to_sum_of_all_funds()
    totalSupply() >= sum_of_all_funds()


// ***Variable transition*** - tokens amount changes direction should be predictable
rule tokenAmountRelativeChanges(method f) {
    uint256 token0before = spartan.token0Amount;
    uint256 token1before = spartan.token1Amount;

    env e;
    calldataarg args;
    f(e, args);
    uint256 token0After = spartan.token0Amount;
    uint256 token1After = spartan.token1Amount;

    if ((f.selector == add_liquidity().selector) || (f.selector == init_pool().selector)) {
        assert ((token1After > token1before) && (token0After > token0before), "Both increase not due to add_liquidity or init_pool");
    } else if (f.selector == remove_liquidity(uint).selector) {
        assert ((token1After < token1before) && (token0After < token0before), "Both decrease not due to remove_liquidity");        
    } else if (f.selector == swap(address).selector) {        
        assert ((token0After - token0before) * (token1After - token1before) < 0, "Move in different directions not due to swap");        
    } else {
        assert true, "Vacuous for other functions");        
    }   
}

// ***Variable transition*** - product of tokens amount are maintained after swap
rule KMaintainedAfterSwap(method f) {
    uint256 KBefore = getK();
    env e;
    calldataarg args;
    swap(e, args);
    uint256 KAfter = getK();

    assert KAfter == KBefore, "K shouldnt change after a swap";

}
