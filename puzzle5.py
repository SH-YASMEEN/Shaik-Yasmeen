def test(str):
    return str[len(str)-2] in str[len(str)-1]
str=["a","abb","sfs","oo","de","sfde"]
print(test(str))