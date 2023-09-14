animals_queue = input().split(', ')
 
if animals_queue.pop() == "wolf":
    print("Please go away and stop eating my sheep")
    raise SystemExit
 
reversed_queue = animals_queue[::-1]
 
for i in range(len(reversed_queue)):
    if reversed_queue[i] != "sheep":
        print(f"Oi! Sheep number {i + 1}! You are about to be eaten by a wolf!")
