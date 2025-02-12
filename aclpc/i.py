from atcoder.string import suffix_array, lcp_array

S = input()

sa = suffix_array(S)
la = lcp_array(S, sa)

ans = len(S) * (len(S) + 1) // 2
ans -= sum(la)

print(ans)
