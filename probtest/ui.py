import sys
import __main__

def error(str):
	print(f"{__main__.__file__.split('/')[-1]}: {str}", file=sys.stderr)
	sys.exit(1)

def warn():
	return