#!/usr/bin/env python
# -*- coding: utf-8 -*-
import httplib
import json

init = True
memo = {}
def main(argv):
	seed = argv[0]
	n = int(argv[1])
	conn = httplib.HTTPConnection("challenge-server.code-check.io",80)
	# http://challenge-server.code-check.io/api/recursive/ask?n=3&seed=b0c2b89f-4862-4814-8728-ddb0b36076ba
	conn.request("GET", "/api/recursive/ask?n="+str(n)+"&seed="+str(seed))
	response = conn.getresponse()

	# hash has 'n','seed','result'
	# {"seed":"b0c2b89f-4862-4814-8728-ddb0b36076ba","n":3,"result":114}
	js = json.loads(response.read())
	memo[(seed, n)] = js['result']

	
	ans = f(n, seed)
	print ans



	# for i, v in enumerate(argv):
	#   print("argv[{0}]: {1}".format(i, v))

def askServer(n, seed):
	conn = httplib.HTTPConnection("challenge-server.code-check.io",80)
	# http://challenge-server.code-check.io/api/recursive/ask?n=3&seed=b0c2b89f-4862-4814-8728-ddb0b36076ba
	conn.request("GET", "/api/recursive/ask?n="+str(n)+"&seed="+str(seed))
	response = conn.getresponse()

	# hash has 'n','seed','result'
	# {"seed":"b0c2b89f-4862-4814-8728-ddb0b36076ba","n":3,"result":114}
	js = json.loads(response.read())

	memo[(seed, n)] = js['result']
	return js['result']

def f(n, seed):
	if n == 0:
		return 1
	if n == 2:
		return 2
	
	if n % 2 == 0:
		f4 = isInMemo(n, seed)
		f3 = isInMemo(n, seed)
		f2 = isInMemo(n, seed)
		f1 = isInMemo(n, seed)

		if f4 == False:
			f4 = f(n-4, seed)
		if f3 == False:
			f3 = f(n-3, seed)
		if f2 == False:
			f2 = f(n-2, seed)
		if f1 == False:
			f1 = f(n-1, seed)
		return f1 + f2 + f3 + f4
	else: 
		askServer(n, seed)

def isInMemo(n, seed):
	if (seed,n) in memo:
		return memo[(seed,n)]
	else:
		return False


# f(n) = (
# 	if n mod 2 = 0 then
#   	f(n − 1) + f(n − 2) + f(n − 3) + f(n − 4)
# 	else
#   	askServer(n)
# )