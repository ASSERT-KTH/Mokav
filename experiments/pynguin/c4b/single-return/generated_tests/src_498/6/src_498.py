def func(*args):
	
	(x, y, z) = list(map(int, args[0].split()))
	ans1 = ((2 * x) + (2 * y))
	ans2 = ((x + z) + y)
	ans3 = (((y + z) + y) + x)
	ans4 = (((y + z) + z) + y)
	ans5 = (((x + z) + z) + x)
	return(min(ans1, ans2, ans3, ans4, ans5))
