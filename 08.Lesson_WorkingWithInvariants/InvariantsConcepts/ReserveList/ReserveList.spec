
// Try to prove the following list of properties:

//  Both lists are correlated - If we use the id of a token in reserves to retrieve a token in underlyingList, we get the same toke.
// Hint:
// If index i is nonzero and token t is a valid address then t.id equals i iff the i-th reserve is t.
// If i is zero, i-th token is t implies t.id equals i. @note 2 why single out zero?
//  There should not be a token saved at an index greater or equal to reserve counter.
// Hint:
// If index i is nonzero and token t is a valid address then t.id equals i iff the i-th reserve is t.
// If i is zero, i-th token is t implies t.id equals i.
//  Id of assets is injective (i.e. different tokens should have distinct ids).
// Hint:
// If index i is nonzero and token t is a valid address then t.id equals i iff the i-th reserve is t.
// If i is zero, i-th token is t implies t.id equals i.
//  Independency of tokens in list - removing one token from the list doesn't affect other tokens.

//  Each non-view function changes reservesCount by 1.

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
	addReserve(address, address, address, uint256)
	removeReserve(address)
}

// invariant validId(uint256 id)
// 	id!=0

// invariant validToken(address token)
// 	token!=address(0)

invariant indexLessThanCount(address token)
    (getReserveCount() > 0 => getIdOfToken(token) < getReserveCount()) &&
    (getReserveCount() == 0 => getIdOfToken(token) == 0)
        {
            preserved removeReserve(address t) {
                require t == token;
            }
        }


invariant CorrelatedLists(address token, uint256 id)
	(id!=0 && token!=0) => (getIdOfToken(token) == id <=> getTokenAtIndex(id) == token)
 	&&
	(id==0 && getTokenAtIndex(id) == token) => getIdOfToken(token) == id
	
		preserved
            {
                requireInvariant indexLessThanCount(token);
            }

        preserved removeReserve(address t) {
                require t == token;
            }
        }
	 
// If index i is nonzero and token t is a valid address then t.id equals i iff the i-th reserve is t.
// If i is zero, i-th token is t implies t.id equals i.

// 	{ 
//         preserved
//         {
//             requireInvariant validId(id);
//             requireInvariant validToken(token);
//         }
//     }

// invariant LessThanReserverCounter(uint256 id)
// 	id < getReserveCount() || getTokenAtIndex(id) == 0

// invariant LessThanReserverCounter(address token1, address token2)
// 	token1!=token2 && getIdOfToken(token1)!=getIdOfToken(token2)


// rule ReservesCountByOne(method f) {
// 	uint countBefore = getReserveCount(); 
// 	env e;
// 	if (f.selector == addReserve(address, address, address, uint256).selector
// 		|| f.selector == removeReserve(address).selector)
// 	{
// 		calldataarg args;
// 		f(e,args);
	
// 		uint countAfter = getReserveCount(); 
// 		assert countAfter - countBefore == 1 || countAfter - countBefore == -1, "reservesCount changes more than 1";
// 	}
// }



		
	
