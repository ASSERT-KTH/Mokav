def func(*args):
	ret_values = []
	
	import sys, threading, os.path
	import collections, heapq, math, bisect
	import string
	from platform import python_version
	import itertools
	sys.setrecursionlimit((10 ** 6))
	threading.stack_size((2 ** 27))
	
	def next(nstr, minone, maxone, lis):
	    if ((int(nstr) < minone) or (int(nstr) > maxone)):
	        if (max(lis) < maxone):
	            lis.append(int(nstr))
	        return
	    lis.append(int(nstr))
	    next((nstr + '4'), minone, maxone, lis)
	    next((nstr + '7'), minone, maxone, lis)
	
	def main():
	    if os.path.exists('input.txt'):
	        input = open('input.txt', 'r')
	    else:
	        input = sys.stdin
	    (n1, n2) = list(map(int, input.readline().split()))
	    lis = []
	    next('4', 1, 1000000000, lis)
	    next('7', 1, 1000000000, lis)
	    lis.sort()
	    sum = 0
	    begin = bisect.bisect_left(lis, n1)
	    for i in range(begin, len(lis)):
	        if (i == begin):
	            if (lis[i] <= n2):
	                sum += (lis[i] * ((lis[i] - n1) + 1))
	            elif (n2 < 4):
	                sum += (4 * ((n2 - n1) + 1))
	                break
	            else:
	                sum += (lis[i] * ((n2 - max(n1, lis[(i - 1)])) + 1))
	                break
	            continue
	        if (lis[i] <= n2):
	            sum += (lis[i] * (lis[i] - lis[(i - 1)]))
	        else:
	            sum += (lis[i] * (n2 - max(n1, lis[(i - 1)])))
	            break
	    output = sum
	    if os.path.exists('output.txt'):
	        open('output.txt', 'w').writelines(str(output))
	    else:
	        sys.stdout.write(str(output))
	if (__name__ == '__main__'):
	    main()

	return ret_values
