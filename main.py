def LCS(x, y, m, n, lookup):
    if m == 0 or n == 0:
        return ['']
    if x[m - 1] == y[n - 1]:
        lcs = LCS(x, y, m - 1, n - 1, lookup)
        for i in range(len(lcs)):
            lcs[i] = lcs[i] + (x[m - 1])
        return lcs
    if lookup[m - 1][n] > lookup[m][n - 1]:
        return LCS(x, y, m - 1, n, lookup)
    if lookup[m][n - 1] > lookup[m - 1][n]:
        return LCS(x, y, m, n - 1, lookup)
    top = LCS(x, y, m - 1, n, lookup)
    left = LCS(x, y, m, n - 1, lookup)
    return top + left


def get_length(x, y, lookup):
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i - 1] == y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])


def find(X, Y):
    lookup = [[0 for x in range(len(Y) + 1)] for y in range(len(X) + 1)]
    get_length(X, Y, lookup)
    lcs = LCS(X, Y, len(X), len(Y), lookup)
    return lcs[0], len(lcs[0])


if __name__ == '__main__':
    X = 'CAGGGTAGTC'
    Y = 'TCATATC'
    print(find(X, Y))  # CATATC

    X = 'CCGCAGTGGA'
    Y = 'ACCATGTGAG'
    print(find(X, Y))  # CCAGTGG

    X = 'CCGCAGTGGAA'
    Y = 'CGTTTGGCGGTCCAGATTGC'
    print(find(X, Y))  # CCGCAGTG

    X = 'CCGCAGTGGAACC'
    Y = 'AACACACCG'
    print(find(X, Y))  # CCACC
