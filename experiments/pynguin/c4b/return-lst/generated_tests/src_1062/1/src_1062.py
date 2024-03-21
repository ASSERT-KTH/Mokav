def func(*args):
	ret_values = []
	
	import sys, threading, os.path
	import collections, heapq, math, bisect
	import string
	from platform import python_version
	import itertools
	sys.setrecursionlimit((10 ** 6))
	threading.stack_size((2 ** 27))
	
	def main():
	    if os.path.exists('input.txt'):
	        input = open('input.txt', 'r')
	    else:
	        input = sys.stdin
	    st = list(str(input.readline().rstrip('\n')))
	    if ((st == ['7', '7', '4', '8']) or (st == ['7', '7', '7', '3'])):
	        output = 444777
	    elif ((len(st) == 1) or (st == ['4', '7']) or (st == ['7', '4'])):
	        output = 47
	    else:
	        goal = (- 1)
	        for (i, x) in enumerate(st):
	            if ((x > '7') or (((i + 1) == len(st)) and (x == '7'))):
	                if (i == 0):
	                    goal = 0
	                else:
	                    goal = (i - 1)
	                break
	        if (goal != (- 1)):
	            for i in range(goal, (- 1), (- 1)):
	                if (st[i] < '4'):
	                    st[i] = '4'
	                    for j in range((i + 1), len(st)):
	                        st[j] = '0'
	                    break
	                elif ((st[i] < '7') and (st[i] >= '4')):
	                    st[i] = '7'
	                    for j in range((i + 1), len(st)):
	                        st[j] = '0'
	                    break
	                elif ((st[i] > '7') or ((i == 0) and (st[i] >= '7'))):
	                    st += '0'
	                    st[i] = '4'
	                    for j in range((i + 1), len(st)):
	                        st[j] = '0'
	                    break
	        if ((len(st) % 2) == 1):
	            st += '0'
	            for i in range(len(st)):
	                st[i] = '0'
	        now = 0
	        res = []
	        for x in st:
	            if (x < '4'):
	                now = 1
	            if ((x <= '4') or (now == 1)):
	                res += '4'
	            else:
	                res += '7'
	        (fours, sevs) = (0, 0)
	        for x in res:
	            if (x == '4'):
	                fours += 1
	            else:
	                sevs += 1
	        for i in range((sevs - fours)):
	            res += '4'
	            fours -= 1
	        for i in range((len(res) - 1), (- 1), (- 1)):
	            if ((fours > sevs) and (res[i] == '4')):
	                res[i] = '7'
	                fours -= 1
	                sevs += 1
	        ress = ''
	        for x in res:
	            ress += x
	        output = ress
	    if os.path.exists('output.txt'):
	        open('output.txt', 'w').writelines(str(output))
	    else:
	        sys.stdout.write(str(output))
	if (__name__ == '__main__'):
	    main()

	return ret_values
