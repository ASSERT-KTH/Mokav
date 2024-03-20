def func(*args):
	
	from sys import stdin
	from random import randint
	
	def pollard_brent(n):
	    (y, c, m) = (randint(1, (n - 1)), randint(1, (n - 1)), randint(1, (n - 1)))
	    g = r = q = 1
	    while (g == 1):
	        x = y
	        for i in range(r):
	            y = ((pow(y, 2, n) + c) % n)
	        k = 0
	        while ((k < r) and (g == 1)):
	            ys = y
	            for i in range(min(m, (r - k))):
	                y = ((pow(y, 2, n) + c) % n)
	                q = ((q * abs((x - y))) % n)
	            (g, b) = (n, q)
	            while b:
	                (g, b) = (b, (g % b))
	            k += m
	        r *= 2
	    if (g == n):
	        while True:
	            ys = ((pow(ys, 2, n) + c) % n)
	            (g, b) = (n, abs((x - ys)))
	            while b:
	                (g, b) = (b, (g % b))
	            if (g > 1):
	                break
	    return g
	
	def MillerRabin(n):
	    a = 7
	    while (a and (n >= (0, 341550071728321, 3474749660383, 2152302898747, 1122004669633, 4759123141, 9080191, 1373653)[a])):
	        a -= 1
	    d = nn = (n - 1)
	    s = 0
	    if a:
	        l = (None, (2, 3, 5, 7, 11, 13, 17), (2, 3, 5, 7, 11, 13), (2, 3, 5, 7, 11), (2, 13, 23, 1662803), (2, 7, 61), (31, 73), (2, 3))[a]
	    else:
	        l = tuple((randint(1, nn) for a in range(40)))
	    while ((d & 1) == 0):
	        d >>= 1
	        s += 1
	    for a in l:
	        a = pow(a, d, n)
	        if (a != 1):
	            r = s
	            while r:
	                if (a == nn):
	                    break
	                a = ((a * a) % n)
	                r -= 1
	            if (r == 0):
	                return False
	    return True
	
	def factor(x):
	    result = {}
	    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171):
	        (y, rest) = divmod(x, p)
	        if (not rest):
	            cnt = 0
	            while (not rest):
	                x = y
	                (y, rest) = divmod(x, p)
	                cnt += 1
	            result[p] = cnt
	            if (x == 1):
	                return result
	    if (x < 1394761):
	        result[x] = 1
	        return result
	    l = []
	    while ((x > 1) or l):
	        if (x == 1):
	            (x, l) = (l[(- 1)], l[:(- 1)])
	        if MillerRabin(x):
	            if (x in result):
	                result[x] += 1
	            else:
	                result[x] = 1
	            x = 1
	        else:
	            y = pollard_brent(x)
	            x //= y
	            l.append(y)
	    return result
	
	def divisors(x):
	    l = [1]
	    for (k, v) in factor(x).items():
	        for i in range(len(l)):
	            x = l[i]
	            for j in range(v):
	                x *= k
	                l.append(x)
	    return l
	
	def main():
	    s = stdin.readline().strip()
	    x = int(s)
	    if (x < 10):
	        return 1
	    digits = tuple(set(s))
	    return sum((any(((c in digits) for c in str(y))) for y in divisors(x)))
	return(main())
