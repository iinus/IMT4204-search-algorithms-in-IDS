#!/usr/bin/python
# Compiled with python 3.6.3

import sys, stat, os, timeit
from optparse import OptionParser
import BNDM
import shift_or

CEND = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ITALIC = '\033[3m'
CGREEN  = '\33[32m'
CRED    = '\033[1m\33[31m'
CBLUE   = '\33[34m'

if __name__=="__main__":

    if sys.version_info < (3, 0, 0):
        sys.stderr.write("fastsearch requires python version > 3.0, please upgrade your python installation.")
        sys.exit(1)
    
    usage = "usage: python3 %prog [options] [text] [pattern] " 
    parser = OptionParser(usage=usage)
    parser.add_option("--SO", help="Specify Shift-OR as alogorithm. Default is BNDM. ", default=None, action='store_true', dest="shift_or")
    parser.add_option("--time", help="Print the execution time of algorithm.", default=None, action='store_true', dest="time")

    (options, args) = parser.parse_args()

    text = args[0]
    pattern = args[1]
    m = len(pattern)
    number = 100000
    isFile = os.path.isfile(text)

    print(ITALIC + "*** Seraching for pattern " + pattern + " ***" + CEND)
    if isFile:
        with open (text, "r") as myfile:
            text=myfile.read()
    if options.shift_or:
        positions = shift_or.shift_or(text, pattern)
        execution_time = timeit.timeit('shift_or.shift_or(text, pattern)', 'from __main__ import shift_or, text, pattern', number=number)
    else:
        positions = BNDM.BNDM(text, pattern)
        execution_time = timeit.timeit('BNDM.BNDM(text, pattern)', 'from __main__ import BNDM, text, pattern', number=number)
    if options.time:        
        execution_time = execution_time / number
        print (BOLD + "[*] Execution time: " + CBLUE + str(execution_time) + CEND)
    if len(positions) > 0:
        for pos in positions:
            print(BOLD + "[+] Found pattern " + CGREEN + text[pos:pos+m] + CEND + BOLD + " at pos " + CBLUE + str(pos) + CEND)
    else:
        print(BOLD + CRED + "No occurences found." + CEND)
    


