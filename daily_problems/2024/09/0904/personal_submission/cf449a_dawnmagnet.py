def deal(n, m, k):
    res = -1

    if k > n + m - 2:
        return -1

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            a = i
            b = n // i

            na = m // max(k - (a - 1) + 1, 1) if a - 1 < k else m
            nb = m // max(k - (b - 1) + 1, 1) if b - 1 < k else m

            # ic(na, b, na * b)
            # ic(nb, a, nb * a)

            res = max(res, max(na * b, nb * a))
    return res


def main():
    n, m, k = MII()
    r = deal(n, m, k)
    r2 = deal(m, n, k)
    print(max(r, r2))


if __name__ == "__main__":
    main()