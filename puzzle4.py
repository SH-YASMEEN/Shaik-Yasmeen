def test(n):
    return [n+2*i for i in range(n)]
n=4
print("Number of piles:",n)
print("Number of stones in each pile:",test(n))
