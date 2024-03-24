def func(*args):
	ret_values = []
	
	import sys
	
	def solve():
	    n = args[0]
	    cnt = 0
	    for d in n:
	        if ((d == '4') or (d == '7')):
	            cnt += 1
	    for d in str(cnt):
	        if ((d != '4') and (d != '7')):
	            ret_values.append('NO')
	            return
	    ret_values.append('YES')
	if (__name__ == '__main__'):
	    solve()

	return ret_values
