#!/usr/bin/evn python3
# _*_ conding: utf-8 _*_

__author__ = 'Ftong Tong'

'''
init database: awesome
'''

import orm
from models import User, Blog, Comment

def test(loop):
	yield from orm.create_pool(loop = loop, user = 'www-data', password = 'www-data', database = 'awesome')
	
	u = User(name = 'Test', email = 'test@example.com', passwd = '1234567890', image = 'about:blank')

	yield from u.save()

for x in test():
	pass
