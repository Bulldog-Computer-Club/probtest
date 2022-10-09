import os
import sys
import json
import argparse

import langs.util

import langs.python
import langs.c
import langs.cxx

parser = argparse.ArgumentParser(description="SImple competitive programming judge")
parser.add_argument("file", nargs="+", help="file to judge")

args = parser.parse_args(sys.argv)