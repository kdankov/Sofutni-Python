guests_count = int(input())

reservations = set()

for _ in range(guests_count):
    reservation_code = input()

    reservations.add(reservation_code)

guest = input()

while guest != 'END':
    if guest in reservations:
        reservations.remove(guest)

    guest = input()


print(len(reservations))

for code in sorted(reservations):
    print(code)