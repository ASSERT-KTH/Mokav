def func(*args):
	ret_values = []
	
	from sys import stdin
	
	def move(x):
	    a = 0
	    b = 0
	    for i in range(len(x)):
	        for j in range(len(x)):
	            if (x[i][j] == 1):
	                a = i
	                b = j
	    d = (abs((a - 2)) + abs((b - 2)))
	    ret_values.append(d)
	
	def main():
	    a = 5
	    l = []
	    while (a != 0):
	        x = [int(i) for i in stdin.readline().strip().split()]
	        l.append(x)
	        a -= 1
	    move(l)
	main()

	return ret_values
