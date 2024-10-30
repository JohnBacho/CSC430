import time
d = 256

def RabinKarpSearch(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1
 
    # The value of h would be "pow(d, M-1)%q"
    for i in range(M-1):
        h = (h*d) % q
 
    # Calculate the hash value of pattern and first window of text
    for i in range(M):
        p = (d*p + ord(pat[i])) % q
        t = (d*t + ord(txt[i])) % q
 
    # Slide the pattern over text one by one
    for i in range(N-M+1):
        if p == t:
            # Check for characters one by one
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
                else:
                    j += 1
 
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j == M:
                print("Pattern found at index " + str(i))
 
        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q
 
            # We might get negative values of t, converting it to positive
            if t < 0:
                t = t + q
 
if __name__ == '__main__':
    with open("worst_case_brute_force.txt", "r") as file1:
        worst_case_txt = file1.read()
    with open("average_case_brute_force.txt", "r") as file2:
        average_case_txt = file2.read()
    with open("best_case_all_matches_brute_force.txt", "r") as file3:
        best_case_txt = file3.read()
    
    pat = "string"
 
    # A prime number
    q = 101
 
    # Function Call for worst case
    start1 = time.time()
    RabinKarpSearch(pat, worst_case_txt, q)
    end1 = time.time()
    print("Worst case:")
    print("Total time elapsed: ", end1 - start1)

    # Function Call for average case
    start2 = time.time()
    RabinKarpSearch(pat, average_case_txt, q)
    end2 = time.time()
    print("Average case:")
    print("Total time elapsed: ", end2 - start2)

    # Function Call for best case
    start3 = time.time()
    RabinKarpSearch(pat, best_case_txt, q)
    end3 = time.time()
    print("Best case:")
    print("Total time elapsed: ", end3 - start3)