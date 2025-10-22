for _ in range(int(input())):
    n, k = map(int,input().split())
    s = input()
    
    distances = []

    # get list of distances


    cnt = 0
    if distances:
        for x in distances:
            cnt += 1 if x >= (k-1) else 0
        cnt += 1

    print(cnt)
