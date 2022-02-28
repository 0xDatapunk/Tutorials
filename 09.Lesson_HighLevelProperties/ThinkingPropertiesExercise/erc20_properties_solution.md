
***High level*** - 
Checks that the sum of sender and recipient accounts remains the same after transfer(), i.e. assets doesn't disappear nor created out of thin air

***Variable transition*** - 
Checks that transferFrom() correctly decrease allowance of e.msg.sender

***Variable transition*** - 
Checks that increaseAllowance() increases allowance of spender

***Variable transition*** - 
Users' balance can be changed only as a result of transfer(), transderFrom(), mint(), burn()

***High level*** - 
Checks that the totalSupply of the token is at least equal to a single user's balance

***High level*** - 
Checks that the totalSupply of the token is at least equal to the sum of all user's balances

Above all share high priority