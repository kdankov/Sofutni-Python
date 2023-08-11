distances = [int(x) for x in input().split()]

removed_elements_sum = 0

while len(distances) > 0:
    index = int(input())
    removed_num = 0
    
    if index < 0:
        removed_num = distances.pop(0)
        distances.insert(0, distances[-1])
    elif index > len(distances) - 1:
        removed_num = distances.pop()
        distances.append(distances[0])
    else:
        removed_num = distances.pop(index)
    
    removed_elements_sum += removed_num
    
    for index, num in enumerate(distances):
        if num <= removed_num:
            distances[index] += removed_num
        else:
            distances[index] -= removed_num
    
print(removed_elements_sum)