# 정수 자료형과 연산
x = 100
y = 200
print (x,y)
print (id(x))
print (id(y))

# 정수 객체는 immutable(객체를 수정할 수 없음)
a = 10
print (id(a))
a = 20
print (id(a))
print (a)

# 정수 자료형은 크기 제한이 없다
print (2**1024)

# 할당 연산자와 산술 연산자
a = 10
b = 20
c = a + b
a = a + 50
b = b + a
print (a, b, c)
