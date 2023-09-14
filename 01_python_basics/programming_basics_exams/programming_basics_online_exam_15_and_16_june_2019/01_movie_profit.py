movie_name = input()
days = int(input())
tickets_count = int(input())
ticket_price = float(input())
cinema_percentage = int(input())

profit = ticket_price * tickets_count * days
profit = profit - profit * cinema_percentage / 100

print(f'The profit from the movie {movie_name} is {profit:.2f} lv.')