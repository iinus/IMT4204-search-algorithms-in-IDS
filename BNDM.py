
# Input: two strings T (length n) and P (length m)
# Output: The locations of all occurences of P in T 
# incidence_matrix(G, nodelist=None, edgelist=None, oriented=False, weight=None) ? 

def BNDM(Text, Pattern):
    print("pre-processing...")
    print("Text: " + Text + " Pattern: " + Pattern)
    n = len(Text)
    m = len(Pattern)
    r = 26 # alphabet size
# pre-processing: compute incidence matrix B of P 
    B = [[ 0 for i in range(r) ] for j in range(m)]
    B = {(rx, cx): c for rx, r in enumerate(B)\
                for cx, c in enumerate(r)}
    s = 0x1 
    q = int(format(0, '0'+str(m)))
    for i in range (0, m):
        key_exists = 0x1
        if Pattern[i] in B: 
            key_exists = 0x0 
        B[Pattern[i]] = s | key_exists
        s <<= 1
        #q = int(format(0, '0'+ str(m)))   
    print(B)

# search phase
    print("searching...")
    i = m
    while i <= n:
        j = -1
        last = 0
        d = ~0
        D = 1 ^ m
        W=Text[i - m]
        while D != 0 ^ m:
            j = j + 1
            D = D & B[W]
            if D == 0^m:
                break
            if j == m:
                print("Occurence of T: " + Pattern[i-m] + " at pos " + str(i-m))
                break
            if j < m:
                last = j
            D = D << 1
        i = i + (m - last)

if __name__ == "__main__": 
    BNDM("acggtgac", "tgac")
