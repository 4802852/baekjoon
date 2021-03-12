n = str(input())
cycle = 0
if int(n) < 10:
    n = '0' + n
m = n
while 1:
    m_new = 0
    for i in range(len(m)):
        m_new += int(m[i])
    m = m[-1] + str(m_new)[-1]
    cycle += 1
    if n == m:
        break

print(cycle)