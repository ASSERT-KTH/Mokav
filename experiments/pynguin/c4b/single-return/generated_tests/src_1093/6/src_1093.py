def func(*args):
	
	import math
	
	def main():
	    n = int(args[0])
	    phib = [1, 1]
	    ans = 0
	    while ((phib[(- 1)] + phib[(- 2)]) <= n):
	        phib.append((phib[(- 1)] + phib[(- 2)]))
	        ans += 1
	    return(ans)
	main()
