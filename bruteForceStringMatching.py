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
    print("# Matches:", len(match), "\n")
    print("Time: ", end - start)

#############################################################################################################################

if __name__ == '__main__':
    print("[0] Shakespear\n[1] Bee Movie\n[2] The Lottery")
    type = input("Which dataset would you like to run? \nEnter an Int: ")
    match type:
        case '0':
            print("\n*** running on shakespear dataset, Length = 5458199 ***")
            print("Long Text Datasets: ")
            file = open("Shakespear.txt", "r+")
            print("Shakespear")
            T = file.read()
            P = input("Enter a string: ")
            call(T, P)
        case '1':
            print("\n*** running bee movie script, Length = 86091 ***")
            file = open("Bee_movie.txt", "r+")
            print("Bee Movie")
            T = file.read()
            P = input("Enter a string: ")
            call(T, P)
        case '2':
            print("\n*** running on The Lottery dataset, Length = 86091 ***")
            file = open("The Lottery.txt", "r+", encoding="utf-8")
            print("The Lottery")
            T = file.read()
            P = input("Enter a string: ")
            call(T, P)
        case _:
            print("\n*** running default test cases ***")
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