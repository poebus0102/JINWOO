
python = "Python is Amazing"

print(python.lower()) # 소문자로
print(python.upper()) # 대문자로 
print(python[0].isupper()) # 해당 열이 대문자인가?
print(len(python))  #해당 문자는 몇가지인가
print(python.replace("Python", "jave")) # 파이선을 자바로 변경하여 출력하라

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)
print(python.find("n")) # n 을 찾다
print(python.find("java")) # 찾는 값이 없으면 변수 없을시 1 반환 
# print(python. endex("java"))  endex 눈 값이 없으면 오류 발생 뒤에 있는 문자 프린드 안됨

print(python.count("n"))
