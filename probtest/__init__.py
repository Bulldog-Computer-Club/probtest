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
	parser.add_argument("file", help="file to judge")
	parser.add_argument("--lang", default=argparse.SUPPRESS, help="manually specify the file's language")
	parser.add_argument('--foo', default=argparse.SUPPRESS)
	
	if len(sys.argv)==1:
    		parser.print_help(sys.stderr)
    		sys.exit(1)

	args = parser.parse_args(sys.argv)
	return 0

if __name__ == "__main__":
	main()
