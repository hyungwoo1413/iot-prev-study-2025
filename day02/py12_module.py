# 모듈

import py10_function as calc
import math # 수학 함수를 편하게 모아둔 모듈
import requests

# calc.multi(10, 4)

result = math.pow(2, 10) # 결과값 실수
print(result)

result = math.log2(4)
print(result)

## 패키지 - 모듈들을 모아둔 디렉토리(폴더)
## pip install requests

res = requests.get('https://www.naver.com') # 네이버 사이트를 접속하라

print(res.status_code) # 200

print(res.content)