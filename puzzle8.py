def test(s):
    import re
    merged=re.split(r"([ ,]+)", s)
    return[merged[::2], merged[1::2]]
s=str(input("Enter the string:"))
print(s)
print(test(s))