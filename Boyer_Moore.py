import time
def search(txt, pat):
    a = len(pat)
    b = len(txt)
    Char = charMismatch(pat, a)
    r = 0
    while(r <= b-a):
        j = a-1
        while j >= 0 and pat[j] == txt[r+j]:
            j -= 1
        if j < 0:
            # print("Substring found at =", r)
            r += (a-Char[ord(txt[r+a])] if r+a < b else 1)
        else:
            r += max(1, j-Char[ord(txt[r+j])])

def charMismatch(string, size):
    Characters = [-1]*256
    for i in range(size):
        Characters[ord(string[i])] = i
    return Characters
 
if __name__ == '__main__':
    pat = "string"
    with open("worst_case_brute_force.txt", "r") as file1:
        worst_case_txt = file1.read()
        
    with open("average_case_brute_force.txt", "r") as file2:
        average_case_txt = file2.read()
        
    with open("best_case_all_matches_brute_force.txt", "r") as file3:
        best_case_txt = file3.read()

    start = time.time()
    search(worst_case_txt, pat)
    end = time.time()
    print("Worst:   ", end - start)

    start = time.time()
    search(average_case_txt, pat)
    end = time.time()
    print("Average: ", end - start)

    start = time.time()
    search(best_case_txt, pat)
    end = time.time()
    print("Best:    ", end - start)