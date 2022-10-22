from probtest.ui import error
import os.path

def read_config(file):
	if (os.path.exists(file)):
		tests = []
		with open(file, "r") as f:
			test_cases = f.read().split("--")
			for test_case in test_cases:
				test_rule = test_case.split("=")
				tests.append({ "input": test_rule[0].split("\n"), "output": test_rule[1].split("\n")})
		return tests
	else:
		error(f"{file}: no such file or directory")
		