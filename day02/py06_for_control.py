# 프로그래밍의 꽃!

# range(9) => 0, 1, 2, 3, 4, 5, 6, 7, 8 
# print(range(9))

for i in range(9): # for문 흐름제어로 들어간다
    print(i, end='\t') # \n 한줄내림 end인자로 출력 끝을 조정

# 1부터 10까지 합 - 55
sum = 0
for i in range(1, 11): # range(11) -> 0~10까지 라서 결과값 45나옴
    sum = sum + i

print(sum)

sum = 0
for i in range(1, 10, 2):
    print(i)