def func(*args):
	
	
	def solve(position, size, level):
	    if (position == (size // 2)):
	        return level
	    return solve(abs((position - (size // 2))), (size // 2), (level - 1))
	(n, k) = map(int, args[0].split())
	Size = (2 ** n)
	return(solve(k, Size, n))
