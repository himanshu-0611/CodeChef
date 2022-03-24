# https://www.codechef.com/START31D/problems/UNCHANGEDOR

def pow2(bits):
    return 1 << bits
    
def max_num(bits):
    return pow2(bits + 1) - 1
    
def solution():
    N = int(input())
    
    bit_count = 0
    while N >> bit_count:
        bit_count += 1
        
    ans = 0
    for i in range(1, bit_count):
        ans += min(N, max_num(i)) - pow2(i)
        
    print(ans)
    
T = int(input())
while(T > 0):
    T -= 1
    solution()