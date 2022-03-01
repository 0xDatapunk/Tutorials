***Variable transitions*** - totalSupply() and asset.balanceOf(address(this)) should change in the same directions

***High-level*** - totalSupply() should be less or equal to asset.balanceOf(address(this))

***High-level*** - totalSupply() should be great or equal to sum of all users' balances

***High-level*** - flashloan call increases the discrepancy between the after/before differences of totalSupply() and asset.balanceOf(address(this))

 

