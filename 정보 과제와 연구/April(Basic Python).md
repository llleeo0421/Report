## **변수**
- 변수명 만들기
	1. 시작은 문자(English),  _(밑줄)
	2. 공백, -(대시)사용불가
	3. 대소문자 구분
	4. 예약어(if, else, while...) ❌
- 변수형
```python
int a=7 '''정수'''
float b=4.21 '''실수''' 
list d=[728, 501, 917, 126, 404, 909, 618] '''배열'''
str c='o'  '''문자 1'''
str ohmygirl="omg"  '''문자 2'''
bool t=true  '''참'''
bool f=false '''거짓'''
```

## **출력**
``` python
print ('이름') '''문자'''
print (a) '''변수 1개'''
print (a, b)  '''변수 여러개'''
print ('이름은', a) '''변수, 문자 동시 출력'''
```

## **입력**
```python
a=input('안내 문구') '''문자형 변수 입력'''
a=변수형(input()) '''원하는 형태(정수, 실수등등)의 변수 입력'''
```

## **연산자**
- 산술연산
```python
a+b '''덧셈'''
a-b '''뻴셈'''
a*b '''곱셈'''
a/b '''나눗셈 1'''
a//b '''나눗셈 2'''
a%b '''나머지'''
```
- 비교 연산
```python
a<b '''a는 b보다 작음'''
a<=b '''a는 b보다 작거나 같음'''
a>b '''a는 b보다 큶'''
a>=b '''a는 b보다 크거나 같음'''
a==b '''a는 b와 같음'''
```
- 논리연산
```python
a and b '''둘다 만족'''
a or b '''하나만 만족'''
```
- 대입연산
```python
i=i+1
```

## **조건문**
- if 문
```python
if
elif
else
```
```python
n=int(input())
if n%4==0:
  print('나머지 : 없음')
elif n%4==1:
  print('나머지 : 1')
	elif n%4==2:
  print('나머지 : 2')
else :
	print('나머지 : 3')
```
- for 문
```python
for i in range () :
```
```python
sum=0
for i in range(101)
	sum=sum+i
print(sum)
```
- while 문
```python
while 조건식 :
```
```python
i=0
while i<10 :
  print(i+1)
  i+=1
```
```python
i=0
sum=0
while i<11 :
  sum=sum+i
  i+=1
	print(sum)
```

## **도형 1**
```python
from turtle import*
forward ()
left()
```
```python
from turtle import*
forward (100)
left(120)
forward (100)
left(120)
forward (100)
left(120)
```
```python
from turtle import*
for i in range (3) :
	forward (100)
	left(120)
```
```python
from turtle import*
shape('turtle')
a=int(input())
for i range in (a) :
	forward(100)
	left(360/a)
```
```python
from turtle import*
shape('turtle')
for i in range(12) :
  for i in range (3) :
  	forward (100)
  	left(120)
  left(30)
```
```python
from turtle import*
speed(0)
shape('turtle')
for i in range(12) :
  for i in range (3) :
  	forward (100)
  	left(120)
  left(30)
```
```python
from turtle import*
speed(0)
shape('turtle')
for i in range(500) :
  fd(i*4)
  lt(121)
```

## **도형 2**
```python
from turtle import*
forward ()
right()
```
```python
from turtle import*
forward (100)
right(120)
forward (100)
right(120)
forward (100)
right(120)
```
```python
from turtle import*
for i in range (3) :
	forward (100)
	right(120)
```
```python
from turtle import*
shape('turtle')
a=int(input())
for i range in (a) :
	forward(100)
	right(360/a)
```
```python
from turtle import*
shape('turtle')
for i in range(12) :
  for i in range (3) :
  	forward (100)
  	right(120)
  right(30)
```
```python
from turtle import*
speed(0)
shape('turtle')
for i in range(12) :
  for i in range (3) :
  	forward (100)
  	right(120)
  right(30)
```
```python
from turtle import*
speed(0)
shape('turtle')
for i in range(500) :
  fd(i*4)
  rt(121)
```

## **Written by Rocket Ride([@llleeo0421](https://github.com/llleeo0421))**
- Blog : [날 찾아온 낯선 여행자](https://llleeo0421.tistory.com)
- GitHub : [@August-Leo-0805](https://github.com/August-Leo-0805)
- Instagram : [@llleeo__](https://instagram.com/llleeo__)
- Twitter : [@llleeo0421](https://twitter.com/llleeo0421)
- Youtube : [llleeo](https://www.youtube.com/channel/UCoHALWM5iYLzsrytWGbNCxg)

|[Download PDF File](https://github.com/llleeo0421/Report/files/8549525/Basic.Python.pdf)|
|:---:|
