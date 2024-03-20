def func(*args):
	
	(k2, k3, k5, k6) = map(int, args[0].split())
	table = {2: k2, 3: k3, 5: k5, 6: k6}
	tot = 0
	m_256 = min(table[2], table[5], table[6])
	tot += (256 * m_256)
	table[2] -= m_256
	table[5] -= m_256
	table[6] -= m_256
	m_32 = min(table[2], table[3])
	tot += (32 * m_32)
	table[2] -= m_32
	table[3] -= m_32
	return(tot)
