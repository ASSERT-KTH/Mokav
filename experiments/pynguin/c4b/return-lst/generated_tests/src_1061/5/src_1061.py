def func(*args):
	ret_values = []
	
	import sys, threading, os.path
	import collections, heapq, math, bisect
	import string
	from platform import python_version
	import itertools
	sys.setrecursionlimit((10 ** 6))
	threading.stack_size((2 ** 27))
	
	def tryall(state, n, m):
	    lis = []
	    (temn, temm) = (n, m)
	    for i in range((n + m)):
	        if (i == 0):
	            if (((state == 1) and (temn > 0)) or ((temn > 0) and (temm == 0))):
	                lis.append(1)
	                temn -= 1
	            elif (((state == 2) and (temm > 0)) or ((temm > 0) and (temn == 0))):
	                lis.append(2)
	                temm -= 1
	            continue
	        if ((i % 2) == 0):
	            if (((lis[(i - 1)] == 1) and (temn > 0)) or ((temn > 0) and (temm == 0))):
	                temn -= 1
	                lis.append(1)
	            else:
	                temm -= 1
	                lis.append(2)
	        elif (((lis[(i - 1)] == 2) and (temn > 0)) or ((temn > 0) and (temm == 0))):
	            temn -= 1
	            lis.append(1)
	        else:
	            temm -= 1
	            lis.append(2)
	    (count1, count2) = (0, 0)
	    for i in range(1, (n + m)):
	        if (lis[i] == lis[(i - 1)]):
	            count1 += 1
	        else:
	            count2 += 1
	    return (count1, count2)
	
	def main():
	    if os.path.exists('input.txt'):
	        input = open('input.txt', 'r')
	    else:
	        input = sys.stdin
	    (n, m) = list(map(int, input.readline().split()))
	    sol1 = tryall(1, n, m)
	    sol2 = tryall(2, n, m)
	    if (sol1[0] > sol2[0]):
	        (count1, count2) = (sol1[0], sol1[1])
	    else:
	        (count1, count2) = (sol2[0], sol2[1])
	    output = ((str(count1) + ' ') + str(count2))
	    if os.path.exists('output.txt'):
	        open('output.txt', 'w').writelines(str(output))
	    else:
	        sys.stdout.write(str(output))
	if (__name__ == '__main__'):
	    main()

	return ret_values
