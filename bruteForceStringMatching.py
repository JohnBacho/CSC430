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
    start = time.process_time()
    match = BruteForceStringMatch(T, P)
    end = time.process_time()  # Measure CPU time
    print("Matches:", match, "\n")
    print("# Matches:", len(match), "\n")
    print("CPU Time: ", end - start)

#############################################################################################################################

if __name__ == '__main__':
    print("[0] best_case\n[1] average_case\n[2] worst_case")
    type = input("Which dataset would you like to run? \nEnter an Int: ")
    match type:
        case '0':
            print("\n*** running on best case dataset ***")
            file = open("The Lottery.txt", "r+")
            print("The Lottery: P = string")
            T = file.read()
            P = "the"
            call(T, P)
        case '1':
            print("\n*** running average case dataset ***")
            file = open("Bee_movie.txt", "r+")
            print("Bee movie: P = string")
            T = file.read()
            P = "the"
            call(T, P)
        case '2':
            print("\n*** running on worst case dataset ***")
            file = open("Shakespear.txt", "r+", encoding="utf-8")
            print("Shakespear: P = string")
            T = file.read()
            P = "the"
            call(T, P)
        case _:
            print("\n*** running default test cases ***")
            T = "stringstrindstrindstrindstrind"
            P = "string"
            print("Match at Front: P = string")
            call(T, P)

            T = "strindstrindstrindstrindstring"
            P = "string"
            print("Match at End: P = string")
            call(T, P)

            T = "strindstrindstringstrindstrind"
            P = "string"
            print("Match in Middle: P = string")
            call(T, P)

            T = "stringstringstringstringstring"
            P = "string"
            print("Lots of Matches: P = string")
            call(T, P)

            T = "strindstrindstrindstrindstrind"
            P = "string"
            print("No Matches: P = string")
            call(T, P)    