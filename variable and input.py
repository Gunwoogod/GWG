#변수 만들기 / 사용하기
pi = 3.14159265             #변수 선언 및 할당  (C,C++,JAVA,C# 등에서는 기본적으로 변수의 자료형도 선언해준다.)
print(pi)                   #변수 참조
print()

#변수를 이용한 연산
print(pi+2)
print()
print(pi-2)
print()
print(pi*2)
print()
print(pi/2)
print()
print(pi//2)
print()
print(pi%2)
print()
print(pi*pi)
print()

#원의 둘레와 넓이 구하기
pi = 3.14159265  
r = 3

print("원의둘레 =",2*pi*r)
print("원의넓이 =", pi*r*r)
print()

#복합 대입 연산자
number = 100
number += 10
number += 20
number += 30
print("number :" , number)
print()

#문자열 복합 대입 연산자
string = "Hello"
string += "!"
string += "!"
print("string :", string)
print()

#사용자 입력 (input())
string = input("인사말을 입력하세요>>")
print(string)
print(type(string))         # 자료형 확인
print()

#문자열을 숫자로 바꾸기
string_a = input("입력A>>")
string_b = input("입력B>>")
int_a = input(string_a)
int_b = input(string_b)

print("문자열 자료 : ", string_a + string_b)            #문자열이기 때문에 문자열을 연결한대로 출력
print("숫자 자료 : ", int_a + int_b)                    #숫자이기 때문에 숫자의 합으로 출력
print()

#숫자를 문자열로 바꾸기
output_a = str(52)
output_b = str(52.273)

print(type(output_a), output_a)
print(type(output_b), output_b)
print(output_a + output_b)                             #언뜻보면 숫자같지만 문자열이기 때문에 문자열 연결로 출력
print()
