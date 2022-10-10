import probtest.langs.util

import os

class ProbtestPython(probtest.langs.util.LangTest):
	def run_hook(self):
		os.system(f"python3 {self.file}")

probtest.langs.util.supported_langs["py"] = ProbtestPython