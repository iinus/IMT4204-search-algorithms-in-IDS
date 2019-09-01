#!/usr/bin/python
# Compiled with python 3.6.3

# Input: two strings text (length n) and pattern (length m)
# Output: all occurences of P in T 

CEND = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
CGREEN  = '\33[32m'
OKRED    = '\033[1m\33[31m'
CBLUE   = '\33[34m'

def create_bitmask_table(pattern, m):
    # creates the bitmask table from pattern
    bitmask = {} 
    for i in range(m):
        bitmask[pattern[i]] = (bitmask.get(pattern[i], 0) | (1 << i))
    bitmask = {k: neg(bitmask[k]) for k in bitmask}
    return bitmask

def shift_or(text, pattern):
    print( "Text: " + text + " Pattern: " + pattern) 
    n = len(text)
    m = len(pattern)
    allones = neg(0)

    # Pre-processing: create bitmask table
    bitmask = create_bitmask_table(pattern, m)

    # search phase
    d = allones
    hit = (1 << (m - 1))
    for i in range(0, n):
        found = 0
        d = (((d << 1) & allones) | bitmask.get(text[i], allones))
        if d & hit == 0:
            found = 1
            pos = i - m + 1
            print(BOLD + "[+] Found pattern " + CGREEN + text[pos:pos+m] + CEND + BOLD + " at pos " + CBLUE + str(pos) + CEND)
    if found == 0:
        print(BOLD + OKRED + "No mathes found." + CEND)

def neg(x):
    return 0b11111111111111111111111111111111 - x

if __name__ == "__main__": 
    shift_or("bbr", "bra")
