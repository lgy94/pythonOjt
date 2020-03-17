# 문자열 인덱싱
greeting = 'hello world'
print(greeting[7])
print(greeting[0])

#greeting[0] = 'H'

# 문자열 슬라이싱
lang = 'python programming'
print (lang[3:10])
print (lang[:5])
print (lang[10:])   #10부터 끝까지
print (lang[5:-8])  #양수, 음수 섞어서 사용
print (lang[10:5])
print (lang[-10:-13])
print (lang[2:10:3])
print (lang[:10:3]) #[0:10:3]
print (lang[10::2]) #10부터 끝까지 2칸씩
print (lang[12:3:-2])   #12에서 4까지 2칸식 앞으로
