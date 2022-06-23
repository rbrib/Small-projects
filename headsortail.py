import random


ans = input('heads or tails?')
coin = ['head', 'tail']
rc = random.choice(coin)
if ans == 'heads':
    if rc == coin[0]:
        print(f'You win \n {rc}')
    elif rc == coin[1]:
        print(f'You lose \n {rc}')

if ans == 'tails':
    if rc == coin[1]:
        print(f'You win \n {rc}')
    elif rc == coin[0]:
        print(f'You lose \n {rc}')
