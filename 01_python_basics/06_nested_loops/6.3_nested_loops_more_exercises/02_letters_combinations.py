start_letter = input()
end_letter = input()
except_letter = input()

count = 0

for i in range(ord(start_letter), ord(end_letter) + 1):

    if i == ord(except_letter):
        continue
    
    for j in range(ord(start_letter), ord(end_letter) + 1):
        
        if j == ord(except_letter):
            continue
        
        for k in range(ord(start_letter), ord(end_letter) + 1):
            
            if k == ord(except_letter):
                continue
            
            print(f'{chr(i)}{chr(j)}{chr(k)}', end=' ')
            count += 1
            
print(count)