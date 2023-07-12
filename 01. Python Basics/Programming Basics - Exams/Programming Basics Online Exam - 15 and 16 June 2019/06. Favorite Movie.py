movie_name = input()

count = 0

best_movie = {
    'name': '',
    'ascii_sum': 0
}

while movie_name != 'STOP':
    current_sum = 0
    for letter in movie_name:
        if letter.islower():
            current_sum += ord(letter) - len(movie_name) * 2
        elif letter.isupper():
            current_sum += ord(letter) - len(movie_name)
        else:
            current_sum += ord(letter)
    
    if best_movie['ascii_sum'] < current_sum:
        best_movie['name'] = movie_name
        best_movie['ascii_sum'] = current_sum
    
    count += 1
    
    if count == 7:
        break
    
    movie_name = input()
    
if count == 7:
    print('The limit is reached.')

print(f'The best movie for you is {best_movie["name"]} with {best_movie["ascii_sum"]} ASCII sum.')
