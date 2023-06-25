length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = (length * width * height) / 1000

needed_litres = volume * (1 - (percent / 100))

print(needed_litres)
