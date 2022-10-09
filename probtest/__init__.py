import os
import sys
import json
import argparse

import probtest.langs.util

import probtest.langs.python
import probtest.langs.c
import probtest.langs.cxx


def main():
	parser = argparse.ArgumentParser(description="SImple competitive programming judge")
	parser.add_argument("file", default="solution.py", type=str, nargs="?")
	parser.add_argument("--lang", default=argparse.SUPPRESS, help="manually specify the file's language")
	
	if len(sys.argv)==1:
    		parser.print_help(sys.stderr)
    		sys.exit(1)

	args = parser.parse_args()

	print(args)

	return 0