from itertools import zip_longest
import time

def BruteForceStringMatch(T, P):
    n = len(T)
    m = len(P)
    result = []
    for i in range(n-m+1):
        j = 0
        while j<m and P[j]==T[i+j]:         # Checks the pair of chars for matches for the length of P
            j+=1                            # Iterates j for each consecutive match
        if j==m:                            # If j is the length of the Pattern they match
            result.append(i)                # Adds the starting index if a pattern is found to result
    return result

def call(T, P):
    start = time.time()
    match = BruteForceStringMatch(T, P)
    end = time.time()

    print("Matches:", match, "\n")
    print("Time: ", end - start)

#############################################################################################################################

if __name__ == '__main__':
    T = "stringstrindstrindstrindstrind"
    P = "string"
    print("Match at Front")
    call(T, P)

    T = "strindstrindstrindstrindstring"
    P = "string"
    print("Match at End")
    call(T, P)

    T = "strindstrindstringstrindstrind"
    P = "string"
    print("Match in Middle")
    call(T, P)

    T = "stringstringstringstringstring"
    P = "string"
    print("Lots of Matches")
    call(T, P)

    T = "strindstrindstrindstrindstrind"
    P = "string"
    print("No Matches")
    call(T, P)

    print("Long Text Datasets: ")
    # Length of Shakespear 5458199
    file1 = open("Shakespear.txt", "r+")
    T = file1.read()
    P = input("Enter a string: ")
    print("Shake Spear")
    call(T, P)

    # Length of bee movie 86091
    file1 = open("Bee_movie.txt", "r+")
    T = file1.read()
    P = input("Enter a string: ")
    print("Bee Movie")
    call(T, P)

    # Length of bee movie 86091
    file1 = open("Bee_movie.txt", "r+")
    T = file1.read()
    P = input("Enter a string: ")
    print("Bee Movie")
    call(T, P)

    # Length of bee movie 86091
    file3 = open("The Lottery.txt", "r+", encoding="utf-8")
    T = file1.read()
    P = input("Enter a string: ")
    print("The Lottery")
    call(T, P)