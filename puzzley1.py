def test(list):
    list=[2,19,7,7,4,1,19,5,4,5,5,2]
    return list.count(19)==2 and list.count(5)>=3
print(test(list))