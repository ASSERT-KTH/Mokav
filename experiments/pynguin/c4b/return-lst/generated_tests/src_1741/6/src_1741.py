def func(*args):
	ret_values = []
	
	from collections import defaultdict
	
	def main():
	    (a1, a2) = map(int, args[0].split())
	    ans = 0
	    while ((a1 > 0) and (a2 > 0)):
	        if (a1 > a2):
	            a1 -= 2
	            a2 += 1
	        else:
	            a1 += 1
	            a2 -= 2
	        if ((a1 < 0) or (a2 < 0)):
	            break
	        ans += 1
	    ret_values.append(ans)
	if (__name__ == '__main__'):
	    main()

	return ret_values
