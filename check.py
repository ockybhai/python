list1=[1,2,45,78,98]
list2=[3,6,87,9,12,5]
print("list1:",list1)
print("list2:",list2)
print("length of list1=",len(list1))
print("length of list2=",len(list2))
if len(list1)==len(list2):
    print("length of both are same")
else:
    print("not same")
    print("sum of list1=",sum(list1))
    print("sum of list2=",sum(list2))
if sum(list1)==sum(list2):
    print("sum of two lists are same")
else:
    print("sun of list not same")
check=any(item in list2 for item in list2)
print("any value occur same:",check)

