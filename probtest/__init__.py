import os
import sys
import argparse

import probtest.langs.util

import probtest.langs.python
import probtest.langs.c
import probtest.langs.cxx

import probtest.reader

from probtest.ui import error

def main():
	parser = argparse.ArgumentParser(description="SImple competitive programming judge")
	parser.add_argument("file", default="solution.py", type=str, nargs="?")
	parser.add_argument("testsfile", default="tests.probtest", type=str, nargs="?", help="config file specifying the test to run on solution")
	parser.add_argument("--run", help="run with default options, this option might be removed in the future", action="store_true")
	parser.add_argument("--lang", default=argparse.SUPPRESS, help="manually specify the file's language")
	parser.add_argument("--timeout", default=1.0, type=float, help="timeout for solutions, in seconds")
	
	if len(sys.argv)==1:
    		parser.print_help(sys.stderr)
    		sys.exit(1)

	args = parser.parse_args()

	if os.path.exists(args.file):
		if (os.path.isdir(args.file)):
			error(f"{args.file} is a directory")
		if "." in args.file:
			extension =  args.file.split(".")[-1]
			if extension not in probtest.langs.util.supported_langs:
				error(f"\"{extension}\" not a supported language")
			tests = probtest.reader.read_config(args.testsfile)
			tester = probtest.langs.util.supported_langs[extension](args.file, tests, args.timeout)
			time = tester.start_tests()
			print("tests finished in", time, "seconds", file=sys.stderr)
		else:
			# Assume running binary. This functionality is subject to change
			pass
	else:
		error(f"{args.file}: no such file or directory")

	return 0
