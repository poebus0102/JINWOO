#문자열
sentence = "나는 소년입니다"
print(sentence)
sentence2 = "파이선은 쉬워요"
sentence3 = """
나는소년입니다
파이선은 쉬워요
""" 
#""" = 띄어쓰기?
print(sentence2)
print(sentence3)

jumin = "820202-1187517"
print("성별 : " + jumin[7]) #0부터 시작하면 7곱번째 수 가자오고
print("연 :" + jumin[0:2]) # 0~2까지 값
print("월 :" + jumin[2:4])
print("일 ;" + jumin[4:6])
print("생년월일 :" + jumin[0:6])
print("뒤 7자리 :" + jumin[7:])
print("뒤 7자리(뒤에서부터):" + jumin[-7:])
# [-:] 마이너스는 뒤에서 부터

python = "Python is Amazing"

print(python.lower()) # 소문자로
print(python.upper()) # 대문자로 
print(python[0].isupper()) # 해당 열이 대문자인가?
print(len(python))
print(python.replace("Python", "jave"))
print(python.replace(p))