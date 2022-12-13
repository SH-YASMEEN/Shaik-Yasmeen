def test(list):
    list=[2,7,3,5,3,7,3,1]
    return len(list)==8 and list.count(list[4])==3
print(test(list))