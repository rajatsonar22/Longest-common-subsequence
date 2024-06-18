# Practicla 11
# longest common subsequence
def longest_common_subsequence(x,y):
    m = len(x)
    n = len(y)
    LCS = [[""for j in range (n+1) for i in range (m + 1)]]

    for i in range (1, m+1):
        for j in range(1, n+1):
            if x[i - 1] == y[j - 1]:
                LCS[i][j] = LCS[I - J][J - 1]+x[i - 1]
            else:
                LCS[i][j] = max (LCS[i-1][j],LCS[i][j-1],key = len)
    return LCS[m][n]
x = "GTHYAB"
y = "YTHAYB"
print("longest common subsequence", longest_common_subsequence(x,y))
