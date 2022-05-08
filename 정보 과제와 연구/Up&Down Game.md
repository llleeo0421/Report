```python
from random import*
a=randint(1, 100)
```
```python
from random import*
a=randint(1, 30)

print('Game Start')
print('1~30 사이 숫자')
print('기회는 3번')

for i in range(3) :
  n=int(input('당신의 선택은? :'))
  if a==n :
    print(n, ', 정답')
  break
  elif a>n :
    print(n, ', UP')
  else :
    print(n, ', Down')

if a==n :
  print('축하')
else :
  print('정답은', a)
```

## **Written by Rocket Ride([@llleeo0421](https://github.com/llleeo0421))**
- Blog : [날 찾아온 낯선 여행자](https://llleeo0421.tistory.com)
- GitHub : [@August-Leo-0805](https://github.com/August-Leo-0805)
- Instagram : [@llleeo__](https://instagram.com/llleeo__)
- Twitter : [@llleeo0421](https://twitter.com/llleeo0421)
- Youtube : [llleeo](https://www.youtube.com/channel/UCoHALWM5iYLzsrytWGbNCxg)

|[Download PDF File](https://github.com/llleeo0421/Report/files/8646279/up.down.game.pdf)|
|:---:|
