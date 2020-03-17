name = 'steve jobs'
print (name.upper())

school = 'SOGANG University'
print (school.lower())

a = 'hello'; b = 'WORLD'
print (a.islower())
print (b.isupper())

y = 'steve jobs made toy story'
print (y.capitalize())
print (y.title())

x = 'I Am Learning Programming'
print (x.istitle())
print (y.istitle())

state = 'mississippi'
print (state.count('s'))
print (state.count('ssi'))
print (state.count('s',5))  #[5:]으로 잘라서 count한 결과
print (state.count('s',1,5))    #[1:5]범위
print (state.find('s'))
print (state.find('i',5))   #[5:]범위에서 'i'를 찾는다

friends = ['alice', 'bob', 'cindy']
dash = '-'
print (dash.join(friends))

lists = 'alice bob cindy david'
print (lists.split())

date = '2020/03/16'
print (date.split('/'))
