pumps_count = int(input())

petrol_list = []
miles_list = []

fuel_in_tank = 0

trip_done = False
current_index = 0

for num in range(pumps_count):
    data = input().split()
    petrol_amount = int(data[0])
    miles_amount = int(data[1])

    petrol_list.append(petrol_amount)
    miles_list.append(miles_amount)

while True:
    for i in range(0, len(petrol_list)):
        petrol = petrol_list[i]
        miles = miles_list[i]

        fuel_in_tank += petrol
        fuel_in_tank -= miles

        if i == len(petrol_list) - 1:
            if fuel_in_tank >= 0:
                trip_done = True
                break

        if fuel_in_tank < 0:
            fuel_in_tank = 0
            petrol_list.append(petrol_list.pop(0))
            miles_list.append(miles_list.pop(0))
            break

    if trip_done:
        break

    current_index = current_index + 1

print(current_index)
