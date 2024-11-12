
import time

import random
from sys import stdin
from itertools import combinations as comb


def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

primes = sieve(1000)
prime_set = set(primes)

def generate_graph(n):
    if n < 5:
        return -1
    
    edges = []
    for i in range(1, n + 1):
        edges.append((i, (i % n) + 1))
    
    m = n
    
    if m not in prime_set:
        edges.append((1, 3))
        m += 1
    
    if m in prime_set:
        return m, edges
    else:
        return -1

T = int(input().strip())
results = []
s = time.time()  # 시작 시간 기록

for _ in range(T):
    n = int(input().strip())
    result = generate_graph(n)
    if result == -1:
        results.append("-1")
    else:
        m, edges = result
        results.append(f"{m}")
        results.extend(f"{u} {v}" for u, v in edges)

print("\n".join(results))


e = time.time()  # 종료 시간 기록`
print("실행시간: ",round(e-s,3),'s', sep='')