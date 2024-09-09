import sys

input = lambda: sys.stdin.readline().strip()
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LFI = lambda: list(map(float, input().split()))
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))

try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa


def main():
    s = input()
    cur = 0
    ans = 0
    fcnt = 0
    for id, ch in enumerate(s):
        if ch == "F":
            if id != fcnt:
                ans = max(ans, cur + id - fcnt)
                ic(ans, cur, id, fcnt)
                cur += 1
            fcnt += 1
        else:
            cur -= 1
            cur = max(cur, 0)
    print(ans)


if __name__ == "__main__":
    main()