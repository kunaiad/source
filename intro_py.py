'''
print(5+9+3)

print(100-7)



print(9//5)


a=95
temp = a - 3
a =temp
print(a)


a = 95
a -= 3
print(a)

a *= 2
print(a)

a = 200
a /= 3
print(a)

a = 13
a//=4
print(a)


print(2+3*4)
print(0b10)

print(int(True))
print(int(False))

print(4+7.0)

googol = 10**100
print(googol)


print('\tabc')
print('a\tabc')

'''

# 3.2 리스트

# 리스트는 0 혹은 그 이상의 요소로 만들어진다 .
# 콤마(,)로 구분하고 대괄호 ([]) 로 둘러 싸여있다.

empty_list = []
weekdays = ['Monday']
big_birds = ['emu','ostrich','cassowary']


#또한 list()함수로 빈 리스트를 할당할수 있다.

another_empty_list = list()
another_empty_list

# 3.2.2 다른 데이터 타입을 리스트로 변환하기 :  ist()
# a='cat'
# print(type(a))
# a=list(a)
# print(list(a))
# print(type(a))

# 튜플 -> 리스트

a_tuple = ('ready','fire','aim')
print(a_tuple)
print(type(a_tuple))

print(type(list(a_tuple)))
print(type(a_tuple))


birthday = '1/6/1952'
print(birthday.split('/'))


# 3.2.3 [offset] 으로 항목 얻기
# 문자열과 마찬가지로 리스트는 오프셋으로 하나의 특정 값을 추출할 수 있다.

marxes = ['Groucho','Chico','Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])

print(marxes[-1])
print(marxes[-2])
print(marxes[-3])

# 리스트 오프셋은 값을 할당한 위치에 맞게 입력되어야 한다.
# 오프셋의 위치가 리스트의 범위를 벗어날 경우 에러가 난다.

# print(marxes[-4])
#     print(marxes[-4])
# IndexError: list index out of range




#3.2.4 리스트의 리스트

# 리스트는 다음과 같이 리스트 뿐만 아니라 다른 타입 요소도 포함 될 수 있다...


small_birds = ['humingbird','finch']
extinct_birds = ['dodo','passenger pigeon','Norwegian Blue']
carol_birds = [3, 'French hens',2,'turtledoves']
all_birds = [small_birds,extinct_birds,'macaw',carol_birds]

# 리스트의 리스트 , all_birds 는 어떻게 생겼는지?

print(all_birds)

print(all_birds[0])

#3.2.5 off set 으로  항목 바꾸기

# 오프셋으로 항목을 얻어서 바꿀 수 있다.

marxes = ['Groucho','Chico','Harpo']

#marxes[2] = 'wanda'

print(marxes)




#3.2.6 슬라이스로 항목 추출하기

#처음부터 오른쪽으로 2칸씩 항목을 추출한다
print(marxes[0:2])
#끝에서 왼쪽으로 2칸의 항목을 추출한다
print(marxes[::-2])
#리스트 반전
print(marxes[::-1])



#3.2.7 리스트의 끝에 항목 추가하기

# append()

marxes.append('Zeppo')
print(marxes)




#3.2.8 리스트 병합하기 : extend() or +=

#extend() 를 사용하여 다른 리스트를 병합 할 수 있다. 리스트 marxes 에 새로운 리스트 others fmf qudgkqgoqhwk




marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo','karl']
#marxes.extend(others)
#print(marxes)


# += 로 추가하는 방법

marxes += others
print(marxes)


# append() 를 사용하면 항목을 병합하지 않고 , others 가 하나의 리스트로 추가된다


marxes.append(others)
print(marxes)


# 3.2.9 오프셋과 insert()로 항목 추가하기

# insert() 함수는 원하는 위치에 항목을 추가 할 수 있다
# 오프셋 0 은 시작 지점에 항목을 사입한다. 리스트의 끝을 넘는 오프셋은 append() 처럼 끝에 항목을 추가한다

#3번째 0 1 2 3 번째에 'Gummo' 를 넣는다
marxes.insert(3,'Gummo')
print(marxes)

marxes.insert(10,'Karl')
#이 경우에는 숫자가 리스트의 범위를 벗어날 경우에는 맨 뒤에 배치시킨다

# 3.2.12 오프셋으로 항목을 얻은 후 삭제하기 pop()

# pop()은 리스트에서 항목을 가져오는 동시에 항목을 삭제한다.
# 오프셋과 함께 pop() 을 호출했다면 그 오프셋의 항목이 반환된다. 인자가 없다면 -1을 사용한다.
# pop(0) 은 리스트의 헤드 (머리, 시작)을 반환한다. 그리고 pop() 혹은 pop(-1)은 리스트의 테일 (꼬리,끝) 을 반환한다.

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']

marxes.pop()
#이렇게 코드를 작성하면 Zeppo 만 삭제되게 된다
print(marxes)
# 결과값 ['Groucho', 'Chico', 'Harpo']
marxes.pop(1)
# Chico
print(marxes)