from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
value_of_the_intelligence = int(input())

bullets_in_barrel = gun_barrel_size
bullets_shot = 0

has_failed = False

while True:
    if bullets:
        current_bullet = bullets.pop()

        bullets_in_barrel -= 1
        bullets_shot += 1

        if current_bullet <= locks[0]:
            locks.popleft()
            print('Bang!')

        else:
            print('Ping!')

        if bullets_in_barrel == 0 and len(bullets) > 0:
            print('Reloading!')
            bullets_in_barrel = gun_barrel_size

        if not locks:
            break
    else:
        has_failed = True
        break

if has_failed:
    print(f'Couldn\'t get through. Locks left: {len(locks)}')
else:
    earned = value_of_the_intelligence - bullet_price * bullets_shot
    print(f'{len(bullets)} bullets left. Earned ${earned}')
