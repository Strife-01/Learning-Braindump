# Xn+1 = (Xn)^2 - Xn + 1
# X1 = 2

# lim(n -> inf) (X1 * X2 ...)/ Xn+1
k = 0
def memo_cache(f):
    cache = {}
    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return inner

@memo_cache
def recurrence(n):
    global k 
    k += 1
    if n == 1:
        return 2
    return recurrence(n - 1) ** 2 - recurrence(n - 1) + 1

p = 1
for i in range(1, 14):
    p *= recurrence(i)

print(p / recurrence(14))
print(k)
