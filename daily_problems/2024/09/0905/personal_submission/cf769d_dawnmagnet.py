import sys
from collections import Counter

input = lambda: sys.stdin.readline().strip()
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
    l = LII()

    m = Counter(l)
    # print(m)
    res = 0
    if k == 0:
        res = 0
        for a, b in m.items():
            res += b * (b - 1) // 2
        print(res)
        return

    avai = [n for n in range(1 << 14) if n.bit_count() == k]
    for a, b in m.items():
        for n in avai:
            c = a ^ n
            if c in m:
                res += b * m[c]
    print(res // 2)


if __name__ == "__main__":
    main()