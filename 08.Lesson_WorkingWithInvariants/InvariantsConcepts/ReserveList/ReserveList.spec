
// Try to prove the following list of properties:




// implication 
// a => b
// if a is true, b must be true
// if a is false, can be whatever


// billateral implication
// if a is true, b must be true
// a <=> b


methods {
	getTokenAtIndex(uint256) returns (address) envfree
	getIdOfToken(address) returns (uint256) envfree
	getReserveCount() returns (uint256) envfree
	addReserve(address, address, address, uint256) envfree
	removeReserve(address) envfree
}

//  Both lists are correlated - If we use the id of a token in reserves to retrieve a token in underlyingList, we get the same toke.
// Hint:
// If index i is nonzero and token t is a valid address then t.id equals i iff the i-th reserve is t.
// If i is zero, i-th token is t implies t.id equals i. @note 2 why single out zero?
invariant correlationOfLists(address token, uint256 id)
	(id!=0 && token!=0) => (getIdOfToken(token) == id <=> getTokenAtIndex(id) == token)
 	&&
	(id==0 && getTokenAtIndex(id) == token) => getIdOfToken(token) == id

    
//  There should not be a token saved at an index greater or equal to reserve counter.
// Hint:
// If index i is nonzero and token t is a valid address then t.id equals i iff the i-th reserve is t.
// If i is zero, i-th token is t implies t.id equals i.
invariant indexLessThanCount(address token)
    (getReserveCount() > 0 => getIdOfToken(token) < getReserveCount()) &&
    (getReserveCount() == 0 => getIdOfToken(token) == 0)
    {
        preserved removeReserve(address t) {
            require t == token;
        }
    }

//  Id of assets is injective (i.e. different tokens should have distinct ids).
// Hint:
// If index i is nonzero and token t is a valid address then t.id equals i iff the i-th reserve is t.
// If i is zero, i-th token is t implies t.id equals i.
invariant idIsInjective(address token1, address token2)
        (token1 != token2 && getIdOfToken(token1) != 0)  => (getIdOfToken(token1) != getIdOfToken(token2))
	{
		preserved addReserve(address token, address stableToken, address varToken, uint256 fee) {
			require token != 0;
			bool alreadyAdded = getTokenAtIndex(getIdOfToken(token)) != 0 || getTokenAtIndex(0) == token;
			require !alreadyAdded;
		}
		
		preserved removeReserve(address token) {
			require getTokenAtIndex(getIdOfToken(token)) != 0;
		}
	}

//  Independency of tokens in list - removing one token from the list doesn't affect other tokens.
rule independencyOfTokensInAList(address token1, address token2, address stableToken, address varToken, uint256 fee, method f) {
	env e;
	require token1 != token2;
    requireInvariant correlationOfLists(token1, token2);
	uint256 tokenId1Before = getIdOfToken(token1);
    uint256 tokenId2Before = getIdOfToken(token2);
	
	if (f.selector == addReserve(address, address, address, uint256).selector) {		
        require token2 != 0;
		bool alreadyAdded = getIdOfToken(token2) != 0 || getTokenAtIndex(0) == token2;
		require !alreadyAdded;
		addReserve(token2, stableToken, varToken, fee);
	}
	else {
        require getTokenAtIndex(getIdOfToken(token2)) != 0;
		removeReserve(token2);
	}
	
	uint256 tokenId1After = getIdOfToken(token1);
	assert tokenId1Before == tokenId1After, "not same Id after function call";
    // @note 3 how to compare struct before and after?
}

//  Each non-view function changes reservesCount by 1.
rule addRemoveChangeReserveCountBy1(method func, address token, address stableToken, address varToken, uint256 fee) {
	env e;
	calldataarg args;
    uint256 reserveBefore = getReserveCount();
    if (func.selector == addReserve(address, address, address, uint256).selector
		|| func.selector == removeReserve(address).selector) {    
        func@norevert(e, args);
    
        uint256 reserveAfter = getReserveCount();
        assert reserveAfter - reserveBefore == 1 
            || reserveAfter - reserveBefore == -1        
            , "wrong increase/decrease in reserveCount";
    } else {
        uint256 reserveAfter = getReserveCount();
        assert reserveBefore==reserveAfter, "view only functions should not change ReserveCount";
    }
}
