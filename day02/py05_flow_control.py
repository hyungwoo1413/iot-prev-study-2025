# 흐름제어
# if, for, while

## int(정수화), float(실수화), double(복소수화)
age = int(input('나이를 입력하세요 > ')) # age 문자열이 입력 30 -> '30'

## if 문이 시작된다는 것을 의미하는 마지막 단어 -> :
if age > 19 and age < 61:
    # if문이 참(True)이면, 아래 구문 실행
    # if문(흐름제어) 안으로 들어왔다!
    print('술 사가세요!!')
elif age > 60: # 다른 조건이 필요할 때 (else if) - 여러번 사용가능
    print('아저씨, 치매와요~ 조심하세요~')
else:
    #if문이 거짓(False)이면, 아래 구문 실행
    print('야, 집에가!!')