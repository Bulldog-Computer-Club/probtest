import probtest.langs.util

import os

class ProbtestPython(probtest.langs.util.LangTest):
	def run_hook(self):
		self.output = os.popen(f"python3 {self.file}").read()

probtest.langs.util.supported_langs["py"] = ProbtestPython