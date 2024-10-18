"""Fibo Prove"""
MEMO = {0:0, 1:1}
def fibo(n):
    """Fibonacci MEMO Recursive"""
    if n in MEMO:
        return MEMO[n]
    call = fibo(n-1) + fibo(n-2)
    MEMO[n] = call
    return call
def loop_(n, now=0):
    """MEMO Using Another Function"""
    if now < n:
        fibo(now+950)
        loop_(n, now+950)
def fibo_main(n):
    """Fibonacci Main Function"""
    loop_(n)
    return fibo(n)
print(fibo_main(int(input())))
