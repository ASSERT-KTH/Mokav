def func(*args):
	ret_values = []
	
	
	def solve(position, size, level):
	    if (position == (size // 2)):
	        return level
	    return solve(abs((position - (size // 2))), (size // 2), (level - 1))
	(n, k) = map(int, args[0].split())
	Size = (2 ** n)
	ret_values.append(solve(k, Size, n))

	return ret_values
