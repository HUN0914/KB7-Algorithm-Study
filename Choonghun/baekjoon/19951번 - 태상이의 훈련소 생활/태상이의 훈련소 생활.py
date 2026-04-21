import sys
input = sys.stdin.readline

n, m = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]

diff = [arr[0]]
for i in range(1, n): #차분 배열 구현
    diff.append(arr[i]-arr[i-1])
diff.append(0)

for _ in range(m): # 모든 구간을 돌 필요 없이 a랑 b+1에서만 각각 k를 더하고, 빼주면 된다.
    a,b,k = [int(i) for i in input().split()]
    a -= 1
    diff[a] += k
    diff[b] -= k

restore = [diff[0]]
for i in range(1, n): # 차분 배열을 원본으로 복원
    restore.append(restore[i-1]+diff[i])
print(' '.join(map(str,restore)))
