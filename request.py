import urllib3

class Request:

	"""Module for requests using urllib3"""

	def __init__(self):
		pass

	# function for sending request and receiving response
	def make_request(self, url, retries=4, timeout=5, proxy=None, headers=None):
		http = None
		if proxy:
			http = urllib3.ProxyManager(proxy)
		else:
			http = urllib3.PoolManager()
		try:
			resp = http.request("GET", 
				url.replace("https", "http"), 
				retries=retries, 
				timeout=timeout,
				preload_content=False,
				headers=headers)
		except urllib3.exceptions.NewConnectionError:
			# if failed to create connection
			print ("Connection Failed!")
		except urllib3.exceptions.SSLError:
			# if failed to establish secure connection (https)
			print ("SSL Error!")

		return resp	
		