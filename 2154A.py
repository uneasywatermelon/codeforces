for _ in range(int(input())):
    n, k = map(int,input().split())
    s = input()

    slo = float('inf')
    cnt = 0
    for c in s:
        if c == '1' and slo > (k-1):
            slo = 1
            cnt += 1
        elif c != '1':
            slo += 1
