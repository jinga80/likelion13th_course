#  randrange 이용해 난수 발생
import random
for i in range(5):
    n = random.randrange(1, 10)
    print(f'{i+1}번째 난수 : {n}')