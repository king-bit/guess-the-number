import random
num = random.randrange(20)
res = int(input('Guess a number between 0 and 20: '))
print('your guess is ', + res)
print('the number is', + num)

if res == num:
    print('congratulations you got the number right')
if res > num:
    print('your guess was too high')
if res < num:
    print('your guess was too low')
