def count(c, m, n ):

	# If n is 0 then there is 1 solution (do not include any coin)
	if (n == 0):
		return 1

	# If n is less than 0 then no solution exists
	if (n < 0):
		return 0;

	# If there are no coins and n is greater than 0,
    # then no solution exist
	if (m <=0 and n >= 1):
		return 0

	# count is sum of solutions
    # (i) including c[m-1] (ii) excluding c[m-1]
	return count( c, m - 1, n ) + count( c, m, n-c[m-1] )

# Driver program to test above function
c = [1, 2, 3]
m = len(c)
print("Number of way:",count(c, m, 4))

