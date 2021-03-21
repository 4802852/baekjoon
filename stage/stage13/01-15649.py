import sys


n, m = map(int, sys.stdin.readline().split())
c = [i for i in range(1, n + 1)]
result = []
for i in range(len(c)):
    cc = c[:]
    mm = m
    ans = []
    ans.append(cc[i])
    cc.remove(cc[i])
    mm -= 1
    if m > 0:
        for j in range(len(cc)):
            ans.append(cc[j])
            cc.remove(cc[j])
            m -= 1
            if m > 0:
                for k in range(len(cc)):
                    ans.append(cc[k])
                    cc.remove(cc[k])
                    m -= 1
                    if m > 0:
                        for l in range(len(cc)):
                            ans.append(cc[l])
                            cc.remove(cc[l])
                            m -= 1
                            if m > 0:
                                for p in range(len(cc)):
                                    ans.append(cc[p])
                                    cc.remove(cc[p])
                                    m -= 1
                                    if m > 0:
                                        for q in range(len(cc)):
                                            ans.append(cc[q])
                                            cc.remove(cc[q])
                                            m -= 1
                                            if m > 0:
                                                for r in range(len(cc)):
                                                    ans.append(cc[r])
                                                    cc.remove(cc[r])
                                                    m -= 1
                                                    if m > 0:
                                                        for s in range(len(cc)):
                                                            ans.append(cc[s])
                                                            cc.remove(cc[s])

