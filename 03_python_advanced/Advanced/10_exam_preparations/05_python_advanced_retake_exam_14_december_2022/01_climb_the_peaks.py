from collections import deque

daily_food_portions = [int(x) for x in input().split(', ')]
daily_stamina = deque([int(x) for x in input().split(', ')])

peaks_to_climb = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])

conquered_peaks = []
has_succeeded = False
day = 1

while True:
    if len(conquered_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
    if day > 7 or not daily_food_portions or not daily_stamina:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break

    current_food = daily_food_portions.pop()
    current_stamina = daily_stamina.popleft()
    result = current_food + current_stamina
    next_peak = peaks_to_climb.popleft()

    if result >= next_peak[1]:
        conquered_peaks.append(next_peak[0])
    else:
        peaks_to_climb.appendleft(next_peak)

    day += 1

if conquered_peaks:
    print('Conquered peaks:')
    [print(peak) for peak in conquered_peaks]