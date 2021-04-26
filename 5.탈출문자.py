# /n : 줄바꿈 역슬러시n 
print("백문이 불여일견\n백견이 불여일타")
# 저는 "나도코딩"입니다.
# \   문장 \  따옴표 출력 그대로
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print('저는 \"나도코딩"입니다.')
print('저는 \'나도코딩\'입니다.')
print("저는 \"나도코딩\"입니다.")

# \\ : 문장 내에서 \가 한개이면 문장이랑 합쳐짐 두먼 너어야함
#print("c\users\nadocoding\desktop") 경로 출력 안됨
print("c\\users\\nadocoding\\desktop")

# \r : 커서를 맨앞으로 이동하여 남음 값 실행 
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("REdd\bapple") # 앞에 한글 자 삭제 됨 

# quiz 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오 

# 예 )j http://naver.com
# 규칙 1 : http: // 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점 (.) 이후 부분은 제외 => naver 
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자내 'e'갯수 + "!" fh rntjd 
#       (nav)                    (5)            (1)                 (!)
# 예) 생선된 비밀번호 : nav51!

url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙1 
#print(my_str)
my_str = (my_str[:my_str.index(".")]) # 규칙2
#print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password)) 


