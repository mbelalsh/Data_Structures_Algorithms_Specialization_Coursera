# python3
import random
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def hash_func(s, prime_no, x):
    z = 0
    for st in reversed(s):
        z = (z * x + ord(st)) % prime_no
    return z

def precomputation_hashes(text, pattern_len, prime_no, x):
    H = [0] * (len(text) - pattern_len + 1)
    s = text[-pattern_len:]
    H[len(text)-pattern_len] = hash_func(s, prime_no, x)
    y = 1
    for i in range(1, pattern_len+1):
        y = (y * x) % prime_no
    for i in reversed(range(len(text) - pattern_len)):
        #print(i)
        precomp_hash = x * H[i + 1] + ord(text[i]) - y * ord(text[i + pattern_len])
        while(precomp_hash < 0):
            precomp_hash += prime_no
        H[i] = precomp_hash % prime_no
    #print(H)
    return H

def get_occurrences(pattern, text):
    prime_no = 1000000007
    x = random.randint(1, prime_no)
    text_len = len(text)
    pattern_len = len(pattern)
    pat_hash = hash_func(pattern, prime_no, x)
    #print(phash)
    H = precomputation_hashes(text, pattern_len, prime_no, x)
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if pat_hash == H[i] and text[i:i + len(pattern)] == pattern
    ]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))