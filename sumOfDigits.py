def digit_sum(n, s=0):
    l = str(n)
    for x in l:
        s += int(x)
    return s
    