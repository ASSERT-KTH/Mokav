def func(*args):
	ret_values = []
	
	
	def get_digit(n):
	    return len(str(n))
	
	def get_last(n):
	    return (n % 10)
	
	def get_first(n):
	    m = str(n)
	    return int(m[0])
	
	def get_mid(n):
	    if (n < 100):
	        return 0
	    m = str(n)
	    return int(m[1:(len(m) - 1)])
	
	def f(n):
	    if (n < 10):
	        return n
	    d = get_digit(n)
	    la = get_last(n)
	    fi = get_first(n)
	    m = get_mid(n)
	    ans = 0
	    for i in range(0, (d - 1)):
	        for j in range(1, 10):
	            if (i < (d - 2)):
	                ans += (10 ** i)
	            elif (j < fi):
	                ans += (10 ** i)
	            elif (j == fi):
	                ans += m
	                if (j <= la):
	                    ans += 1
	    return (ans + 9)
	
	def main():
	    (l, r) = list(map(int, args[0].split()))
	    ret_values.append((f(r) - f((l - 1))))
	main()

	return ret_values
