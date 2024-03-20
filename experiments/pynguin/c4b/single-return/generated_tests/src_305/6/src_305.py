def func(*args):
	
	if (__name__ == '__main__'):
	    n = int(args[0])
	    prime = ([True] * (n + 1))
	    candi = [set() for _ in range((n + 1))]
	    for i in range(2, (n + 1)):
	        if prime[i]:
	            for j in range((i + i), (n + 1), i):
	                prime[j] = False
	                candi[j].add(i)
	    rest = 0
	    for i in range(2, (n + 1)):
	        if (len(candi[i]) == 2):
	            rest += 1
	    return(rest)
