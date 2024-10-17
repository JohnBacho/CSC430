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

    # Length of Shakespear 5458199
    file1 = open("Shakespear.txt", "r+")
    txt = file1.read()
    pat = input("Enter a string: ")
    start = time.time()
    search(txt, pat)
    end = time.time()
    print("Shake Spear: ",end - start)

    # Length of bee movie 86091
    file2 = open("Bee_movie.txt", "r+")
    txt = file2.read()
    start = time.time()
    search(txt, pat)
    end = time.time()
    print("Bee moive: ",end - start)

    # length of the Lottery 20049
    file3 = open("The Lottery.txt", "r+", encoding="utf-8")
    txt = file3.read()
    start = time.time()
    search(txt, pat)
    end = time.time()
    print("The Lottery: ",end - start)