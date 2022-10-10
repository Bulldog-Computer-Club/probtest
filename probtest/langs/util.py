import datetime
import multiprocessing

# dictionary of all languages supported
# this will be filled out during runtime
supported_langs = {}

class LangTest:
	def __init__(self, file, timeout):
		self.file = file
		self.timeout = timeout
		self.output = None

	def run_tests(self):
		start = datetime.datetime.now()
		p = multiprocessing.Process(target=self.run_hook)
		p.start()
		
		# Timeout for solution
		# TODO: make this value configurable
		p.join(self.timeout)

		# make sure process is dead
		if p.is_alive():
			p.kill()
			p.join()

		end = datetime.datetime.now()
		delta = end - start
		return delta.total_seconds()

	# Submission actually run here, the method is overrided in each specific language module
	# This method is supposed to be blocking
	# Called by run_test()
	def run_hook(self):
		pass