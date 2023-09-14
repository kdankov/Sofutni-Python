import sys

movies_count = int(input())

highest_rating_movie = {
    "name": '',
    "rating": 0
}

lowest_rating_movie = {
    "name": '',
    "rating": sys.maxsize
}

average_rating = 0

for i in range(movies_count):
    current_movie = input()
    current_rating = float(input())
    
    if current_rating > highest_rating_movie['rating']:
        highest_rating_movie['name'] = current_movie
        highest_rating_movie['rating'] = current_rating
        
    if current_rating < lowest_rating_movie['rating']:
        lowest_rating_movie['name'] = current_movie
        lowest_rating_movie['rating'] = current_rating
        
    average_rating += current_rating
    
average_rating /= movies_count

print(f'{highest_rating_movie["name"]} is with highest rating: {highest_rating_movie["rating"]:.1f}')
print(f'{lowest_rating_movie["name"]} is with lowest rating: {lowest_rating_movie["rating"]:.1f}')
print(f'Average rating: {average_rating:.1f}')