
methods {
	ballAt() returns uint256 envfree
}

invariant neverReachPlayer4() 
	ballAt() != 4 && ballAt() != 3


rule neverReachPlayer4Rule(method f) {
	env e; 
	
	require  ballAt()==1;
	
	// execute some method
   	calldataarg arg; // any argument
	f(e, arg);
	
	assert (ballAt() != 4, "Should never reach player4" );
}
