methods {	
	deposit() 
	withdraw(uint256) 
    collectFees() 
	OwnerDoItsJobAndEarnsFeesToItsClients() 
	assetsOf(address) returns (uint256) envfree

    totalSupply() returns (uint256) envfree
    balanceOf(address) returns (uint256) envfree
    transfer(address, uint256) returns (bool)
    transferFrom(address,address, uint256) returns (bool)
    allowanceOf(address , address )  returns (uint256) envfree
    approve(address , uint256 )  returns (bool) 
    increase_allowance(address , uint ) 
    decrease_allowance(address , uint ) 

    getTotalFeesEarnedPerShare() returns (uint256) envfree
    getFeesCollectedPerShare(address) returns (uint256) envfree
    getRewards(address) returns (uint256) envfree
}


// 1. ***Valid state*** - totalFeesEarnedPerShare >= accounts[msg.sender].feesCollectedPerShare 
invariant totalFeesEarnedPerShare_GE_user_feesCollectedPerShare()
    forall address user. getTotalFeesEarnedPerShare() >= getFeesCollectedPerShare(user)

// 2. totalFeesEarnedPerShare non-decreasing
rule totalFeesEarnedPerShareNonDecreasing(method f) {
    uint256 totalFeesEarnedPerShareBefore = getTotalFeesEarnedPerShare();
    env e; calldataarg args;
    f(e, args);
    uint256 totalFeesEarnedPerShareAfter = getTotalFeesEarnedPerShare();
    assert (totalFeesEarnedPerShareAfter>=totalFeesEarnedPerShareBefore, "totalFeesEarnedPerShare should be monotonically increasing");
}

// 3. ***Variable transition*** - accounts[msg.sender].Rewards decreases => accounts[msg.sender].Rewards==0 && collectFees called
rule rewardsDecreaseOnlyIfCollected(method f, address user) {
    uint256 rewardsBefore = getRewards(user);
    env e; calldataarg args;
    f(e, args);
    uint256 rewardsAfter = getRewards(user);
    assert (rewardsBefore>rewardsAfter => f.selector==collectFees().selector, "Rewards decrease only if collected");
}

// 4. ***High-level*** - Solvency - this.totalSupply() >= balances[user] * (1+totalFeesEarnedPerShare)
invariant totalFunds_GE_single_user_funds()
    forall address user. totalSupply() >= balanceOf(user)

// 5. ***High-level*** - Solvency - this.totalSupply() >= sum(balances[user]) * (1+totalFeesEarnedPerShare)
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

