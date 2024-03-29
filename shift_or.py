#!/usr/bin/python
# Compiled with python 3.6.3

# Input: two strings text (length n) and pattern (length m)
# Output: all occurences of P in T 

def create_bitmask_table(pattern, m):
    # creates the bitmask table from pattern
    bitmask = {} 
    for i in range(m):
        bitmask[pattern[i]] = (bitmask.get(pattern[i], 0) | (1 << i))
    bitmask = {k: neg(bitmask[k]) for k in bitmask}
    return bitmask

def shift_or(text, pattern):
    n = len(text)
    m = len(pattern)
    allones = neg(0)
    positions = []

# Pre-processing: create bitmask table
    B = create_bitmask_table(pattern, m)

# search phase
    d = allones
    hit = (1 << (m - 1))
    for i in range(0, n):
        d = (((d << 1) & allones) | B.get(text[i], allones))
        if d & hit == 0:
            pos = i - m + 1
            positions.append(pos)

    return positions

def neg(x):
    return 0b11111111111111111111111111111111 - x

