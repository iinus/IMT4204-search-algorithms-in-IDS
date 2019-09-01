#!/usr/bin/python
# Compiled with python 3.6.3

# Input: two strings T (length n) and P (length m)
# Output: The locations of all occurences of P in T 

CEND = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
CGREEN  = '\33[32m'
OKRED    = '\033[1m\33[31m'
CBLUE   = '\33[34m'

def create_bitmask_table(pattern, m):
    B={-1:0}
    m = len(pattern)
    s=1
    for i in range(m-1,-1,-1):
        B[pattern[i]] = B.get(pattern[i],0) | s
        s <<= 1
    return B


def BNDM(text, pattern):
    print("pre-processing...")
    print("Text: " + text + " Pattern: " + pattern)
    n = len(text)
    m = len(pattern)
    B = create_bitmask_table(pattern, m)

# search phase
    print("searching...")
    pos = 0
    while (pos <= n-m):
        j = m - 1
        last = m 
        d = ~0
        while (d != 0 and j >= 0):
            if text[pos+j] in B: 
                d = d & B[text[pos+j]]    
            else:
                d = d & 0
            j = j - 1
            if d != 0:
                if (j >= 0):
                    last = j + 1
                else:
                    print(BOLD + "[+] Found pattern " + CGREEN + text[pos:pos+m] + CEND + BOLD + " at pos " + CBLUE + str(pos) + CEND)
                    
            d = d << 1
        pos = pos + last
           
if __name__ == "__main__": 
    BNDM("abacadabrabra", "bra")
