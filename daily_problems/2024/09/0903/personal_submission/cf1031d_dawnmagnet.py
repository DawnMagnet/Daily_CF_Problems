import sys

try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa

input = lambda: str(sys.stdin.readline().strip())
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LFI = lambda: list(map(float, input().split()))
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))


def main():
    n, k = MII()
    s = [I() for _ in range(n)]
    ic(s)

    dp = [[1e9] * n for _ in range(n)]
    dp[0][0] = int(s[0][0] != "a")

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + int(s[i][j] != "a"))
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + int(s[i][j] != "a"))
    ic(dp)

    points = []
    res = ""

    for xr in range(2 * n - 2, -1, -1):
        for i in range(n):
            j = xr - i
            if j >= 0 and j < n:
                if dp[i][j] <= k:
                    points.append((i, j))
        if len(points):
            res = "a" * (xr + 1)
            break
    ic(points)
    nxt_points = []
    for i, j in points:
        if j + 1 < n and (len(nxt_points) == 0 or (i, j + 1) != nxt_points[-1]):
            nxt_points.append((i, j + 1))
        if i + 1 < n:
            nxt_points.append((i + 1, j))
    points = nxt_points

    if k == 0:
        res = ""
        points = [(0, 0)]

    while len(points):
        min_ch = min([s[i][j] for i, j in points])
        ic(points)
        ic(min_ch, k, res)
        nxt_points = []
        res += min_ch
        for i, j in points:
            if s[i][j] == min_ch:
                if j + 1 < n and (len(nxt_points) == 0 or (i, j + 1) != nxt_points[-1]):
                    nxt_points.append((i, j + 1))
                if i + 1 < n:
                    nxt_points.append((i + 1, j))
        points = nxt_points
    print(res)


if __name__ == "__main__":
    main()
