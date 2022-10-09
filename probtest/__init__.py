#!/usr/bin/env python3

import os
import sys
import json
import argparse

def main(argv):
	parser = argparse.ArgumentParser(description="SImple competitive programming judge")
	parser.add_argument("file", nargs="+", help="file to judge")

	args = parser.parse_args(argv)

if __name__ == "__main__":
	main(sys.argv)