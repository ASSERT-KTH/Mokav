def func(*args):
	ret_values = []
	
	'\nSolution to the 165B problem on CodeForces.\n'
	import sys
	import math
	cache = []
	
	def updater(n: int, *inputs) -> None:
	    global cache
	    for i in range(1, len(cache)):
	        for num in inputs:
	            if ((i - num) == 0):
	                cache[i] = max(1, cache[i])
	            elif (((i - num) > 0) and (cache[(i - num)] != 0)):
	                cache[i] = max((cache[(i - num)] + 1), cache[i])
	
	def main() -> None:
	    '\n    The main method.\n    '
	    global cache
	    inputs = list(map(int, args[0].split()))
	    cache = [0 for _ in range((inputs[0] + 1))]
	    updater(*inputs)
	    ret_values.append(cache[inputs[0]])
	if (__name__ == '__main__'):
	    main()

	return ret_values
