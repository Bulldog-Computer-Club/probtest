import datetime
import multiprocessing
import subprocess

import probtest.reader

# dictionary of all languages supported
# this will be filled out during runtime
supported_langs = {}

class LangTest:
	def __init__(self, file, tests, timeout):
		self.file = file
		self.tests = tests
		self.timeout = timeout
		self.output = None
	
	def start_tests(self):
		for test in self.tests:
			self.run_test(test)

	def run_with_input(self, command, input):
		process=subprocess.Popen([command], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		stdoutdata,stderrdata=process.communicate(input=input)
		return (stdoutdata, stderrdata)

	def run_test(self, test):
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
