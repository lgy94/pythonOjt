'''x=100; y=200
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)
print(x==y)
print(x!=y)'''

'''a=10; b=20
print(a>5 and b>10)
print(a>5 and b<5)
print(a<5 and b>10)
print(a<5 and b<5)
print(0<a<b)'''

'''a=10; b=20
print(a>5 or b>10)
print(a>5 or b<5)
print(a<5 or b>10)
print(a<5 or b<5)
print(not a<5)
print(not b>10)'''

#if 조건문
'''score = int(input('성적을 입력하시오 : '))
if score >= 70 :
    print('축하합니다.')
print('수고하셨습니다.')'''

'''number = int(input('정수를 입력하시오 : '))
if number%2==0 :
    print(number,'는 짝수입니다.')
else :
    print(number,'는 홀수립니다.')
print('프로그램 종료')'''

'''a=int(input('Enter a : '))
b=int(input('Enter b : '))

if a>b : max = a
else : max = b
print (max)'''

'''score = int(input('성적을 입력하시오 : '))

if score >= 90 :
    grade = 'A'
elif 80 <= score < 90 : # elif 80 <= score:
    grade = 'B'
elif 70 <= score < 80 : # elif 70 <= score:
    grade = 'C'
else :
    grade = 'D'
print('당신의 학점은',grade,'입니다.')'''

score = int(input('성적을 입력하시오 : '))

if score >= 70 :
    print('통과하셨습니다.')
    if score >= 90 :
        print('A장학금 대상자')
    elif score >= 80 :
        print('B장학금 지급 대상자')
elif score >= 60 :
    print('조건부 통과')
else :
    print('재수강')

print('수고하셨습니다.')
