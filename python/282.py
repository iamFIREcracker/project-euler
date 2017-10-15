def A(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return A, (m - 1, 1)
    elif m > 0 and n > 0:
        v = A(m, n - 1)
        return A, (m - 1, v)

def trampoline(func, args):
    while True:
        print func, args:
        res = func(*args)
        if len(res) == 1:
            return res
        func, args = res

print trampoline(A, (3, 3))
