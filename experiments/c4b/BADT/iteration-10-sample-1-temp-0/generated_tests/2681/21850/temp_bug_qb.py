def original_func(*args):
	global_list = []
	
	from math import *
	
	def resheto(n):
	    prime = [True for _ in range((n + 1))]
	    prime[0] = prime[1] = False
	    for i in range(2, (n + 1)):
	        if prime[i]:
	            if ((i ** 2) <= n):
	                for j in range((i ** 2), (n + 1), i):
	                    prime[j] = False
	    answer = []
	    for i in range((n + 1)):
	        if prime[i]:
	            answer.append(i)
	    return answer
	
	class Integer(int):
	
	    def __pow__(self, power, modulo=None):
	        k = power
	        bbb = 1
	        c = self
	        while k:
	            if ((k % 2) == 0):
	                k /= 2
	                c *= c
	            else:
	                k -= 1
	                bbb *= c
	        return bbb
	
	    def can_divide(self, n):
	        if (n == 0):
	            return False
	        elif ((self % n) == 0):
	            return True
	        else:
	            return False
	
	    def trial_division(self):
	        divisions = []
	        d = 2
	        number = self
	        while (number > 1):
	            if ((number % d) == 0):
	                divisions.append(d)
	                number /= d
	            else:
	                d += 1
	        return sorted(divisions)
	
	    def is_prime(self):
	        if (self == 2):
	            return True
	        j = int((sqrt(self) + 1))
	        for i in range(2, (j + 1)):
	            if ((self % i) == 0):
	                return False
	        return True
	
	    def gcd(self, bb):
	        aa = self
	        while bb:
	            aa %= bb
	            (aa, bb) = (bb, aa)
	        return aa
	
	    def lmc(self, bull):
	        return int(((self / gcd(self, bull)) * bull))
	
	class Matrix():
	
	    def __init__(self, size):
	        matrix = []
	        for i in range(size):
	            matrix.append([])
	            for j in range(size):
	                matrix[i].append(0)
	        self.matrix = matrix
	        self.n = size
	
	    def edit_element(self, cords, new_value):
	        self.matrix[cords[0]][cords[1]] = new_value
	
	    def __add__(self, other_matrix):
	        c = Matrix(self.n)
	        for i in range(self.n):
	            for j in range(self.n):
	                c.edit_element((i, j), (self.matrix[i][j] + other_matrix.matrix[i][j]))
	        return c
	
	    def __mul__(self, other_matrix):
	        c = Matrix(self.n)
	        for i in range(self.n):
	            for j in range(i):
	                k = other_matrix.matrix[i][j]
	                other_matrix.matrix[i][j] = other_matrix.matrix[j][i]
	                other_matrix.matrix[j][i] = k
	        for i in range(self.n):
	            for j in range(self.n):
	                c.matrix[i][j] = 0
	                for k in range(self.n):
	                    c.matrix[i][j] += (self.matrix[i][k] * other_matrix.matrix[j][k])
	        for i in range(self.n):
	            for j in range(i):
	                k = other_matrix.matrix[i][j]
	                other_matrix.matrix[i][j] = other_matrix.matrix[j][i]
	                other_matrix.matrix[j][i] = k
	        return c
	a = Integer(args[0])
	global_list.append((a ** 3))
	return global_list