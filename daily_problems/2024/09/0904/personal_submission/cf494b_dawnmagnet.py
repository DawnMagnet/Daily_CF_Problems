
def main():
    a = I()
    b = I()
    z = f"{b}#{a}"
    # print(z)

    n = len(z)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and z[i] != z[j]:
            j = pi[j - 1]
        if z[i] == z[j]:
            j += 1
        pi[i] = j

    n = len(a)
    dp = [0] * n
    res = 0
    acc = 1
    cur = 1
    pre = -1
    # print(pi[len(b) + 1 :])
    for i in range(n):
        if pi[i + len(b) + 1] == len(b):
            pre = i
            dp[i] = cur
        else:
            if pre != -1:
                dp[i] = dp[pre]
        res += dp[i]
        res %= MOD
        if i >= len(b) - 1:
            # print(acc, cur, dp, i, len(b))

            acc += dp[i - len(b) + 1]
            acc %= MOD
            cur += acc
            cur %= MOD
            # print(acc, cur)

    # print(dp)
    print(res)


if __name__ == "__main__":
    main()