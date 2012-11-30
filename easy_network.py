# -*- coding:utf-8 -*-
"""cut corners script around network."""

def within_network(target):
	'''
	return a function to check ip address is in specified ipaddress with/o netmask
	>>> f = within_network('192.168.0.20')
	>>> f('192.168.0.20')
	True
	>>> f('192.168.0.21')
	False
	>>> f('192.168.0.16', netmask=28)
	True
	>>> f('192.168.0.15', netmask=28)
	False
	>>> f('192.168.0.15', netmask=27)
	True
	>>> f('192.168.0.254', netmask=24)
	True
	'''
	target_binary = ''.join([format(int(x), '08b') for x in target.split('.')])
	def _within_network(check_address, netmask=32):
		check_binary = ''.join([format(int(x), '08b') for x in check_address.split('.')])[:netmask]
		return check_binary == target_binary[:netmask]
	return _within_network

if __name__ == '__main__':
	import doctest
	doctest.testmod()
