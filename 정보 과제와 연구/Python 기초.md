## **변수**
- 변수형
```python
int a=7 '''정수'''
float b=4.21 '''실수''' 
list d=[728, 501, 917, 126, 404, 909, 618] '''배열'''
str omg='OH MY GIRL' '''문자 1'''
str ohmygirl="omg" '''문자 2'''
bool t=true  '''참'''
bool f=false '''거짓'''
```
- 변수명 만들기
	1. 시작은 문자(English), _(밑줄)
	2. 대소문자 구분
	3. 예약어 X
		- 예약어 : if, else, while...
	4. -(대시), 공백 사용불가

## **출력**
```python
print ('이름') '''문자'''
print (a) '''변수 1개'''
print (a, b)  '''변수 여러개'''
print ('이름은', a) '''변수, 문자 동시 출력'''
```
## **입력**
```python
a= input('안내 문구') '''문자형 입력'''
a= float(input()) '''원하는 형태의 변수 입력'''
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

## 조건문
- if 문
```python
if 
elif
else
```
```python
n=int(input())
if n%3==0:
  print('나머지 : 없음')
elif n%3==1:
  print('나머지 : 1')
else :
	print('나머지 : 2')
```
- for 문
```python
for i range () :
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
## 도형 1
```python
from turtle import*
forward ()
left() right()
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

## 도형 2
