def findWays(f, d, s):
	# Create a table to store results of subproblems. One extra
	# row and column are used for simpilicity (Number of dice
	# is directly used as row index and sum is directly used
	# as column index). The entries in 0th row and 0th column
	# are never used.
	mem = [[0 for i in range(s+1)] for j in range(d+1)]
	# Table entries for no dices
	# If you do not have any data, then the value must be 0, so the result is 1
	mem[0][0] = 1
	# Iterate over dices
	for i in range(1, d+1):

		# Iterate over sum
		for j in range(1, s+1):

			mem[i][j] = mem[i][j - 1] + mem[i - 1][j - 1]
			if j - f - 1 >= 0:
				mem[i][j] -= mem[i - 1][j - f - 1]
	return mem[d][s]

# Driver code
print(findWays(4, 2, 1))
print(findWays(2, 2, 3))
print(findWays(6, 3, 8))
print(findWays(4, 2, 5))
print(findWays(4, 3, 5))

