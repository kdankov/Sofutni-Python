file_path = input().split('\\')

file = file_path[-1].split('.')

name = file[0]
extension = file[1]

print(f'File name: {name}')
print(f'File extension: {extension}')