'''#문제1
kor = int(input('국어 성적을 입력하시오 : '))
math = int(input('수학 성적을 입력하시오 : '))
eng = int(input('영어 성적을 입력하시오 : '))
print()
print('입력받은 성적')
print('-'*15)
print('국어 성적 : ', kor)
print('수학 성적 : ', math)
print('영어 성적 : ', eng)

total = kor+math+eng
avg = total/3

print('총점 : ', total)
print('평균 : %.2f' % (avg))

#문제2

radius = input('반지름을 입력하시오 : ')
radius = int(radius)
radius = int(input('반지름을 입력하시오 : '))

print('반지름 : ', radius)

area = 3.141592 * pow(radius, 2)
perimeter = 2 * 3.141592 * radius

print('원의 넓이 : %7.3f' % area)
print('원의 둘레 : %.3f' % perimeter)'''


#문제3
n = int(input('다섯 자리 정수를 입력하시오 : '))
n10000 = n // 10000
n = n % 10000

n1000 = n // 1000
n = n % 1000

n100 = n // 100
n = n % 100

n10 = n // 10
n1 = n % 10

print(n10000, ',', n1000, ',', n100, ',', n10, ',', n1)
print('프로그램을 끝내려면 엔터를 누리시오')
input()
