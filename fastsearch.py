#!/usr/bin/python
# Compiled with python 3.6.3

import sys, stat, os, timeit
from optparse import OptionParser
import BNDM
import shift_or

CEND = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
CGREEN  = '\33[32m'
OKRED    = '\033[1m\33[31m'
CBLUE   = '\33[34m'

if __name__=="__main__":

    if sys.version_info < (3, 0, 0):
        sys.stderr.write("fastsearch requires python version > 3.0, please upgrade your python installation.")
        sys.exit(1)
    
    usage = "usage: python3 %prog [options] " 
    parser = OptionParser(usage=usage, version = "%prog 1.0")
    parser.add_option("-s", help="Specify search algorithm: BNDM or Shift-Or. Default is BNDM. ", default=None, dest="search")
    parser.add_option("--time", help="Print the time it takes to search", default=None, action='store_true', dest="time")

    (options, args) = parser.parse_args()

    if options.time:
        text = "abacadabra"
        pattern = "bra"
        print (timeit.timeit('BNDM.BNDM("abacadabra", "bra")', 'from __main__ import BNDM, text, pattern', number=10))
    else:
        positions = BNDM.BNDM("abacadabra", "bra")
        for pos in positions:
            print(BOLD + "[+] Found pattern " + CGREEN + text[pos:pos+m] + CEND + BOLD + " at pos " + CBLUE + str(pos) + CEND)

