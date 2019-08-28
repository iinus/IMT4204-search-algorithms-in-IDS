
# Input: two strings T (length n) and P (length m)
# Output: The locations of all occurences of P in T 
# incidence_matrix(G, nodelist=None, edgelist=None, oriented=False, weight=None) ? 

def BNDM(Text, Pattern):
    print("init...")
    n = len(Text)
    m = len(Pattern)
    r = 26 # alphabet size
# pre-processing: compute incidence matrix B of P 
    B = [[ 0 for i in range(r) ] for j in range(m)]
    s = 1 
    for i in range (0, m-1):
        B[Pattern[i]] = B[Pattern[i]] | s # Assigment by bitwise OR 
        s <<= 1 # bitwise left-shift
    print(B)
# search phase
    j = 0
    while j <= (n-m):
        i = m-1
        last = m
        d = ~0
        while i>=0 and d != 0:
            d = d & B[j+i]
            i = i-1
            if i >= 0:
                last = i + 1
            else:
                print(j)
            d <<= 1
        j += last

if __name__ == "__main__": 
    BNDM("acggtgac", "tgac")
