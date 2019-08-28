
# Input: two strings T (length n) and P (length m)
# Output: The locations of all occurences of P in T 

def BNDM(Text, Pattern):
    print("pre-processing...")
    print("Text: " + Text + " Pattern: " + Pattern)
    n = len(Text)
    m = len(Pattern)
    r = 26 # alphabet size
# pre-processing: compute incidence matrix B of P 
    B = [[ 0 for i in range(m) ] for j in range(m)]
    B = {(rx, cx): c for rx, r in enumerate(B)\
                for cx, c in enumerate(r)}
    s = 1 
    for i in range (m-1, -1, -1):
        key_exists = 0
        if Pattern[m-i-1] in B: 
            key_exists = B[Pattern[m-i-1]]
        B[Pattern[m-i-1]] = s | key_exists
        s <<= 1

# search phase
    print("searching...")
    pos = 0
    while (pos <= n-m):
        j = m - 1
        last = m 
        d = 1
        while (d != 0 and j >= 0):
            if Text[pos+j] in B: 
                d = d & B[Text[pos+j]]    
            else:
                d = d & 0
            j = j - 1
            if d != 0:
                if (j >= 0):
                    last = j
                else:
                    print(pos)
            d = d << 1
        pos = pos + last
        
if __name__ == "__main__": 
    BNDM("acggtgac", "tgac")
