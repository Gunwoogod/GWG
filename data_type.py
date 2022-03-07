#자료의 형식 확인
print(type("Hello"))
print(type(13))
print()

#따옴표 사용
print("Hello")
print('Hello')
print()
print('said "Hello"')
print("think that 'I am hungry'")
print()

#이스케이프 문자 사용
print("said \"Hello\"")
print('think that \'I am hungry\'')
print()
print("Hello\nmy friend")
print("Hello\tmy friend")
print()
print("\\ \\ \\ \\")
print()

#문자열 연산자

#연결 연산자
print("Hello" + "my friend")
print("Hello" + "!")
print()

#반복 연산자
print("Hello" * 3)
print(3 * "Hello")
print()

#선택 연산자(인덱싱)  [] 기호를 이용하여 특정 위치의 문자 참조
print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])
print()

#거꾸로 출력
print("Hello"[-1])
print("Hello"[-2])
print("Hello"[-3])
print("Hello"[-4])
print("Hello"[-5])
print()

#선택 연산자(슬라이싱)   [:] 기호를 이용하여 문자열의 일부를 추출
print("Hello"[1:4])
print("Hello"[0:2])
print("Hello"[1:3])
print("Hello"[2:4])
print("Hello"[1:])
print("Hello"[:3])
print()

HI = "Hello"
print(HI[0:2])
print()
#IndexError
#print("Hello"[10])   문자열의 수를 넘는 요소/글자를 선택할 때 발생

#문자열의 길이 구하기
print(len("Hello"))
print()


