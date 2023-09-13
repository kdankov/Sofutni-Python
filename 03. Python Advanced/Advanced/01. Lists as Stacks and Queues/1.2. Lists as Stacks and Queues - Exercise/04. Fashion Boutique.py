clothes_boxes = [int(x) for x in input().split()]
rack_capacity = int(input())

clothes_sum = 0

racks_count = 1

while clothes_boxes:
    current_box = clothes_boxes.pop()
    clothes_sum += current_box

    if clothes_sum == rack_capacity:
        if clothes_boxes:
            racks_count += 1
            clothes_sum = 0
    elif clothes_sum > rack_capacity:
        racks_count += 1
        clothes_sum = current_box

print(racks_count)
