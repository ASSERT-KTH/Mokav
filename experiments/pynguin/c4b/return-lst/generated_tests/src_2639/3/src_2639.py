def func(*args):
	ret_values = []
	
	import sys
	__author__ = 'buyvich'
	
	def calc_substr(s, sub):
	    "\n    >>> calc_substr('KV', 'VK')\n    0\n    >>> calc_substr('VK', 'VK')\n    1\n    >>> calc_substr('VV', 'VK')\n    1\n    >>> calc_substr('V', 'VK')\n    0\n    >>> calc_substr('VKKKKKKKKKVVVVVVVVVK', 'VK')\n    3\n    >>> calc_substr('KVKV', 'VK')\n    1\n    >>> calc_substr('VKKKK', 'VK')\n    2\n    "
	    max_cnt = s.count(sub)
	    for i in range(len(s)):
	        l = list(s)
	        for k in 'VK':
	            l[i] = k
	            tmp_cnt = ''.join(l).count(sub)
	            max_cnt = max(max_cnt, tmp_cnt)
	    return max_cnt
	if (__name__ == '__main__'):
	    s = sys.stdin.readline().strip()
	    r = calc_substr(s, 'VK')
	    sys.stdout.write(('%s' % r))

	return ret_values
