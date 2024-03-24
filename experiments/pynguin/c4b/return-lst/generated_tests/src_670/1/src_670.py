def func(*args):
	ret_values = []
	
	from collections import defaultdict
	from pprint import pprint
	import sys
	import time
	from collections import Counter
	from functools import total_ordering, lru_cache
	from random import randint
	from sys import stderr
	from typing import Union
	INF = ((10 ** 18) + 3)
	EPS = 1e-10
	MAX_CACHE = (10 ** 9)
	
	def time_it(function, output=stderr):
	
	    def wrapped(*args, **kwargs):
	        start = time.time()
	        res = function(*args, **kwargs)
	        elapsed_time = (time.time() - start)
	        ret_values.append(('"%s" took %f ms' % (function.__name__, (elapsed_time * 1000))), file=output)
	        return res
	    return wrapped
	
	@time_it
	def main():
	    (n, a, b, c) = map(int, (args[0] for _ in range(4)))
	    or_n = n
	    opt1 = (n // a)
	    opt2 = (max(0, (n - c)) // (b - c))
	    n -= (opt2 * (b - c))
	    opt2 += (n // a)
	    n = (or_n % a)
	    opt1 += (max(0, (n - c)) // (b - c))
	    res = max(opt1, opt2)
	    ret_values.append(res)
	
	def set_input(file):
	    global input
	    input = (lambda : file.readline().strip())
	
	def set_output(file):
	    global print
	    local_print = print
	
	    def ret_values.append(*args, **kwargs):
	        kwargs['file'] = kwargs.get('file', file)
	        return local_ret_values.append(*args, **kwargs)
	if (__name__ == '__main__'):
	    set_input((open('input.txt', 'r') if ('MINE' in sys.argv) else sys.stdin))
	    set_output(sys.stdout)
	    main()

	return ret_values
