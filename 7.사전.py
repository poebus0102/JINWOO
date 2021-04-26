cabinet = {3:"유재석",100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))

#pritn(cabinet).[5])# 값이 없는경우 오류 발생됨 
print("hi")
print(cabinet.get(5))
print("hi")
print(cabinet.get(5,"값이없음"))
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False\

cabinet = {"A-3":"유재석","B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet ["B-100"])

# 새로운 손님 

print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["c-20"] = "조세호"
print(cabinet)

# 간 손님 

del cabinet["A-3"]
print(cabinet)
 
 # key 들만 출력

print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# keym value 둘다 출력 
print(cabinet.items())

# 목욕탕 폐점 
cabinet.clear()
print(cabinet)