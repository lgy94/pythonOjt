# 복소수 표현하기(허수부에 j or J를 붙인다)
x = 2+5j
y = 3.2+2.5J
z = x+y
print(z)
print(type(z))

x=5+10j
print(x.real)   #실수부
print(x.imag)   #허수부
print(x.conjugate())    #켤레복소수 반환
