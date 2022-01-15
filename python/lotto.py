import random

num = range(1,46)

for i in range(5):
    lotto = random.sample(num, 6)
    lotto.sort()
    print(lotto)