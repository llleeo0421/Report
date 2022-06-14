import random
import time

ino=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lunch=['차조밥', '낙지버섯매운국', '호박전', '치킨텐더&머스터드', '사과', '자몽에이드']
tomlunch=['쌀밥', '마라탕', '청경채 겉절이', '고추잡채/꽃빵', '메밀전병', '깍두기', '딸기 아이스바']
ment=['정말 맛있겠다.', '두근 두근', '급식 좋아', '우. 와. 정. 말. 맛. 있. 겠. 다.', '급식 기대중']
j=random.randint(1, 5)

print('순서 안내 : 순서 or 급식순서')
print('오늘점심 메뉴 : 급식 or 오늘급식 or 오늘 급식')
print('내일 점심 메뉴 : 내일급식 or 내일 급식')
print('')

com=input('명령어를 입력하시오 : ')
if com=='순서' or com=='급식순서' :
    print('이번주는', ino[0], '반 부터 들어감.')
    for i in range (10) :
        print(i+1, '번째,', ino[i], '반')
        time.sleep(0.5)
        
elif com=='오늘 급식' or com=='오늘급식' or com=='급식' :
    print('오늘 급식은')
    print('')
    for i in range (6) :
        print(lunch[i])
        time.sleep(1)
    print('')
    print(ment[j-1])
        
elif com=='내일 급식' or com=='내일급식' :
    print('내일 급식은')
    print('')
    for i in range (6) :
        print(tomlunch[i])
        time.sleep(1)
    print('')
    print(ment[j-1])
    
else :
    print('')
    print('이것이 무슨말인지 알 수 없읍니다.')
