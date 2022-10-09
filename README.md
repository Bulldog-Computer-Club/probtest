# Probtest

Probtest is a simple work in progress framework for easily and securely grading competitive programming submissions.


# Goals

- be easily callable from a cgi interface
- remain small and portable across operating systems
- safeguard against malicious submissions
- have an easy to use configuration syntax for writing up test cases

# Non Goals

- deliver a complex web interface
- implement a persistent scoring system
- rely on third party libraries for core functionality

## Running

Running probtest is easy, simply call `probtest.py` from inside the project root. If you wish to install probtest, run `pip install --upgrade .` (from inside the project root, of course). This will install probtest in $HOME/.local/lib/python3.x/site-packages, as well as a script inside $HOME/.local/bin. Make sure the bin directory is inside your PATH variable. 