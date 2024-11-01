import time
def bad_symbol_table(pattern):
    table = {}
    m = len(pattern)
    for i in range(m):
        table[pattern[i]] = i
    for c in range(256):
        char = chr(c)
        if char not in table:
            table[char] = -1
    return table

def good_suffix_table(pattern):
    m = len(pattern)
    table = [0] * m
    last_prefix_index = m

    for j in range(m - 1, -1, -1):
        if is_prefix(pattern, j + 1):
            last_prefix_index = j + 1
        table[m - 1 - j] = last_prefix_index - j + (m - 1 - j)

    for j in range(m - 1):
        length = suffix_length(pattern, j)
        table[length] = m - 1 - j + length

    return table

def is_prefix(pattern, p):
    m = len(pattern)
    for i in range(p, m):
        if pattern[i] != pattern[i - p]:
            return False
    return True

def suffix_length(pattern, p):
    length = 0
    m = len(pattern)
    for i in range(m - 1, p, -1):
        if pattern[i] == pattern[m - 1 - length]:
            length += 1
        else:
            break
    return length

def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    
    bad_symbol = bad_symbol_table(pattern)
    good_suffix = good_suffix_table(pattern)
    
    s = 0
    while s <= n - m:
        j = m - 1 
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        if j < 0:
            print(f"Pattern found at index {s}")
            s += good_suffix[0]  
        else:
            # Compute the shifts
            bad_symbol_shift = j - bad_symbol.get(text[s + j], -1)
            good_suffix_shift = good_suffix[j]
            s += max(bad_symbol_shift, good_suffix_shift)

if __name__ == '__main__':
    with open("worst_case_brute_force.txt", "r") as file1:
        worst_case_txt = file1.read()
        
    with open("average_case_brute_force.txt", "r") as file2:
        average_case_txt = file2.read()
        
    with open("best_case_all_matches_brute_force.txt", "r") as file3:
        best_case_txt = file3.read()

    pat_worst = "string"
    
    start = time.time()
    worst_matches = boyer_moore_search(worst_case_txt, pat_worst)
    end = time.time()
    print("Worst case time:   ", end - start)
    print("Matches in worst case:", worst_matches)

    pat_average = "string"
    start = time.time()
    average_matches = boyer_moore_search(average_case_txt, pat_average)
    end = time.time()
    print("Average case time: ", end - start)
    print("Matches in average case:", average_matches)

    start = time.time()
    best_matches = boyer_moore_search(best_case_txt, pat_average)
    end = time.time()
    print("Best case time:    ", end - start)
    print("Matches in best case:", best_matches)
