count = int(input())
previousSum = int(input()) + int(input())
maxDiff = 0

for i in range(count - 1):
    currentSum = int(input()) + int(input())

    if abs(previousSum - currentSum) > maxDiff:
        maxDiff = abs(previousSum - currentSum)

    previousSum = currentSum

if maxDiff == 0:
    print(f"Yes, value={previousSum}")
else:
    print(f"No, maxdiff={maxDiff}")