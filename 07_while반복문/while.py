'''a=1
while a <= 5 :
    print(a)
    a += 1'''

'''a=1
sum=0
while a <= 10 :
    sum += a
    a += 1
    print('sum:',sum)

print(sum(range(11)))'''

'''a=2
sum=0
while a<=10:
    sum+=a
    a+=2
print('sum:',sum)'''

'''a=1
sum=0
while a<=10 :
    if a%2==0 :
        sum +=a
    a+=1
print('sum:',sum)'''

'''a=1
while a<=10:
    print('a=',a)
    if a>=5:
        break
    a+=1
print('after while')'''

'''a=1
while True :
    print(a)
    if a==5 : break
    a+=1'''

'''a=0
while a<=10 :
    a+=1
    if a%3==0 :
        continue
    print('a=',a)
print('after while')'''

'''dan=2
while dan<=9 :
    n=1
    while n<=10 :
        value=dan*n
        print('%3d'%(value),end='')
        n+=1
    print()
    dan+=1'''

#문제1
'''working_hour = int(input('근무 시간을 입력하시오 : '))
pay_hour = int(input('시간당 수당을 입력하시오 : '))

total = working_hour * pay_hour

if working_hour > 12 :
    add_pay = (working_hour-12) * pay_hour * 0.3
    total += add_pay

print('총 급여는', total,'원입니다.')'''

#문제2
'''n = int(input('정수를 입력하시오 : '))
a = 1
count = 0

while a<=n:
    if n%a==0:
        print(a)
        count+=1
    a+=1

print(n,'의 약수의 개수 :', count)'''

#문제3
n = int(input('정수를 입력하시오 : '))
max = n

loop_count = 1
while loop_count <= 4 :
    n = int(input('정수를 입력하시오 : '))
    if n > max:
        max = n
    loop_count += 1

print('가장 큰 값 : ',max)
