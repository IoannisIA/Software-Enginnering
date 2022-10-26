def minDrives(total, used):
    total , used = zip(*sorted(zip(total, used), reverse=True))
    total = list(total)
    used = list(used)
    n = len(total)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(n-1):
        step = 1
        while total[i] != used[i]:
            space = total[i] - used[i]
            if used[i+step] >= space:
                used[i+step] -= space
                used[i] += space
            elif used[i+step] < space:
                used[i] += used[i+step]
                used[i+step] = 0
            if used[i+step] == 0 :
                step += 1
            if (i+step) == n:
                break
    return n - used.count(0)

used =  [331,242,384,366,428,114,145,89,381,170,329,190,482,246,2,38,220,290,402,385]
total = [992,509,997,946,976,873,771,565,693,714,755,878,897,789,969,727,765,521,961,906]
print("Number of drives required :", minDrives(total, used))
