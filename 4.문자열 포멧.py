#print("a" + "b")
#print("a" , "b")
# 방법1  %
print("나는 %d살입니다."%20) #d 는 정수를 위미함 정수만 넣을수 있음
print("나는 %s를 좋아해요,"%"파이선") #s 는 문자열 문자만 넣을수 있음 
print("Apple은 %c로 시작해요." %"a") #c 는 한가지 캐릭터 한자만 출력됨
# %s
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨강"))

#방법2 {}
print("나는 {}살입니다.".format(20))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨강"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨강"))

#방법4 
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨강"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨강",age = 20))

#방법5 (버전 3.6이상)
age=20
color="빨깅"
print(f"나는{age}"살이며,{color}색을 좋아해요")