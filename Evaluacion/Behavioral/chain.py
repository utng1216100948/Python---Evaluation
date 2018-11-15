#Chain.py

class Handler:
	"""Abstract Handler"""
	def __init__(self, successor):
		self._successor = successor

	def handle(self, request):
			handled = self._handle(request)

			
			if not handled:
				self._successor.handle(request)	

	def _handle(self, request):
		raise NotImplementedError('Must provide implementation in subclass!')

class ConcreteHandler1(Handler): 
	"""Concrete handler 1"""
	def _handle(self, request):
		if 0 < request <= 10: 
			print("Request {} handled in handler 1".format(request))
			return True 

class DefaultHandler(Handler): 
	"""Default handler"""

	def _handle(self, request):
		"""If there is no handler available"""
		print("End of chain, no handler for {}".format(request))
		return True

class Client: 
	def __init__(self):
		self.handler = ConcreteHandler1(DefaultHandler(None))
	def delegate(self, requests):
		for request in requests:
				self.handler.handle(request)

# Create a client
c = Client()
# Create requests
requests = [2, 5, 30]
# Send the requests
c.delegate(requests)

