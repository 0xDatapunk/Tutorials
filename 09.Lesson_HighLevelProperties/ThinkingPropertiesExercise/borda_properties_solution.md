***State transition*** - 
Checks that a blocked voter cannot get unlisted


***Variable transition*** - 
Checks that a voter's "registered" mark is changed correctly - 
if it's false after a function call, it was false before
if it's true after a function call it either started as true or changed from false to true via registerVoter()

***Variable transition*** -
Checks that a each voted contender's points received the correct amount of points

***Variable transition*** -
Checks that a contender's point count is non-decreasing

***High-level*** - 
cannot vote more than once. 

***High-level*** - 
does not allow voting if blacklisted. 

***High-level*** - 
cannot decrease a contender points. 



Above all share high priority