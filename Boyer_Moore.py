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

    file1 = open("worst_case_brute_force.txt", "r+")
    txt = file1.read()
    pat = "string"
    start = time.time()
    search(txt, pat)
    end = time.time()
    print("Worst:   ",end - start)

    file2 = open("average_case_brute_force.txt", "r+")
    txt = file2.read()
    start2 = time.time()
    search(txt, pat)
    end2 = time.time()
    print("Average: ",end2 - start2)

    file3 = open("best_case_all_matches_brute_force.txt", "r+")
    txt = file3.read()
    start = time.time()
    search(txt, pat)
    end = time.time()
    print("Best:    ",end - start)