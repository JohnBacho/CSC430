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
 
        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q
 
            # We might get negative values of t, converting it to positive
            if t < 0:
                t = t + q
 
if __name__ == '__main__':
    with open("Shakespear.txt", "r") as file1:
        shakespear = file1.read()
    with open("titanic.txt", "r") as file2:
        titanic = file2.read()
    with open("The Lottery.txt", "r") as file3:
        lottery = file3.read()
    
    pat = "the"
 
    # A prime number
    q = 101
 
    # Function Call for worst case
    start1 = time.process_time()  # Measure CPU time
    RabinKarpSearch(pat, shakespear, q)
    end1 = time.process_time()  # Measure CPU time
    print("Shakespear:")
    print("CPU Time: ", end1 - start1)  # Display CPU time used

    # Function Call for average case
    start2 = time.process_time()  # Measure CPU time
    RabinKarpSearch(pat, titanic, q)
    end2 = time.process_time()  # Measure CPU time
    print("Titanic:")
    print("CPU Time: ", end2 - start2)  # Display CPU time used

    # Function Call for best case
    start3 = time.process_time()  # Measure CPU time
    RabinKarpSearch(pat, lottery, q)
    end3 = time.process_time()  # Measure CPU time
    print("The Lottery:")
    print("CPU Time: ", end3 - start3)  # Display CPU time used